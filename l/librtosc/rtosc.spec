Name: librtosc
Version: 0.2.0
Release: alt1

Summary: Realtime safe OSC Messaging
License: MIT
Group: System/Libraries
Url: https://github.com/fundamental/rtosc

Source: %name-%version-%release.tar

BuildRequires: cmake gcc-c++

%package devel
Summary: Realtime safe OSC Messaging
Group: Development/C

%define desc\
A realtime safe library for handling OSC messages. This library is influenced by\
liblo and libmapper.

%description %desc

%description devel %desc
this package contains development part of librtosc

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_libdir/*.so.*

%files devel
%_includedir/rtosc
%_libdir/*.so
%_pkgconfigdir/*.pc

%changelog
* Wed Dec 01 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- v0.2.0-51-g75a5893
