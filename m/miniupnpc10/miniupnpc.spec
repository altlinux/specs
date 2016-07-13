%define pkgname miniupnpc
%define soversion 10

Name: %pkgname%soversion
Version: 1.9
Release: alt3

Summary: UPnP client library
License: BSD
Group: System/Legacy libraries

Url: http://miniupnp.free.fr/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: http://miniupnp.free.fr/files/%pkgname-%version.tar.gz

BuildRequires: cmake

%description
The miniupnpc library implement the UPnP protocol defined
to dialog with Internet Gateway Devices.

%package -n lib%pkgname
Summary: UPnP client library
Group: System/Legacy libraries

%description -n lib%pkgname
The miniupnpc library implement the UPnP protocol defined
to dialog with Internet Gateway Devices.

%prep
%setup -n %pkgname-%version

%build
%define lib_suffix %nil
%ifarch x86_64
%define lib_suffix 64
%endif

%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING='Release' \
	-DUPNPC_BUILD_STATIC:BOOL=FALSE \
	-DLIB_SUFFIX=%lib_suffix

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform

%__rm -rf %buildroot%_includedir/%pkgname
%__rm -rf %buildroot%_libdir/lib%pkgname.so

%files -n lib%pkgname
%doc Changelog.txt LICENSE README VERSION
%_libdir/lib%pkgname.so.*

%changelog
* Wed Jul 13 2016 Nazarov Denis <nenderus@altlinux.org> 1.9-alt3
- Build as legacy library

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
