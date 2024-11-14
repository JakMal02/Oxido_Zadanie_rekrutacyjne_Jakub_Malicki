Program jest aplikacją konsolową.

Działa w następujący sposób:

iportuje bibliotekę openai
importuje bibliotekę do odczytywania indywidualnych zmiennych środowiskowych, w tym przypadku mojego klucza do API OpenAI.
Klucz jest przechowywany w pliku .env
Plik jest wyłączony z udostępniania za pomocą .gitignore w celu bezpieczeństwa.

Program ustawia jak bot ma się zachowywać (jaką ma mieć rolę). Ustawiłem, żeby był pomocnym asytentem, bo tak zauważyłem, że działa to najlepiej.

W kolejnych linijkach kodu program otwiera pliki tresc_artykulu.txt, w którym znajduje się treść artykułu skopiowana z zadania oraz prompt.txt, w tym pliku znajduje się napisany przeze mnie prompt jakiego chatGPT ma użyć do uzyskania wyniku określonego w poleceniu.
Zastosowałem taką metodę w celu zachowania czystości i przejrzystości kodu. Połączyłem oba pliki w jedną zmienną, którą później będę przekazywać do chatuGPT

Kolejnym etapem jest prosta instrukcja sprawdzająca, czy faktycznie użytkownik chce dokonać generacji odpowiedzi przez ChatGPT.
Zastosowałem to w celu prostego zabezpieczenia przed przypadkowym uruchomieniem, żeby od razu nie było wysyłane zapytanie do bota, dzięki czemu nie będą się przypadkowo marnować tokeny.

Później wypisuje w terminalu prompt wraz z artykułem, jako wiadomość wprowadzoną od użytkownika.

Kolejnym krokiem jest już wywołanie zapytania do bota. Wykorzystuję tu model chatu 4o, zauważyłem, że stosunek użytych tokenów do satysfakcjonującej odpowiedzi jest najbardziej optymalny.

Tutaj odpoweidź od ChatuGPT również wyświetlam na ekranie w terminalu.

Następnie zapisuję wygenerowaną odpowiedź do pliku artykul.html (jeśli nie ma takiego pliku w folderze utworzyłby się). Dodałem szyfrowanie utf-8 w celu możliwości zapisu polskich znaków.

Kolejne linijki kodu są do sprawdzenia błędów, poinformowaniu o tym użytkownika oraz zamknięcia otwartych plików w celu uwolnienia pamięci.
