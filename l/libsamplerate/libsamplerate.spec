%def_disable static

Name: libsamplerate
Version: 0.1.8
Release: alt1

Summary: Sample Rate Converter audio library
License: GPL
Group: System/Libraries
Url: http://www.mega-nerd.com/SRC
Source: %url/%name-%version.tar.gz
Patch: %name-0.1.7-test.patch

%define libsndfile_ver 1.0.6
Requires: libsndfile >= %libsndfile_ver

BuildPreReq: libsndfile-devel >= %libsndfile_ver

# Automatically added by buildreq on Mon Sep 13 2004
BuildRequires: libfftw3-devel libsndfile-devel

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
%setup -q
#%%patch -p1

%build
%autoreconf -I M4
%configure \
    %{subst_enable static}

%make_build

%check
%make -C tests check

%install
%makeinstall_std

rm -f doc/Makefile*

%files
%_libdir/*.so.*
%doc AUTHORS ChangeLog NEWS

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*
%doc doc/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%files utils
%_bindir/*

%changelog
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
