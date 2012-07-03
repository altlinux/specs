Name: libwpd9
Version: 0.9.4
Release: alt1.1
Summary: Library for reading and converting WordPerfect(tm) documents
License: LGPL
Group: System/Libraries
URL: http://libwpd.sf.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: libwpd-%version.tar.bz2

BuildRequires: doxygen gcc-c++ libgsf-devel

%description
Library that handles Word Perfect documents

%package tools
Requires: libwpd
Summary: Tools to transform WordPerfect Documents into other formats
Group: Publishing
Requires: %name = %version-%release
Conflicts: libwpd-tools < %version

%description tools
Tools to transform WordPerfect Documents into other formats.
Currently supported: html, raw, text

%package devel
Requires: libwpd
Summary: Files for developing with libwpd
Group: Development/C++
Requires: %name = %version-%release
Conflicts: libwpd-devel < %version

%description devel
Includes and definitions for developing with libwpd

%prep
%setup -q -n libwpd-%version

%build
%configure \
    --disable-static
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%make DESTDIR=%buildroot install

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
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.1
- Removed bad RPATH

* Tue Dec 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Sat Dec 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.0-alt1
- 0.9.0
