%define  oname llvmlite
%define  llvm_version 20.1
%define  clang_version %(echo %llvm_version | cut -d . -f 1)
%define  optflags_lto -flto=thin

#[armh] LLVM ERROR: Symbol not found: __aeabi_unwind_cpp_pr0
%ifnarch armh
%def_with check
%else
%def_without check
%endif

Name:    python3-module-%oname
Version: 0.46.0
Release: alt1.1

Summary: A lightweight LLVM python binding for writing JIT compilers

License: BSD-2-Clause
Group:   Development/Python3
URL:     https://pypi.org/project/llvmlite
VCS:     https://github.com/numba/llvmlite

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires: clang%{llvm_version} llvm%{llvm_version}-devel libstdc++-devel lld%{llvm_version}
BuildRequires: cmake
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: zlib-devel

Source:  %name-%version.tar

Patch: llvmlite-alt-normalize-i586-name.patch

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
%patch -p1

sed -i 's|"version": "0+unknown"|"version": "%version"|' versioneer.py

# Hotfix for new setuptools
sed -i 's/, dry_run=dry_run//' setup.py

%build
export ALTWRAP_LLVM_VERSION=%{llvm_version}
export CXX=/usr/bin/clang++-%{clang_version}
export CC=/usr/bin/clang-%{clang_version}
%pyproject_build

%install
%pyproject_install

%check
%__python3 ./runtests.py

%files
%doc LICENSE CHANGE_LOG *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}

%changelog
* Sat Mar 28 2026 Grigory Ustinov <grenka@altlinux.org> 0.46.0-alt1.1
- Fixed FTBFS

* Mon Jan 26 2026 Grigory Ustinov <grenka@altlinux.org> 0.46.0-alt1
- Automatically updated to 0.46.0.

* Sun Oct 12 2025 Grigory Ustinov <grenka@altlinux.org> 0.45.1-alt1
- Automatically updated to 0.45.1.

* Sat Feb 01 2025 Grigory Ustinov <grenka@altlinux.org> 0.44.0-alt1
- Automatically updated to 0.44.0.

* Sun Jun 30 2024 Grigory Ustinov <grenka@altlinux.org> 0.43.0-alt1
- Automatically updated to 0.43.0.

* Tue Mar 26 2024 Grigory Ustinov <grenka@altlinux.org> 0.42.0-alt1
- Automatically updated to 0.42.0.

* Sat Feb 10 2024 Grigory Ustinov <grenka@altlinux.org> 0.41.0-alt1
- Automatically updated to 0.41.0.

* Wed Sep 13 2023 L.A. Kostis <lakostis@altlinux.ru> 0.40.1-alt3
- llvm12.0->llvm14.0.

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
