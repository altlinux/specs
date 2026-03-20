%define _unpackaged_files_terminate_build 1

%define audiosover 2
%define coresover 10
%define sover 5
%define progectlicense GPL-2.0

Name:    RHVoice
Version: 1.18.3
Release: alt1

Summary: a free and open source speech synthesizer for Russian and other languages
License: %progectlicense
Group: Sound
Url: https://github.com/RHVoice/RHVoice
VCS: https://github.com/RHVoice/RHVoice.git

Source: %name-%version.tar

BuildRequires: scons
BuildRequires: gcc-c++        
BuildRequires: libgio-devel
BuildRequires: pkg-config
BuildRequires: libpulseaudio-devel
BuildRequires: libao-devel
BuildRequires: libportaudio2-devel
BuildRequires: libspeechd-devel
BuildRequires: flite-devel
BuildRequires: boost-devel
BuildRequires: libsonic-devel

%description
RHVoice uses statistical parametric synthesis. It relies on existing open
 source speech technologies (mainly HTS and related software).
 .
 Voices are built from recordings of natural speech. They have small footprints,
 because only statistical models are stored on users' computers. And though
 the voices lack the naturalness of the synthesizers which generate speech
 by combining segments of the recordings themselves, they are still very
 intelligible and resemble the speakers who recorded the source material.


%package -n lib%name%sover
Summary: Lib files for %name
Group: System/Libraries
Provides: RHVoice = %EVR
Obsoletes: RHVoice < %EVR
Provides: libRHVoice = %EVR
Obsoletes: libRHVoice < %EVR

%description -n lib%name%sover
%summary

%files -n lib%name%sover
%_libdir/lib%name.so.%sover
%_libdir/lib%name.so.%sover.*
%dir %_sysconfdir/RHVoice/
%config(noreplace) %_sysconfdir/RHVoice/RHVoice.conf
%_libdir/speech-dispatcher-modules/sd_rhvoice

%package -n lib%{name}_audio%audiosover
Summary: Audio lib files for %name
Group: System/Libraries

%description -n lib%{name}_audio%audiosover
%summary

%files -n lib%{name}_audio%audiosover
%_libdir/lib%{name}_audio.so.%audiosover
%_libdir/lib%{name}_audio.so.%audiosover.*

%package -n lib%{name}_core%coresover
Summary: Core lib file for %name
Group: System/Libraries

%description -n lib%{name}_core%coresover
%summary

%files -n lib%{name}_core%coresover
%_libdir/lib%{name}_core.so.%coresover
%_libdir/lib%{name}_core.so.%coresover.*

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %EVR

%description -n lib%name-devel
Development files for %name

%files -n lib%name-devel
%_includedir/%name.h
%_includedir/%{name}_common.h
%_libdir/lib%name.so
%_libdir/lib%{name}_audio.so
%_libdir/lib%{name}_core.so

%package bin
Summary: Test bin for %name
Group: Other
Requires: %name = %EVR

%description bin
%summary

%files bin
%_bindir/*

%package doc
Summary: Doc for %name
Group: Other
BuildArch: noarch
Requires: %name = %EVR

%description doc
%summary

%files doc
%doc LICENSE.md README.md

# Languages

%define langpackage() \
%package %1 \
Summary: %1 language for  %name \
Group: Sound \
License: %2 \
BuildArch: noarch \
Requires: %name = %EVR \
\
%description %1 \
%1 language for  %name \
\
%files %1 \
%dir %_datadir/%name/languages/%1 \
%_datadir/%name/languages/%1/* \


%langpackage Russian GPL-2.0
%langpackage Belarusian GPL-2.0-or-later
%langpackage English GPL-2.0
%langpackage Albanian GPL-2.0
%langpackage Czech GPL-2.0
%langpackage Croatian GPL-3.0
%langpackage Esperanto GPL-2.0
%langpackage Georgian GPL-2.0
%langpackage Kyrgyz GPL-2.0
%langpackage Macedonian AGPL-3.0
%langpackage Polish GPL-2.0
%langpackage Serbian GPL-3.0
%langpackage Slovak LGPL-2.1
%langpackage Spanish LGPL-2.1
%langpackage Tatar GPL-2.0
%langpackage Ukrainian GPL-2.0
%langpackage Uzbek LGPL-2.1

%package Brazilian
Summary: Brazilian and Portuguese language for  %name
Group: Sound
BuildArch: noarch
Requires: %name = %EVR
Provides: %name-Portuguese = %EVR

%description Brazilian
%summary

%files Brazilian
%dir %_datadir/%name/languages/Brazilian-Portuguese
%_datadir/%name/languages/Brazilian-Portuguese/*


# voices

%define voicepackage() \
%define voicename %2 \
%{?4: %define voicename %4} \
%package %1-%voicename \
Summary: %1 %voicename voice for  %name \
Group: Sound \
License: %3 \
BuildArch: noarch \
Requires: %name-%1 = %EVR \
\
%description %1-%voicename \
%1 %voicename voice for  %name \
\
%files %1-%voicename \
%dir %_datadir/%name/voices/%2 \
%_datadir/%name/voices/%2/* \


# Russian

%voicepackage Russian aleksandr %progectlicense
%voicepackage Russian aleksandr-hq CC-BY-SA-4.0
%voicepackage Russian anna %progectlicense
%voicepackage Russian arina CC-BY-NC-ND-4.0
%voicepackage Russian artemiy CC-BY-NC-ND-4.0
%voicepackage Russian dasha-rus CC-BY-SA-4.0 dasha
%voicepackage Russian elena GPL-3.0
%voicepackage Russian evgeniy-rus CC-BY-NC-ND-4.0 evgeniy
%voicepackage Russian lyudmila-rus CC-BY-NC-SA-4.0 lyudmila
%voicepackage Russian irina %progectlicense
%voicepackage Russian mikhail CC-BY-NC-ND-4.0
%voicepackage Russian michal-rus CC-BY-NC-SA-4.0 michal
%voicepackage Russian pavel CC-BY-NC-ND-4.0
%voicepackage Russian ryhor-rus CC-BY-NC-SA-4.0 ryhor
%voicepackage Russian seva CC-BY-NC-ND-4.0
%voicepackage Russian tatiana CC-BY-NC-ND-4.0
%voicepackage Russian timofey CC-BY-NC-ND-4.0
%voicepackage Russian umka CC-BY-NC-ND-4.0
%voicepackage Russian victoria CC-BY-NC-ND-4.0
%voicepackage Russian vitaliy CC-BY-NC-ND-4.0
%voicepackage Russian vitaliy-ng CC-BY-NC-ND-4.0
%voicepackage Russian vsevolod CC-BY-NC-ND-4.0
%voicepackage Russian yuriy CC-BY-NC-ND-4.0


# belarusian

%voicepackage Belarusian alena-blr CC0-1.0 alena
%voicepackage Belarusian dasha-blr CC-BY-SA-4.0 dasha
%voicepackage Belarusian lyudmila-blr CC-BY-NC-SA-4.0 lyudmila
%voicepackage Belarusian michal-blr CC-BY-NC-SA-4.0 michal
%voicepackage Belarusian ryhor-blr CC-BY-NC-SA-4.0 ryhor


# English

%voicepackage English alan %progectlicense
%voicepackage English bdl %progectlicense
%voicepackage English clb %progectlicense
%voicepackage English dasha-eng CC-BY-SA-4.0 dasha
%voicepackage English evgeniy-eng CC-BY-NC-ND-4.0 evgeniy
%voicepackage English ksp RHVoice-Natia-License
%voicepackage English lyubov CC-BY-NC-ND-4.0
%voicepackage English slt CMU-License


# Albanian

%voicepackage Albanian hana CC-BY-NC-SA-4.0


# Brazilian-Portuguese

%package Brazilian-Leticia-F123
Summary: Brazilian and Portuguese Leticia-F123 voice for  %name
Group: Sound
License: CC-BY-SA-4.0
BuildArch: noarch
Requires: %name-Brazilian = %EVR
Provides: %name-Portuguese-Leticia-F123 = %EVR

%description Brazilian-Leticia-F123
%summary

%files Brazilian-Leticia-F123
%dir %_datadir/%name/voices/Leticia-F123
%_datadir/%name/voices/Leticia-F123/*


# Czech

%voicepackage Czech radek CC0-1.0
%voicepackage Czech zdenek CC0-1.0


# Croatian

%voicepackage Croatian karmela CC0-1.0
%voicepackage Croatian marija CC-BY-SA-4.0


# Esperanto

%voicepackage Esperanto spomenka GPL-3.0


# Georgian

%voicepackage Georgian natia  RHVoice-Natia-License


# Kyrgyz

%voicepackage Kyrgyz azamat %progectlicense
%voicepackage Kyrgyz nazgul %progectlicense


# Macedonian

%voicepackage Macedonian kiko CC-BY-NC-SA-4.0
%voicepackage Macedonian suze %progectlicense


# Polish

%voicepackage Polish alicja CC-BY-4.0
%voicepackage Polish cezary CC-BY-NC-ND-4.0
%voicepackage Polish magda CC-BY-4.0
%voicepackage Polish michal CC0-1.0
%voicepackage Polish natan CC0-1.0


# Serbian

%voicepackage Serbian dragana CC0-1.0


# Slovak

%voicepackage Slovak jasietka CC0-1.0
%voicepackage Slovak ondro CC0-1.0


# Spanish

%voicepackage Spanish Mateo unlicense


# Tatar

%voicepackage Tatar talgat RHVoice-Talgat-License


# Ukrainian

%voicepackage Ukrainian anatol LGPL-2.1
%voicepackage Ukrainian marianna CC-BY-ND-4.0
%voicepackage Ukrainian natalia LGPL-2.1
%voicepackage Ukrainian volodymyr CC-BY-ND-4.0


# Uzbek

%voicepackage Uzbek sevinch CC-BY-NC-SA-4.0
%voicepackage Uzbek dilnavoz CC-BY-NC-SA-4.0
%voicepackage Uzbek islom CC-BY-NC-SA-4.0

%prep
%setup

%build
scons \
  languages=all \
  voices=all \
  audio_libs=all \
  enable_sonic=True

%install
scons install \
  DESTDIR=%buildroot \
  prefix=%prefix \
  sysconfdir=%_sysconfdir \
  bindir=%_bindir \
  libdir=%_libdir \
  includedir=%_includedir \
  datadir=%_datadir \
  servicedir=default

%changelog
* Fri Mar 20 2026 Artem Semenov <savoptik@altlinux.org> 1.18.3-alt1
- Updated to new version 1.18.3

* Thu Mar 12 2026 Artem Semenov <savoptik@altlinux.org> 1.18.2-alt1
- Updated to new version 1.18.2
- Added libsonic support

* Wed Mar 11 2026 Artem Semenov <savoptik@altlinux.org> 1.18.1-alt2
- Fixed voice subpackage names (Closes: 58198)

* Sun Mar 01 2026 Artem Semenov <savoptik@altlinux.org> 1.18.1-alt1
- Updated to new version 1.18.1
- Added new croatian voice marija
- Added new russian voices
- Added new dasha voice for english
- Packaged belarusian voices

* Tue May 06 2025 Artem Semenov <savoptik@altlinux.org> 1.16.5-alt1
- Packaged new voices and languages
- Updated to 1.16.5

* Sat Aug 31 2024 Artem Semenov <savoptik@altlinux.org> 1.14.0-alt2
- - Obsoleted old RHVoice packages

* Tue Jul 16 2024 Artem Semenov <savoptik@altlinux.org> 1.14.0-alt1
- New version 1.14.0 (ALT bug: 50789)
- Languages and voices are placed in separate sub-packages

* Thu Nov 17 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.10.0-alt0.2.git5d7cb73
- Fixed build for Elbrus.

* Wed Nov 16 2022 Leontiy Volodin <lvol@altlinux.org> 1.10.0-alt0.1.git5d7cb73
- Built from git commit 5d7cb73935590fabf8131f0f19f894df92895823:
  + Fixed missing languages.
- Built via cmake instead scons:
  + Fixed missing binaries.

* Wed Nov 16 2022 Leontiy Volodin <lvol@altlinux.org> 1.8.0-alt1
- New version.
- Built from upstream Git tag (by cas@).
- Fixed URL, Git upstram and license (by cas@).

* Tue Dec 04 2018 Vitaly Lipatov <lav@altlinux.ru> 0.7.1-alt1
- new version 0.7.1 (with rpmrb script)

* Wed Jun 20 2018 Vitaly Lipatov <lav@altlinux.ru> 0.7.0-alt1
- new version 0.7.0 (with rpmrb script)

* Sun Apr 24 2016 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- build 0.5 from https://github.com/Olga-Yakovleva/RHVoice

* Thu Apr 07 2011 Michael Pozhidaev <msp@altlinux.ru> 0.3-alt3
- Added VoiceMan configuration for English in translit mode

* Tue Apr 05 2011 Michael Pozhidaev <msp@altlinux.ru> 0.3-alt2
- Added tts_unregister call to preun section
- tts-devel buildreq replaced by rpm-macros-tts

* Mon Jan 31 2011 Michael Pozhidaev <msp@altlinux.ru> 0.3-alt1
- New version with fixed flite sprintf bug and autotools support

* Wed Jul 28 2010 Michael Pozhidaev <msp@altlinux.ru> 0.1-alt1
- First release for ALT Linux Sisyphus
