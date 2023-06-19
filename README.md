# Aplicación de Streamlit

Esta es una aplicación de Streamlit escrita en Python que utiliza la biblioteca Streamlit para interactuar con la API de OpenAI y realizar diversas tareas de procesamiento de lenguaje natural.

## **Instalación**

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python instalado. Se recomienda utilizar Python 3.7 o una versión posterior.
3. Instala las dependencias utilizando el siguiente comando:
    
    ```bash
    pip install -r requirements.tx
    ```
    
4. Configura la API de OpenAI proporcionando tu clave de API en el archivo **`app.py`**. Reemplaza la variable **`_open_ai_api_key`** con tu propia clave de API.

## **Uso**

1. Ejecuta la aplicación utilizando el siguiente comando:
    
    ```bash
    streamlit run app.py
    ```
    
2. Se abrirá una ventana del navegador con la aplicación de Streamlit. Verás una barra lateral en la que puedes configurar los parámetros de la API de OpenAI, como el modelo a utilizar, el número máximo de tokens y la temperatura.
3. La aplicación tiene varias pestañas que realizan diferentes tareas de procesamiento de lenguaje natural, como resumir texto, inferir sentimientos y transformar texto. Haz clic en cada pestaña para acceder a las diferentes funcionalidades.
4. Sigue las instrucciones en la aplicación para ingresar el texto de entrada y realizar las tareas deseadas. Algunas tareas pueden requerir la selección de opciones adicionales, como el límite de palabras o el idioma de traducción.
5. Una vez que hayas ingresado los datos requeridos, haz clic en los botones correspondientes para ejecutar las tareas. La aplicación llamará a la API de OpenAI y mostrará los resultados en la interfaz de la aplicación.

## **Contribución**

Si deseas contribuir a este proyecto, puedes seguir los pasos a continuación:

1. Realiza un fork de este repositorio.
2. Crea una rama para tu nueva característica:
    
    ```bash
    git checkout -b nueva-caracteristica
    ```
    
3. Realiza los cambios necesarios y realiza commit de tus modificaciones:
    
    ```bash
    git commit -m "Agrega nueva característica"
    ```
    
4. Envía tus cambios al repositorio remoto:
    
    ```bash
    git push origin nueva-caracteristica
    ```
    
5. Abre una solicitud de extracción en GitHub.

## **Créditos**

- Esta aplicación utiliza la biblioteca Streamlit (**[https://streamlit.io/](https://streamlit.io/)**) para la creación de la interfaz de usuario.
- La comunicación con la API de OpenAI se realiza utilizando la biblioteca **`openai`** (**[https://github.com/openai/openai-python](https://github.com/openai/openai-python)**).

## **Licencia**

Este proyecto se encuentra bajo la licencia **[MIT](https://chat.openai.com/LICENSE)**.