Name: libwpd9
Version: 0.10.1
Release: alt1

Summary: Library for reading and converting WordPerfect(tm) documents

License: LGPL
Group: System/Libraries
Url: http://libwpd.sf.net/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: libwpd-%version.tar.xz

BuildRequires: doxygen gcc-c++ libgsf-devel zlib-devel librevenge-devel

%description
Library that handles Word Perfect documents

%package tools
Summary: Tools to transform WordPerfect Documents into other formats
Group: Publishing
Requires: %name = %version-%release
Conflicts: libwpd-tools < %version

%description tools
Tools to transform WordPerfect Documents into other formats.
Currently supported: html, raw, text

%package devel
Summary: Files for developing with libwpd
Group: Development/C++
Requires: %name = %version-%release
Conflicts: libwpd-devel < %version

%description devel
Includes and definitions for developing with libwpd

%prep
%setup -n libwpd-%version

%build
%configure \
    --disable-static
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

%files
%_libdir/*.so.*

%files tools
%_bindir/wpd2*

%files devel
%doc %_docdir/libwpd
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Mon Oct 31 2016 Fr. Br. George <george@altlinux.ru> 0.10.1-alt1
- Autobuild version bump to 0.10.1

* Mon Aug 25 2014 Fr. Br. George <george@altlinux.ru> 0.10.0-alt1
- Autobuild version bump to 0.10.0
- Fix buildreq

* Tue Mar 18 2014 Fr. Br. George <george@altlinux.ru> 0.9.9-alt1
- Autobuild version bump to 0.9.9

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9.7-alt2
- drop broken requires on libwpd, cleanup spec

* Mon Jul 29 2013 Fr. Br. George <george@altlinux.ru> 0.9.7-alt1
- Autobuild version bump to 0.9.7

* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.1
- Removed bad RPATH

* Tue Dec 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Sat Dec 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0-alt1
- 0.9.0
