%define oname ezV24

Name: libezV24
Version: 0.1.1
Release: alt3.qa1

Summary: Serial ports interface library

License: LGPL
Group: System/Libraries
Url: http://ezV24.sourceforge.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%oname/%name-%version.tar.bz2
Patch: %name-0.1.1-alt-makefile.patch

%description
%name library provides a easy to use interface to the serial ports of the
linux system.

%package devel
Summary: Header files and libraries for %name development
Group: Development/C
Requires: %name = %version-%release

%description devel
%name libary provides a easy to use interface to the serial ports of the
linux system.

This package provides the header files and libraries
needed for %name development.

%prep
%setup -q
%patch -p1
%__subst "s|%oname/%oname|%oname|g" test-v24.c
%__subst "s|/lib/|/%_lib/|g" Makefile

%build
%make

%install
%makeinstall_std

install -pD test-v24 %buildroot%_bindir/test-v24
rm -f %buildroot%_libdir/*.a

%files
%_libdir/*.so.*

%files devel
%_bindir/test-v24
%_includedir/ezV24/
%_libdir/*.so
%doc README api-html

%changelog
* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.1.1-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Fri Jan 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt3
- cleanup spec
- change license to LGPL (as in COPYING)

* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.1-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libezV24
  * postun_ldconfig for libezV24
  * postclean-05-filetriggers for spec file

* Tue Jul 31 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt2
- change Packager, cleanup spec
- fix x86_64 build

* Wed Oct 29 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.1.1-alt1
- First build for Sisyphus.

