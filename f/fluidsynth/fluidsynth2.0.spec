%def_disable snapshot

%define api_ver 2
%define sover %api_ver

%def_disable static
%def_disable ladcca
%def_enable lash
%def_enable ladspa
%def_enable jack
%def_enable pulseaudio
%def_disable portaudio
%def_enable sdl2
%def_enable libinstpatch
%def_enable dbus
%def_enable systemd
%def_disable docs
%def_enable check

Name: fluidsynth
Version: 2.3.7
Release: alt1

Summary: Software real-time synthesizer
Summary(ru_RU.UTF-8): Программный синтезатор, работающий в режиме реального времени
Group: Sound
Url: http://www.fluidsynth.org
License: LGPL-2.1-or-later

%if_disabled snapshot
Source: https://github.com/FluidSynth/%name/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/FluidSynth/fluidsynth.git
Source: %name-%version.tar
%endif

Requires: lib%name = %EVR

%define cmake_ver 3.0.2
%define glib_ver 2.30
%define jack_ver 0.75.0
%define ladcca_ver 0.4.0
%define alsa_ver 0.9.8-alt2
%define instpatch_ver 1.1.0

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake >= %cmake_ver gcc-c++ libgomp-devel
BuildRequires: doxygen graphviz xsltproc docbook-dtds docbook-style-xsl
BuildRequires: glib2-devel >= %glib_ver libsndfile-devel libalsa-devel >= %alsa_ver
BuildRequires: libalsa-devel >= %alsa_ver libe2fs-devel
BuildRequires: libncurses-devel libreadline-devel
%{?_enable_static:BuildRequires: glibc-devel-static}
%{?_enable_ladcca:BuildRequires: libladcca-devel >= %ladcca_ver}
%{?_enable_lash:BuildRequires: liblash-devel}
%{?_enable_ladspa:BuildRequires: ladspa_sdk}
%{?_enable_jack:BuildRequires: libjack-devel >= %jack_ver}
%{?_enable_pulseaudio:BuildRequires: libpulseaudio-devel}
%{?_enable_dbus:BuildRequires: libdbus-devel}
%{?_enable_systemd:BuildRequires: pkgconfig(systemd)}
%{?_enable_portaudio:BuildRequires: libportaudio-devel}
%{?_enable_sdl2:BuildRequires: libSDL2-devel}
%{?_enable_libinstpatch:BuildRequires: libinstpatch-devel >= %instpatch_ver}
%{?_enable_check:BuildRequires: ctest}

%description
FluidSynth is a software real-time synthesizer based on the
Soundfont 2 specifications.

FluidSynth reads and handles MIDI events from the MIDI input
device. It is the software analogue of a MIDI synthesizer. FluidSynth
can also play midifiles using a Soundfont.

%description -l ru_RU.UTF-8
FluidSynth -- это программный синтезатор, работающий в режиме реального
времени и основанный на спецификациях Soundfont 2.

FluidSynth считывает и обрабатывает MIDI-события из входного
MIDI-устройства. Иными словами, программа является программным аналогом
MIDI-синтезатора. FluidSynth также может воспроизводить MIDI-файлы,
используя Soundfont.

%package -n lib%name
Summary: Shared libraries for %name
Summary(ru_RU.UTF-8): Разделяемые библиотеки для %name
Group: System/Libraries

%description -n lib%name
FluidSynth is a software real-time synthesizer based on the
Soundfont 2 specifications.

FluidSynth reads and handles MIDI events from the MIDI input
device. It is the software analogue of a MIDI synthesizer. FluidSynth
can also play midifiles using a Soundfont.

This package contains libraries for %name package

%description -n lib%name -l ru_RU.UTF-8
FluidSynth -- это программный синтезатор, работающий в режиме реального
времени и основанный на спецификациях Soundfont 2.

FluidSynth считывает и обрабатывает MIDI-события из входного
MIDI-устройства. Иными словами, программа является программным аналогом
MIDI-синтезатора. FluidSynth также может воспроизводить MIDI-файлы,
используя Soundfont.

Этот пакет содержит разделяемые библиотеки, необходимые для работы %name

%package -n lib%name-devel
Summary: Development environment for %name
Summary(ru_RU.UTF-8): Среда разработки для %name
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
FluidSynth is a software real-time synthesizer based on the
Soundfont 2 specifications.

FluidSynth reads and handles MIDI events from the MIDI input
device. It is the software analogue of a MIDI synthesizer. FluidSynth
can also play midifiles using a Soundfont.

This package contains headers and development files for lib%name package

%description -n lib%name-devel -l ru_RU.UTF-8
FluidSynth -- это программный синтезатор, работающий в режиме реального
времени и основанный на спецификациях Soundfont 2.

FluidSynth считывает и обрабатывает MIDI-события из входного
MIDI-устройства. Иными словами, программа является программным аналогом
MIDI-синтезатора. FluidSynth также может воспроизводить MIDI-файлы,
используя Soundfont.

Этот пакет содержит файлы, необходимы для разработки с использованием 
%name

%package -n lib%name-devel-static
Summary: Static %name library
Summary(ru_RU.UTF-8): Статические библиотеки для %name
Group: Development/C
Obsoletes: libiiwusynth-devel-static
Provides: libiiwusynth-devel-static = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
FluidSynth is a software real-time synthesizer based on the
Soundfont 2 specifications.

FluidSynth reads and handles MIDI events from the MIDI input
device. It is the software analogue of a MIDI synthesizer. FluidSynth
can also play midifiles using a Soundfont.

This package contains static libraries for %name package

%description -n lib%name-devel-static -l ru_RU.UTF-8
FluidSynth -- это программный синтезатор, работающий в режиме реального
времени и основанный на спецификациях Soundfont 2.

FluidSynth считывает и обрабатывает MIDI-события из входного
MIDI-устройства. Иными словами, программа является программным аналогом
MIDI-синтезатора. FluidSynth также может воспроизводить MIDI-файлы,
используя Soundfont.

Этот пакет содержит статические библиотеки для %name

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
    -DLIB_INSTALL_DIR:PATH=%_lib \
    -DINCLUDE_INSTALL_DIR:PATH=include \
    -DDEFAULT_SOUNDFONT:STRING="%_datadir/soundfonts/default.sf2" \
    -DCMAKE_BUILD_TYPE:STRING="Release" \
    %{?_enable_lash:-Denable-lash:bool=true} \
    %{?_enable_ladcca:-Denable-ladcca:bool=true} \
    %{?_enable_ladspa:-Denable-ladspa:bool=true} \
    %{?_enable_jack:-Denable-jack:bool=true} \
    %{?_enable_pulseaudio:-Denable-pulseaudio:bool=true} \
    %{?_enable_dbus:-Denable-dbus:bool=true} \
    %{?_disable_systemd:-Denable-systemd:bool=false} \
    %{?_enable_portaudio:-Denable-portaudio:bool=true} \
    %{?_enable_sdl2:-Denable-sdl2:bool=true}
%nil
%cmake_build
%{?_enable_docs:%cmake_build -t doxygen}

%install
%cmake_install
%{?_enable_docs:cp -r %_cmake__builddir/doc/api/html ./}

%check
%cmake_build -t check

%files
%_bindir/%name
%_man1dir/%name.1.*

%files -n lib%name
%_libdir/lib%name.so.*
%doc AUTHORS README.md THANKS

%files -n lib%name-devel
%_includedir/*
%_libdir/lib%name.so
%_pkgconfigdir/%name.pc
%_libdir/cmake/%name/FluidSynthConfig.cmake
%_libdir/cmake/%name/FluidSynthConfigVersion.cmake
%_libdir/cmake/%name/FluidSynthTargets-release.cmake
%_libdir/cmake/%name/FluidSynthTargets.cmake
%{?_enable_docs:%doc html}
%doc TODO

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Mon Oct 21 2024 Yuri N. Sedunov <aris@altlinux.org> 2.3.7-alt1
- 2.3.7

* Sat Aug 03 2024 Yuri N. Sedunov <aris@altlinux.org> 2.3.6-alt1
- 2.3.6

* Thu Mar 28 2024 Yuri N. Sedunov <aris@altlinux.org> 2.3.5-alt1
- 2.3.5

* Mon Sep 25 2023 Yuri N. Sedunov <aris@altlinux.org> 2.3.4-alt1
- 2.3.4

* Thu Jun 15 2023 Yuri N. Sedunov <aris@altlinux.org> 2.3.3-alt1
- 2.3.3

* Sun Apr 02 2023 Yuri N. Sedunov <aris@altlinux.org> 2.3.2-alt1
- 2.3.2

* Thu Dec 29 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3.1-alt1
- 2.3.1

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 2.3.0-alt1
- 2.3.0

* Tue Sep 06 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.9-alt1
- 2.2.9

* Mon Jul 11 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.8-alt1
- 2.2.8

* Tue Apr 26 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.7-alt1
- 2.2.7

* Sun Mar 20 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.6-alt1
- 2.2.6

* Mon Jan 24 2022 Yuri N. Sedunov <aris@altlinux.org> 2.2.5-alt1
- 2.2.5

* Mon Nov 22 2021 Yuri N. Sedunov <aris@altlinux.org> 2.2.4-alt1
- 2.2.4

* Sun Sep 12 2021 Yuri N. Sedunov <aris@altlinux.org> 2.2.3-alt1
- 2.2.3

* Tue Jul 13 2021 Yuri N. Sedunov <aris@altlinux.org> 2.2.2-alt1
- 2.2.2

* Mon May 31 2021 Yuri N. Sedunov <aris@altlinux.org> 2.2.1-alt1
- 2.2.1
- adapted to new cmake macros

* Tue Mar 16 2021 Yuri N. Sedunov <aris@altlinux.org> 2.1.8-alt1
- 2.1.8

* Sat Jan 30 2021 Yuri N. Sedunov <aris@altlinux.org> 2.1.7-alt1
- 2.1.7

* Mon Jan 04 2021 Yuri N. Sedunov <aris@altlinux.org> 2.1.6-alt1
- 2.1.6

* Mon Sep 21 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.5-alt1
- 2.1.5

* Tue Jul 14 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.4-alt1
- 2.1.4

* Fri May 29 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.3-alt1
- 2.1.3

* Mon Apr 06 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.2-alt1
- 2.1.2

* Tue Mar 17 2020 Yuri N. Sedunov <aris@altlinux.org> 2.1.1-alt1
- 2.1.1
- enabled libinstpatch support, SDL2 audio support

* Tue Nov 26 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.9-alt1
- 2.0.9
- updated License tag

* Mon Oct 28 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.8-alt1
- 2.0.8

* Sun Sep 29 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.7-alt1
- 2.0.7

* Tue Aug 20 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.6-alt1
- 2.0.6

* Fri Apr 19 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.5-alt1
- 2.0.5

* Mon Feb 25 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.4-alt1
- 2.0.4

* Thu Jan 17 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.3-alt1
- 2.0.3

* Fri Dec 21 2018 Yuri N. Sedunov <aris@altlinux.org> 1.1.11-alt2
- rebuilt against libreadline.so.7

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 1.1.11-alt1
- 1.1.11

* Mon Feb 26 2018 Yuri N. Sedunov <aris@altlinux.org> 1.1.10-alt1
- 1.1.10

* Thu Jan 11 2018 Yuri N. Sedunov <aris@altlinux.org> 1.1.9-alt1
- 1.1.9

* Thu Nov 23 2017 Fr. Br. George <george@altlinux.ru> 1.1.8-alt1.1
- fix sf2 path (Closes: #32137)

* Tue Oct 17 2017 Yuri N. Sedunov <aris@altlinux.org> 1.1.8-alt1
- 1.1.8

* Fri Sep 22 2017 Yuri N. Sedunov <aris@altlinux.org> 1.1.7-alt1
- updated to v1.1.7-26-geba43fa

* Thu Sep 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt3
- rebuilt against libreadline.so.6
- re-encoded spec to UTF-8

* Wed Nov 06 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt2
- fixed build

* Mon Dec 24 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt1
- 1.1.6

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt2
- used %%autoreconf to fix RPATH problem

* Sun Sep 04 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5
- removed upstream patches

* Fri Aug 19 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4

* Wed Nov 10 2010 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3

* Sat May 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Aug 25 2009 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt2
- use LASH, not LADCCA

* Thu Aug 20 2009 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt1
- 1.0.9
- enabled pulseaudio support
- updated buildreqs

* Tue Dec 02 2008 Yuri N. Sedunov <aris@altlinux.org> 1.0.8-alt1
- new version
- removed obsolete %%post{,un}_ldconfig

* Mon Jul 03 2006 Mikhail Yakshin <greycat@altlinux.org> 1.0.7a-alt2
- rebuild for x86_64

* Mon May 15 2006 Mikhail Yakshin <greycat@altlinux.org> 1.0.7a-alt1
- 1.0.7a

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.5-alt2.1
- Rebuilt with libreadline.so.5.

* Tue Mar 08 2005 Mikhail Yakshin <greycat@altlinux.ru> 1.0.5-alt2
- fixed SSE bug: configure script treats 'disable-SSE' as 'enable-SSE'

* Tue Sep 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.5-alt1
- new version.

* Sun Nov 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt2cvs20031109
- do not package .la files.
- do not build devel-static subpackage by default.

* Sun Nov 16 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1.2cvs20031109
- rebuild to fix .la files.
- summary, description by avp.

* Sun Nov 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1.1cvs20031109
- current cvs snapshot required to build muse-0.6.2.
- ladcca support temporarily disabled, not ready for 0.4.0 yet.

* Thu Aug 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1
- 1.0.3

* Fri Apr 25 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Sat Mar 15 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.0-alt1
- iiwusynth->fluidsynth
- new version

* Tue Mar 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.2.5-alt1
- 0.2.5

* Tue Sep 17 2002 Sergey V Turchin <zerg@altlinux.ru> 0.2.2-alt1
- initial spec

