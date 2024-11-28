# Primera etapa: Build
FROM python:3.11-alpine AS builder

# Establecer variables de entorno para evitar archivos .pyc y forzar salida sin búfer en Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias necesarias para compilar Python y las librerías
RUN apk add --no-cache gcc musl-dev libffi-dev python3-dev

# Copiar archivo de requerimientos e instalar dependencias
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . .

# Segunda etapa: Runtime
FROM python:3.11-alpine

# Establecer variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instalar dependencias en tiempo de ejecución
RUN apk add --no-cache libffi

# Copiar las librerías instaladas y el binario de `uvicorn` desde la etapa builder
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY . .

# Configurar variables de entorno
ENV PORT=8000

# Verificar que `uvicorn` está disponible
RUN uvicorn --version || (echo "Error: uvicorn no está instalado" && exit 1)

# Ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


