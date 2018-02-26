Name: ru_tts
Version: 20110405
Release: alt1
Packager: Michael Pozhidaev <msp@altlinux.ru>

Summary: %name is a russian text-to-speech tool
Summary(ru_RU.UTF-8): Синтезатор русской речи
Group: Sound
License: non-free
Url: ftp://ftp.rakurs.spb.ru:/pub/Goga/projects/speech-interface/

Requires: tts-base
Requires: %name-data
BuildRequires: rpm-macros-tts

Source: %name.static.bz2
Source1: lexicon.bz2
Source2: permission.txt
Source3: %name.voiceman
Source4: replacements.%name

%package data
Summary: Lexicon file for %name speech synthesizer
Summary(ru_RU.UTF-8): Словарь ударений для синтезатора ru_tts
License: non-free
Group: Sound 
BuildArch: noarch

%description
%name is a speech synthesizer for russian language written by Igor B. Poretsky.
It produces speech output with stress processing. Lexicon file is stored as /usr/share/ru_tts/lexicon.
Text input should be sent to the stdin of ru_tts in koi8-r encoding. The format of the output is 10000, 8but mono.

%description -l ru_RU.UTF-8
ru_tts - это синтезатор русской речи, разработанный Игорем
Порецким. ru_tts произносит слова с расстановкой ударений, используя
словарь, который разположенв /usr/share/ru_tts/lexicon. Текст для
обработки должен поступать на стандартный поток ввода в кодировке koi8-r, и речь будет
синтезирована как PCM данные в формате 8-бит, моно с частотой
дискретизации 10000Гц.

%description data
This package contains dictionary for stress processing.

%description -l ru_RU.UTF-8 data
Этот пакет содержит словарь ударений для синтезатора русской речи ru_tts.

%prep
%build
%__cp %SOURCE2 ./permission.txt
%install
%__install -d %buildroot%_bindir
bunzip2 < %SOURCE0 > %buildroot%_bindir/%name
%__install -d %buildroot%_datadir/ru_tts
bunzip2 < %SOURCE1 > %buildroot%_datadir/ru_tts/lexicon
chmod 755 %buildroot%_bindir/%name
chmod 644 %buildroot%_datadir/ru_tts/lexicon
%__install -pD -m 644 %SOURCE3 %buildroot%_ttsdir/%name.voiceman
%__install -pD -m 644 %SOURCE4 %buildroot%_datadir/%name/replacements.%name

%preun
%tts_unregister ru_tts

%files
%_bindir/*
%_ttsdir/*
%doc permission.txt

%files data
%_datadir/ru_tts

%changelog
* Tue Apr 05 2011 Michael Pozhidaev <msp@altlinux.ru> 20110405-alt1
- Removed old version
- tts-devel buildreq replaced by rpm-macros-tts

* Wed Dec 22 2010 Michael Pozhidaev <msp@altlinux.ru> 20101222-alt1
- Temporarily added old synthesizer binary

* Fri Nov 26 2010 Michael Pozhidaev <msp@altlinux.ru> 20101126-alt1
- VoiceMan configuration entry updated for VoiceMan version 1.5.0
- Package ru_tts-lexicon renamed to ru_tts-data

* Thu Dec 11 2008 Michael Pozhidaev <msp@altlinux.ru> 20081211-alt1
- Lexicon file moved to the separate noarch subpackage
- Added more legal permission from the author (Igor Poretsky)
- Added Russian descriptions

* Fri Sep 05 2008 Michael Pozhidaev <msp@altlinux.ru> 20080905-alt1
- Added VoiceMan configuration file

* Wed Sep 20 2006 Michael Pozhidaev <msp@altlinux.ru> 1.0-alt1
- initial rpm
