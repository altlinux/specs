%define  oname llvmlite
%define  llvm_version 11
%define  optflags_lto -flto=thin

Name:    python3-module-%oname
Version: 0.37.0
Release: alt2

Summary: A lightweight LLVM python binding for writing JIT compilers

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/llvmlite

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: clang%{llvm_version}.0 llvm%{llvm_version}.0-devel libstdc++-devel lld%{llvm_version}.0

Source:  %name-%version.tar

%description
A lightweight LLVM python binding for writing JIT compilers

The old llvmpy  binding exposes a lot of LLVM APIs but the mapping of
C++-style memory management to Python is error prone. Numba_ and many JIT
compilers do not need a full LLVM API.  Only the IR builder, optimizer,
and JIT compiler APIs are necessary.

llvmlite is a project originally tailored for Numba's needs, using the
following approach:

* A small C wrapper around the parts of the LLVM C++ API we need that are
  not already exposed by the LLVM C API.
* A ctypes Python wrapper around the C API.
* A pure Python implementation of the subset of the LLVM IR builder that we
  need for Numba.

%prep
%setup
# seems to be fine with 3.10 but we need to remove the guard
# https://github.com/numba/llvmlite/issues/740
sed -i 's/max_python_version =.*/max_python_version = "3.11"/' setup.py

%build
%remove_optflags -frecord-gcc-switches
%add_optflags -grecord-gcc-switches -fPIC -fuse-ld=lld -DNDEBUG
export CXX='clang++-%llvm_version'
export LLVM_CONFIG=%_bindir/llvm-config-%llvm_version
#export LLVMLITE_SKIP_LLVM_VERSION_CHECK=1
%python3_build

%install
%python3_install

mv %buildroot%python3_sitelibdir/%oname-*.egg-info %buildroot%python3_sitelibdir/%oname-%version-py$(python3 -V | sed 's|^P.*\(3\.[0-9]\).*|\1|').egg-info

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Mon Dec 06 2021 Grigory Ustinov <grenka@altlinux.org> 0.37.0-alt2
- Fixed build with python3.10.

* Fri Sep 10 2021 Grigory Ustinov <grenka@altlinux.org> 0.37.0-alt1
- Build new version (thx sbolshakov@).

* Wed Jun 30 2021 Grigory Ustinov <grenka@altlinux.org> 0.36.0-alt1.git.dd00288
- Build from last commit.

* Mon Mar 15 2021 Grigory Ustinov <grenka@altlinux.org> 0.36.0-alt1
- Build new version.

* Sun Oct 04 2020 Grigory Ustinov <grenka@altlinux.org> 0.34.0-alt1
- Build new version.

* Sat Jun 27 2020 Grigory Ustinov <grenka@altlinux.org> 0.33.0-alt1
- Build new version.
- Build without python2 support.

* Fri Feb 14 2020 Grigory Ustinov <grenka@altlinux.org> 0.31.0-alt2
- Add explicit BR on llvm7, because porting on llvm9 is still not finished.

* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 0.31.0-alt1
- Build new version.

* Thu Dec 19 2019 Grigory Ustinov <grenka@altlinux.org> 0.30.0-alt1
- Build new version.

* Thu Sep 05 2019 Grigory Ustinov <grenka@altlinux.org> 0.29.0-alt1
- Initial build for Sisyphus.
