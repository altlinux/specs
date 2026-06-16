%define _unpackaged_files_terminate_build 1

%define oname hdf5
%define sover 320
%define soverhl 320

Name: lib%oname
Version: 2.1.1
Release: alt1

Summary: Hierarchical Data Format 5 library
License: BSD
Group: System/Libraries

Url: http://www.hdfgroup.org/HDF5/
VCS: https://github.com/HDFGroup/hdf5.git
Source: %name-%version.tar
Patch0: %name-alt-disable-rpath.patch

BuildRequires: gcc-c++
BuildRequires: libssl-devel
BuildRequires: zlib-devel
BuildRequires: cmake
BuildRequires: libaec-devel

%description
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

%package -n lib%oname-%sover
Summary: Hierarchical Data Format 5 library
Group: System/Libraries

%description -n lib%oname-%sover
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

%package -n lib%oname-hl-%soverhl
Summary: Hierarchical Data Format 5 library
Group: System/Libraries
Requires: lib%oname-%sover = %EVR

%description -n lib%oname-hl-%soverhl
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

%package -n lib%oname-devel
Summary: HDF5 library development package
Group: Development/C
Requires: libstdc++-devel zlib-devel libaec-devel
Requires: lib%oname-%sover = %EVR
Requires: lib%oname-hl-%soverhl = %EVR
Conflicts: lib%oname-mpi-devel < 1.8.3-alt5

%description -n lib%oname-devel
Header files for HDF5 library.

%package -n %oname-tools
Summary: HDF5 tools
Group: Development/Tools
Conflicts: %oname-mpi-tools < 1.8.3-alt5

%description -n %oname-tools
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

This package contains tools for work with HDF5.

%prep
%setup
# ALT: h5cc/h5c++ add -Wl,-rpath,%_libdir by default; RPATH to the standard
# libdir is forbidden by verify-elf and breaks packages linking via h5cc.
%patch0 -p1

%ifarch %e2k
# too many unsupported warning options
find config/gnu-warnings/ -type f ! -name '*general' \
	-exec rm -f {} \; -exec touch {} \;
%endif

%build
%cmake \
            -DCMAKE_BUILD_TYPE=Release \
	    -DHDF5_USE_GNU_DIRS=ON \
            -DBUILD_SHARED_LIBS=ON \
            -DBUILD_STATIC_LIBS=OFF \
            -DHDF5_ENABLE_ALL_WARNINGS=ON \
            -DHDF5_ENABLE_PARALLEL=OFF \
            -DHDF5_BUILD_CPP_LIB=ON \
            -DHDF5_BUILD_FORTRAN=OFF \
            -DHDF5_BUILD_JAVA=OFF \
            -DHDF5_BUILD_DOC=OFF \
            -DHDF5_ENABLE_MIRROR_VFD=ON \
            -DHDF5_ENABLE_DIRECT_VFD=ON \
	    -DHDF5_BUILD_HL_LIB=ON \
	    -DHDF5_ENABLE_ZLIB_SUPPORT=ON \
	    -DHDF5_ENABLE_SZIP_SUPPORT=ON \
            -DHDF5_USE_ZLIB_NG=OFF

%cmake_build

%install
%cmake_install

rm -rf %buildroot%_datadir/LICENSE %buildroot%_datadir/doc
rm -rf %buildroot%_libdir/cmake/Modules/Findlibaec.cmake

%files -n lib%oname-%sover
%_libdir/lib*.so.%{sover}
%_libdir/lib*.so.%{sover}.*
%exclude %_libdir/libhdf5_hl*.so*

%files -n lib%oname-hl-%soverhl
%_libdir/libhdf5_hl*.so.%{soverhl}
%_libdir/libhdf5_hl*.so.%{soverhl}.*

%files -n lib%oname-devel
%doc LICENSE
%doc README.md release_docs/USING_HDF5_CMake.txt
%doc release_docs/CHANGELOG.md
%_libdir/lib*.so
%_libdir/cmake/*.cmake
%_includedir/*
%_pkgconfigdir/*

%files -n %oname-tools
%_bindir/*
# used to show configuration at runtime
%_libdir/libhdf5.settings

%changelog
* Thu Jun 11 2026 Anton Farygin <rider@altlinux.org> 2.1.1-alt1
- 2.0.0 -> 2.1.1

* Thu Jun 11 2026 Anton Farygin <rider@altlinux.org> 2.0.0-alt1
- 1.14.6 -> 2.0.0

* Mon Feb 24 2025 Anton Farygin <rider@altlinux.ru> 1.14.6-alt1
- 1.14.5 -> 1.14.6

* Fri Oct 18 2024 Anton Farygin <rider@altlinux.ru> 1.14.5-alt1
- 1.14.3 -> 1.14.5

* Thu Aug 29 2024 Alexander Danilov <admsasha@altlinux.org> 1.14.3-alt3
- Set the version of autoconf to 2.71 to simplify the build
  into the old branches.

* Wed Feb 28 2024 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.14.3-alt2
- Fixed build for Elbrus

* Sun Nov 26 2023 Anton Farygin <rider@altlinux.ru> 1.14.3-alt1
- 1.14.3

* Sat May 15 2021 Michael Shigorin <mike@altlinux.org> 1.10.6-alt2
- E2K: avoid lcc-unsupported options

* Wed Apr 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.6-alt1
- Updated to upstream version 1.10.6.
- Removed alternatives.
- Updated packaging scheme.

* Wed Oct 31 2018 Michael Shigorin <mike@altlinux.org> 1.8.13-alt1.qa4
- Replace e2k arch name with %%e2k macro (grenka@)

* Mon Oct 09 2017 Michael Shigorin <mike@altlinux.org> 1.8.13-alt1.qa3
- E2K: avoid lcc-unsupported options
- introduce fortran knob (on by default)

* Thu May 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.13-alt1.qa2
- Fix library names in pkgconfig file

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.8.13-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.13-alt1
- Version 1.8.13

* Thu Sep 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt2
- Added links to headers into %_includedir

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt1
- Version 1.8.11

* Tue Oct 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.9-alt2
- Rebuilt with gcc 4.7

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.9-alt1
- Version 1.8.9

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt2
- Set native directory as %_libdir/%oname-seq instead of
  %_libexecdir/%oname-seq

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt1
- Version 1.8.8

* Tue Sep 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.7-alt1
- Version 1.8.7

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.6-alt1
- Version 1.8.6
- Disabled static package

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5_patch1-alt2
- Rebuilt for debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5_patch1-alt1
- Version 1.8.5-patch1

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt6
- Fixed soname set-versions by ghost links (thnx ldv@)

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt5
- Rebuilt for soname set-versions

* Wed Jul 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt4
- Added pkgconfig file

* Thu Jun 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt3
- Created alternatives

* Thu Jun 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt2
- Added explicit conflict with parallel version of HDF5 tools

* Thu May 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt1
- Version 1.8.3
- Added static libraries
- Add fortran interface libraries
- Add zlib support

* Sun Dec 14 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.6-alt2
- fixed build with gcc4.3

* Sat Sep 15 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6.6-alt1
- initial build for ALT Linux Sisyphus

