
Name: libwpg
Version: 0.3.1
Release: alt1

Summary: Library for importing and converting Corel WordPerfect(tm) Graphics images

Group: System/Libraries
License: LGPL
Url: http://libwpg.sf.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/libwpg/%name-%version.tar

Provides: libwpg2 = %version-%release
Obsoletes: libwpg2 < %version-%release

BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: help2man
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(libwpd-0.10)

%description
libwpg is a library for reading and converting WPG images

%package tools
Requires: %name = %version-%release
Summary: Tools to convert WPG images into other formats
Group: Office

%description tools
Tools to convert WPG images into other formats.
Currently supported: raw svg

%package devel
Requires: %name = %version-%release
Summary: Files for developing with libwpg
Group: Development/C
Provides: libwpg2-devel = %version-%release
Obsoletes: libwpg2-devel < %version-%release

%description devel
Includes and definitions for developing with libwpg.

%package docs
Requires: %name = %version-%release
BuildRequires: doxygen
Summary: Documentation of libwpg API
Group: Documentation
BuildArch: noarch

%description docs
Documentation of libwpg API for developing with libwpg

%prep
%setup

%build
%autoreconf
%configure --disable-static --disable-werror
%make_build

find docs/doxygen/html |xargs touch -r docs/doxygen/doxygen.cfg
export LD_LIBRARY_PATH=`pwd`/src/lib/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -n 'debug the conversion library' -o wpg2raw.1 ./src/conv/raw/.libs/wpg2raw
help2man -N -n 'convert WordPerfect Graphics into SVG' -o wpg2svg.1 ./src/conv/svg/.libs/wpg2svg
help2man -N -n 'batch convert WordPerfect Graphics files into SVG' \
    --help-option=-h --no-discard-stderr \
    -o wpg2svgbatch.pl.1 ./src/conv/svg/wpg2svgbatch.pl

%install
%makeinstall_std

# we install API docs directly from build
rm -rf %buildroot%_docdir/%name

install -m 0755 -d %buildroot%_man1dir
install -m 0644 wpg2*.1 %buildroot%_man1dir/

%files
%doc AUTHORS COPYING.LGPL COPYING.MPL
%_libdir/libwpg*.so.*

%files tools
%_bindir/*
%_man1dir/*.1*

%files devel
%_libdir/*.so
%_pkgconfigdir/*.pc
%_includedir/*

%files docs
%doc COPYING.LGPL COPYING.MPL
%doc docs/doxygen/html

%changelog
* Sun Jan 03 2016 Vitaly Lipatov <lav@altlinux.ru> 0.3.1-alt1
- new version 0.3.1 (with rpmrb script)

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Wed Aug 07 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt3
- add provides/obsoletes for libwpg2-devel

* Tue Aug 06 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt2
- add provides/obsoletes for libwpg2

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2.2-alt1
- new version 0.2.2 (with rpmrb script)

* Tue Apr 23 2013 Repocop Q. A. Robot <repocop@altlinux.org> 0.1.3-alt2.qa3
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for libwpg-docs
  * postclean-03-private-rpm-macros for the spec file

* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt2.qa2
- Removed bad RPATH

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 0.1.3-alt2.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Sat Nov 08 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt2
- fix docs packing

* Wed Nov 05 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.3-alt1
- new version 0.1.3 (with rpmrb script)

* Sat Nov 03 2007 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- initial build for ALT Linux Sisyphus

* Fri Apr 20 2007 Fridrich Strba <fridrich.strba@bluewin.ch>
- Add documentation packaging
- Make doc and stream optional

* Tue Jan 27 2004 Fridrich Strba <fridrich.strba@bluewin.ch>
- Create rpm spec according to the rpm spec of libwpD
- of Rui M. Seabra
