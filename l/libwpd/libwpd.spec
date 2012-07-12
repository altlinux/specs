Name: libwpd
Version: 0.8.14
Release: alt3.1
Summary: Library for reading and converting WordPerfect(tm) documents.
License: LGPL
Group: System/Libraries
URL: http://libwpd.sf.net/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.bz2
Patch: libwpd-0.8.14-alt-gcc4.6.patch

# Automatically added by buildreq on Thu Oct 05 2006
BuildRequires: doxygen gcc-c++ libgsf-devel

%description
Library that handles Word Perfect documents.

%package tools
Requires: libwpd
Summary: Tools to transform WordPerfect Documents into other formats
Group: Publishing

%description tools
Tools to transform WordPerfect Documents into other formats.
Currently supported: html, raw, text

%package devel
Requires: libwpd
Summary: Files for developing with libwpd.
Group: Development/C++

%description devel
Includes and definitions for developing with libwpd.

%prep
%setup -q
%patch -p2

%build
%configure \
    --disable-static
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%make DESTDIR=%buildroot install

find %buildroot%_docdir/%name-%version -type f -exec chmod -x {} \;

%files
%_libdir/*.so.*

%files tools
%_bindir/wpd2*

%files devel
%doc %_docdir/%name-%version
%_includedir/libwpd-0.8
%_libdir/*.so
%_pkgconfigdir/*

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.14-alt3.1
- Fixed build

* Tue Nov 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.8.14-alt3
- rebuild

* Sat Nov 22 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.8.14-alt2
- removed obsolete %%post_ldconfig/%%postun_ldconfig calls

* Wed Feb 13 2008 Valery Inozemtsev <shrek@altlinux.ru> 0.8.14-alt1
- 0.8.14

* Fri Dec 28 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.8.13-alt1
- 0.8.13

* Fri Oct 19 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.8.12-alt1
- 0.8.12

* Wed Sep 12 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.8.11-alt1
- 0.8.11

* Mon Jul 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.8.10-alt1
- 0.8.10

* Fri Mar 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.8.9-alt1
- 0.8.9
  + fixed CVE-2007-0002

* Tue Jan 16 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.8.8-alt1
- 0.8.8

* Thu Oct 05 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.8.6-alt1
- 0.8.6
- updated build dependencies
- build doc

* Fri Mar 31 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.0-alt1.1.1.1
- Rebuild with libgsf-1.so.114.

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.0-alt1.1.1
- Rebuilt for new pkg-config dependencies.

* Tue Nov 15 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.0-alt1.1
- rebuild with libgsf-1.so.113 .

* Tue Mar 29 2005 Kachalov Anton <mouse@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Fri Sep 19 2003 AEN <aen@altlinux.ru> 0.6.2-alt1
- new package for Sisyphus,based on RH package

* Mon Sep 15 2003 Jeremy Katz <katzj@redhat.com> 0.6.2-1
- 0.6.2

* Sun Jul  6 2003 Jeremy Katz <katzj@redhat.com> 0.5.0-1
- initial build for Red Hat Linux, tweak accordingly

* Sat Apr 26 2003 Rui M. Seabra <rms@1407.org>
- Create rpm spec
