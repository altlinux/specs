Name: z3
Version: 4.13.0
Release: alt1
Summary: High-performance theorem prover
License: MIT
Group: Sciences/Mathematics
Url: https://github.com/Z3Prover/z3

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildRequires(pre): rpm-build-python3
BuildRequires: cmake
BuildRequires: gcc-c++ doxygen graphviz
BuildRequires: libgmp-devel libgmpxx-devel
BuildRequires: python3-devel
BuildRequires: python3(pkg_resources)
BuildRequires: python3(setuptools)

%description
Z3 is a high-performance theorem prover being developed at Microsoft
Research.

%package -n lib%name
Summary: Shared library of %name
Group: System/Libraries

%description -n lib%name
Z3 is a high-performance theorem prover being developed at Microsoft
Research.

This package contains shared library of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
Z3 is a high-performance theorem prover being developed at Microsoft
Research.

This package contains development files of %name.

%package -n lib%name-devel-docs
Summary: Documentation for %name
Group: Development/Documentation

%description -n lib%name-devel-docs
Z3 is a high-performance theorem prover being developed at Microsoft
Research.

This package contains documentation for %name.

%package -n python3-module-%name
Summary: Python bindings of %name
Group: Development/Python3
BuildArch: noarch
Requires: lib%name = %EVR
%py3_provides %name

%description -n python3-module-%name
Z3 is a high-performance theorem prover being developed at Microsoft
Research.

This package contains Python bindings of %name.

%prep
%setup

%build
%cmake \
	-DZ3_INCLUDE_GIT_HASH:BOOL=OFF \
	-DZ3_INCLUDE_GIT_DESCRIBE:BOOL=OFF \
	-DZ3_BUILD_DOCUMENTATION:BOOL=ON \
	-DZ3_ENABLE_EXAMPLE_TARGETS:BOOL=OFF \
	-DPYTHON_EXECUTABLE=$(which python3) \
	-DZ3_BUILD_PYTHON_BINDINGS:BOOL=ON \
	-DZ3_INSTALL_PYTHON_BINDINGS:BOOL=ON \
	-DZ3_USE_LIB_GMP:BOOL=ON \
	%nil

%cmake_build

%install
%cmakeinstall_std

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
python3 -c "import z3; print (z3.get_version_string())"
python3 examples/python/example.py

%files
%doc LICENSE.txt *.md
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/cmake/%name
%_libdir/pkgconfig/z3.pc

%files -n lib%name-devel-docs
%doc examples
%_defaultdocdir/Z3

%files -n python3-module-%name
%python3_sitelibdir_noarch/%name

%changelog
* Tue Jun 04 2024 Grigory Ustinov <grenka@altlinux.org> 4.13.0-alt1
- Automatically updated to 4.13.0.

* Thu Jan 25 2024 Grigory Ustinov <grenka@altlinux.org> 4.8.8-alt1.1
- NMU: Fixed FTBFS.

* Fri Jul 10 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.8.8-alt1
- Updated to upstream version 4.8.8.

* Thu Apr 02 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.8.7-alt1
- Updated to upstream version 4.8.7.
- Disabled bindings for python-2.

* Fri Jul 27 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.5.0-alt2
- Updated build dependencies.

* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.5.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Oct 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.5.0-alt1
- Updated to upstream version 4.5.0.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.3.2-alt1.git20141024.1.1
- (AUTO) subst_x86_64.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.3.2-alt1.git20141024.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1.git20141024
- Initial build for Sisyphus

