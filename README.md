# HashIdentifier

**HashIdentifier** es una herramienta escrita en **Python** que permite **identificar el tipo de hash** a partir de una cadena hash, basándose en su **longitud y formato**.

Es una utilidad muy común en el mundo del **hacking**, **CTFs** y **seguridad informática**, especialmente como paso previo al cracking de hashes.

---

## Características

- Identificación automática de hashes
- Detección basada en longitud y formato
- Soporte para hashes comunes:
  - MD5
  - SHA1
  - SHA256
  - SHA512
  - NTLM
  - MySQL (antiguo)
- Interfaz estética en consola (colores + banner)
- Validación de entrada (no permite hashes vacíos)
- Bucle interactivo (permite identificar varios hashes sin cerrar)
- Código limpio y fácil de ampliar
