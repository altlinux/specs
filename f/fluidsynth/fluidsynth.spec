%define cvs_date 20031109
%undefine cvs_date
%def_disable static
%def_disable ladcca
%def_enable lash
%def_enable ladspa
%def_disable SSE

Name: fluidsynth
Version: 1.1.5
%define release alt2

%ifdef cvs_date
Release: %{release}cvs%cvs_date
%else
Release: %release
%endif

Summary: Software real-time synthesizer
Summary(ru_RU.KOI8-R): Программный синтезатор, работающий в режиме реального времени
Group: Sound
URL: http://www.fluidsynth.org
License: LGPL

%ifdef cvs_date
Source: %name-%version-%cvs_date.tar.bz2
%else
Source: http://savannah.nongnu.org/download/fluid/%name-%version.tar.bz2
%endif
Source1: fluidsynth-autogen.sh

Obsoletes: iiwusynth
Provides: iiwusynth = %version-%release

Requires: lib%name = %version-%release

%define jack_ver 0.75.0
%define ladcca_ver 0.4.0
%define alsa_ver 0.9.8-alt2

%if_enabled ladcca
BuildPreReq: libladcca-devel >= %ladcca_ver
%endif

%if_enabled ladspa
BuildPreReq: ladspa_sdk
%endif

%{?_enable_lash:BuildPreReq: liblash-devel}

BuildPreReq: jackit-devel >= %jack_ver
BuildPreReq: libalsa-devel >= %alsa_ver

# Automatically added by buildreq on Tue Sep 21 2004
#BuildRequires: doxygen gcc-c++ gcc-g77 glib2 jackit-devel ladspa_sdk libalsa-devel libe2fs-devel libladcca-devel libncurses-devel libreadline-devel libstdc++-devel pkgconfig
BuildRequires: gcc-c++ doxygen xsltproc docbook-dtds docbook-style-xsl
BuildRequires: glib2-devel libsndfile-devel jackit-devel libalsa-devel libe2fs-devel
BuildRequires: libncurses-devel libreadline-devel libpulseaudio-devel

%description
FluidSynth is a software real-time synthesizer based on the
Soundfont 2 specifications.

FluidSynth reads and handles MIDI events from the MIDI input
device. It is the software analogue of a MIDI synthesizer. FluidSynth
can also play midifiles using a Soundfont.

%description -l ru_RU.KOI8-R
FluidSynth -- это программный синтезатор, работающий в режиме реального 
времени и основанный на спецификациях Soundfont 2.

FluidSynth считывает и обрабатывает MIDI-события из входного 
MIDI-устройства. Иными словами, программа является программным аналогом 
MIDI-синтезатора. FluidSynth также может воспроизводить MIDI-файлы, 
используя Soundfont.

%package -n lib%name
Summary: Shared libraries for %name
Summary(ru_RU.KOI8-R): Разделяемые библиотеки для %name
Group: System/Libraries
Obsoletes: libiiwusynth
Provides: libiiwusynth = %version-%release
Requires: libjack >= %jack_ver
%if_enabled ladcca
Requires: libladcca >= %ladcca_ver
%endif
Requires: libalsa >= %alsa_ver

%description -n lib%name
FluidSynth is a software real-time synthesizer based on the
Soundfont 2 specifications.

FluidSynth reads and handles MIDI events from the MIDI input
device. It is the software analogue of a MIDI synthesizer. FluidSynth
can also play midifiles using a Soundfont.

This package contains libraries for %name package

%description -n lib%name -l ru_RU.KOI8-R
FluidSynth -- это программный синтезатор, работающий в режиме реального
времени и основанный на спецификациях Soundfont 2.

FluidSynth считывает и обрабатывает MIDI-события из входного
MIDI-устройства. Иными словами, программа является программным аналогом
MIDI-синтезатора. FluidSynth также может воспроизводить MIDI-файлы,
используя Soundfont.

Этот пакет содержит разделяемые библиотеки, необходимые для работы %name

%package -n lib%name-devel
Summary: Development environment for %name
Summary(ru_RU.KOI8-R): Среда разработки для %name
Group: Development/C
Obsoletes: libiiwusynth-devel
Provides: libiiwusynth-devel = %version-%release
Requires: lib%name = %version-%release
Requires: libalsa-devel >= %alsa_ver
Requires: jackit-devel >= %jack_ver
%if_enabled ladcca
Requires: libladcca-devel >= %ladcca_ver
%endif

%description -n lib%name-devel
FluidSynth is a software real-time synthesizer based on the
Soundfont 2 specifications.

FluidSynth reads and handles MIDI events from the MIDI input
device. It is the software analogue of a MIDI synthesizer. FluidSynth
can also play midifiles using a Soundfont.

This package contains headers and development files for lib%name package

%description -n lib%name-devel -l ru_RU.KOI8-R
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
Summary(ru_RU.KOI8-R): Статические библиотеки для %name
Group: Development/C
Obsoletes: libiiwusynth-devel-static
Provides: libiiwusynth-devel-static = %version-%release
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
FluidSynth is a software real-time synthesizer based on the
Soundfont 2 specifications.

FluidSynth reads and handles MIDI events from the MIDI input
device. It is the software analogue of a MIDI synthesizer. FluidSynth
can also play midifiles using a Soundfont.

This package contains static libraries for %name package

%description -n lib%name-devel-static -l ru_RU.KOI8-R
FluidSynth -- это программный синтезатор, работающий в режиме реального
времени и основанный на спецификациях Soundfont 2.

FluidSynth считывает и обрабатывает MIDI-события из входного
MIDI-устройства. Иными словами, программа является программным аналогом
MIDI-синтезатора. FluidSynth также может воспроизводить MIDI-файлы,
используя Soundfont.

Этот пакет содержит статические библиотеки для %name

%prep
%ifdef cvs_date
%setup -q -n %name
%else
%setup -q -n %name-%version
%endif

install -m755 %SOURCE1 ./autogen.sh

%build
%ifdef cvs_date
./autogen.sh
%endif
NOCONFIGURE=1 ./autogen.sh
%configure \
	%{subst_enable static} \
	%{subst_enable ladspa} \
	%{subst_enable ladcca} \
	%{subst_enable lash} \
	--enable-oss-support \
	--enable-alsa-support \
	--enable-jack-support \
	--enable-pulse-support

# Once there was an option for SSE, but buggy configure treats both
# 'enable-SSE' and 'disable-SSE' as SSE-enabling option, thus resulting
# binaries fail to work on most non-Intel processors:
#
#	%{subst_enable SSE} \

%make_build
%make -C doc update-docs

%install
%makeinstall

%files
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS README THANKS NEWS

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
%doc ChangeLog TODO
%doc doc/{api,html}

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
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

