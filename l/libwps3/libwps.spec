
Name: libwps3
Version: 0.3.0
Release: alt2
Summary: Library for reading and converting Microsoft Works word processor documents

Group: System/Libraries
License: LGPLv2+ or MPLv2.0
Url: http://libwps.sourceforge.net/
Source: libwps-%version.tar

BuildRequires: gcc-c++
BuildRequires: boost-devel-headers
BuildRequires: pkgconfig(librevenge-0.0) pkgconfig(librevenge-stream-0.0) pkgconfig(librevenge-generators-0.0)

BuildRequires: doxygen
BuildRequires: gperf

%description
Library that handles Microsoft Works documents and spreadsheets.

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package tools
Summary: Tools to transform Works documents into other formats
Group: Publishing
Requires: %name = %version-%release

%description tools
Tools to transform Works documents and spreadsheets into other formats.
Currently supported: CSV, HTML, raw, text

%package doc
Summary: Documentation of %name API
Group: Documentation
BuildArch: noarch

%description doc
The %name-doc package contains documentation files for %name

%prep
%setup -n libwps-%version

%build
mkdir -p m4
%autoreconf
%configure --disable-silent-rules --disable-static --disable-werror
%make_build

%install
%makeinstall_std

# we install API docs directly from build
rm -rf %buildroot%_defaultdocdir/libwps

%files
%doc COPYING.LGPL COPYING.MPL CREDITS NEWS README
%_libdir/*.so.*

%files devel
%doc HACKING
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files tools
%_bindir/*
# ??? GONE
#_man1dir/man1/*.1*

%files doc
%doc COPYING.LGPL COPYING.MPL
%doc docs/doxygen/html

%changelog
* Mon Nov 02 2015 Fr. Br. George <george@altlinux.ru> 0.3.0-alt2
- Build legacy version

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- initial build
