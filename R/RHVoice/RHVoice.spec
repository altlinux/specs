%define _unpackaged_files_terminate_build 1
  
%define audiosover 2
%define coresover 10
%define sover 5

Name:    RHVoice
Version: 1.14.0
Release: alt1

Summary: a free and open source speech synthesizer for Russian and other languages
License: GPL-2.0
Group: Sound
Url: https://github.com/RHVoice/RHVoice

Source0: %name-%version.tar

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

%description
%summary

%package -n lib%name%sover
Summary: Lib files for %name
Group: System/Libraries
Provides: RHVoice = %EVR

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
Provides: RHVoice-devel = %EVR

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

%package Russian
Summary: Russian language for  %name
Group: Sound
BuildArch: noarch
Requires: %name = %EVR

%description Russian
%summary

%files Russian
%_datadir/%name/languages/Russian/*

%package English
Summary: English language for  %name
Group: Sound
BuildArch: noarch
Requires: %name = %EVR

%description English
%summary

%files English
%_datadir/%name/languages/English/*

%package Albanian
Summary: Albanian language for  %name
Group: Sound
BuildArch: noarch
Requires: %name = %EVR

%description Albanian
%summary

%files Albanian
%_datadir/%name/languages/Albanian/*

%package Brazilian
Summary: Brazilian and Portuguese language for  %name
Group: Sound
BuildArch: noarch
Requires: %name = %EVR
Provides: %name-Portuguese = %EVR

%description Brazilian
%summary

%files Brazilian
%_datadir/%name/languages/Brazilian-Portuguese/*

%package Czech
Summary: Czech language for  %name
Group: Sound
License: GPL-2.0
BuildArch: noarch
Requires: %name = %EVR

%description Czech
%summary

%files Czech
%_datadir/%name/languages/Czech/*

%package Esperanto
Summary: Esperanto language for  %name
Group: Sound
BuildArch: noarch
Requires: %name = %EVR

%description Esperanto
%summary

%files Esperanto
%_datadir/%name/languages/Esperanto/*

%package Georgian
Summary: Georgian language for  %name
Group: Sound
BuildArch: noarch
Requires: %name = %EVR

%description Georgian
%summary

%files Georgian
%_datadir/%name/languages/Georgian/*

%package Kyrgyz
Summary: Kyrgyz language for  %name
Group: Sound
BuildArch: noarch
Requires: %name = %EVR

%description Kyrgyz
%summary

%files Kyrgyz
%_datadir/%name/languages/Kyrgyz/*

%package Macedonian
Summary: Macedonian language for  %name
Group: Sound
License: AGPL-3.0
BuildArch: noarch
Requires: %name = %EVR

%description Macedonian
%summary

%files Macedonian
%_datadir/%name/languages/Macedonian/*

%package Polish
Summary: Polish language for  %name
Group: Sound
License: GPL-2.0
BuildArch: noarch
Requires: %name = %EVR

%description Polish
%summary

%files Polish
%_datadir/%name/languages/Polish/*

%package Slovak
Summary: Slovak language for  %name
Group: Sound
License: LGPL-2.1
BuildArch: noarch
Requires: %name = %EVR

%description Slovak
%summary

%files Slovak
%_datadir/%name/languages/Slovak/*

%package Tatar
Summary: Tatar language for  %name
Group: Sound
BuildArch: noarch
Requires: %name = %EVR

%description Tatar
%summary

%files Tatar
%_datadir/%name/languages/Tatar/*

%package Ukrainian
Summary: Ukrainian language for  %name
Group: Sound
BuildArch: noarch
Requires: %name = %EVR

%description Ukrainian
%summary

%files Ukrainian
%_datadir/%name/languages/Ukrainian/*

%package Uzbek
Summary: Uzbek language for  %name
Group: Sound
License: LGPL-2.1
BuildArch: noarch
Requires: %name = %EVR

%description Uzbek
%summary

%files Uzbek
%_datadir/%name/languages/Uzbek/*

# voices
# Russian

%package Russian-aleksandr
Summary: Russian aleksandr voice for  %name
Group: Sound
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-aleksandr
%summary

%files Russian-aleksandr
%_datadir/%name/voices/aleksandr/*

%package Russian-aleksandr-hq
Summary: Russian aleksandr-hq voice for  %name
Group: Sound
License: CC-BY-SA-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-aleksandr-hq
%summary

%files Russian-aleksandr-hq
%_datadir/%name/voices/aleksandr-hq/*

%package Russian-anna
Summary: Russian anna voice for  %name
Group: Sound
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-anna
%summary

%files Russian-anna
%_datadir/%name/voices/anna/*

%package Russian-arina
Summary: Russian arina voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-arina
%summary

%files Russian-arina
%_datadir/%name/voices/arina/*

%package Russian-artemiy
Summary: Russian artemiy voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-artemiy
%summary

%files Russian-artemiy
%_datadir/%name/voices/artemiy/*

%package Russian-elena
Summary: Russian elena voice for  %name
Group: Sound
License: GPL-3.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-elena
%summary

%files Russian-elena
%_datadir/%name/voices/elena/*

%package Russian-evgeniy
Summary: Russian evgeniy voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-evgeniy
%summary

%files Russian-evgeniy
%_datadir/%name/voices/evgeniy-rus/*

%package Russian-irina
Summary: Russian irina voice for  %name
Group: Sound
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-irina
%summary

%files Russian-irina
%_datadir/%name/voices/irina/*

%package Russian-mikhail
Summary: Russian mikhail voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-mikhail
%summary

%files Russian-mikhail
%_datadir/%name/voices/mikhail/*

%package Russian-pavel
Summary: Russian pavel voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-pavel
%summary

%files Russian-pavel
%_datadir/%name/voices/pavel/*

%package Russian-tatiana
Summary: Russian tatiana voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-tatiana
%summary

%files Russian-tatiana
%_datadir/%name/voices/tatiana/*

%package Russian-timofey
Summary: Russian timofey voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-timofey
%summary

%files Russian-timofey
%_datadir/%name/voices/timofey/*

%package Russian-umka
Summary: Russian umka voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-umka
%summary

%files Russian-umka
%_datadir/%name/voices/umka/*

%package Russian-victoria
Summary: Russian victoria voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-victoria
%summary

%files Russian-victoria
%_datadir/%name/voices/victoria/*

%package Russian-vitaliy
Summary: Russian vitaliy voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-vitaliy
%summary

%files Russian-vitaliy
%_datadir/%name/voices/vitaliy/*

%package Russian-vitaliy-ng
Summary: Russian vitaliy-ng voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-vitaliy-ng
%summary

%files Russian-vitaliy-ng
%_datadir/%name/voices/vitaliy-ng/*

%package Russian-vsevolod
Summary: vsevolod voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-vsevolod
%summary

%files Russian-vsevolod
%_datadir/%name/voices/vsevolod/*

%package Russian-yuriy
Summary: Russian yuriy voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Russian = %EVR

%description Russian-yuriy
%summary

%files Russian-yuriy
%_datadir/%name/voices/yuriy/*

# English

%package English-alan
Summary: English alan voice for  %name
Group: Sound
BuildArch: noarch
Requires: %name-English = %EVR

%description English-alan
%summary

%files English-alan
%_datadir/%name/voices/alan/*

%package English-bdl
Summary: English bdl voice for  %name
Group: Sound
BuildArch: noarch
Requires: %name-English = %EVR

%description English-bdl
%summary

%files English-bdl
%_datadir/%name/voices/bdl/*

%package English-clb
Summary: English clb voice for  %name
Group: Sound
BuildArch: noarch
Requires: %name-English = %EVR

%description English-clb
%summary

%files English-clb
%_datadir/%name/voices/clb/*

%package English-evgeniy
Summary: English evgeniy voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-English = %EVR

%description English-evgeniy
%summary

%files English-evgeniy
%_datadir/%name/voices/evgeniy-eng/*

%package English-lyubov
Summary: English lyubov voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-English = %EVR

%description English-lyubov
%summary

%files English-lyubov
%_datadir/%name/voices/lyubov/*

%package English-slt
Summary: English slt voice for  %name
Group: Sound
License: CMU-License
BuildArch: noarch
Requires: %name-English = %EVR

%description English-slt
%summary

%files English-slt
%_datadir/%name/voices/slt/*

# Albanian

%package Albanian-hana
Summary: Albanian hana voice for  %name
Group: Sound
License: CC-BY-NC-SA-4.0
BuildArch: noarch
Requires: %name-Albanian = %EVR

%description Albanian-hana
%summary

%files Albanian-hana
%_datadir/%name/voices/hana/*

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
%_datadir/%name/voices/Leticia-F123/*

# Czech

%package Czech-zdenek
Summary: Czech zdenek voice for  %name
Group: Sound
License: CC0-1.0
BuildArch: noarch
Requires: %name-Czech = %EVR

%description Czech-zdenek
%summary

%files Czech-zdenek
%_datadir/%name/voices/zdenek/*

# Esperanto

%package Esperanto-spomenka
Summary: Esperanto spomenka voice for  %name
Group: Sound
License: GPL-3.0
BuildArch: noarch
Requires: %name-Esperanto = %EVR

%description Esperanto-spomenka
%summary

%files Esperanto-spomenka
%_datadir/%name/voices/spomenka/*

# Georgian

%package Georgian-natia
Summary: Georgian natia voice for  %name
Group: Sound
License: RHVoice-Natia-License
BuildArch: noarch
Requires: %name-Georgian = %EVR

%description Georgian-natia
%summary

%files Georgian-natia
%_datadir/%name/voices/natia/*

# Kyrgyz

%package Kyrgyz-azamat
Summary: Kyrgyz azamat voice for  %name
Group: Sound
BuildArch: noarch
Requires: %name-Kyrgyz = %EVR

%description Kyrgyz-azamat
%summary

%files Kyrgyz-azamat
%_datadir/%name/voices/azamat/*

%package Kyrgyz-nazgul
Summary: Kyrgyz nazgul voice for  %name
Group: Sound
BuildArch: noarch
Requires: %name-Kyrgyz = %EVR

%description Kyrgyz-nazgul
%summary

%files Kyrgyz-nazgul
%_datadir/%name/voices/nazgul/*

# Macedonian

%package Macedonian-kiko
Summary: Macedonian kiko voice for  %name
Group: Sound
License: CC-BY-NC-SA-4.0
BuildArch: noarch
Requires: %name-Macedonian = %EVR

%description Macedonian-kiko
%summary

%files Macedonian-kiko
%_datadir/%name/voices/kiko/*

%package Macedonian-suze
Summary: Macedonian suze voice for  %name
Group: Sound
BuildArch: noarch
Requires: %name-Macedonian = %EVR

%description Macedonian-suze
%summary

%files Macedonian-suze
%_datadir/%name/voices/suze/*

# Polish

%package Polish-alicja
Summary: Polish alicja voice for  %name
Group: Sound
License: CC-BY-4.0
BuildArch: noarch
Requires: %name-Polish = %EVR

%description Polish-alicja
%summary

%files Polish-alicja
%_datadir/%name/voices/alicja/*

%package Polish-cezary
Summary: Polish cezary voice for  %name
Group: Sound
License: CC-BY-NC-ND-4.0
BuildArch: noarch
Requires: %name-Polish = %EVR

%description Polish-cezary
%summary

%files Polish-cezary
%_datadir/%name/voices/cezary/*

%package Polish-magda
Summary: Polish magda voice for  %name
Group: Sound
License: CC-BY-4.0
BuildArch: noarch
Requires: %name-Polish = %EVR

%description Polish-magda
%summary

%files Polish-magda
%_datadir/%name/voices/magda/*

%package Polish-michal
Summary: Polish michal voice for  %name
Group: Sound
License: CC0-1.0
BuildArch: noarch
Requires: %name-Polish = %EVR

%description Polish-michal
%summary

%files Polish-michal
%_datadir/%name/voices/michal/*

%package Polish-natan
Summary: Polish natan voice for  %name
Group: Sound
License: CC0-1.0
BuildArch: noarch
Requires: %name-Polish = %EVR

%description Polish-natan
%summary

%files Polish-natan
%_datadir/%name/voices/natan/*

# Slovak

%package Slovak-ondro
Summary: Slovak ondro voice for  %name
Group: Sound
License: CC0-1.0
BuildArch: noarch
Requires: %name-Slovak = %EVR

%description Slovak-ondro
%summary

%files Slovak-ondro
%_datadir/%name/voices/ondro/*

# Tatar

%package Tatar-talgat
Summary: Tatar talgat voice for  %name
Group: Sound
License: RHVoice-Talgat-License
BuildArch: noarch
Requires: %name-Tatar = %EVR

%description Tatar-talgat
%summary

%files Tatar-talgat
%_datadir/%name/voices/talgat/*

# Ukrainian

%package Ukrainian-anatol
Summary: Ukrainian anatol voice for  %name
Group: Sound
License: LGPL-2.1
BuildArch: noarch
Requires: %name-Ukrainian = %EVR

%description Ukrainian-anatol
%summary

%files Ukrainian-anatol
%_datadir/%name/voices/anatol/*

%package Ukrainian-marianna
Summary: Ukrainian marianna voice for  %name
Group: Sound
License: CC-BY-ND-4.0
BuildArch: noarch
Requires: %name-Ukrainian = %EVR

%description Ukrainian-marianna
%summary

%files Ukrainian-marianna
%_datadir/%name/voices/marianna/*

%package Ukrainian-natalia
Summary: Ukrainian natalia voice for  %name
Group: Sound
License: LGPL-2.1
BuildArch: noarch
Requires: %name-Ukrainian = %EVR

%description Ukrainian-natalia
%summary

%files Ukrainian-natalia
%_datadir/%name/voices/natalia/*

%package Ukrainian-volodymyr
Summary: Ukrainian volodymyr voice for  %name
Group: Sound
License: CC-BY-ND-4.0
BuildArch: noarch
Requires: %name-Ukrainian = %EVR

%description Ukrainian-volodymyr
%summary

%files Ukrainian-volodymyr
%_datadir/%name/voices/volodymyr/*

# Uzbek

%package Uzbek-sevinch
Summary: Uzbek sevinch voice for  %name
Group: Sound
License: CC-BY-NC-SA-4.0
BuildArch: noarch
Requires: %name-Uzbek = %EVR

%description Uzbek-sevinch
%summary

%files Uzbek-sevinch
%_datadir/%name/voices/sevinch/*

%prep
%setup

%build
scons languages=all voices=all audio_libs=all

%install
scons install DESTDIR=%buildroot \
prefix=%prefix sysconfdir=%_sysconfdir bindir=%_bindir libdir=%_libdir includedir=%_includedir datadir=%_datadir

%changelog
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
