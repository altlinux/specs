%define _unpackaged_files_terminate_build 1
%define pypi_name Levenshtein
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.27.1
Release: alt1

Summary: Python extension for computing string edit distances and similarities
License: GPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/Levenshtein/
Vcs: https://github.com/rapidfuzz/Levenshtein

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
Provides: python3-module-%{pep503_name %pypi_name} = %EVR
BuildRequires(pre): rpm-build-pyproject

# For reason yet unknown, dependency on 'ninja>=1.5' is generated
# on most, platforms, but is not generated on loongarch64 and
# riscv64. In fact, the ninja module is not required for build
# the package, so let's just filter it out form all the stages
# including the verification of the generated dependencies.
%global _pyproject_deps_pep517_filter %_pyproject_deps_pep517_filter ninja

%add_pyproject_deps_build_filter cmake
%add_pyproject_deps_build_filter ninja
%pyproject_builddeps_build
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: rapidfuzz-cpp-devel
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
BuildRequires: python3-module-pytest
%endif

%description
The Levenshtein Python C extension module contains functions for fast
computation of

* Levenshtein (edit) distance, and edit operations
* string similarity
* approximate median strings, and generally string averaging
* string sequence and set similarity

It supports both normal and Unicode strings.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%ifarch %e2k
# standard is not specified, but rapidfuzz requires at least C++17
%add_optflags -std=c++17
%endif
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc HISTORY.md README.md SECURITY.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Mar 04 2025 Anton Zhukharev <ancieg@altlinux.org> 0.27.1-alt1
- Updated to 0.27.1.

* Fri Feb 14 2025 Ivan A. Melnikov <iv@altlinux.org> 0.27.0-alt1.1
- NMU: skip pep517 dependency on ninja (fixes build on
  riscv64 and loongarch64).

* Tue Feb 04 2025 Anton Zhukharev <ancieg@altlinux.org> 0.27.0-alt1
- Updated to 0.27.0.

* Wed Dec 18 2024 Anton Zhukharev <ancieg@altlinux.org> 0.26.1-alt1
- Updated to 0.26.1.

* Thu Sep 26 2024 Anton Zhukharev <ancieg@altlinux.org> 0.26.0-alt1
- Updated to 0.26.0.

* Thu Apr 11 2024 Anton Zhukharev <ancieg@altlinux.org> 0.25.1-alt1
- Updated to 0.25.1.

* Mon Feb 12 2024 Anton Zhukharev <ancieg@altlinux.org> 0.25.0-alt1
- Updated to 0.25.0.

* Mon Nov 20 2023 Anton Zhukharev <ancieg@altlinux.org> 0.23.0-alt2
- Fixed FTBFS (rapidfuzz-devel -> rapidfuzz-cpp-devel).

* Mon Oct 16 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 0.23.0-alt1.1
- Fixed build for Elbrus.

* Fri Oct 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.23.0-alt1
- Updated to 0.23.0.

* Fri Feb 21 2020 Grigory Ustinov <grenka@altlinux.org> 0.12.0-alt1
- Build new version for python3.8.

* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.11.2-alt2
- Build for python2 disabled.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.11.2-alt1.git20140923.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.11.2-alt1.git20140923.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.11.2-alt1.git20140923.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.11.2-alt1.git20140923
- Initial build for Sisyphus

