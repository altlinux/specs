%define oname aften
Name: libaften
Version: 0.0.8
Release: alt1.qa2
Serial: 1

Summary: Aften: A/52 audio encoder

License: LGPL
Group: System/Libraries
Url: http://%oname.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sourceforge.net/%oname/%oname-%version.tar.bz2

# Automatically added by buildreq on Thu Aug 02 2007
BuildRequires: cmake yasm subversion

%description
A simple AC3-compatible audio encoder based on FFmpeg.

%package devel
Summary: Header files for %name library
Group: Development/C++
Requires: %name = %version-%release

%description devel
Header files for %name library.

%prep
%setup -q -n %oname-%version

%build
mkdir -p default && cd default
cmake .. -DCMAKE_INSTALL_PREFIX:STRING="/usr" -DSHARED=yes
%make_build

%install
cd default
%make_install install DESTDIR=%buildroot
# hack due broken install target in CMakeList
test -d %buildroot%_libdir || mv %buildroot%_prefix/lib %buildroot%_libdir

%files
%_bindir/*
%doc README
%_libdir/lib*.so.*

%files devel
%_libdir/lib*.so
%_includedir/*

%changelog
* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 1:0.0.8-alt1.qa2
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1:0.0.8-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libaften
  * postun_ldconfig for libaften
  * postclean-05-filetriggers for spec file

* Thu Sep 20 2007 Vitaly Lipatov <lav@altlinux.ru> 1:0.0.8-alt1
- new version 0.0.8 (with rpmrb script)
- add Serial:1 due version format change

* Fri Aug 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt2
- use yasm instead nasm
- fix build on x86_64

* Thu Aug 02 2007 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt1
- initial build for ALT Linux Sisyphus

