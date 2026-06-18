USE Datos_Colombia;
GO
SELECT TOP 10 
    municipio, 
    departamento, 
    COUNT(*) AS total_proveedores
FROM secop_colombia
WHERE municipio IS NOT NULL AND municipio <> 'NO PROVISTO'
GROUP BY municipio, departamento
ORDER BY total_proveedores DESC;

SELECT 
    tipo_empresa, 
    COUNT(*) AS cantidad,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM secop_colombia), 2) AS porcentaje
FROM secop_colombia
WHERE tipo_empresa IS NOT NULL AND tipo_empresa <> 'NAN'
GROUP BY tipo_empresa
ORDER BY cantidad DESC;

SELECT 
    YEAR(fecha_creacion) AS ano_creacion, 
    COUNT(*) AS nuevos_proveedores_registrados
FROM secop_colombia
WHERE fecha_creacion IS NOT NULL
GROUP BY YEAR(fecha_creacion)
ORDER BY ano_creacion DESC;

SELECT 
    CASE 
        WHEN correo LIKE '%@gmail.com%' THEN 'Gmail (Personal)'
        WHEN correo LIKE '%@hotmail.com%' OR correo LIKE '%@outlook.%' THEN 'Hotmail/Outlook (Personal)'
        WHEN correo LIKE '%@yahoo.%' THEN 'Yahoo (Personal)'
        WHEN correo IS NULL OR correo = 'NO PROVISTO' THEN 'Sin Correo / No Provisto'
        ELSE 'Correo Corporativo / Propio'
    END AS tipo_correo,
    COUNT(*) AS cantidad_empresas,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM secop_colombia), 2) AS porcentaje
FROM secop_colombia
GROUP BY 
    CASE 
        WHEN correo LIKE '%@gmail.com%' THEN 'Gmail (Personal)'
        WHEN correo LIKE '%@hotmail.com%' OR correo LIKE '%@outlook.%' THEN 'Hotmail/Outlook (Personal)'
        WHEN correo LIKE '%@yahoo.%' THEN 'Yahoo (Personal)'
        WHEN correo IS NULL OR correo = 'NO PROVISTO' THEN 'Sin Correo / No Provisto'
        ELSE 'Correo Corporativo / Propio'
    END
ORDER BY cantidad_empresas DESC;

SELECT 
    telefono,
    COUNT(DISTINCT nit) AS cantidad_nits_diferentes,
    STRING_AGG(nombre, ' | ') AS empresas_asociadas 
FROM secop_colombia
WHERE telefono IS NOT NULL 
  AND telefono <> 'NO PROVISTO' 
  AND telefono <> ''
GROUP BY telefono
HAVING COUNT(DISTINCT nit) > 1 
ORDER BY cantidad_nits_diferentes DESC;