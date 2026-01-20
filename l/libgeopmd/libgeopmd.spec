%define soversion 2
%define abi_ver 2.2.0

Name: libgeopmd
Version: 3.2.2
Release: alt1

Summary: C/C++ implementation of the GEOPM access service
License: BSD-3-Clause
Group: System/Libraries

URL: https://geopm.github.io
VCS: https://github.com/geopm/geopm.git
Source0: %name-%version.tar
ExclusiveArch: x86_64

BuildRequires: gcc-c++
BuildRequires: libgrpc++-devel
BuildRequires: glibc-devel
BuildRequires: libgmock-devel
BuildRequires: libgrpc-devel
BuildRequires: libgtest-devel
BuildRequires: libcap-devel
BuildRequires: libtool
BuildRequires: liburing-devel
BuildRequires: libprotobuf-devel
BuildRequires: libsystemd-devel
BuildRequires: zlib-ng-devel
BuildRequires: protobuf-compiler
BuildRequires: grpc-plugins
BuildRequires: rpm-build-vm

%description
The GEOPM framework allows users to monitor system energy consumption
and safely optimize hardware settings to meet
efficiency or performance goals.

%package -n libgeopmd%soversion
Summary: GEOPM access service library (ABI version %soversion)
Group: System/Configuration/Other

%description -n libgeopmd%soversion
The GEOPM access service library (ABI version %soversion).

%package -n libgeopmd-devel
Summary: Development files for %name
Requires: %name%soversion = %EVR
Group: System/Configuration/Other

%description -n libgeopmd-devel
The %name-devel package contains libraries and header files for
applications that use %name.

%package -n geopmd-cli
Group: System/Configuration/Other
Summary: libgeopmd command-line tools
Requires: %name%soversion = %EVR

%description -n geopmd-cli
Command-line tools for GEOPM access service.

%prep
%setup -q %name-%version
pushd %name
echo %version > VERSION
popd

%build
pushd %name
%autoreconf
%configure \
        --disable-build-gtest \
        --enable-grpc
%make_build
popd

%install
pushd %name
mkdir -p %buildroot/%_sbindir
%makeinstall_std
rm -v %buildroot/%_libdir/libgeopmd.a
mv %buildroot/%_bindir/geopmbatch %buildroot/%_sbindir/
popd

%check
pushd %name
vm-run --cpu=4 --kvm=cond --user make check
popd

%files -n libgeopmd%soversion
%doc CONTRIBUTING.rst
%doc %_docdir/%name/README.md
%doc %_docdir/%name/LICENSE-BSD-3-Clause
%doc %_docdir/%name/VERSION
%_libdir/libgeopmd.so.%abi_ver
%_libdir/libgeopmd.so.%soversion

%files devel
%_includedir/geopm
%_includedir/geopm_*
%_libdir/libgeopmd.so

%files -n geopmd-cli
%_sbindir/geopmbatch

%changelog
* Thu Jan 15 2026 Danila Skachedubov <skachedubov@altlinux.org> 3.2.2-alt1
- first build for ALT
