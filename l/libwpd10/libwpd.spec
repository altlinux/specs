%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%define oname wpd
%define soname 10

Name: lib%oname%soname
Version: 0.10.3
Release: alt2
Summary: Library for reading and converting WordPerfect(tm) documents
License: LGPLv2+ or MPL-2.0
Group: System/Libraries
Url: http://libwpd.sf.net/

Source: libwpd-%version.tar

Patch1: libwpd-alt-build.patch

BuildRequires: boost-devel-headers help2man librevenge-devel
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(zlib)

Obsoletes: libwpd9 >= 0.10.0

%description
Library that handles Word Perfect documents

%package tools
Summary: Tools to transform WordPerfect Documents into other formats
Group: Publishing
Requires: %name = %EVR
Conflicts: libwpd-tools < %version
Conflicts: libwpd9-tools < %version
Provides: lib%oname-tools = %EVR

%description tools
Tools to transform WordPerfect Documents into other formats.
Currently supported: html, raw, text

%package devel
Summary: Files for developing with libwpd
Group: Development/C++
Requires: %name = %EVR
Conflicts: libwpd-devel < %version
Conflicts: libwpd9-devel < %version
Provides: lib%oname-devel = %EVR

%description devel
Includes and definitions for developing with libwpd

%package doc
Summary: Documentation of %name API
Group: Documentation
BuildArch: noarch
Provides: lib%oname-doc = %EVR

%description doc
The %name-doc package contains API documentation for %name.

%prep
%setup -n lib%oname-%version
%patch1 -p2

%build
%autoreconf
%configure --disable-static --disable-werror
%make_build

export LD_LIBRARY_PATH=`pwd`/src/lib/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
help2man -N -n 'debug the conversion library' -o wpd2raw.1 ./src/conv/raw/.libs/wpd2raw
help2man -N -n 'convert WordPerfect document into HTML' -o wpd2html.1 ./src/conv/html/.libs/wpd2html
help2man -N -n 'convert WordPerfect document into plain text' -o wpd2text.1 ./src/conv/text/.libs/wpd2text

%install
%makeinstall_std
# we install API docs directly from build
rm -rf %buildroot%_docdir/libwpd

install -m 0755 -d %buildroot%_man1dir
install -m 0644 wpd2*.1 %buildroot%_man1dir/

%check
LD_LIBRARY_PATH=../lib/.libs make check

%files
%doc COPYING.LGPL COPYING.MPL CREDITS README
%_libdir/*.so.%soname
%_libdir/*.so.%soname.*

%files tools
%_bindir/*
%_man1dir/*.1*

%files devel
%doc HACKING TODO
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc COPYING.LGPL COPYING.MPL
%doc docs/doxygen/html
%doc docs/*.dia
%doc docs/*.png

%changelog
* Wed Oct 06 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.3-alt2
- Fixed build with gcc-11.

* Thu Jul 09 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.10.3-alt1
- Updated to upstream version 0.10.3.

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 0.10.2-alt1
- Autobuild version bump to 0.10.2

* Mon Jul 31 2017 Fr. Br. George <george@altlinux.ru> 0.10.1-alt1
- Autobuild version bump to 0.10.1

* Tue May 10 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.10.0-alt2
- NMU
- added "Obsoletes: libwpd9 >= 0.10.0" (ALT #31956)

* Wed Apr 13 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.10.0-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.10.0-alt1
- 0.10.0
- build as libwpd10

* Tue Mar 18 2014 Fr. Br. George <george@altlinux.ru> 0.9.9-alt1
- Autobuild version bump to 0.9.9

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2
- drop broken requires on libwpd, cleanup spec

* Mon Jul 29 2013 Fr. Br. George <george@altlinux.ru> 0.9.7-alt1
- Autobuild version bump to 0.9.7

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.1
- Removed bad RPATH

* Mon Dec 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Sat Dec 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0-alt1
- 0.9.0
