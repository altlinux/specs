
Name: libmwaw
Version: 0.3.13
Release: alt1
Summary: Import library for some old mac text documents
Group: System/Libraries
# The entire source code is LGPLv2+/MPLv2.0 except
# src/lib/MWAWOLEStream.[ch]xx which are BSD. There is also
# src/tools/zip/zip.cpp which is GPLv2+, but we do not build the binary
# it is used for.
License: (LGPLv2+ or MPLv2.0) and BSD
Url: http://sourceforge.net/projects/libmwaw/
Source: %name-%version.tar

BuildRequires: gcc-c++
BuildRequires: boost-devel-headers
BuildRequires: libattr-devel
BuildRequires: pkgconfig(librevenge-0.0) pkgconfig(librevenge-stream-0.0) pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(zlib)
BuildRequires: doxygen

%description
libmwaw contains some import filters for old mac text documents
(MacWrite, ClarisWorks, ... ) based on top of the libwpd (which is
already used in three word processors).

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package doc
Summary: Documentation of %name API
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name.

%package tools
Summary: Tools to transform the supported formats into other formats
Group: Publishing
License: LGPLv2+
Requires: %name = %version-%release

%description tools
Tools to transform the supported document formats into other formats.
Supported output formats are XHTML, text and raw.

%prep
%setup

%build
mkdir -p m4
%autoreconf
%configure --disable-static --disable-werror

%make_build

%install
%makeinstall_std
# it seems this tool is only useful on MacOS
rm -f %buildroot/%_bindir/mwawFile

%files
%doc CHANGES COPYING.* README
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc COPYING.*
%dir %_docdir/%name
%_docdir/%name/html

%files tools
%_bindir/*

%changelog
* Mon Feb 12 2018 Alexey Shabalin <shaba@altlinux.ru> 0.3.13-alt1
- 0.3.13

* Tue Aug 18 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.5-alt1
- 0.3.5

* Mon Jan 19 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.4-alt1
- 0.3.4

* Wed Dec 17 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Thu Aug 28 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 0.2.0-alt1
- new version

* Tue Aug 13 2013 Alexey Shabalin <shaba@altlinux.ru> 0.1.10-alt1
- initial build
