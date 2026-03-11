%define pypi_name z3-solver
%set_verify_elf_method strict

Name:     z3
Version:  4.16.0
Release:  alt2

Summary:  High-performance theorem prover (SMT solver)

License:  MIT
Group:    Sciences/Mathematics
URL:      https://z3prover.github.io
VCS:      https://github.com/Z3Prover/z3

Source:   %name-%version.tar

Patch:    python-use-non-devel-so.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: libgmpxx-devel
BuildRequires: python3-devel
BuildRequires: python3-module-pkg_resources
BuildRequires: python3-module-setuptools

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

%package -n python3-module-%name
Summary: Python bindings of %name
Group: Development/Python3
BuildArch: noarch
Requires: lib%name = %EVR
%py3_provides %name
# mapping from PyPI name
Provides: python3-module-%{pep503_name %pypi_name} = %EVR

%description -n python3-module-%name
Z3 is a high-performance theorem prover being developed at Microsoft
Research.

This package contains Python bindings of %name.

%prep
%setup
%patch -p1

%build
%add_optflags %(getconf LFS_CFLAGS)
%cmake \
    -DZ3_INCLUDE_GIT_HASH:BOOL=OFF \
    -DZ3_INCLUDE_GIT_DESCRIBE:BOOL=OFF \
    -DZ3_BUILD_DOCUMENTATION:BOOL=OFF \
    -DZ3_ENABLE_EXAMPLE_TARGETS:BOOL=OFF \
    -DPYTHON_EXECUTABLE=$(which python3) \
    -DZ3_BUILD_PYTHON_BINDINGS:BOOL=ON \
    -DZ3_INSTALL_PYTHON_BINDINGS:BOOL=ON \
    -DZ3_USE_LIB_GMP:BOOL=ON \
    -DZ3_LINK_TIME_OPTIMIZATION=ON \
    %nil

%cmake_build

%install
%cmakeinstall_std

%check
set -o pipefail
%cmake_build --target test-z3
%_cmake__builddir/test-z3 -a | tail
export LD_LIBRARY_PATH=%buildroot%_libdir
export PYTHONPATH=%buildroot%python3_sitelibdir_noarch
python3 -c "import z3; print (z3.get_version_string())"
python3 examples/python/example.py

%files
%doc LICENSE.txt README.md RELEASE_NOTES.md
%_bindir/%name

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%{name}*.h
%_libdir/lib%name.so
%_libdir/cmake/%name
%_libdir/pkgconfig/%name.pc

%files -n python3-module-%name
%python3_sitelibdir_noarch/%name

%changelog
* Wed Mar 11 2026 Grigory Ustinov <grenka@altlinux.org> 4.16.0-alt2
- Fixed package URL.
- Built without docs.

* Mon Feb 23 2026 Grigory Ustinov <grenka@altlinux.org> 4.16.0-alt1
- Automatically updated to 4.16.0.

* Tue Feb 17 2026 Grigory Ustinov <grenka@altlinux.org> 4.15.8-alt1
- Automatically updated to 4.15.8.

* Wed Feb 11 2026 Grigory Ustinov <grenka@altlinux.org> 4.15.7-alt1
- Automatically updated to 4.15.7.

* Sun Feb 08 2026 Grigory Ustinov <grenka@altlinux.org> 4.15.5-alt1
- Automatically updated to 4.15.5.

* Thu Nov 13 2025 Grigory Ustinov <grenka@altlinux.org> 4.15.4-alt1
- Automatically updated to 4.15.4.

* Tue Oct 14 2025 Grigory Ustinov <grenka@altlinux.org> 4.15.3-alt1
- Automatically updated to 4.15.3.

* Tue Jul 01 2025 Anton Zhukharev <ancieg@altlinux.org> 4.15.2-alt3
- Mapped PyPI name to distro's one.

* Tue Jul 01 2025 Grigory Ustinov <grenka@altlinux.org> 4.15.2-alt2
- Added patch, fixing libz3 loading (Closes: #54994).

* Thu Jun 26 2025 Grigory Ustinov <grenka@altlinux.org> 4.15.2-alt1
- Automatically updated to 4.15.2.

* Tue Jun 24 2025 Grigory Ustinov <grenka@altlinux.org> 4.15.1-alt1
- Automatically updated to 4.15.1.

* Tue May 13 2025 Grigory Ustinov <grenka@altlinux.org> 4.15.0-alt1
- Automatically updated to 4.15.0.

* Tue Mar 11 2025 Grigory Ustinov <grenka@altlinux.org> 4.14.1-alt1
- Automatically updated to 4.14.1.

* Wed Feb 19 2025 Grigory Ustinov <grenka@altlinux.org> 4.14.0-alt1
- Automatically updated to 4.14.0.

* Mon Dec 23 2024 Grigory Ustinov <grenka@altlinux.org> 4.13.4-alt1
- Automatically updated to 4.13.4.

* Sat Oct 12 2024 Grigory Ustinov <grenka@altlinux.org> 4.13.3-alt1
- Automatically updated to 4.13.3.

* Mon Sep 30 2024 Grigory Ustinov <grenka@altlinux.org> 4.13.2-alt1
- Automatically updated to 4.13.2.

* Tue Sep 03 2024 Vitaly Chikunov <vt@altlinux.org> 4.13.0-alt2
- spec: Enable additional post-build QA checks.
- spec: Enable LFS on 32-bit architectures.
- spec: check: Run test-z3.

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

