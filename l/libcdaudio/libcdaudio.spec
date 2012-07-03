Name: libcdaudio
Version: 0.99.12p2
Release: alt3

Summary: A library of functions for controlling audio CD-ROM players
License: GPL
Group: System/Libraries

URL: http://sourceforge.net/projects/libcdaudio/
Source: %name-%version.tar.gz

# from Fedora
Patch0: libcdaudio-0.99.12-buffovfl.patch
Patch1: libcdaudio-0.99.12p2-libdir.patch
Patch2: libcdaudio-0.99-CAN-2005-0706.patch

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: gcc-c++

%description
libcdaudio is a library designed to provide functions to control
operation of a CD-ROM when playing audio CDs. It also contains
functions for CDDB and CD Index lookup.

%package devel
Summary: Header files and libraries for libcdaudio development
Group: Development/C
Requires: %name = %version-%release

%description devel
The libcdaudio-devel package provides the header files and libraries
needed for libcdaudio development.

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%configure --disable-static
%make_build

%install
%make_install DESTDIR=%buildroot install

%files
%_libdir/*.so.*

%files devel
%_bindir/*-config
%_includedir/*
%_libdir/*.so
%_datadir/aclocal/*
%_pkgconfigdir/*

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.99.12p2-alt3
- rebuilt for debuginfo
- imported Fedora patches

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.99.12p2-alt2
- Rebuilt for soname set-versions

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.99.12p2-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libcdaudio
  * postun_ldconfig for libcdaudio

* Tue May 08 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.99.12p2-alt1
- 0.99.12p2.
- Some spec cleanup.

* Tue Apr 06 2004 Yuri N. Sedunov <aris@altlinux.ru> 0.99.10-alt1
- 0.99.10

* Fri Nov 28 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.99.4-alt2
- do not package .la files.

* Wed Apr 09 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.99.4-alt1
- Adopted for Sisyphus PLD package. Thanks PLD Team.

