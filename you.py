from pytube import YouTube

try:
    # URL completa do vídeo
    url = 'https://www.youtube.com/watch?v=YV_JQmZNFsk'

    # Cria o objeto YouTube
    video = YouTube(url)

    # Exibe informações do vídeo (para verificar se carregou corretamente)
    print(f"Título: {video.title}")
    print(f"Autor: {video.author}")
    print(f"Duração: {video.length} segundos")

    # Seleciona a maior qualidade disponível
    stream = video.streams.get_highest_resolution()

    # Baixa o vídeo
    stream.download(output_path='C:\\Users\\guisi\\Videos\\Captures', filename='video.mp4')

    print("Download concluído!")

except Exception as e:
    print(f"Erro ao tentar baixar o vídeo: {e}")

