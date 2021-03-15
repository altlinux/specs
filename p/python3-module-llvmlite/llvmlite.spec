%define  oname llvmlite

Name:    python3-module-%oname
Version: 0.36.0
Release: alt1

Summary: A lightweight LLVM python binding for writing JIT compilers

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/llvmlite

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3 python3-dev
BuildRequires: clang10.0 llvm10.0-devel libstdc++-devel

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
%ifarch armh
sed -ri '/^\S+FLTO_FLAGS/ s,=.+$,=,' ffi/Makefile.linux
%endif

%build
%remove_optflags -frecord-gcc-switches
# http://llvm.1065342.n5.nabble.com/llvm-dev-Code-Coverage-Compile-Issue-LLVM-10-td141053.html
%ifarch armh
%remove_optflags -O2
%endif
%add_optflags -grecord-gcc-switches -fPIC
export CXX="clang++"
export LLVM_CONFIG=%_bindir/llvm-config
export LLVMLITE_SKIP_LLVM_VERSION_CHECK=1
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%doc *.rst

%changelog
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
