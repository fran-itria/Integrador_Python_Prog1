Objetivo: Desarrollar una solución de software para gestionar la compra, venta y mantenimiento de vehículos
usados en una concesionaria.

Realizado el análisis de requerimientos con el gerente de la concesionaria se ha determinado necesario
registrar los siguientes datos:

Requerimientos:
    1. Registro de :
        ● ID de vehículo (número único y autoincremental)
        ● Nº de Patente o Dominio
        ● Marca
        ● Modelo
        ● Tipo (Sedán, Hatchback, SUV, Pick Up, etc)
        ● Año
        ● Kilometraje
        ● Precio de Compra
        ● Precio de Venta
        ● Estado (Disponible, Reservado, Vendido)
    2. Gestión de Clientes:
        ● ID de Cliente (número único y autoincremental)
        ● Nombre
        ● Documento
        ● Apellido
        ● Dirección
        ● Teléfono
        ● Correo Electrónico
    3. Registro de Transacciones:
        ● ID de Transacción (número único y autoincremental)
        ● ID de Vehículo
        ● ID de Cliente
        ● Tipo de Transacción (Compra/Venta)
        ● Fecha
        ● Monto
        ● Observaciones

Características del Software:
    ● Almacenamiento de Información: utilización de archivos JSON para almacenar los datos solicitados.
    ● Interfaces de usuario interactiva que permitan registrar:
        ● Vehículos:
            ● Crear, editar y eliminar vehículos.
            ● Listados de búsqueda por patente, marca, modelo y precios de compra/venta.
        ● Clientes:
            ● Crear, editar y eliminar clientes.
            ● Listados de búsqueda por documento, por apellido y/o nombres.
        ● Transacciones:
            ● Registrar compras y ventas de vehículos.
            ● Imprimir listados de compras por cliente, vehículo y rango de fechas (deben incluir
            totalizadores de montos de dinero).
            ● Imprimir listados de ventas por cliente, vehículo y rango de fechas (deben incluir
            totalizadores de montos de dinero).
    ● Por último, se deberá desarrollar una funcionalidad extra del software a criterio del
    alumno/grupo. Esta nueva funcionalidad puede incluir, como por ejemplo: desarrollo de
    interfaz gráfica, consumo de una api externa, búsquedas avanzadas, nuevas funcionalidades
    similares a las anteriores que aporten valor agregado, etc.
