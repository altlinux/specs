%define  oname llvmlite
%define  llvm_version 12.0
%define  optflags_lto -flto=thin

#[armh] LLVM ERROR: Symbol not found: __aeabi_unwind_cpp_pr0
%ifnarch armh
%def_with check
%else
%def_without check
%endif

Name:    python3-module-%oname
Version: 0.40.1
Release: alt2

Summary: A lightweight LLVM python binding for writing JIT compilers

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/llvmlite

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3 python3-module-setuptools python3-module-wheel
BuildRequires: clang%{llvm_version} llvm%{llvm_version}-devel libstdc++-devel lld%{llvm_version}

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
sed -i 's|"version": "0+unknown"|"version": "%version"|' versioneer.py

%build
%remove_optflags -frecord-gcc-switches
%add_optflags -grecord-gcc-switches -fPIC -DNDEBUG
export ALTWRAP_LLVM_VERSION=%{llvm_version}
export CXX=clang
export LDFLAGS='-fuse-ld=lld'
%pyproject_build

%install
%pyproject_install

%check
%__python3 ./runtests.py

%files
%doc *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}/

%changelog
* Tue Sep 12 2023 L.A. Kostis <lakostis@altlinux.ru> 0.40.1-alt2
- Bump llvm version to 12.0 (to get rid of llvm11.1).
- .spec: upgrade python3 macros.

* Mon Jul 17 2023 Grigory Ustinov <grenka@altlinux.org> 0.40.1-alt1
- Automatically updated to 0.40.1.

* Sun Jun 25 2023 L.A. Kostis <lakostis@altlinux.ru> 0.40.0-alt1.1
- Fix FTBFS:
  + llvm11.0->llvm11.1.

* Wed May 03 2023 Grigory Ustinov <grenka@altlinux.org> 0.40.0-alt1
- Automatically updated to 0.40.0.

* Fri Sep 16 2022 Grigory Ustinov <grenka@altlinux.org> 0.39.1-alt1
- Build new version.
- Build with check.

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
