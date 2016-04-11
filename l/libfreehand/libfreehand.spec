Name: libfreehand
Version: 0.1.0
Release: alt1.qa1
Summary: A library for import of Macromedia/Adobe FreeHand documents

Group: System/Libraries
License: MPLv2.0
Url: http://www.freedesktop.org/wiki/Software/libfreehand/
Source: http://dev-www.libreoffice.org/src/%name-%version.tar.xz

BuildRequires: gcc-c++
BuildRequires: boost-devel-headers
BuildRequires: pkgconfig(librevenge-0.0) pkgconfig(librevenge-stream-0.0) pkgconfig(librevenge-generators-0.0)
BuildRequires: pkgconfig(zlib)

BuildRequires: doxygen
BuildRequires: gperf

%description
libfreehand is library providing ability to interpret and import
Macromedia/Adobe FreeHand documents into various applications.

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
Summary: Tools to transform Macromedia/Adobe FreeHand documents into other formats
Group: Publishing

%description tools
Tools to transform Macromedia/Adobe FreeHand documents into other formats.
Currently supported: SVG, raw.

%prep
%setup

%build
mkdir -p m4
%autoreconf
%configure --disable-silent-rules --disable-static --disable-werror
%make_build

%install
%makeinstall_std
# we install API docs directly from build
rm -rf %buildroot/%_docdir/%name

%files
%doc AUTHORS COPYING
%_libdir/*.so.*

%files devel
%doc ChangeLog
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc

%files doc
%doc COPYING
%doc docs/doxygen/html

%files tools
%_bindir/*

%changelog
* Mon Apr 11 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 0.1.0-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Thu Jun 05 2014 Alexey Shabalin <shaba@altlinux.ru> 0.1.0-alt1
- 0.1.0

* Wed Mar 19 2014 Fr. Br. George <george@altlinux.ru> 0.0.0-alt1
- Initial build from FC

* Mon Nov 04 2013 David Tardon <dtardon@redhat.com> - 0.0.0-3
- fix memory leak

* Thu Oct 31 2013 David Tardon <dtardon@redhat.com> 0.0.0-2
- add gperf to BuildRequires

* Thu Oct 31 2013 David Tardon <dtardon@redhat.com> 0.0.0-1
- initial import
