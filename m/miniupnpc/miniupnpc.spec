%define soversion 16

Name: miniupnpc
Version: 2.0
Release: alt2

Summary: UPnP client library
License: BSD
Group: System/Libraries

Url: http://miniupnp.free.fr/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: http://miniupnp.free.fr/files/%name-%version.tar.gz

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

%build

%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING='Release' \
	-DUPNPC_BUILD_STATIC:BOOL=FALSE \
%if "%_lib" == "lib64"
	-DLIB_SUFFIX=64
%endif

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%__xz man3/%name.3
%__install -Dp -m0644 man3/%name.3.xz %buildroot%_man3dir/%name.3.xz

%files -n lib%name%soversion
%doc Changelog.txt LICENSE README VERSION
%_libdir/lib%name.so.*

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/lib%name.so
%_man3dir/%name.3.*

%changelog
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
