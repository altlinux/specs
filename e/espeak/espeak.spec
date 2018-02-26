
Name: espeak
Version: 1.44.05
Release: alt4
Packager: Michael Pozhidaev <msp@altlinux.org>

Summary:%name is a software speech synthesizer for English and other languages
Summary(ru_RU.UTF-8): Программный синтезатор речи для английского и других языков 
Group: Sound
License: %gpl3plus
URL:http://espeak.sourceforge.net

Requires: tts-base

# Automatically added by buildreq on Fri Aug 21 2009
BuildRequires: gcc-c++ unzip

BuildRequires: rpm-macros-tts rpm-build-licenses libao-devel

Source: %name-%version-source.zip
Source1: %name.replacements
Source2: russian_data.zip
Source3: %name-dict.mak
Source4: espeak.voiceman
Source5: espeak-ru.voiceman
Source6: wave_ao.cpp

Patch1: %name-alt-libao.patch

%description
%name is a software text-to-speech tool. It produces speech in enlish
and other languages. Currently it contains the preliminary
implementation of Russian text processing. It uses a different
synthesis method from other open source TTS engines, and sounds quite
different.  It's perhaps not as natural or "smooth", but the
articulation clearer and easier to listen to for long periods.

%description -l ru_RU.UTF-8
Espeak - программный синтезатор речи, подготовленный разработчиком из
Великобритании - Джонатаном Даддингтоном. В основе этого синтезатора
лежат наиболее удачные алгоритмы других свободных разработок. Espeak
способен синтезировать речь на анг. и других языках. Поддержка
русского языка присутствует в начальном варианте.

%package -n lib%name
License: %gpl3plus
Summary: This is a shared library which contains the espeak's text to speech engine
Summary(ru_RU.UTF-8): Динамически подключаемая библиотека с реализацией системы синтеза речи espeak
Group: Sound
Requires: %name-data = %version-%release
%description -n lib%name
This package contains the shared library with text-to-speech
engine. This library is used in 'speak' TTS tool. 

%description -l ru_RU.UTF-8 -n lib%name
Динамически подключаемая библиотека, содержащая
реализацию синтеза речи проекта espeak.

%package -n lib%name-devel
Summary: Library headers for libespeak
License: %gpl3plus
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Library headers for libespeak.
Install this package if you want
to build applications with libespeak.

%package data
Group: Sound
Summary: Data files used to generate speech by espeak
Summary(ru_RU.UTF-8): Вспомогательные данные для работы синтезатора espeak
BuildArch: noarch
License: %gpl3plus

%description data 
This package contains  architecture-independent 
data used by espeak speech synthesizer.

%description -l ru_RU.UTF-8 data
Вспомогательные данные о языках, используемые 
в работе синтезатором%name.

%prep
%setup -q -n %name-%version-source
%patch1 -p1
# To enable portaudio19 and newer using instead of portaudio18;
%__rm -f ./src/portaudio.h
%__mv ./src/portaudio19.h ./src/portaudio.h

%__cp %SOURCE6 ./src

%build
cp %SOURCE2 ./
unzip russian_data.zip
mv russian_data/ru_listx dictsource/
cd src
cp %SOURCE3 ./dict.mak
make -f dict.mak
cd ../dictsource
../src/speak --compile=ru
cd ../src
make clean
%make_build CXXFLAGS="%optflags"
cd ..

%install
cd src
make DESTDIR=$RPM_BUILD_ROOT LIBDIR=%_libdir install
cd ..
%__install -pD -m 644 %SOURCE4 %buildroot%_ttsdir/espeak.voiceman
%__install -pD -m 644 %SOURCE5 %buildroot%_ttsdir/espeak-ru.voiceman
%__install -pD -m 644 %SOURCE1 %buildroot%_datadir/espeak-data/replacements

%preun
%tts_unregister espeak
%tts_unregister espeak-ru

%files
%_bindir/*
%_ttsdir/*
%doc ChangeLog.txt docs License.txt ReadMe

%files data
%_datadir/espeak-data

%files -n lib%name
%_libdir/libespeak.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/libespeak.a
%_libdir/libespeak.so

%changelog
* Mon Aug 29 2011 Michael Pozhidaev <msp@altlinux.ru> 1.44.05-alt4
- Experimental build with libao instead of portaudio

* Tue Apr 05 2011 Michael Pozhidaev <msp@altlinux.ru> 1.44.05-alt3
- tts-devel buildreq replaced by rpm-macros-tts
- Added tts_unregister call to preun

* Wed Oct 06 2010 Michael Pozhidaev <msp@altlinux.ru> 1.44.05-alt2
- Removed espeak-ru script
- Added VoiceMan replacements file
- Spec clean up

* Fri Oct 01 2010 Michael Pozhidaev <msp@altlinux.ru> 1.44.05-alt1
- Updated to 1.44.05
- Updated VoiceMan configuration files for voiceman-1.5.0

* Fri Aug 21 2009 Michael Pozhidaev <msp@altlinux.ru> 1.39-alt2
- Removed libportaudio using (no longer supported in ALT Linux)

* Thu Dec 11 2008 Michael Pozhidaev <msp@altlinux.ru> 1.39-alt1
- New version
- Data files moved to noarch subpackage
- Removed ldconfig calls
- Added Russian descriptions

* Mon Sep 08 2008 Michael Pozhidaev <msp@altlinux.ru> 1.37-alt2
- Added voiceman compatibility files

* Sun Aug 03 2008 Michael Pozhidaev <msp@altlinux.ru> 1.37-alt1
- New version

* Sat Dec 29 2007 Michael Pozhidaev <msp@altlinux.ru> 1.29-alt3
- /usr/lib/espeak.so moved to espeak-devel

* Wed Dec 26 2007 Michael Pozhidaev <msp@altlinux.ru> 1.29-alt2
- Fixed compilation for x86_64

* Wed Dec 26 2007 Michael Pozhidaev <msp@altlinux.ru> 1.29-alt1
- new version and fixed libespeak.so bug

* Sat Aug 18 2007 Michael Pozhidaev <msp@altlinux.ru> 1.28-alt1
- Splitted for creating libespeak-devel.

* Fri Apr 27 2007 Michael Pozhidaev <msp@altlinux.ru> 1.22.05-alt1
- Added stress dictionary

* Mon Mar 26 2007 Michael Pozhidaev <msp@altlinux.org> 1.21.11-alt1
- initial rpm
