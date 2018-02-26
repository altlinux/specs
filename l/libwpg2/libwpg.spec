Name: libwpg2
Version: 0.2.1
Release: alt1.1
Summary: Library for importing and converting Corel WordPerfect(tm) Graphics images
License: LGPL
Group: System/Libraries
URL: http://libwpg.sf.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: libwpg-%version.tar.bz2

BuildRequires: doxygen libwpd9-devel gcc-c++

%description
libwpg is a library for reading and converting WPG images

%package tools
Summary: Tools to convert WPG images into other formats
Group: Publishing
Requires: %name = %version-%release
Conflicts: libwpg < %version

%description tools
Tools to convert WPG images into other formats.
Currently supported: raw svg

%package devel
Summary: Files for developing with libwpg
Group: Development/C++
Requires: %name = %version-%release
Conflicts: libwpg-devel < %version

%description devel
Includes and definitions for developing with libwpg

%prep
%setup -q -n libwpg-%version

%build
%configure \
	--disable-static
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%make DESTDIR=%buildroot install

%files
%_libdir/libwpg*.so.*

%files tools
%_bindir/wpg2*

%files devel
%_docdir/libwpg
%_includedir/libwpg*
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1.1
- Removed bad RPATH

* Tue Dec 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Sat Dec 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- 0.2.0
