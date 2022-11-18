Name: RHVoice
Version: 1.10.0
Release: alt0.2.git5d7cb73

Summary: RHVoice is a Russian speech synthesizer written by Olga Yakovleva
License: LGPL-2.1+
Group: Sound
URL: https://rhvoice.org/
VCS: https://github.com/RHVoice/RHVoice

# BuildRequires(pre): rpm-macros-tts
BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
#BuildRequires: scons
BuildRequires: flite-devel
BuildRequires: libao-devel
BuildRequires: libglibmm-devel
BuildRequires: libportaudio2-devel
BuildRequires: libpulseaudio-devel
BuildRequires: libtclap-devel
BuildRequires: libunistring-devel
BuildRequires: libunistring-devel
BuildRequires: libspeechd-devel
BuildRequires: libpcre2-devel
BuildRequires: libdbus-devel
BuildRequires: boost-devel

Provides: rhvoice = %EVR
# Requires: tts-base

# Source-url: https://github.com/Olga-Yakovleva/RHVoice/archive/%version.tar.gz
Source: RHVoice-%version.tar
Source2: rhvoice.voiceman
Source3: rhvoice-en.voiceman
Patch: RHVoice-alt-fix-undefined-elfs.patch

%description
RHVoice is a Russian speech synthesizer written by Olga Yakovleva.
It uses the following free software components:
* Russian speech database and Russian language description for
  Festival by Nickolay V. Shmyrev (https://developer.berlios.de/projects/festlang)
  The phoneset and almost all of the main lts rules are used as is,
  but I've made changes in other parts, either to simplify conversion
  to the flite format, or to add new features, or just to understand
  how it all works.
* The voice has been trained with The HMM-based Speech Synthesis
  System (HTS) (http://hts.sp.nitech.ac.jp)
* The hts_engine API is used for runtime speech generation
  (http://hts-engine.sourceforge.net/)
  Since the library does not support streaming synthesis, the original
  version has been modified to implement this functionality, and the
  synthesizer distribution includes this patched version.
* The C implementation of the Russian text analyzer uses Flite
  (http://www.speech.cs.cmu.edu/flite)
  I used the flite's implementation of English language support as an
  example, some functions were used as a starting point.
* the stress information for the stress dictionary has been extracted
  from the test dictionary in the RuLex package by Igor B. Poretsky
  (http://poretsky.homelinux.net/packages/)
* GNU libunistring is used for working with unicode text
  (http://www.gnu.org/software/libunistring/)

%package -n lib%name
Summary: RHVoice is a Russian speech synthesizer written by Olga Yakovleva
Group: System/Libraries
Requires: %name = %version-%release

%description -n lib%name
RHVoice is a Russian speech synthesizer written by Olga Yakovleva.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for %name

%prep
%setup
%patch -p1
cp /usr/share/license/LGPL-2.1 licenses/lgpl-2.1.txt

%build
%ifnarch %e2k
%add_optflags -fsanitize=address
%endif
%cmake -GNinja \
       -DVERSION_FROM_GIT=%version \
       -DISO639_1_NAME2CODE_Polish=pl \
       -DVOICE_magda_LANG=pl \
       -DVOICE_natan_LANG=pl \
       -DVOICE_suze_LANG=mk \
       -Dcommon_doc_dir=%_datadir/doc/%name-%version
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"
#__install -pD -m 644 %SOURCE2 %buildroot%_ttsdir/rhvoice.voiceman
#__install -pD -m 644 %SOURCE3 %buildroot%_ttsdir/rhvoice-en.voiceman

# %%preun
# %%tts_unregister rhvoice
# %%tts_unregister rhvoice-en

%files
%doc LICENSE.md README.md
%dir %_sysconfdir/RHVoice/
%config(noreplace) %_sysconfdir/RHVoice/RHVoice.conf
# %%_ttsdir/*
%_bindir/*
%_datadir/%name/
%_datadir/dbus-1/services/com.github.OlgaYakovleva.RHVoice.service
%_libdir/speech-dispatcher-modules/sd_rhvoice

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

%changelog
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

