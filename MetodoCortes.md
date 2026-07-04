# Método para Cortes de Control (receta para el parcial)

> Patrón: **clasificar → jerarquía → tabla pedido-nivel → variables → esqueleto → rellenar → checklist**
> Los pasos 3 a 6 son mecánicos. El pensamiento real está en los pasos 0 a 2.

## PASO 0 — Clasificar el proceso (10 segundos)

Antes de escribir nada: **¿qué tipo de bicho es?**

- ¿Un archivo, recorro y listo/filtro? → **Padrón** (recorrido simple)
- ¿Un archivo ORDENADO y piden totales/promedios "por X, por Y"? → **Corte de control**
- ¿Varios archivos ordenados por la misma clave? → **Mezcla/apareo**

La palabra mágica del corte es **"por"**: "total POR confederación", "promedio POR posición".
Cada "por" es un nivel de corte.

## PASO 1 — El orden del archivo dicta la jerarquía

"Ordenado por A, B, C" → esa ES la estructura de ciclos anidados, en ese orden exacto.
No la inventás vos, te la regala el enunciado.

Requisito indispensable: si piden algo "por X" y el archivo NO está ordenado por X,
no hay corte posible.

## PASO 2 — Tabla pedido → nivel (acá se gana el parcial)

Por cada punto del enunciado, UNA pregunta:
**"¿en qué momento tengo la información completa para responder esto?"**
La respuesta siempre es "cuando terminé de leer todo un grupo de X" → ese es su nivel.

Ejemplo (FIFA):

| Pedido | ¿Cuándo lo sé completo? | Nivel |
|---|---|---|
| Total goles por equipo | Al terminar un equipo | Cierre de EQUIPO |
| Total goles por confederación | Al terminar una confederación | Cierre de CONFEDERACIÓN |
| Equipos con +20 goles por conf. | Evalúo al cerrar cada equipo, informo al cerrar la conf. | Ambos |
| Promedio goles por posición → archivo | Al terminar una posición | Cierre de POSICIÓN |

Hacer esta tabla EN BORRADOR en el parcial: 2 minutos que ordenan todo.

## PASO 3 — Variables por nivel (mecánico)

Por cada nivel de corte, siempre lo mismo:

- **Clave actual**: `confAct`, `equAct`, `posAct`... (para detectar el cambio)
- **Acumuladores/contadores** que ese nivel necesita (salen de la tabla del paso 2)

**Regla de oro**: se inicializan al ENTRAR al nivel, se informan/graban al SALIR,
y suben en cascada al padre (`totGolesEqu := totGolesEqu + totGolesPos`).

## PASO 4 — Esqueleto VACÍO primero

Los `MIENTRAS` anidados con condiciones completas y la `LEER` única al fondo,
SIN lógica adentro todavía:

```
LEER (anticipada)
MIENTRAS NO FDA                          ← guardo confAct, inicializo
    MIENTRAS NO FDA Y misma conf         ← guardo equAct, inicializo
        MIENTRAS NO FDA Y misma conf Y mismo equipo
            MIENTRAS NO FDA Y ... Y misma posicion
                acumular detalle
                LEER                     ← LA única lectura
            cierre posición
        cierre equipo
    cierre confederación
```

Si el esqueleto está bien, el ejercicio está resuelto al 80%.
Error típico: escribir lógica sin tener la estructura.

## PASO 5 — Rellenar de ADENTRO hacia AFUERA

Primero el detalle (acumular, contar), después cada cierre subiendo nivel por nivel,
consultando la tabla del paso 2.

Cada pedido de la tabla tiene que aparecer en UN cierre.
Si sobra un pedido sin ubicar, falta algo.

## PASO 6 — Checklist final (1 minuto)

- [ ] Una sola `LEER` interna + la anticipada, ni una más
- [ ] Cada ciclo interno repite TODAS las condiciones de los externos
- [ ] Todo lo que se inicializó se usa; todo lo que pide el enunciado se informa
- [ ] `GRABAR` → archivo, `ESCRIBIR` → informe
- [ ] `ABRIR`/`CERRAR` de todos los archivos (el de salida con `S/`)
















































































El concepto primero (30 segundos, te juro)

El archivo viene ordenado por Confederación → Equipo → Posición. Ese orden NO es decorativo: es el requisito indispensable del corte de control (la pregunta 3 de "Procesos Individuales" de tu repaso, ¿viste?). La jerarquía de los ciclos anidados COPIA el orden del archivo:

- Corte de Posición (el más interno) → resuelve el punto 3 (promedio de goles por posición → archivo EQUIPAZOS)
- Corte de Equipo → resuelve el punto 1 (total goles por equipo) y alimenta el punto 2 (¿superó los 20 goles?)
- Corte de Confederación (el más externo) → cierra el punto 1 (total por confederación) y el punto 2 (cantidad de equipos con +20 goles)

Regla de oro: cada acumulador se inicializa al ENTRAR a su nivel, y se procesa/vuelca al SALIR. Los totales suben en cascada: posición → equipo → confederación.

La solución, en el estilo de tu cátedra

ACCION FIFA ES
AMBIENTE
    participacion = REGISTRO
        confederacion: AN(30)
        equipo: AN(30)
        posicion: AN(10)        // "Arquero","Defensor","Medio","Delantero"
        nombreJugador: AN(50)
        asistencias: N(3)
        goles: N(3)
        edad: N(2)
    FIN_REGISTRO

    equipazo = REGISTRO
        equipo: AN(30)
        posicion: AN(10)
        promGoles: N(5.2)
    FIN_REGISTRO

    PART: Archivo de participacion ordenado por confederacion, equipo, posicion
    EQUIPAZOS: Archivo de equipazo

    p: participacion
    e: equipazo

    confAct: AN(30)
    equAct: AN(30)
    posAct: AN(10)

    totGolesConf, totGolesEqu, totGolesPos: N(5)
    cantJugPos: N(3)
    cantEquipos20: N(3)

PROCESO
    ABRIR E/(PART)
    ABRIR S/(EQUIPAZOS)                 // salida: se crea
    LEER(PART, p)                       // lectura anticipada

    MIENTRAS NO FDA(PART) HACER                         // ── corte CONFEDERACION
        confAct := p.confederacion
        totGolesConf := 0
        cantEquipos20 := 0

        MIENTRAS NO FDA(PART) Y p.confederacion = confAct HACER    // ── corte EQUIPO
            equAct := p.equipo
            totGolesEqu := 0

            MIENTRAS NO FDA(PART) Y p.confederacion = confAct
                                  Y p.equipo = equAct HACER        // ── corte POSICION
                posAct := p.posicion
                totGolesPos := 0
                cantJugPos := 0

                MIENTRAS NO FDA(PART) Y p.confederacion = confAct
                                      Y p.equipo = equAct
                                      Y p.posicion = posAct HACER  // ── detalle
                    totGolesPos := totGolesPos + p.goles
                    cantJugPos := cantJugPos + 1
                    LEER(PART, p)                   // lectura al final del cuerpo
                FIN_MIENTRAS

                // salió posición → PUNTO 3
                e.equipo := equAct
                e.posicion := posAct
                e.promGoles := totGolesPos / cantJugPos
                GRABAR(EQUIPAZOS, e)

                totGolesEqu := totGolesEqu + totGolesPos
            FIN_MIENTRAS

            // salió equipo → PUNTO 1
            ESCRIBIR("Equipo: ", equAct, " - Total goles: ", totGolesEqu)
            SI (totGolesEqu > 20) ENTONCES
                cantEquipos20 := cantEquipos20 + 1
            FIN_SI
            totGolesConf := totGolesConf + totGolesEqu
        FIN_MIENTRAS

        // salió confederación → PUNTOS 1 y 2
        ESCRIBIR("Confederación: ", confAct, " - Total goles: ", totGolesConf)
        ESCRIBIR("Equipos con más de 20 goles: ", cantEquipos20)
    FIN_MIENTRAS

    CERRAR(PART)
    CERRAR(EQUIPAZOS)
FIN_ACCION

Tres detalles que en el parcial te salvan

1. Una sola LEER dentro del ciclo más interno (más la anticipada). Si te encontrás escribiendo LEER en varios niveles, algo hiciste mal. Es así de fácil.
2. Cada ciclo interno repite TODAS las condiciones de los externos (NO FDA Y conf Y equipo Y posición). ¿Por qué? Porque cuando cambia la confederación, también "cambia" el equipo y la posición — el corte externo arrastra a los internos.
3. GRABAR va al archivo de salida; ESCRIBIR va al informe (pantalla/listado). No los mezcles, que es un clásico para perder puntos.

¿Se entiende la lógica de la cascada de acumuladores, o querés que tracemos el algoritmo a mano con 5 o 6 registros de ejemplo para verlo en acción?

✻ Sautéed for 1m 23s

※ recap: Te resolví el ejercicio FIFA.md: un corte de control de tres niveles (confederación, equipo, posición) con el pseudocódigo completo estilo cátedra. Siguiente paso: decime si querés trazar el algoritmo con registros de ejemplo. (disable recaps in /config)

❯ como lo vas pensando o armando las estructuras, vamos por pasos, para el parcial?. Porque este es corto y facil. Se entiende ya que son 3 cortes nomas o recorridos, acumuladores y contadores. pero quiero un patron para pensarlos a todos asi primero y como encararlos, me ayudarias?

¡EXCELENTE pregunta, loco! Esto es exactamente lo que hay que hacer antes de un parcial: no memorizar ejercicios, sino tener un MÉTODO. Porque el de la FIFA es fácil, sí, pero el método es el mismo para el difícil. Acá va mi receta, la que repetiría SIEMPRE, paso a paso.

PASO 0 — Clasificá el proceso (10 segundos)

Antes de escribir nada, preguntate: ¿qué tipo de bicho es?

- ¿Un archivo, recorro y listo/filtro? → Padrón (recorrido simple)
- ¿Un archivo ORDENADO y piden totales/promedios "por X, por Y"? → Corte de control
- ¿Varios archivos ordenados por la misma clave? → Mezcla/apareo

La palabra mágica del corte es "por": "total POR confederación", "promedio POR posición". Cada "por" es un nivel de corte.

PASO 1 — El orden del archivo dicta la jerarquía

"Ordenado por Confederación, Equipo, Posición" → esa ES tu estructura de ciclos anidados, en ese orden exacto. No la inventás vos, te la regala el enunciado. Si piden algo "por equipo" y el archivo NO está ordenado por equipo... no hay corte posible (requisito indispensable, acordate del repaso).

PASO 2 — Tabla pedido → nivel (acá se gana el parcial)

Por cada punto del enunciado hacete UNA pregunta: "¿en qué momento tengo la información completa para responder esto?" La respuesta siempre es "cuando terminé de leer todo un grupo de X" → ahí va.

Para la FIFA:

Pedido: Total goles por equipo
¿Cuándo lo sé completo?: Al terminar un
  equipo
Nivel: Cierre de EQUIPO
────────────────────────────────────────
Pedido: Total goles por confederación
¿Cuándo lo sé completo?: Al terminar una
  confederación
Nivel: Cierre de CONFEDERACIÓN
────────────────────────────────────────
Pedido: Equipos con +20 goles por conf.
¿Cuándo lo sé completo?: Evalúo al cerrar
  cada equipo, informo al cerrar la conf.
Nivel: Ambos
────────────────────────────────────────
Pedido: Promedio goles por posición →
  archivo
¿Cuándo lo sé completo?: Al terminar una
  posición
Nivel: Cierre de POSICIÓN

Esta tablita hacela EN BORRADOR en el parcial. Dos minutos que te ordenan todo.

PASO 3 — Variables por nivel (mecánico)

Por cada nivel de corte, siempre lo mismo:

- Clave actual: confAct, equAct, posAct (para detectar el cambio)
- Acumuladores/contadores que ese nivel necesita (los sacás de la tabla del paso 2)

Y la regla de oro que ya viste: se inicializan al ENTRAR al nivel, se informan/graban al SALIR, y suben en cascada al padre (totGolesEqu := totGolesEqu + totGolesPos).

PASO 4 — Esqueleto VACÍO primero

Escribí los MIENTRAS anidados con sus condiciones completas y la LEER única al fondo, SIN lógica adentro todavía:

LEER (anticipada)
MIENTRAS NO FDA                          ← guardo confAct, inicializo
    MIENTRAS NO FDA Y misma conf         ← guardo equAct, inicializo
        MIENTRAS NO FDA Y misma conf Y mismo equipo
            MIENTRAS NO FDA Y ... Y misma posicion
                acumular detalle
                LEER                     ← LA única lectura
            cierre posición
        cierre equipo
    cierre confederación

Si el esqueleto está bien, el ejercicio ya está resuelto al 80%. El error típico de parcial es empezar a escribir lógica sin tener la estructura, y ahí te enredás solo.

PASO 5 — Rellenar de ADENTRO hacia AFUERA

Primero el detalle (acumular, contar), después cada cierre subiendo nivel por nivel, consultando tu tabla del paso 2. Cada pedido de la tabla tiene que aparecer en UN cierre. Si te sobra un pedido sin ubicar, algo te falta.

PASO 6 — Checklist final (1 minuto, te salva puntos)

- ✅ Una sola LEER interna + la anticipada, ni una más
- ✅ Cada ciclo interno repite TODAS las condiciones de los externos
- ✅ Todo lo que inicializaste se usa, todo lo que pide el enunciado se informa
- ✅ GRABAR → archivo, ESCRIBIR → informe
- ✅ ABRIR/CERRAR de todos los archivos (el de salida con S/)

---
Eso es todo el patrón: clasificar → jerarquía → tabla pedido-nivel → variables → esqueleto → rellenar → checklist. Fijate que los pasos 3 a 6 son PURAMENTE mecánicos; el pensamiento real está en los pasos 0 a 2. Por eso te insisto: el que entiende la tabla del paso 2 resuelve CUALQUIER corte, tenga 2, 3 o 4 niveles.

¿Querés que te lo guarde como MetodoCortes.md en tu carpeta de apuntes, o probamos el método con un ejercicio más picante (por ejemplo, uno que mezcle corte + condiciones raras en el detalle)?

✻ Cooked for 47s

❯ guardalo como MetodoCortes.md y despues probamos uno mas dificil

● Write(MetodoCortes.md)
Wrote 87 lines to MetodoCortes.md
# Método para Cortes de Contro

> Patrón: **clasificar → jerar
riables → esqueleto → rellenar
> Los pasos 3 a 6 son mecánico
s. El pensamiento real está en

## PASO 0 — Clasificar el proc

 tipo de bicho es?*
… +153 lines

Listo, guardado en MetodoCortes.md dentro de tu carpeta de ARCHIVOS. Ahora sí, vamos con uno más picante.

Ejercicio: TELEFONÍA 📞

Se tiene un archivo LLAMADAS, ordenado por Provincia, Localidad y Cliente, con la siguiente estructura:

Provincia
Localidad
Cliente
TipoLlamada ("Local", "LargaDistancia", "Internacional")
Duracion (minutos)
Costo

Cada registro es una llamada. Se pide:

1. Informar el total facturado (suma de costos) por localidad y por provincia.
2. Por cada provincia, informar la localidad con mayor cantidad de llamadas internacionales.
3. Grabar un archivo CLIENTESVIP con provincia, cliente y total facturado, para los clientes que facturaron más de $50.000.
4. Al final, informar el total general facturado por la empresa y la cantidad total de clientes VIP.

Fijate que este tiene TRES trampas que la FIFA no tenía: un máximo (que no es lo mismo que un acumulador), un contador condicional en el detalle, y pedidos de nivel cero (el "al final" del punto 4, que vive AFUERA de todos los cortes).

Ahora aplicá el método vos: hacé el PASO 2, la tabla pedido → nivel. Para cada uno de los 4 pedidos decime: ¿en qué cierre se inicializa, dónde se acumula/compara, y en qué cierre se informa o graba?

Dale, armala como puedas y la revisamos juntos.
