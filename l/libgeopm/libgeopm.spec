%define abi_ver 2.2.0
%define soversion 2

Name: libgeopm
Version: 3.2.2
Release: alt1

Summary: Global Extensible Open Power Manager runtime library
Group: System/Libraries
License: BSD-3-Clause

URL: https://geopm.github.io
VCS: https://github.com/geopm/geopm.git
Source0: %name-%version.tar
ExclusiveArch: x86_64

BuildRequires: gcc-c++
BuildRequires: libgmock-devel
BuildRequires: libgtest-devel
BuildRequires: libtool
BuildRequires: libelf-devel
BuildRequires: libgeopmd-devel
BuildRequires: rpm-build-vm

%description
The Global Extensible Open Power Manager (GEOPM) provides a framework
to explore power and energy optimizations on heterogeneous hardware.
Users can monitor system energy consumption and optimize hardware
settings for efficiency or performance goals.

%package -n libgeopm%soversion
Summary: GEOPM runtime library (ABI version %soversion)
Group: System/Libraries

%description -n libgeopm%soversion
Runtime library for GEOPM power management framework (ABI version %soversion).

%package -n libgeopm-devel
Summary: Development files for %name
Group: Development/C
Requires: %name%soversion = %EVR

%description -n libgeopm-devel
The %name-devel package contains libraries and header files for
applications that use %name.

%package -n geopm-cli
Summary: The libgeopm command-line tools
Group: System/Configuration/Other
Requires: %name%soversion = %EVR

%description -n geopm-cli
Command-line utilities for GEOPM power management framework.

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
    --disable-mpi \
    --disable-openmp \
    --disable-fortran \
    --disable-geopmd-local \
    || ( cat config.log && false )
%make_build
popd

%install
pushd %name
mkdir -p %buildroot%_sbindir
%makeinstall_std
rm -v %buildroot/%_libdir/%name.a
rm -v %buildroot/%_libdir/geopm/libgeopmiogroup_profile.a
rm -v %buildroot/%_libdir/geopm/libgeopmiogroup_profile.la
mv %buildroot%_bindir/geopmadmin %buildroot%_sbindir/
popd

%check
pushd %name
vm-run --cpu=4 --kvm=cond --user make check
popd

%files -n libgeopm%soversion
%doc %_docdir/%name/README.md
%doc %_docdir/%name/LICENSE-BSD-3-Clause
%doc %_docdir/%name/VERSION
%_libdir/libgeopm.so.%soversion
%_libdir/libgeopm.so.%soversion.*
%_libdir/geopm/libgeopmiogroup_profile.so.%soversion
%_libdir/geopm/libgeopmiogroup_profile.so.%soversion.*

%files devel
%_includedir/geopm
%_includedir/geopm_*
%_libdir/libgeopm.so
%_libdir/geopm/libgeopmiogroup_profile.so

%files -n geopm-cli
%_sbindir/geopmadmin
%_bindir/geopmagent
%_bindir/geopmctl

%changelog
* Thu Jan 15 2026 Danila Skachedubov <skachedubov@altlinux.org> 3.2.2-alt1
- first build for ALT
