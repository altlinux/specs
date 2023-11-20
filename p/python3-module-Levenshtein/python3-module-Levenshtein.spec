%define _unpackaged_files_terminate_build 1
%define pypi_name Levenshtein

%def_with check

Name: python3-module-%pypi_name
Version: 0.23.0
Release: alt2

Summary: Python extension for computing string edit distances and similarities
License: GPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/Levenshtein/
Vcs: https://github.com/maxbachmann/Levenshtein

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: python3-module-Levenshtein-0.23.0-alt-use-base-cython.patch

%py3_provides %pypi_name

%pyproject_runtimedeps_metadata
Provides: python3-module-%{pep503_name %pypi_name}
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
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
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info

%changelog
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

