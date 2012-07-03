Name: libwps
Version: 0.2.4
Release: alt1.1
Summary: Library for reading and converting Microsoft Works word processor documents
License: LGPL
Group: System/Libraries
URL: http://libwps.sourceforge.net/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar.bz2

BuildRequires: libwpd9-devel gcc-c++ doxygen

%description
Library that handles Microsoft Works documents

%package tools
Summary: Tools to transform Works documents into other formats
Group: Publishing
Requires: %name = %version-%release

%description tools
Tools to transform Works documents into other formats.
Currently supported: html, raw, text

%package devel
Summary: Files for developing with libwps
Group: Development/C++
Requires: %name = %version-%release

%description devel
Includes and definitions for developing with libwps

%prep
%setup -q

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
%_bindir/wps2*

%files devel
%_docdir/%name
%_includedir/%name-0.2
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Sat Feb 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.4-alt1.1
- Removed bad RPATH

* Tue Dec 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.2.4-alt1
- 0.2.4

* Sat Dec 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.2.0-alt1
- initial release
