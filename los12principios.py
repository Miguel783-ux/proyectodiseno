import pygame
import math
import sys
import cv2
pygame.init()
# ==========================================
# CONFIGURACION
# ==========================================
ANCHO = 800
ALTO = 600

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Los 12 Principios de la Animacion")

reloj = pygame.time.Clock()
fuente = pygame.font.SysFont("Arial", 28)

principio = 1
t = 0

x = 100
vel = 0
cola = 100

contador_pose = 0
indice_pose = 0

video = cv2.VideoCapture("stopmotion.mp4")

frame_video = None

# ==========================================
# BUCLE PRINCIPAL
# ==========================================
while True:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:

            if evento.key == pygame.K_1:
                principio = 1

            elif evento.key == pygame.K_2:
                principio = 2

            elif evento.key == pygame.K_3:
                principio = 3

            elif evento.key == pygame.K_4:
                principio = 4

            elif evento.key == pygame.K_5:
                principio = 5

            elif evento.key == pygame.K_6:
                principio = 6

            elif evento.key == pygame.K_7:
                principio = 7

            elif evento.key == pygame.K_8:
                principio = 8

            elif evento.key == pygame.K_9:
                principio = 9

            elif evento.key == pygame.K_F1:
                principio = 10

            elif evento.key == pygame.K_F2:
                principio = 11

            elif evento.key == pygame.K_F3:
                principio = 12
            elif evento.key == pygame.K_F4:
                principio = 13

    pantalla.fill((240, 240, 240))

    # ==========================================
    # 1 ESTIRAR Y ENCOGER
    # ==========================================
    if principio == 1:

        texto = fuente.render(
            "1. Estirar y Encoger (Squash & Stretch)",
            True,
            (0, 0, 0)
        )
        pantalla.blit(texto, (20, 20))

        escala = abs(math.sin(t)) + 0.5

        ancho = int(100 * escala)
        alto = int(100 / escala)

        pygame.draw.ellipse(
            pantalla,
            (255, 0, 0),
            (400 - ancho // 2,
             300 - alto // 2,
             ancho,
             alto)
        )

    # ==========================================
    # 2 ANTICIPACION
    # ==========================================
    elif principio == 2:

        texto = fuente.render(
            "2. Anticipacion",
            True,
            (0, 0, 0)
        )
        pantalla.blit(texto, (20, 20))

        salto = math.sin(t) * 150

        pygame.draw.circle(
            pantalla,
            (0, 0, 255),
            (400, int(350 - salto)),
            40
        )

    # ==========================================
    # 3 PUESTA EN ESCENA
    # ==========================================
    elif principio == 3:

        texto = fuente.render(
            "3. Puesta en Escena",
            True,
            (0, 0, 0)
        )
        pantalla.blit(texto, (20, 20))

        pygame.draw.circle(
            pantalla,
            (100,100,100),
            (200,300),
            40
        )

        pygame.draw.circle(
            pantalla,
            (255,0,0),
            (400,300),
            80
        )

        pygame.draw.circle(
            pantalla,
            (100,100,100),
            (600,300),
            40
        )

    # ==========================================
    # 4 DIRECTA Y POSE A POSE
    # ==========================================
    elif principio == 4:

        texto = fuente.render(
            "4. Animacion Directa y Pose a Pose",
            True,
            (0,0,0)
        )
        pantalla.blit(texto,(20,20))

        # DIRECTA
        x_directa = 150 + (t * 120) % 250

        pygame.draw.line(
            pantalla,
            (0,0,0),
            (50,250),
            (350,250),
            2
        )

        pygame.draw.circle(
            pantalla,
            (255,0,0),
            (int(x_directa),250),
            30
        )

        txt1 = fuente.render(
            "Directa",
            True,
            (0,0,0)
        )
        pantalla.blit(txt1,(120,320))

        # POSE A POSE
        poses = [500,600,700,600]

        contador_pose += 1

        if contador_pose > 25:
            indice_pose = (indice_pose + 1) % len(poses)
            contador_pose = 0

        pygame.draw.line(
            pantalla,
            (0,0,0),
            (450,250),
            (750,250),
            2
        )

        pygame.draw.circle(
            pantalla,
            (0,0,255),
            (poses[indice_pose],250),
            30
        )

        txt2 = fuente.render(
            "Pose a Pose",
            True,
            (0,0,0)
        )
        pantalla.blit(txt2,(520,320))

    # ==========================================
    # 5 ACCIONES COMPLEMENTARIAS
    # ==========================================
    elif principio == 5:

        texto = fuente.render(
            "5. Acciones Complementarias y Superpuestas",
            True,
            (0,0,0)
        )
        pantalla.blit(texto,(20,20))

        x = 400 + math.sin(t) * 200

        cola += (x - cola) * 0.05

        pygame.draw.circle(
            pantalla,
            (0,0,255),
            (int(x),300),
            40
        )

        pygame.draw.circle(
            pantalla,
            (255,0,0),
            (int(cola),300),
            20
        )

    # ==========================================
    # 6 ACELERAR Y DESACELERAR
    # ==========================================
    elif principio == 6:

        texto = fuente.render(
            "6. Acelerar y Desacelerar",
            True,
            (0,0,0)
        )
        pantalla.blit(texto,(20,20))

        vel += 0.05

        if x > 700:
            vel = -5

        if x < 100:
            vel = 0

        x += vel

        pygame.draw.circle(
            pantalla,
            (255,100,0),
            (int(x),300),
            40
        )

    # ==========================================
    # 7 ARCOS
    # ==========================================
    elif principio == 7:

        texto = fuente.render(
            "7. Arcos",
            True,
            (0,0,0)
        )
        pantalla.blit(texto,(20,20))

        px = 400 + 200 * math.cos(t)
        py = 300 + 120 * math.sin(t)

        pygame.draw.circle(
            pantalla,
            (0,0,255),
            (int(px), int(py)),
            30
        )

    # ==========================================
    # 8 ACCION SECUNDARIA
    # ==========================================
    elif principio == 8:

        texto = fuente.render(
            "8. Accion Secundaria",
            True,
            (0,0,0)
        )
        pantalla.blit(texto,(20,20))

        px = 400 + math.sin(t) * 150

        pygame.draw.circle(
            pantalla,
            (255,0,0),
            (int(px),300),
            40
        )

        brazo = 40 * math.sin(t * 4)

        pygame.draw.line(
            pantalla,
            (0,0,0),
            (int(px),300),
            (int(px+60), int(300+brazo)),
            6
        )

    # ==========================================
    # 9 TIMING
    # ==========================================
    elif principio == 9:

        texto = fuente.render(
            "9. Sincronizacion",
            True,
            (0,0,0)
        )
        pantalla.blit(texto,(20,20))

        px = (t * 300) % 800

        pygame.draw.circle(
            pantalla,
            (255,0,0),
            (int(px),300),
            35
        )

    # ==========================================
    # 10 EXAGERACION
    # ==========================================
    elif principio == 10:

        texto = fuente.render(
            "10. Exageracion",
            True,
            (0,0,0)
        )
        pantalla.blit(texto,(20,20))

        escala = abs(math.sin(t * 3)) * 2 + 0.5

        ancho = int(120 * escala)
        alto = int(120 / escala)

        pygame.draw.ellipse(
            pantalla,
            (255,0,0),
            (
                400-ancho//2,
                300-alto//2,
                ancho,
                alto
            )
        )

        pygame.draw.circle(pantalla,(255,255,255),(370,280),20)
        pygame.draw.circle(pantalla,(255,255,255),(430,280),20)

        pygame.draw.circle(pantalla,(0,0,0),(370,280),8)
        pygame.draw.circle(pantalla,(0,0,0),(430,280),8)

        pygame.draw.arc(
            pantalla,
            (0,0,0),
            (320,290,160,120),
            0,
            math.pi,
            8
        )

    # ==========================================
    # 11 DIBUJO SOLIDO
    # ==========================================
    elif principio == 11:

        texto = fuente.render(
            "11. Dibujo Solido",
            True,
            (0,0,0)
        )
        pantalla.blit(texto,(20,20))

        pygame.draw.ellipse(
            pantalla,
            (90,90,90),
            (260,430,240,40)
        )

        frente = [
            (250,220),
            (450,220),
            (450,420),
            (250,420)
        ]

        lado = [
            (450,220),
            (550,170),
            (550,370),
            (450,420)
        ]

        techo = [
            (250,220),
            (350,170),
            (550,170),
            (450,220)
        ]

        pygame.draw.polygon(
            pantalla,
            (170,170,255),
            frente
        )

        pygame.draw.polygon(
            pantalla,
            (90,90,220),
            lado
        )

        pygame.draw.polygon(
            pantalla,
            (220,220,255),
            techo
        )

    # ==========================================
    # 12 ATRACTIVO
    # ==========================================
    elif principio == 12:

        pantalla.fill((180,220,255))

        texto = fuente.render(
            "12. Atractivo (Appeal)",
            True,
            (0,0,0)
        )
        pantalla.blit(texto,(20,20))

        pygame.draw.circle(
            pantalla,
            (255,220,0),
            (400,280),
            100
        )

        pygame.draw.circle(
            pantalla,
            (255,255,255),
            (360,240),
            25
        )

        pygame.draw.circle(
            pantalla,
            (255,255,255),
            (440,240),
            25
        )

        pygame.draw.circle(
            pantalla,
            (0,0,0),
            (360,240),
            10
        )

        pygame.draw.circle(
            pantalla,
            (0,0,0),
            (440,240),
            10
        )

        pygame.draw.circle(
            pantalla,
            (255,150,150),
            (330,290),
            15
        )

        pygame.draw.circle(
            pantalla,
            (255,150,150),
            (470,290),
            15
        )

        pygame.draw.arc(
            pantalla,
            (0,0,0),
            (330,260,140,100),
            0.2,
            3.0,
            5
        )
    elif principio == 13:

        texto = fuente.render(
            "Video Stop Motion",
            True,
            (0, 0, 0)
        )
        pantalla.blit(texto, (20, 20))

        ret, frame = video.read()

        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            ret, frame = video.read()

        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            frame = cv2.resize(
                frame,
                (600, 400)
            )

            superficie = pygame.surfarray.make_surface(
                frame.swapaxes(0, 1)
            )

            pantalla.blit(
                superficie,
                (100, 100)
            )

    # ==========================================
    # INFORMACION
    # ==========================================

    info = fuente.render(
        "1-9 = Principios 1-9 | F1=10 | F2=11 | F3=12 | F4=Video Stop Motion",
        True,
        (0,0,0)
    )

    pantalla.blit(info,(20,550))

    t += 0.03

    pygame.display.flip()
    reloj.tick(60)