%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define sover 2
%define modsover 0
%define shortname spd

%add_verify_elf_skiplist %_libdir/libspeechd_module.*

%define libexec %_libdir

# spd modules
%def_with flite
%def_with festival
%def_with pico
%def_with dummy
%def_with espeak
%def_with espeak_ng
%def_with espeak_ng_mbrola
%def_with generic
%def_with cicero
%def_with openjtalk

Name: speech-dispatcher
Version: 0.12.1
Release: alt3

Summary: A speech output processing service
License: GPL-2.0-or-later
Group: Sound
Url: http://www.freebsoft.org/speechd
VCS: https://github.com/brailcom/speechd

Source: %name-%version.tar
Source1: speech-dispatcher.filetrigger
SOURCE2: speech-dispatcher.control
Source3: %name.macros

Patch: speech-dispatcher-0.8-alt-flite.patch
Patch1: modules_order-fix.patch

Requires: %shortname-audio-plugins

BuildRequires(pre): rpm-macros-python3
BuildRequires: libdotconf-devel >= 0.3
BuildRequires: gcc-c++ glib2-devel glibc-devel-static intltool
BuildRequires: libXau-devel  libltdl7-devel
BuildRequires: libalsa-devel libao-devel
%{?_with_flite:BuildRequires: flite-devel}
%{?_with_pico:BuildRequires: svox-pico}
%{?_with_espeak_ng:BuildRequires: libespeak-ng-devel}
%{?_with_espeak:BuildRequires: libespeak-devel}
BuildRequires: rpm-build-python3
BuildRequires: python3-base python3-devel
BuildRequires: libsndfile-devel libpulseaudio-devel
BuildRequires: makeinfo

%description
Speech Dispatcher is a part of the Free(b)soft project, which is
intended to allow blind and visually impaired people to work with
computer and Internet based on free software.

%files -f %name.lang
%_bindir/speech-dispatcher
%config %_sysconfdir/%name
%_controldir/%name
%dir %_libdir/%name
%dir %_libdir/%name-modules
%dir %_datadir/sounds/%name
%_datadir/sounds/%name/*.wav
%dir %_datadir/%name
%dir %_datadir/%name/conf
%_datadir/%name/conf/speechd.conf
%dir %_datadir/%name/conf/clients
%_datadir/%name/conf/clients/emacs.conf
%dir %_datadir/%name/conf/desktop
%_datadir/%name/conf/desktop/speechd.desktop
%dir %_datadir/%name/conf/modules
%dir %_datadir/%name/locale
%_datadir/%name/locale/*
%_infodir/*
%_rpmlibdir/speech-dispatcher.filetrigger
%{?_without_cicero:%exclude %_libdir/%name-modules/sd_cicero}
%{?_without_cicero:%exclude %_datadir/%name/conf/modules/cicero.conf}
%{?_without_festival:%exclude %_libdir/%name-modules/sd_festival}
%{?_without_festival:%exclude %_datadir/%name/conf/modules/festival.conf}
%{?_without_dummy:%exclude %_libdir/%name-modules/sd_dummy}
%{?_without_espeak_ng_mbrola:%exclude %_libdir/%name-modules/sd_espeak-ng-mbrola}
%{?_without_espeak_ng_mbrola:%exclude %_datadir/%name/conf/modules/espeak-ng-mbrola.conf}
%{?_without_generic:%exclude %_libdir/%name-modules/sd_generic}
%{?_without_openjtalk:%exclude %_libdir/%name-modules/sd_openjtalk}

%package -n rpm-macros-%shortname
Summary: RPM macros to package software that depends on %name
Group: Development/Other
BuildArch: noarch
Provides: rpm-macros-%name = %EVR

%description -n rpm-macros-%shortname
%summary.

%files -n rpm-macros-%shortname
%_rpmmacrosdir/%name

%package -n libspeechd%sover
Summary: Client library for speech-dispatcher
Group: System/Libraries

%description -n libspeechd%sover
Applications can use this library to communicate with speech-dispatcher
service and produce speech output.

%files -n libspeechd%sover
%_libdir/libspeechd.so.%sover
%_libdir/libspeechd.so.%sover.*

%package -n libspeechd-devel
Group: Development/C
Summary: Development files to use libspeechd to connect to speech-dispatcher

%description -n libspeechd-devel
Developers can use this library to connect to speech-dispatcher daemon
and produce speech output.

%files -n libspeechd-devel
%_includedir/%name/*
%exclude %_includedir/%name/spd_module_main.h
%_libdir/libspeechd.so
%_pkgconfigdir/*

%package -n libspeechd_module%modsover
Summary: Interface for spd modules
Group: System/Libraries

%description -n libspeechd_module%modsover
%summary
%files -n libspeechd_module%modsover
%_libdir/libspeechd_module.so.%modsover
%_libdir/libspeechd_module.so.%modsover.*

%package -n libspeechd_module-devel
Summary: Devel files fore libspeechd_module
Group: Development/C

%description -n libspeechd_module-devel
%summary

%files -n libspeechd_module-devel
%_includedir/%name/spd_module_main.h
%_libdir/libspeechd_module.so

%package -n %shortname-audio-plugins
Summary: Audio plugins fore %name
Group: Sound
Provides: %name-audio-plugins = %EVR

%description -n %shortname-audio-plugins
%summary

%files -n %shortname-audio-plugins
%_libdir/%name/spd*.so

%package -n %shortname-utils
Group: Sound
Summary: Various utilities for speech-dispatcher
Requires: %name = %EVR
Provides: %name-utils = %EVR
obsoletes: %name-utils < %EVR

%description -n %shortname-utils
Various utilities for speech-dispatcher

%files -n %shortname-utils
%_bindir/spd-conf
%_bindir/spd-say
%_bindir/spdsend
%_datadir/sounds/%name/test.wav

%package -n python3-module-speechd
Summary: Python client for Speech Dispatcher
Group: Development/Python
BuildArch: noarch
Requires: %name = %EVR

%description -n python3-module-speechd
This python module allows programmsaccess speech-dispatcher service.

%files -n python3-module-speechd
%python3_sitelibdir_noarch/*

%package doc
Summary: Doc files for %name
Group: Documentation
BuildArch: noarch

%description doc
%summary

%files doc
%doc FAQ NEWS README.md README.overview.md

# spd module packages

%if_with flite
%package -n %shortname-module-flite
Group: Sound
Summary: Flite support for speech-dispatcher
Requires: %name = %EVR
Provides: %name-module-flite = %EVR
obsoletes: %name-module-flite < %EVR

%description -n %shortname-module-flite
%summary

%files -n %shortname-module-flite
%_libdir/%name-modules/sd_flite
%endif

%if_with festival
%package -n %shortname-module-festival
Group: Sound
Summary: Festival support for speech-dispatcher
Requires: %name = %EVR
Provides: %name-module-festival = %EVR
Obsoletes: %name-module-festival < %EVR

%description -n %shortname-module-festival
%summary

%files -n %shortname-module-festival
%_libdir/%name-modules/sd_festival
%_datadir/%name/conf/modules/festival.conf
%endif

%if_with pico
%package -n %shortname-module-pico
Group: Sound
Summary: Pico support for speech-dispatcher
Requires: %name = %EVR
Requires: svox-pico
Provides: %name-module-pico = %EVR
Obsoletes: %name-module-pico < %EVR


%description -n %shortname-module-pico
%summary

%files -n %shortname-module-pico
%_libdir/%name-modules/sd_pico
%_datadir/%name/conf/modules/pico.conf
%endif

%if_with dummy
%package -n %shortname-module-dummy
Group: Sound
Summary: Pico support for %name
Requires: %name = %EVR
Provides: %name-module-dummy = %EVR
Obsoletes: %name-module-dummy < %EVR

%description -n %shortname-module-dummy
A noop backend for Speech Dispatcher.

Accepts TTS commands, reports status, no speech output.

Useful for testing, CI, debugging when a real synthesizer isnt needed.

%files -n %shortname-module-dummy
%_libdir/%name-modules/sd_dummy
%_datadir/sounds/%name/dummy-message.wav
%endif

%if_with espeak_ng
%package -n %shortname-module-espeak-ng
Group: Sound
Summary: Espeak-ng support for %name
Requires: %name = %EVR
Requires: espeak-ng-data
Provides: %name-module-espeak-ng = %EVR
Obsoletes: %name-module-espeak-ng < %EVR

%description -n %shortname-module-espeak-ng
%summary

%files -n %shortname-module-espeak-ng
%_libdir/%name-modules/sd_espeak-ng
%_datadir/%name/conf/modules/espeak-ng.conf
%{?_without_espeak:%_datadir/%name/conf/modules/espeak.conf}
%endif

%if_with espeak
%package -n %shortname-module-espeak
Summary: Espeak module fore %name
Group: Sound
Requires: %name = %EVR
Requires: espeak-ng-data
Provides: %name-module-espeak = %EVR
Obsoletes: %name-module-espeak < %EVR

%description -n %shortname-module-espeak
%summary

%files -n %shortname-module-espeak
%_libdir/%name-modules/sd_espeak
%_datadir/%name/conf/modules/espeak.conf
%endif

%if_with espeak_ng_mbrola
%package -n %shortname-module-espeak-ng-mbrola
Group: Sound
Summary: Mbrola support for %name
Requires: %name = %EVR
Requires: mbrola
Requires: espeak-ng-mbrola-data
Provides: %name-module-espeak-ng-mbrola = %EVR
Obsoletes: %name-module-espeak-ng-mbrola < %EVR

%description -n %shortname-module-espeak-ng-mbrola
%summary

%files -n %shortname-module-espeak-ng-mbrola
%_libdir/%name-modules/sd_espeak-ng-mbrola
%_datadir/%name/conf/modules/espeak-ng-mbrola.conf
%endif

%if_with generic
%package -n %shortname-module-generic
Group: Sound
Summary: Generic support for %name
Requires: %name = %EVR
Provides: %name-module-generic = %EVR
Obsoletes: %name-module-generic < %EVR

%description -n %shortname-module-generic
%summary

%files -n %shortname-module-generic
%_libdir/%name-modules/sd_generic
%endif

%if_with cicero
%package -n %shortname-module-cicero
Group: Sound
Summary: Cicero support for %name
Requires: %name = %EVR
Provides: %name-module-cicero = %EVR
Obsoletes: %name-module-cicero < %EVR

%description -n %shortname-module-cicero
%summary

%files -n %shortname-module-cicero
%_libdir/%name-modules/sd_cicero
%_datadir/%name/conf/modules/cicero.conf
%endif

%if_with openjtalk
%package -n %shortname-module-openjtalk
Group: Sound
Summary: Openjtalk support for %name
Requires: %name = %EVR
Requires: open_jtalk
Provides: %name-module-openjtalk = %EVR
Obsoletes: %name-module-openjtalk < %EVR

%description -n %shortname-module-openjtalk
%summary

%files -n %shortname-module-openjtalk
%_libdir/%name-modules/sd_openjtalk
%endif

%prep
%setup
%patch0 -p1
%patch1 -p2

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%autoreconf
%configure \
%{?_with_espeak:   --with-espeak} \
%{?_with_espeak_ng:   --with-espeak-ng} \
%{?_with_flite:   --with-flite} \
%{?_with_pico:   --with-pico} \
	   --with-pulse \
	   --with-alsa \
	   --with-libao \
	   --with-oss \
	   --without-voxin \
	   --without-kali \
	   --without-ibmtts \
	   --without-baratinoo \
	   --disable-static \
	   --with-module-bindir=%_libdir/speech-dispatcher-modules
	   %nil
%make_build

%install
%make_install DESTDIR='%buildroot' pyexecdir=%python3_sitelibdir_noarch install

# install filetrigger
install -D -m 755 %SOURCE1 %buildroot/%_rpmlibdir/speech-dispatcher.filetrigger

# install controle
install -Dpm 755 %SOURCE2 %buildroot%_controldir/%name

# install macros
install -Dpm 755 %SOURCE3 %buildroot%_rpmmacrosdir/%name

# unpackaged files
find %buildroot%_libdir -name '*.la' -delete

%find_lang %name

%changelog
* Tue Sep 08 2026 Artem Semenov <savoptik@altlinux.org> 0.12.1-alt3
- Created rpm-macros-spd subpackage.
- Renamed modules to short name.
- Renamed utils subpackage to spd-utils.
- Moved doc to doc subpackage.
- Moved audio plugins to subpackage.
- Moved SPD Module interface to subpackage.
- Spleated modules to subpackages.
- Added %%dir %%_datadir/%%name to get clean uninstall.

* Mon Oct 27 2025 Artem Semenov <savoptik@altlinux.org> 0.12.1-alt2
- Added alsa/pulse switch control

* Mon May 12 2025 Artem Semenov <savoptik@altlinux.org> 0.12.1-alt1
- Updated to new version 0.12.1

* Tue Mar 04 2025 Artem Semenov <savoptik@altlinux.org> 0.12.0-alt1
- New version 0.12.0.

* Fri Dec 20 2024 Artem Semenov <savoptik@altlinux.org> 0.11.5-alt3
- Fixed default priority module order
- remove autoreq filter fore fix spd-conf
- added filetrigger fore update modules automaticaly

* Thu Jun 06 2024 Artem Semenov <savoptik@altlinux.org> 0.11.5-alt2
- Changed espeak to espeak-ng

* Sat Dec 09 2023 Anton Midyukov <antohami@altlinux.org> 0.11.5-alt1
- 0.11.5 (Closes: 48428)

* Fri Oct 15 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.2-alt2
- Fixed build with LTO

* Mon Jan 11 2021 Paul Wolneykien <manowar@altlinux.org> 0.10.2-alt1
- Fixed doc/ files.
- Build without voxin, kali, ibmtts and baratinoo (to avoid "shims").
- New upstream release 0.10.2.

* Wed Nov 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.8.8-alt2
- requires fixed

* Sun Jan 07 2018 Yuri N. Sedunov <aris@altlinux.org> 0.8.8-alt1
- 0.8.8
- removed obsolete pkgconfig.patch (ALT #34372)

* Fri Jun 02 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.7-alt1
- 0.8.7

* Fri Feb 10 2017 Yuri N. Sedunov <aris@altlinux.org> 0.8.6-alt1
- 0.8.6

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 08 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.8.3-alt2
- NMU: added makeinfo to BRs (fixes FTBFS).

* Tue Jun 30 2015 Yuri N. Sedunov <aris@altlinux.org> 0.8.3-alt1
- 0.8.3

* Fri May 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.8.2-alt1
- 0.8.2
- added service file from fc

* Tue Mar 10 2015 Paul Wolneykien <manowar@altlinux.org> 0.8.1-alt2
- speech-dispatcher.pc: Set Cflags to -I${includedir}/speech-dispatcher
  (patch).

* Tue Nov 18 2014 Paul Wolneykien <manowar@altlinux.org> 0.8.1-alt1
- Freshed up to v0.8.1 with the help of cronbuild and update-source-functions.

* Wed Jul 03 2013 Paul Wolneykien <manowar@altlinux.org> 0.8-alt2
- Require speech-dispatcher in all modules.
- Exclude the static libs.
- Explicitly configure all of the modules to be packaged.
- Include the default cicero module into the main package.
- Use plain tar sources.
- Cleanup the spec. Strict the pattern for l10n files.
- Build the Python module noarch.
- Add the PulseAudio output module.
- Add msp@ to the cronbuild CC.
- Add cronbuild scripts based on the update-source-functions.
- Exclude clients/gnome-speech.conf which breaks server autospawn.

* Fri May 10 2013 Michael Pozhidaev <msp@altlinux.ru> 0.8-alt1
- New version 0.8 (closes: #28819)
- New subpackages: output-libao, output-oss, module-flite,
  module-festival, module-pico
- python-module-speech subpackage is renamed to python3-module-speechdd

* Mon Jul 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt5.3
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.7-alt5.2.1
- Rebuild with Python-2.7

* Thu Nov 25 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt5.2
- Rebuilt for soname set-versions

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt5.1
- Rebuilt with python 2.6

* Thu Aug 20 2009 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt5
- 'daemon' term replaced by 'service' one (by mike@ suggestion)

* Mon Aug 17 2009 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt4
- Applied getline patch from sbolshakov@

* Wed Aug 05 2009 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt3
- Applied flite patch (Thanks to sbolshakov@)
- Spec cleanup (removed ldconfig and install_info calls by sbolshakov@)
- Minor fixes

* Mon Sep 15 2008 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt2
- Fixed i586 build

* Sun Sep 07 2008 Michael Pozhidaev <msp@altlinux.ru> 0.6.7-alt1
- Initial RPM

