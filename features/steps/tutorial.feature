#Укажем что это за фича
Feature: Авто переходы ютуб
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: Поисковой запрос и переходы по вкладкам с проверкой инофрмации в профиле
#И используем наши шаги.
  Given website "youtube.com"
  Then push button with text 'Открываем видео переходим по вкладкам канала'
  Then page include text 'Проверяем что страница не пустая'