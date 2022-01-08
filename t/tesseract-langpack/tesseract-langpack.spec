%define srcName tessdata_fast
%define tess tesseract

Name: tesseract-langpack
Version: 4.1.0
Release: alt1

Summary: Fast versions of trained LSTM models for Tesseract OCR
Summary(ru_RU.UTF-8): Быстрые версии обученных моделей LSTM для Tesseract OCR

License: Apache-2.0
Group: Graphics
Url: https://github.com/tesseract-ocr/tessdata_fast

Packager: Evgeny Chuck <koi at altlinux.org>

# Source-url: https://github.com/tesseract-ocr/tessdata_fast/archive/refs/tags/%version.tar.gz
Source: tessdata_fast-%version.tar.gz

BuildArch: noarch

%description
These models only work with the LSTM OCR engine of Tesseract 4 or higher.
These are a speed/accuracy compromise as to what offered the data_best.

%description -l ru_RU.UTF-8
Эти модели работают только с движком LSTM OCR Tesseract 4 или выше.
Это компромисс между скоростью и точностью в отношении того, что предлогает
версия "data_best".

# technical packages
%package osd
Summary: Orientation & Script Detection Data for %tess
Summary(ru_RU.UTF-8): Ориентация и данные обнаружения скриптов для %tess
Group: Graphics
BuildArch: noarch
Requires: %tess >= %version
Requires: %name-doc = %version

%description osd
Orientation & Script Detection data for the Tesseract Open Source OCR Engine.

%description osd -l ru_RU.UTF-8
Данные ориентации и обнаружения скриптов для движка распознавания текста
с открытым исходным кодом Tesseract.

%package equ
Summary: Equation traineddata for %tess
Summary(ru_RU.UTF-8): Модель для обнаружения математических уравнений
Group: Graphics
BuildArch: noarch
Requires: %tess >= %version
Requires: %name-doc = %version

%description equ
Data for processing images of mathematics with the Tesseract Open Source OCR Engine.

%description equ -l ru_RU.UTF-8
Данные для обработки изображений математических символов с использованием
Tesseract Open Source OCR Engine.

# replacement of obsolete language packs
%package da
Group: Graphics
Summary: Danish language data for Tesseract (fast models)
Summary(ru_RU.UTF-8): Датский языковые файлы для Tesseract (быстрые модели)
BuildArch: noarch
Requires: %tess >= %version
Requires: %name-doc = %version
Provides: langpack-da-frak = %EVR
Obsoletes: langpack-da-frak <= %EVR

%description da
Tesseract data files required to recognize Danish text.

%description da -l ru_RU.UTF-8
Обученная языковая модель Датский для движка распознавания текста Tesseract.

%package de
Group: Graphics
Summary: German language data for Tesseract (fast models)
Summary(ru_RU.UTF-8): Немецкий языковые файлы для Tesseract (быстрые модели)
BuildArch: noarch
Requires: %tess >= %version
Requires: %name-doc = %version
Provides: langpack-de-frak = %EVR
Obsoletes: langpack-de-frak <= %EVR

%description de
Tesseract data files required to recognize German text.

%description de -l ru_RU.UTF-8
Обученная языковая модель Немецкий для движка распознавания текста Tesseract.

%package fl
Group: Graphics
Summary: Philippine language data for Tesseract (fast models)
Summary(ru_RU.UTF-8): Филиппинский языковые файлы для Tesseract (быстрые модели)
BuildArch: noarch
Requires: %tess >= %version
Requires: %name-doc = %version
Provides: langpack-tl = %EVR
Obsoletes: langpack-tl <= %EVR

%description fl
Tesseract data files required to recognize Philippine text.

%description fl -l ru_RU.UTF-8
Обученная языковая модель Филиппинский для движка распознавания текста Tesseract.

%package doc
Summary: Documentation for Language Packages Tesseract OCR
Summary(ru_RU.UTF-8): Документация для языковых пакетов Tesseract OCR
Group: Documentation
BuildArch: noarch

%description doc
The documentation contains license files for the LSTM language models.

%description doc -l ru_RU.UTF-8
Документация содержит файлы лицензий для языковых моделей LSTM.

# description and packaging of language files
%define langdata() \
%package %2\
Group: Graphics \
Summary: %3%{?5: %5}%{?6: %6} language data for Tesseract (fast models) \
Summary(ru_RU.UTF-8): %4%{?5: %5}%{?6: %6} языковые файлы для Tesseract (быстрые модели) \
Requires: %tess >= %version \
BuildArch: noarch \
Requires: %name-doc = %version \
%description %2 \
Tesseract data files required to recognize %3%{?5: %5}%{?6: %6} text. \
%description %2 -l ru_RU.UTF-8 \
Обученная языковая модель %4%{?5: %5}%{?6: %6} для движка распознавания текста Tesseract. \
%files %2 \
%_datadir/%tess/tessdata/%1.* \
%nil
# end

# list of language packs
%langdata afr af Afrikaans Африкаанс
%langdata amh am Amharic Амхарский
%langdata ara ar Arabic Арабский
%langdata asm as Assamese Ассамский
%langdata aze_cyrl az_cyrl Azerbaijani Азербайджанский (Cyrillic)
%langdata aze az Azerbauijani Азербайджанский
%langdata bel be Belarusian Белорусский
%langdata ben bn Bengali Бенгальский
%langdata bod bo Tibetan Тибетский Standard
%langdata bos bs Bosnian Боснийский
%langdata bul bg Bulgarian Болгарский
%langdata cat ca Catalan Каталонский
%langdata ceb ceb Cebuano Себуано
%langdata ces cs Czech Чешский
%langdata chi_sim zh_CN Chinese Китайский (Simplified)
%langdata chi_tra zh_TW Chinese Китайский (Traditional)
%langdata chr chr Cherokee Чероки
%langdata cym cy Welsh Валлийский
%langdata dzo dz Dzongkha Дзонгка
%langdata ell el Greek Греческий
%langdata eng en English Английский
%langdata enm en_mdl English Английский Middle (1100-1500)
%langdata epo eo Esperanto Эсперанто
%langdata est et Estonian Эстонский
%langdata eus eu Basque Баскский
%langdata fas fa Persian Персидский
%langdata fin fi Finnish Финский
%langdata fra fr French Французский
%langdata frk frk Frankish Франкский
%langdata frm frm French Французский Middle (1400-1600)
%langdata gle ga Irish Ирландский
%langdata glg gl Galician Галицкий
%langdata grc grc Ancient_Greek Древнегреческий
%langdata guj gu Gujarati Гуджарати
%langdata hat hat Haitian Гаитянский
%langdata heb he Hebrew Иврит
%langdata hin hi Hindi Хинди
%langdata hrv hr Croation Хорватский
%langdata hun hu Hungarian Венгерский
%langdata iku iu Inuktitut Инуктитут
%langdata ind id Indonesian Индонезийский
%langdata isl is Icelandic Исландский
%langdata ita_old it_old Italian Итальянский Old
%langdata ita it Italian Итальянский
%langdata jav jv Javanese Яванский
%langdata jpn ja Japanese Японский
%langdata kan kn Kannada Каннада
%langdata kat_old ka_old Georgian Грузинский Old
%langdata kat ka Georgian Грузинский
%langdata kaz kk Kazakh Казахский
%langdata khm km Khmer Кхмерский
%langdata kir ky Kyrgyz Киргизский
%langdata kor ko Korean Корейский
%langdata lao lo Lao Лаосский
%langdata lat la Latin Латинский
%langdata lav lv Latvian Латышский
%langdata lit lt Lithuanian Литовский
%langdata mal ml Malayalam Малаялам
%langdata mar mr Marathi Маратхи
%langdata mkd mk Macedonian Македонский
%langdata mlt mt Maltese Мальтийский
%langdata msa ms Malay Малайский
%langdata mya my Burmese Бирманский
%langdata nep ne Nepali Непальский
%langdata nld nl Dutch Нидерландский
%langdata nor nn Norwegian Норвежский
%langdata ori or Oriya Ория
%langdata pan pa Punjabi Пенджаби
%langdata pol pl Polish Польский
%langdata por pt Portuguese Португальский
%langdata pus ps Pashto Пушту
%langdata ron ro Romanian Румынский
%langdata rus ru Russian Русский
%langdata san sa Sanskrit Санскрит
%langdata sin si Sinhala Сингальский
%langdata slk sk Slovakian Словацкий
%langdata slv sl Slovenian Словенский
%langdata spa_old es_old Spanish Испанский Old
%langdata spa es Spanish Испанский
%langdata sqi sq Albanian Албанский
%langdata srp_latn sr_latn Serbian Сербский Latin
%langdata srp sr Serbian Сербский
%langdata swa sw Swahili Суахили
%langdata swe sv Swedish Шведский
%langdata syr syr Syriac Сирийский
%langdata tam ta Tamil Тамильский
%langdata tel te Telugu Телугу
%langdata tgk tg Tajik Таджикский
%langdata tha th Thai Тайский
%langdata tir ti Tigrinya Тигринья
%langdata tur tr Turkish Турецкий
%langdata uig ug Uyghur Уйгурский
%langdata ukr uk Ukrainian Украинский
%langdata urd ur Urdu Урду
%langdata uzb_cyrl uz_cyrl Uzbek Узбекский (Cyrillic)
%langdata uzb uz Uzbek Узбекский
%langdata vie vi Vietnamese Вьетнамский
%langdata yid yi Yiddish Идиш
%langdata bre br Breton Бретонский
%langdata chi_sim_vert chi_sim_vert Chinese Китайский (Simplified)
%langdata chi_tra_vert chi_tra_vert Chinese Китайский (Tradizionale)
%langdata cos co Corsican Корсиканский
%langdata div dv Divehi Дивехи (Maldivian)
%langdata fao fo Faroese Фарерские_острова
%langdata fry fy Frisian Фризский
%langdata gla gd Gaelic Гэльский
%langdata hye hy Armenian Армянский
%langdata jpn_vert ja_vert Japanese Японский (Vertical)
%langdata kmr kmr Northern_Kurdish Северокурдский
%langdata kor_vert ko_vert Korean Корейский (Vertical)
%langdata ltz lb Luxembourgish Люксембургский
%langdata mon mn Mongolian Монгольский
%langdata mri mi Maori Маори
%langdata oci oc Occitan Окситанский
%langdata que qu Quechua Кечуа
%langdata snd sd Sindhi Синдхи
%langdata sun su Sundanese Суданский
%langdata tat tt Tatar Татарский
%langdata ton to Tongan Тонга
%langdata yor yo Yoruba Йоруба

%prep
%setup -n %srcName-%version

%build
%install
mkdir -p %buildroot/%_datadir/%tess/tessdata
cp *.traineddata %buildroot/%_datadir/%tess/tessdata

%files doc
%doc README.md LICENSE

%files osd
%_datadir/%tess/tessdata/osd.traineddata

%files equ
%_datadir/%tess/tessdata/equ.traineddata

%files da
%_datadir/%tess/tessdata/dan.traineddata

%files de
%_datadir/%tess/tessdata/deu.traineddata

%files fl
%_datadir/%tess/tessdata/fil.traineddata

%changelog
* Fri Dec 31 2021 Evgeny Chuck <koi@altlinux.org> 4.1.0-alt1
- Update of LSTM language models for Tesseract OCR
