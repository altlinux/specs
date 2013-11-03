Name: miniupnpc
Version: 1.8.20131007
Release: alt1

Summary: UPnP client library
License: BSD
Group: System/Libraries

Url: http://miniupnp.free.fr/
Packager: Nazarov Denis <nenderus@altlinux.org>

Source: http://miniupnp.free.fr/files/%name-%version.tar.gz
Patch0: %name-%version-alt.patch

BuildRequires: cmake

%description
The miniupnpc library implement the UPnP protocol defined
to dialog with Internet Gateway Devices.

%package -n lib%name
Summary: UPnP client library
Group: System/Libraries

%description -n lib%name
The miniupnpc library implement the UPnP protocol defined
to dialog with Internet Gateway Devices.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Contains libraries and header files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

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
%__gzip man3/%name.3
%__install -Dp -m0644 man3/%name.3.gz %buildroot%_man3dir/%name.3.gz

%files -n lib%name
%doc Changelog.txt LICENSE README VERSION
%_libdir/lib%name.so.*

%files -n lib%name-devel
%dir %_includedir/%name
%_includedir/%name/*.h
%_libdir/lib%name.so
%_man3dir/%name.3.gz

%changelog
* Sun Nov 03 2013 Nazarov Denis <nenderus@altlinux.org> 1.8.20131007-alt1
- Initial build for ALT Linux
