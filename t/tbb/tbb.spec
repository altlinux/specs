%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%set_verify_elf_method strict

%def_with python

Name: tbb
Version: 2021.13.0
Release: alt1
Summary: Threading Building Blocks
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/oneapi-src/oneTBB

# https://github.com/oneapi-src/oneTBB.git
Source: %name-%version.tar

# Fedora patches

# Fix compilation on aarch64 and s390x.  See
# https://github.com/oneapi-src/oneTBB/issues/186
Patch4: tbb-2019-fetchadd4.patch

# ALT patches
# https://github.com/oneapi-src/oneTBB/pull/609
Patch1000: tbb-2021.5-upstream-i586-fix.patch

# Elbrus support
Patch2000: tbb-e2k.patch

#Fix for building on GCC13
Patch5: 0001-Fix-build-on-GCC13.patch

Requires: lib%name = %EVR

%if_with python
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif
BuildRequires: gcc-c++
BuildRequires: libgomp-devel
%if_with python
BuildRequires: python3-dev python3-module-setuptools python3-module-wheel
%endif
BuildRequires: swig
BuildRequires: cmake ctest
# needed for some tests
BuildRequires: /proc

%description
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

%package -n lib%name
Summary: Shared libraries of Threading Building Blocks
Group: Development/C++

%description -n lib%name
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains shared libraries of Threading Building Blocks.

%package devel
Summary: Development libraries and headers of Threading Building Blocks
Group: Development/C++
Requires: lib%name = %EVR
Requires: %name-headers = %EVR
Provides: lib%name-devel = %EVR
Conflicts: lib%name-devel < %EVR
Obsoletes: lib%name-devel
Provides: %name-headers = %EVR
Conflicts: %name-headers < %EVR
Obsoletes: %name-headers

%description devel
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains development libraries for Threading Building
Blocks.

%package examples
Summary: Examples for Threading Building Blocks
Group: Development/Documentation
Requires: lib%name = %EVR
BuildArch: noarch

%description examples
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains examples for Threading Building Blocks.

%if_with python
%package -n python3-module-%name
Summary: Python 3 Threading Building Blocks module
Group: Development/Python3

%description -n python3-module-%name
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains python3 module for Threading Building Blocks.
%endif

%prep
%setup
%patch4 -p1
%patch5 -p1
#%%patch1000 -p1
%ifarch %e2k
%patch2000 -p1
%endif

%build
%add_optflags -D_FILE_OFFSET_BITS=64

export CFLAGS="${CFLAGS:-%optflags} -DDO_ITT_NOTIFY -DUSE_PTHREAD"
export CXXFLAGS="${CXXFLAGS:-%optflags} -DDO_ITT_NOTIFY -DUSE_PTHREAD"
export CPLUS_FLAGS="%{optflags} -DDO_ITT_NOTIFY -DUSE_PTHREAD"
export LDFLAGS="${LDFLAGS:-} -lpthread"
export RPM_LD_FLAGS="${RPM_LD_FLAGS:-} -lpthread"
%ifarch riscv64
export LDFLAGS="${LDFLAGS:-} -latomic"
export RPM_LD_FLAGS="${RPM_LD_FLAGS:-} -latomic"
%endif

%cmake \
	-DCMAKE_CXX_STANDARD=14 \
	-DTBB_EXAMPLES:BOOL=ON \
	-DTBB_STRICT:BOOL=OFF \
	-DTBB4PY_BUILD:BOOL=OFF \
	%nil

%cmake_build

%install
%cmakeinstall_std
%if_with python
pushd python
export TBBROOT=%buildroot%_prefix
subst "s|tbb_root, 'lib'|tbb_root, '%_lib'|g" setup.py
subst "s|'irml'||" setup.py
%pyproject_build
%pyproject_install
popd
%endif

rm -f %buildroot%_defaultdocdir/TBB/README.md

%ifnarch ppc64le aarch64
%check
%cmake_build -t test
%endif

%files -n lib%name
%doc LICENSE.txt
%doc README.md
%_libdir/*.so.*

%files devel
%_includedir/oneapi
%_includedir/tbb
%_libdir/cmake/TBB
%_libdir/lib*.so
%_pkgconfigdir/*.pc

%files examples
%doc examples

%if_with python
%files -n python3-module-%name
%python3_sitelibdir/TBB.py
%python3_sitelibdir/TBB*.dist-info
%python3_sitelibdir/tbb
%python3_sitelibdir/__pycache__/*
%endif

%changelog
* Thu Jun 27 2024 L.A. Kostis <lakostis@altlinux.ru> 2021.13.0-alt1
- Updated to upstream version 2021.13.0.
- Restore build of python3 module.

* Fri May 17 2024 L.A. Kostis <lakostis@altlinux.ru> 2021.12.0-alt1
- Updated to upstream version 2021.12.0.

* Wed Jan 03 2024 Grigory Ustinov <grenka@altlinux.org> 2021.10.0-alt1.1
- Build without python.

* Wed Jul 26 2023 L.A. Kostis <lakostis@altlinux.ru> 2021.10.0-alt1
- Updated to upstream version 2021.10.0.

* Thu Jul 06 2023 L.A. Kostis <lakostis@altlinux.ru> 2021.9.0-alt1
- Updated to upstream version 2021.9.0.

* Tue Jul  4 2023 Artyom Bystrov <arbars@altlinux.org> 2021.5.0-alt2
- Fix build on GCC13

* Tue Jan 25 2022 Aleksei Nikiforov <darktemplar@altlinux.org> 2021.5.0-alt1
- Updated to upstream version 2021.5.0.

* Mon Aug 16 2020 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2020.3-alt2
- Added patch with Elbrus support.

* Fri Aug 07 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2020.3-alt1
- Updated to upstream version 2020.3.

* Wed Apr 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2020.2-alt1
- Updated to upstream version 2020.2.

* Sun Mar 22 2020 Nikita Ermakov <arei@altlinux.org> 2019-alt1.u8.1
- Add -latomic for riscv64.

* Wed Jul 24 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 2019-alt1.u8
- Updated to upstream version 2019.U8.

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 2019-alt1.u2
- NMU: new version
- packed cmake
- added and packed pkgconfig

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2018-alt1.u1.1.qa1
- NMU: applied repocop patch

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2018-alt1.u1.1
- (NMU) Rebuilt with python-3.6.4.

* Tue Oct 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2018-alt1.u1
- Updated to upstream version 2018.U1.

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 42_20140601-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Thu Jul 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 42_20140601-alt1
- Version 42_20140601

* Mon Jun 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 42_20140416-alt1
- Version 42_20140416

* Tue Nov 19 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 42_20131003-alt1
- Version 42_20131003

* Fri Jul 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 41_20130613-alt1
- Version 41_20130613

* Mon Feb 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 41_20130116-alt1
- Version 41_20130116

* Fri Aug 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 40_20120613-alt1
- Version 40_20120613

* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 40_20120408-alt1
- Version 40_20120408

* Wed Mar 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 40_297-alt1
- Version 40_297

* Sun Dec 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 40_233-alt1
- Version 40_233

* Sun May 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20110315-alt1
- Version 30_20110315
- Disabled debug packages (we have debuginfo packages now)

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt6
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt5
- Rebuilt for debuginfo

* Wed Jan 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt4
- Added debug subpackages

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt3
- Fixed overlinking of libraries

* Wed Mar 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt2
- Disabled broken test

* Tue Mar 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt1
- Version 30_20100310 (ALT #23196)

* Fri Dec 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20.014-alt1
- Initial build for Sisyphus

