%def_disable snapshot
%def_disable static
# libsndfile & alsa for testing and examples
%def_enable libsndfile
%def_enable alsa
%def_enable check

Name: libsamplerate
Version: 0.2.2
Release: alt1

Summary: Sample Rate Converter audio library
License: BSD-2-Clause
Group: System/Libraries
Url: http://libsndfile.github.io/libsamplerate/

%if_disabled snapshot
Source: https://github.com/libsndfile/%name/releases/download/%version/%name-%version.tar.xz
%else
Vcs: https://github.com/libsndfile/libsamplerate.git
Source: %name-%version.tar
%endif

%if_enabled libsndfile
%define libsndfile_ver 1.0.6
Requires: libsndfile >= %libsndfile_ver
BuildRequires: libsndfile-devel >= %libsndfile_ver
%endif
BuildRequires: libalsa-devel libfftw3-devel

%description
libsamplerate is a Sample Rate Converter for audio. One example of where
such a thing would be useful is converting audio from the CD sample rate
of 44.1kHz to the 48kHz sample rate used by DAT players.

SRC is capable of arbitrary and time varying conversions; from
downsampling by a factor of 12 to upsampling by the same factor.
Arbitrary in this case means that the ratio of input and output sample
rates can be an irrational number. The conversion ratio can also vary
with time for speeding up and slowing down effects.

%package devel
Summary: Development environment for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files required for building
%name-based software.

%package devel-static
Summary: Static %name library
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains development files required for building
statically linked %name-based software.

%package utils
Summary: Simple utilites from %name package
Group: Sound
Requires: %name = %version-%release

%description utils
This package contains utilites and example programs from %name package.

%prep
%setup

%build
%autoreconf -I m4
%configure \
    %{subst_enable static} \
    %{subst_enable libsndfile} \
    %{subst_enable alsa}
%nil
%make_build

%check
%make check

%install
%makeinstall_std

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog NEWS COPYING

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sun Sep 05 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Mon May 03 2021 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- updated to 0.2.1-10-gaae58e2 (new Url/Vcs,
  sndfile-resample moved to sndfile-tools package)
- fixed License tag

* Wed Feb 22 2017 Michael Shigorin <mike@altlinux.org> 0.1.9-alt2
- BOOTSTRAP: introduce check knob to avoid extra BRs
  (needed for sndfile-resample and tests; on by default)

* Mon Nov 14 2016 Yuri N. Sedunov <aris@altlinux.org> 0.1.9-alt1
- 0.1.9

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 0.1.8-alt1
- 0.1.8

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt4
- rebuild for debuginfo

* Mon Nov 01 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt2
- rebuild

* Sat May 29 2010 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- 0.1.7
- %%check section

* Fri Dec 05 2008 Yuri N. Sedunov <aris@altlinux.org> 0.1.4-alt1
- new version
- removed obsolete %%post{,un}_ldconfig
- updated buildreqs

* Wed Apr 18 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.1.2-alt1.0
- Automated rebuild.

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Wed Mar 10 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.0.15-alt1
- 0.0.15

* Fri Mar 07 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.0.14-alt1
- new version.

* Wed Dec 11 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.0.13-alt1
- First build for Sisyphus. 
