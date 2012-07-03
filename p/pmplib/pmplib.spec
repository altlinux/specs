%define name pmplib
%define version 0.14
%define release alt0.1

# Preamble
Summary: Portable Media Player library (PMPlib)
Name: %name
Version: %version
Release: %release.qa1
License: LGPL
Packager: Alex Karpov <karpov@altlinux.ru>
Url: http://pmplib.sourceforge.net/
Group: Sound
Source: %name-%version.tar.gz

# BuildRequires: gcc => 3.0.1, libid3tag-devel => 0.15.1, zlib-devel => 1.2.3, libogg-devel => 1.1.3, libvorbis-devel => 1.1.2

%define pmplibdocdir %_docdir/%name

# Automatically added by buildreq on Thu Jul 26 2007
BuildRequires: gcc-c++ gcc-fortran glibc-devel-static libid3tag-devel libvorbis-devel  zlib-devel

%description
Portable Media Player library (PMPlib) is a management software/library for 
various portable media players.

%package devel
Summary: Shared and static libraries for PMPlib
Group: Development/Other
Requires: %name = %version

%description devel
Portable Media Player library (PMPlib) is a management software/library for 
various portable media players.
This package contains shared libraries from the PMPlib project.

%package tools
Summary: Command-line tools for PMPlib (EasyPMP)
License: GPL
Group: Sound
Requires: %name = %version, libid3tag => 0.15.1, zlib => 1.2.3, libogg => 1.1.3, libvorbis => 1.1.2

%description tools
Portable Media Player library (PMPlib) is a management software/library for 
various portable media players.
This package contains a frontend program (EasyPMP) for PMPlib.

%prep
%setup

%build
%configure --disable-js
%__make

%install
%makeinstall

%files
%doc %pmplibdocdir/AUTHORS
%doc %pmplibdocdir/COPYING
%doc %pmplibdocdir/COPYING.LIB
%doc %pmplibdocdir/ChangeLog
%doc %pmplibdocdir/INSTALL
%doc %pmplibdocdir/README
%_libdir/pmplib/irivnavi.so
%_libdir/pmplib/portalplayer1.so
%_libdir/pmplib/iriverplus2.so
%_libdir/pmplib/iriverplus3.so
%_libdir/libpmp.so*

%files devel
%_libdir/pmplib/irivnavi.a
%_libdir/pmplib/irivnavi.la
%_libdir/pmplib/portalplayer1.a
%_libdir/pmplib/portalplayer1.la
%_libdir/pmplib/iriverplus2.a
%_libdir/pmplib/iriverplus2.la
%_libdir/pmplib/iriverplus3.a
%_libdir/pmplib/iriverplus3.la
%_libdir/libpmp.a
%_includedir/*

%files tools
%_bindir/easypmp
%_mandir/man1/easypmp.1*

%changelog
* Wed Sep 01 2010 Repocop Q. A. Robot <repocop@altlinux.org> 0.14-alt0.1.qa1
- NMU (by repocop): the following fixes applied:
  * deprecated-packages-info-i18n-common for pmplib
  * postclean-05-filetriggers for spec file

* Thu Jul 26 2007 Alex Karpov <karpov@altlinux.ru> 0.14-alt0.1
- initial build for Sisyphus

