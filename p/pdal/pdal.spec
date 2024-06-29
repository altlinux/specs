%define _unpackaged_files_terminate_build 1

Name:    pdal
Version: 2.7.2
Release: alt1

Summary: PDAL is Point Data Abstraction Library. GDAL for point cloud data.
License: BSD-3-Clause
Group:   Other
Url:     https://github.com/PDAL/PDAL

Packager: Andrey Cherepanov <cas@altlinux.org>

Source: PDAL-%version.tar

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: bash-completion
BuildRequires: hdf-devel
BuildRequires: libcryptopp-devel
BuildRequires: libcurl-devel
BuildRequires: libgdal-devel
BuildRequires: libgeotiff-devel
BuildRequires: liblz4-devel
BuildRequires: libpnetcdf-devel
BuildRequires: libssl-devel
%ifnarch %e2k
BuildRequires: libunwind-devel
%endif
BuildRequires: libxml2-devel
BuildRequires: libzstd-devel
BuildRequires: python3-devel
BuildRequires: libsqlite3-devel

%description
%summary

%package -n lib%name
Summary: Library of %name
Group: System/Libraries

%description -n lib%name
%summary

%package -n lib%{name}-devel
Summary: Development files for %name
Group: Development/C++

%description -n lib%{name}-devel
%summary

%prep
%setup -n PDAL-%version
%ifnarch %e2k
sed -i '/{CMAKE_DL_LIBS}/a unwind' CMakeLists.txt
%endif
%ifarch %e2k
# need to disable workarounds for GCC
sed -i "s/EIGEN_GNUC_AT_LEAST(6,0)/0/" \
	vendor/eigen/Eigen/src/Core/products/GeneralBlockPanelKernel.h
%endif

%build
%cmake -GNinja -Wno-dev \
       -DPDAL_LIB_INSTALL_DIR=%_libdir \
       -DWITH_TESTS=false
%ninja_build -C "%_cmake__builddir"

%install
%ninja_install -C "%_cmake__builddir"

%files
%doc AUTHORS.txt LICENSE.txt README.md
%_bindir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/pdal-config
%_includedir/*
%_libdir/*.so
%_libdir/*.so
%_libdir/cmake/PDAL
%_libdir/pkgconfig/%name.pc

%changelog
* Sat Jun 29 2024 Andrey Cherepanov <cas@altlinux.org> 2.7.2-alt1
- New version.

* Thu Mar 28 2024 Andrey Cherepanov <cas@altlinux.org> 2.7.1-alt1
- New version.

* Wed Mar 13 2024 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- New version.

* Thu Feb 29 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.6.3-alt2
- Fixed build for Elbrus.

* Wed Feb 07 2024 Andrey Cherepanov <cas@altlinux.org> 2.6.3-alt1
- New version.

* Tue Dec 12 2023 Andrey Cherepanov <cas@altlinux.org> 2.6.2-alt1
- New version.

* Sat Nov 25 2023 Andrey Cherepanov <cas@altlinux.org> 2.6.1-alt1
- New version.

* Fri Oct 13 2023 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- New version.

* Sun Aug 20 2023 Andrey Cherepanov <cas@altlinux.org> 2.5.6-alt2
- Added libcurl-devel.

* Sat Aug 19 2023 Andrey Cherepanov <cas@altlinux.org> 2.5.6-alt1
- New version.

* Sun Jun 25 2023 Andrey Cherepanov <cas@altlinux.org> 2.5.5-alt1
- Initial build for Sisyphus.
