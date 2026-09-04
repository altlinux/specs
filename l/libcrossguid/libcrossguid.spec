Name: libcrossguid
Version: 0.2.2
Release: alt1
Epoch: 1

Summary: C++ GUID library
License: MIT
Group: System/Libraries
Url: https://github.com/graeme-hill/crossguid/

Source: %name-%version.tar

BuildRequires: cmake gcc-c++ libuuid-devel

%package devel
Summary: C++ GUID library
Group: Development/C++

%description
CrossGuid is a minimal, cross platform, C++ GUID library. It uses the best
native GUID/UUID generator on the given platform and had a generic class
for parsing, stringifying, and comparing IDs.

%description devel
CrossGuid is a minimal, cross platform, C++ GUID library. It uses the best
native GUID/UUID generator on the given platform and had a generic class
for parsing, stringifying, and comparing IDs.
This package contains development part of %name

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%define _customdocdir %_docdir/crossguid

%files
%_docdir/crossguid
%_libdir/*.so.*

%files devel
%_includedir/crossguid
%_libdir/*.so
%_libdir/cmake/crossguid
%_pkgconfigdir/*.pc

%changelog
* Tue Jan 27 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1:0.2.2-alt1
- v0.2.2-52-gca1bf4b

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 20150803-alt1.1
- NMU: added URL

* Tue Mar 08 2016 Sergey Bolshakov <sbolshakov@altlinux.ru> 20150803-alt1
- initial
