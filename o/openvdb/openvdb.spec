%define _unpackaged_files_terminate_build 1

# enable LTO/full debuginfo only on verified arches due resource constrains
%ifnarch x86_64 ppc64le aarch64
%define optflags_debug -g1
%global optflags_lto %nil
%define build_type Release
%else
%define build_type RelWithDebInfo
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict
%endif

%ifarch x86_64
%def_with cuda
%else
%def_without cuda
%endif

%define soname 10.1

Name: openvdb
Version: 10.1.0
Release: alt3.1
Summary: C++ library for sparse volumetric data discretized on three-dimensional grids
Group: Graphics
License: MPL-2.0-no-copyleft-exception
URL: https://www.openvdb.org

# https://github.com/AcademySoftwareFoundation/openvdb
Source: %name-%version.tar

Patch1: openvdb-8.0.0-alt-link-with-libatomic-on-mips.patch
Patch2: openvdb-10.1.0-add-missing-header.patch


BuildRequires(pre): rpm-build-python3
BuildRequires: boost-devel boost-interprocess-devel
BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: ghostscript
BuildRequires: pkgconfig(blosc) >= 1.5.0
BuildRequires: pkgconfig(cppunit) >= 1.10
BuildRequires: pkgconfig(glfw3) >= 2.7
BuildRequires: imath-devel
BuildRequires: pkgconfig(jemalloc)
BuildRequires: pkgconfig(log4cplus) >= 1.0
BuildRequires: tbb-devel
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(zlib) > 1.2.7
BuildRequires: pkgconfig(python3)
BuildRequires: python3-module-numpy libnumpy-py3-devel
BuildRequires: pybind11-devel
%if_with cuda
BuildRequires: nvidia-cuda-devel-static
%endif

%description
OpenVDB is an Academy Award-winning open-source C++ library comprising a novel
hierarchical data structure and a suite of tools for the efficient storage and
manipulation of sparse volumetric data discretized on three-dimensional grids.
It is developed and maintained by Academy Software Foundation for use in
volumetric applications typically encountered in feature film production.

This package contains some graphical tools.

%package -n lib%name%soname
Summary: Core OpenVDB libraries
Group: System/Libraries

%description -n lib%name%soname
OpenVDB is an Academy Award-winning open-source C++ library comprising a novel
hierarchical data structure and a suite of tools for the efficient storage and
manipulation of sparse volumetric data discretized on three-dimensional grids.
It is developed and maintained by Academy Software Foundation for use in
volumetric applications typically encountered in feature film production.

%package devel
Summary: Development files for %{name}
Group: Development/C++
Requires: lib%name%soname = %EVR

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package -n python3-module-%name
Summary: OpenVDB Python module
Group: Development/Python3
Requires: lib%name%soname = %EVR

%description -n python3-module-%name
OpenVDB is an Academy Award-winning open-source C++ library comprising a novel
hierarchical data structure and a suite of tools for the efficient storage and
manipulation of sparse volumetric data discretized on three-dimensional grids.
It is developed and maintained by Academy Software Foundation for use in
volumetric applications typically encountered in feature film production.

This package contains the Python module.

%package doc
Summary: OpenVDB development documentation
Group: Documentation
Requires: %name-devel = %EVR
BuildArch: noarch

%description doc
OpenVDB development documentation

%prep
%setup
%autopatch -p1

# Hardcoded values
sed -i \
	-e 's|lib$|%_lib|g' \
	%name/%name/CMakeLists.txt %name/%name/python/CMakeLists.txt

%ifarch %e2k
# (10.1.0) lcc is not really gcc (still 1.26.21 pretends to be like 9.3.0)
sed -i 's,MINIMUM_GCC_VERSION 9.3.1,MINIMUM_GCC_VERSION 9.3.0,' \
	cmake/config/OpenVDBVersions.cmake
%endif

%build
%cmake \
	-DOPENVDB_BUILD_DOCS=ON \
	-DOPENVDB_CORE_SHARED=ON \
	-DOPENVDB_CORE_STATIC=OFF \
	-DOPENVDB_ENABLE_RPATH=OFF \
	-DOPENVDB_ENABLE_UNINSTALL:BOOL=OFF \
	-DUSE_IMATH_HALF=ON \
	-DUSE_LOG4CPLUS=ON \
	-DOPENVDB_BUILD_PYTHON_MODULE=ON \
	-DUSE_NUMPY:BOOL=ON \
	-DPYOPENVDB_INSTALL_DIRECTORY=%python3_sitelibdir \
	-DPython_EXECUTABLE=%_bindir/python3 \
	-DOPENVDB_USE_IMATH_HALF:BOOL=ON \
	-DOPENVDB_IMATH_VERSION=3 \
	-DOPENVDB_BUILD_NANOVDB:BOOL=ON \
	-DCMAKE_BUILD_TYPE=%build_type \
%ifarch x86_64
	-DOPENVDB_SIMD=SSE42 \
%endif
%if_with cuda
	-DNANOVDB_USE_CUDA=ON \
	-DNANOVDB_CUDA_KEEP_PTX=ON \
	-DNANOVDB_USE_INTRINSICS=ON \
%endif
	%nil

%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/vdb_print
%_bindir/nanovdb_print
%_bindir/nanovdb_validate

%files -n lib%name%soname
%doc %name/%name/LICENSE %name/%name/COPYRIGHT
%doc README.md CHANGES
%_libdir/lib%{name}.so.%{soname}
%_libdir/lib%{name}.so.%{soname}.*

%files -n python3-module-%name
%python3_sitelibdir/py%{name}.cpython-*.so

%files devel
%_includedir/*
%_libdir/lib%{name}.so
%_libdir/cmake/*

%files doc
%_defaultdocdir/OpenVDB

%changelog
* Thu Feb 08 2024 Ivan A. Melnikov <iv@altlinux.org> 10.1.0-alt3.1
- NMU: fix building with boost 1.84.0-alt1

* Mon Dec 18 2023 Michael Shigorin <mike@altlinux.org> 10.1.0-alt3
- E2K: fix build (lcc 1.26.x pretends to be like gcc 9.3.0)

* Mon Dec 11 2023 L.A. Kostis <lakostis@altlinux.ru> 10.1.0-alt2
- x86_64: Build nanovdb with CUDA.

* Thu Nov 16 2023 L.A. Kostis <lakostis@altlinux.ru> 10.1.0-alt1
- Updated to upstream version 10.1.0.
- BR: update.
- Move documentation to separate noarch package.
- Enable LTO/full debuginfo only on verified arches.
- Enable NanoVDB.
- Build with SSE42 on x86_64.

* Mon Mar 20 2023 Alexander Burmatov <thatman@altlinux.org> 9.0.0-alt2
- Fix build requires.

* Thu Feb 24 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 9.0.0-alt1
- Updated to upstream version 9.0.0.

* Thu Jan 27 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 8.1.0-alt2
- Rebuilt with new TBB.

* Fri Jun 18 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 8.1.0-alt1
- Updated to upstream version 8.1.0.

* Thu Jun 03 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 8.0.1-alt1
- Updated to upstream version 8.0.1.

* Mon May 24 2021 Ivan A. Melnikov <iv@altlinux.org> 8.0.0-alt2
- Fix build on mipsel:
  + link with -latomic;
  + reduce debuginfo level to -g1 to avoid OOM in compiler.

* Tue Jan 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 8.0.0-alt1
- Updated to upstream version 8.0.0.

* Tue Sep 01 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 7.1.0-alt1
- Initial build for ALT.

* Mon Aug 24 2020 Simone Caronni <negativo17@gmail.com> - 7.1.0-2
- List shared object versions.

* Fri Aug 14 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 7.1.0-1
- Update to 7.1.0
- Adhere to https://docs.fedoraproject.org/en-US/packaging-guidelines/CMake/

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-9
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 21 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 7.0.0-7
- Disable jemalloc build for RHEL and its derivative

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 7.0.0-6
- Rebuilt for Boost 1.73

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 7.0.0-5
- Rebuilt for Python 3.9

* Sat May 23 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 7.0.0-4
- Drop boost-python3-devel build requirement for Fedora 33+ 

* Sat May 23 2020 Luya Tshimbalanga <luya@fedoraproject.org> - 7.0.0-3
- Disable python3 binding for CentOS and Red Hat Enterprise
- On RHEL and CentOS, glfw is exclusive for x86_64
- Switch to pkgconfig build requirements as possible

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 11 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 7.0.0-1
- Update to 7.0.0
- Set python3 module installation path via cmake
- Drop epydoc dependency

* Thu Sep 19 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 6.2.0-1
- Update to 6.2.0
- Drop no longer needed upstream patch
- Rename subpackge module to python3-*
- Fix correct python module installation path

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 6.1.0-3
- Rebuilt for Python 3.8

* Sun Aug 18 2019 Simone Caronni <negativo17@gmail.com> - 6.1.0-2
- Fix build with latest options.
- Update SPEC file.
- rpmlint fixes.

* Thu Aug 01 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 6.1.0-1
- Update to 6.1.0
- Fix cmake build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Apr 12 2019 Richard Shaw <hobbes1069@gmail.com> - 6.0.0-2
- Rebuild for Ilmbase 2.3.0.

* Sat Feb 16 2019 Luya Tshimbalanga <luya@fedoraproject.org> - 6.0.0-1
- Update to 6.0.0
- Update source url and description
- Apply patch for boost 1.6.9 borrowed from Arch Linux

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 5.1.0-4
- Rebuild for tbb 2019_U1

* Tue Jul 17 2018 Simone Caronni <negativo17@gmail.com> - 5.1.0-3
- Require libs subpackage for python3/devel.

* Tue Jul 17 2018 Simone Caronni <negativo17@gmail.com> - 5.1.0-2
- Fix Python 3 Boost link.

* Tue Jul 17 2018 Simone Caronni <negativo17@gmail.com> - 5.1.0-1
- Update to 5.1.0.
- Switch to Python 3.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 01 2018 Jonathan Wakely <jwakely@redhat.com> - 5.0.0-3
- Add BuildRequires: boost-python2-devel to fix build with boost-1.66.0-7.fc29

* Sun Mar 04 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 5.0.0-2
- Added gcc-c++ dependency
- Upstream patch for Boost compability

* Mon Feb 26 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 5.0.0-1
- Update to 5.0.0
- Use new upstream macro for abi compatibility
- Rebuild for Boost 1.66

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Simone Caronni <negativo17@gmail.com> - 4.0.2-1
- Update to 4.0.2.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 23 2017 Simone Caronni <negativo17@gmail.com> - 4.0.1-5
- Rename python subpackage (module) to python2.

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 4.0.1-4
- Rebuilt for s390x binutils bug

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 4.0.1-3
- Rebuilt for Boost 1.64

* Sat May 06 2017 Simone Caronni <negativo17@gmail.com> - 4.0.1-2
- Review fixes.

* Sat Apr 22 2017 Simone Caronni <negativo17@gmail.com> - 4.0.1-1
- Update to 4.0.1.
- Perform tests, build HTML documentation.
- Require main OpenVDB library for Python module.

* Wed Nov 23 2016 Simone Caronni <negativo17@gmail.com> - 4.0.0-2
- Update to 4.0.0.

* Sun Oct 16 2016 Simone Caronni <negativo17@gmail.com> - 4.0.0-1.20161015git40271e7
- First build.
