%def_with portaudio

# do not enable;
# a part of msp@work in progress for 1.45;
# should be adopted first to espeak 1.48
# to be used together with pulseaudio (a-la runtime)
%def_without libao

Name: espeak
Version: 1.48.04
Release: alt3.2

Summary: %name is a software speech synthesizer for English and other languages
Summary(ru_RU.UTF-8): Программный синтезатор речи для английского и других языков
Group: Sound
License: %gpl3plus
URL: http://espeak.sourceforge.net

Requires: tts-base

# Automatically added by buildreq on Fri Aug 21 2009
BuildRequires: gcc-c++ unzip

BuildRequires: rpm-macros-tts rpm-build-licenses

Source0: http://downloads.sourceforge.net/%{name}/%name-%version-source.zip
Source1: %name.replacements
Source2: russian_data.zip
Source3: wave_ao.cpp
Source4: espeak.voiceman
Source5: espeak-ru.voiceman

# found in fedora espeak 1.48.04-21.fc35
# Upstream ticket: https://sourceforge.net/p/espeak/patches/10/
Source7:        espeak.1
Patch0:         espeak-1.47-makefile-nostaticlibs.patch
Patch1:         espeak-1.47-ftbs-ld-libm.patch
# Upstream ticket: https://sourceforge.net/p/espeak/patches/10/
Patch2:         espeak-1.48-help-fix.patch
# Upstream ticket: https://sourceforge.net/p/espeak/bugs/105/
Patch3:         espeak-1.47-wav-close.patch
Patch4:         espeak-1.48-gcc-6-fix.patch
# Upstream-accepted patch (to the new fork espeak-ng)
# https://github.com/espeak-ng/espeak-ng/commit/7659aaa2e88cc0401d032d04602731ca45070fab
Patch5:         espeak-1.48-read-fifo.patch

Patch11: %name-1.48-alt-libao.patch

BuildRequires:  libpulseaudio-devel
%define backend pulseaudio
%if_with portaudio
BuildRequires:  libportaudio2-devel
%define backend runtime
%endif
%if_with libao
BuildRequires: libao-devel
%define backend ao
%endif

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
#Requires: %name-data = %version-%release
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
в работе синтезатором %name.

%prep
%setup -q -n %name-%version-source

# Fix file permissions in upstream tarball
find . -type f -exec chmod 0644 {} \;

mv docs html
sed -i 's/\r//' License.txt

# To enable portaudio19 and newer using instead of portaudio18;
rm -f ./src/portaudio.h
mv ./src/portaudio19.h ./src/portaudio.h

# Don't use the included binary voice dictionaries; we compile these from source
rm -f espeak-data/*_dict

%patch0 -p1 -b .nostaticlibs
%patch1 -p1 -b .ftbs-ld-libm
%patch2 -p1 -b .help-fix
%patch3 -p1 -b .wav-close
%patch4 -p1 -b .1.48-gcc-6-fix
%patch5 -p1 -b .read-fifo

%if_with libao
%patch11 -p1
cp %SOURCE3 ./src
%endif

unzip %SOURCE2
mv russian_data/ru_listx dictsource/

%build
cd src
%make_build CXXFLAGS="%optflags" AUDIO=%backend

# Compile the TTS voice dictionaries
export ESPEAK_DATA_PATH=%_builddir/espeak-%{version}-source
cd ../dictsource
# Strange sed regex to parse ambiguous output from 'speak --voices', filled upstream BZ 3608811
for voice in $(../src/speak --voices | \
LANG=C sed -n '/Age\/Gender/ ! s/ *[0-9]\+ *\([^ ]\+\) *M\? *[^ ]\+ *\(\((\|[A-Z]\)[^ ]\+\)\? *\([^ ]\+\).*/\1 \4/ p' | \
sort | uniq); do \
    ../src/speak --compile=$voice; \
done
# for ru_listx above; no need, for we compile all langs
#../src/speak --compile=ru

%install
cd src
make DESTDIR=$RPM_BUILD_ROOT LIBDIR=%_libdir install
cd ..
install -pD -m 644 %SOURCE4 %buildroot%_ttsdir/espeak.voiceman
install -pD -m 644 %SOURCE5 %buildroot%_ttsdir/espeak-ru.voiceman
install -pD -m 644 %SOURCE1 %buildroot%_datadir/espeak-data/replacements
install -pD -m 644 %SOURCE7 %buildroot%_man1dir/espeak.1

# altbug #41463
# from espeak-1.46 to espeak-1.47 voices/en changed from dir to a file
mv %buildroot%_datadir/%name-data/voices/en{,-gb}

%if "%version" == "1.48.04"
# no need to return voices/en back for now, it works as is
%else
# voices/en was renamed to voices/en-gb; see #41463.
# It works for 1.48.04, but for the new version test w/and w/o %post"
exit 1
%post data
# Hack for 1.44 -> 1.48: voices/en from dir to file
if [ -d %_datadir/%name-data/voices/en ]
then
  rm -rf %_datadir/%name-data/voices/en
fi
ln -s en-gb %_datadir/%name-data/voices/en ||:
%endif

%preun
%tts_unregister espeak
%tts_unregister espeak-ru

#%files
#doc ChangeLog.txt License.txt ReadMe html
#%_bindir/espeak
#%_man1dir/espeak.1*
#%_ttsdir/*

#%files data
#%_datadir/espeak-data

%files -n lib%name
%_libdir/libespeak.so.*

# use espeak-ng-devel
#%files -n lib%name-devel
#%_includedir/espeak
#%_libdir/libespeak.so

%changelog
* Thu Jul 25 2024 Sergey V Turchin <zerg@altlinux.org> 1.48.04-alt3.2
- NMU: don't espeak subpackage to push espeak-ng

* Wed Jun 26 2024 Sergey V Turchin <zerg@altlinux.org> 1.48.04-alt3.1
- NMU: don't package devel subpackage to push espeak-ng-devel

* Mon Nov 29 2021 Igor Vlasenko <viy@altlinux.org> 1.48.04-alt3
- upgrade fix thanks to andy@ (closes: #41463)

* Mon Nov 29 2021 Igor Vlasenko <viy@altlinux.org> 1.48.04-alt2
- %%pre check for voices/en/ (closes: #41463)

* Sun Nov 28 2021 Igor Vlasenko <viy@altlinux.org> 1.48.04-alt1
- new version
- picked from orphaned

* Sat Dec 05 2020 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.44.05-alt5
- libespeak-devel: Do not pack libespeak.a to pass sisyphus_check
- spec: Remove packager field.

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
