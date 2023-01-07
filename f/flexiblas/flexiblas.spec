%global default_backend netlib
%global default_backend64 %{default_backend}64

%global major_version 3
%global minor_version 3
%global patch_version 0

Name: flexiblas
Version: %major_version.%minor_version.%patch_version
Release: alt1
Summary: A BLAS/LAPACK wrapper library with runtime exchangeable backends
Group: Sciences/Mathematics
# GPLv3 with an exception for the BLAS/LAPACK interface
# https://www.gnu.org/licenses/gpl-faq.en.html#LinkingOverControlledInterface
# libcscutils/ is LGPLv2+
# contributed/ and test/ are BSD
License: GPLv3 with exceptions and LGPLv2+ and BSD
Url: https://www.mpi-magdeburg.mpg.de/projects/%name
Source0: %name-%version.tar
VCS: https://github.com/mpimd-csc/flexiblas

BuildRequires: make, cmake, python3
BuildRequires: gcc-fortran, gcc-c++, /usr/bin/ctest

%define _description FlexiBLAS is a wrapper library that enables the exchange of the BLAS and \
LAPACK implementation used by a program without recompiling or relinking it.

%description
%_description

%package -n lib%name.%major_version
Summary: FlexiBLAS wrapper library
Group: Sciences/Mathematics

%description -n lib%name.%major_version
%_description

%package netlib
Summary: FlexiBLAS wrapper library
Group: Sciences/Mathematics
Requires: %name = %EVR
Requires: %name-%default_backend = %EVR
Requires: lib%name.%major_version = %EVR

%description netlib
%_description
This package contains the wrapper library with 32-bit integer support.

%package hook-profile
Summary: FlexiBLAS profile hook plugin
Group: Sciences/Mathematics
Requires: %name = %EVR
Requires: %name-netlib = %EVR

%description hook-profile
%_description
This package contains a plugin that enables profiling support.

%package -n lib%name-devel
Summary: Development headers and libraries for FlexiBLAS
Group: Development/C
Requires: %name = %EVR
Requires: %name-netlib = %EVR
%if 0%{?__isa_bits} == 64
Requires: %name-netlib64 = %EVR
%endif

%description -n lib%name-devel
%_description
This package contains the development headers and libraries.

%if "%_pointer_size" == "64"
%package -n lib%{name}64.%major_version
Summary: FlexiBLAS wrapper library
Group: Sciences/Mathematics

%description -n lib%{name}64.%major_version
%_description

%package netlib64
Summary: FlexiBLAS wrapper library (64-bit)
Group: Sciences/Mathematics
Requires: %name = %EVR
Requires: lib%{name}64.%major_version = %EVR
Requires: %name-%default_backend64 = %EVR

%description netlib64
%_description
This package contains the wrapper library with 64-bit integer support.

%package hook-profile64
Summary: FlexiBLAS profile hook plugin (64-bit)
Group: Sciences/Mathematics
Requires: %name = %EVR
Requires: %name-netlib64 = %EVR

%description hook-profile64
%_description
This package contains a plugin that enables profiling support.
%endif

%prep
%setup

%build
%cmake -B build \
    -DCMAKE_INSTALL_PREFIX=%prefix \
    -DINTEGER8=OFF \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DTESTS=ON
%make_build -C build
%if "%_pointer_size" == "64"
%cmake -B build64 \
    -DCMAKE_INSTALL_PREFIX=%prefix \
    -DINTEGER8=ON \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DTESTS=ON
%make_build -C build64
%endif

%install
%makeinstall_std -C build
echo "default = %default_backend" > %buildroot%_sysconfdir/%{name}rc
%if "%_pointer_size" == "64"
%makeinstall_std -C build64
echo "default = %default_backend64" > %buildroot%_sysconfdir/%{name}64rc
%endif

# remove dummy hook
rm -f %buildroot%_libdir/%{name}*/lib%{name}_hook_dummy.so

rename -- serial -serial %buildroot%_libdir/%{name}*/* || true
rename -- openmp -openmp %buildroot%_libdir/%{name}*/* || true
rename -- pthread -threads %buildroot%_libdir/%{name}*/* || true
rename NETLIB netlib %buildroot%_sysconfdir/%{name}*.d/* || true
rename ATLAS atlas %buildroot%_sysconfdir/%{name}*.d/* || true
rename Blis blis %buildroot%_sysconfdir/%{name}*.d/* || true
rename OpenBLAS openblas %buildroot%_sysconfdir/%{name}*.d/* || true
rename -- Serial -serial %buildroot%_sysconfdir/%{name}*.d/* || true
rename -- OpenMP -openmp %buildroot%_sysconfdir/%{name}*.d/* || true
rename -- PThread -threads %buildroot%_sysconfdir/%{name}*.d/* || true
find %buildroot%_sysconfdir/%{name}*.d/* -type f \
    -exec sed -i 's NETLIB netlib gI' {} \;\
    -exec sed -i 's ATLAS atlas gI' {} \;\
    -exec sed -i 's Blis blis gI' {} \;\
    -exec sed -i 's OpenBLAS openblas gI' {} \;\
    -exec sed -i 's Serial -serial gI' {} \;\
    -exec sed -i 's OpenMP -openmp gI' {} \;\
    -exec sed -i 's PThread -threads gI' {} \;

%check
export FLEXIBLAS_TEST=%buildroot%_libdir/%name/lib%{name}_%default_backend.so
make -C build test
%if "%_pointer_size" == "64"
export FLEXIBLAS64_TEST=%buildroot%_libdir/%{name}64/lib%{name}_%default_backend64.so
make -C build64 test
%endif

%files
%doc COPYING COPYING.NETLIB
%doc ISSUES.md README.md CHANGELOG

%files -n lib%name.%major_version
%_libdir/lib%name.so.%major_version
%_libdir/lib%name.so.%major_version.%minor_version
%_libdir/lib%{name}_api.so.%major_version
%_libdir/lib%{name}_api.so.%major_version.%minor_version
%_libdir/lib%{name}_mgmt.so.%major_version
%_libdir/lib%{name}_mgmt.so.%major_version.%minor_version

%files netlib
%config(noreplace) %_sysconfdir/%{name}rc
%dir %_sysconfdir/%{name}rc.d
%_sysconfdir/%{name}rc.d/netlib.conf
%_bindir/%name
%dir %_libdir/%name
%_libdir/%name/lib%{name}_fallback_lapack.so
%_libdir/%name/lib%{name}_netlib.so
%_mandir/man1/%name.1*

%files hook-profile
%_libdir/%name/lib%{name}_hook_profile.so

%files -n lib%name-devel
%_bindir/%name-config
%_includedir/%name
%_libdir/lib%name.so
%_libdir/lib%{name}_api.so
%_libdir/lib%{name}_mgmt.so
%_libdir/pkgconfig/%name.pc
%_libdir/pkgconfig/%{name}_api.pc
%if "%_pointer_size" == "64"
%_bindir/%{name}64-config
%_includedir/%{name}64
%_libdir/lib%{name}64.so
%_libdir/lib%{name}64_api.so
%_libdir/lib%{name}64_mgmt.so
%_libdir/pkgconfig/%{name}64.pc
%_libdir/pkgconfig/%{name}64_api.pc
%endif
%_mandir/man3/%{name}_*
%_mandir/man7/%name-api.7*


%if "%_pointer_size" == "64"
%files -n lib%{name}64.%major_version
%_libdir/lib%{name}64.so.%major_version
%_libdir/lib%{name}64.so.%major_version.%minor_version
%_libdir/lib%{name}64_api.so.%major_version
%_libdir/lib%{name}64_api.so.%major_version.%minor_version
%_libdir/lib%{name}64_mgmt.so.%major_version
%_libdir/lib%{name}64_mgmt.so.%major_version.%minor_version

%files netlib64
%config(noreplace) %_sysconfdir/%{name}64rc
%dir %_sysconfdir/%{name}64rc.d
%_sysconfdir/%{name}64rc.d/netlib.conf
%_bindir/%{name}64
%dir %_libdir/%{name}64
%_libdir/%{name}64/lib%{name}_fallback_lapack.so
%_libdir/%{name}64/lib%{name}_netlib.so
%_mandir/man1/%{name}64.1*

%files hook-profile64
%_libdir/%{name}64/lib%{name}_hook_profile.so
%endif

%changelog
* Fri Jan 06 2023 Anton Farygin <rider@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Thu Jan 05 2023 Anton Farygin <rider@altlinux.ru> 3.2.1-alt1
- first build for ALT, based on specfile from Fedora
