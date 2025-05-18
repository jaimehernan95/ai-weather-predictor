#!/bin/bash

echo "🧹 Limpiando entorno de pruebas..."

# 1. Eliminar carpeta tests incorrecta dentro de scripts/
if [ -d "scripts/tests" ]; then
  echo "❌ Eliminando carpeta scripts/tests/..."
  rm -rf scripts/tests
else
  echo "✅ No existe scripts/tests/ (todo bien)"
fi

# 2. Eliminar caché
echo "🗑️ Borrando __pycache__ y .pytest_cache..."
find . -type d -name "__pycache__" -exec rm -rf {} +
rm -rf .pytest_cache
find . -name "*.pyc" -delete

# 3. Verificar ubicación del archivo de prueba
if [ -f "tests/test_predict.py" ]; then
  echo "✅ test_predict.py está correctamente ubicado en tests/"
else
  echo "⚠️ test_predict.py NO está en tests/, por favor muévelo allí."
fi

echo "✅ Limpieza finalizada. Ejecuta ahora: pytest"
