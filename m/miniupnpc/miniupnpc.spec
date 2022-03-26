%define soversion 17

Name: miniupnpc
Version: 2.2.3
Release: alt1

Summary: UPnP client library
License: BSD
Group: System/Libraries

Url: http://miniupnp.free.fr/
Packager: Nazarov Denis <nenderus@altlinux.org>

# http://miniupnp.free.fr/files/%name-%version.tar.gz
Source: %name-%version.tar

Patch0: %name-alt-cmake.patch

BuildRequires: cmake

%description
The miniupnpc library implement the UPnP protocol defined
to dialog with Internet Gateway Devices.

%package -n lib%name%soversion
Summary: UPnP client library
Group: System/Libraries

%description -n lib%name%soversion
The miniupnpc library implement the UPnP protocol defined
to dialog with Internet Gateway Devices.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C

%description -n lib%name-devel
Contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch0 -p2

%build
%cmake -DUPNPC_BUILD_STATIC:BOOL=FALSE
%cmake_build

%install
%cmakeinstall_std
%__xz man3/%name.3
%__install -Dp -m0644 man3/%name.3.xz %buildroot%_man3dir/%name.3.xz

%files -n lib%name%soversion
%doc Changelog.txt LICENSE README VERSION
%_libdir/lib%name.so.*

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/*.h
%dir %_libdir/cmake/%name
%_libdir/cmake/%name/*.cmake
%_libdir/lib%name.so
%_man3dir/%name.3.*

%changelog
* Sat Mar 26 2022 Nazarov Denis <nenderus@altlinux.org> 2.2.3-alt1
- Version 2.2.3

* Thu Mar 04 2021 Nazarov Denis <nenderus@altlinux.org> 2.2.2-alt1
- Version 2.2.2

* Sun Feb 14 2021 Nazarov Denis <nenderus@altlinux.org> 2.2.1-alt1
- Version 2.2.1

* Thu Apr 12 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0-alt2
- fixed packaging on 64bit arches other than x86_64

* Wed Jul 13 2016 Nazarov Denis <nenderus@altlinux.org> 2.0-alt1
- Version 2.0

* Sun Jan 24 2016 Nazarov Denis <nenderus@altlinux.org> 1.9-alt2
- Fix man file

* Sat Feb 08 2014 Nazarov Denis <nenderus@altlinux.org> 1.9-alt0.M70T.1
- Build for branch t7

* Sat Feb 01 2014 Nazarov Denis <nenderus@altlinux.org> 1.9-alt1
- Version 1.9

* Tue Dec 24 2013 Nazarov Denis <nenderus@altlinux.org> 1.8.20131209-alt1
- Version 1.8.20131209

* Sun Nov 03 2013 Nazarov Denis <nenderus@altlinux.org> 1.8.20131007-alt1
- Initial build for ALT Linux
