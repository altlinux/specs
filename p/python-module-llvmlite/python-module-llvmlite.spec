%define  oname llvmlite

Name:    python-module-%oname
Version: 0.31.0
Release: alt1

Summary: A lightweight LLVM python binding for writing JIT compilers

License: BSD-2-Clause
Group:   Development/Python
URL:     https://pypi.org/project/llvmlite

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python
BuildRequires: python-dev python-module-setuptools
BuildRequires: clang llvm-devel libstdc++-devel
%if ""!="3"
BuildRequires: python-module-enum34
%endif

Source:  %oname-%version.tar

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
%setup -n %oname-%version

%build
%remove_optflags -frecord-gcc-switches
%add_optflags -grecord-gcc-switches
export CXX="clang++"
export LLVM_CONFIG=%_bindir/llvm-config
%python_build

%install
%python_install

%files
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info
%doc *.rst

%changelog
* Thu Jan 09 2020 Grigory Ustinov <grenka@altlinux.org> 0.31.0-alt1
- Build new version.

* Thu Dec 19 2019 Grigory Ustinov <grenka@altlinux.org> 0.30.0-alt1
- Build new version.

* Thu Sep 05 2019 Grigory Ustinov <grenka@altlinux.org> 0.29.0-alt1
- Initial build for Sisyphus.
