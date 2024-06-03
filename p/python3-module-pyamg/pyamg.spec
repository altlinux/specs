%define _unpackaged_files_terminate_build 1
%define pypi_name pyamg
%define mod_name %pypi_name

%ifarch ppc64le
%def_without check
%else
%def_with check
%endif

Name: python3-module-%pypi_name
Version: 5.1.0
Release: alt2

Summary: PyAMG: Algebraic Multigrid Solvers in Python
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pyamg/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(pybind11)
BuildRequires: python3(wheel)

BuildRequires: gcc-c++

%if_with check
# deps
BuildRequires: python3(numpy)
BuildRequires: python3(scipy)

BuildRequires: python3(numpy.testing)
BuildRequires: python3(pytest)
%endif

%description
PyAMG is a library of Algebraic Multigrid (AMG) solvers with a
convenient Python interface.

%prep
%setup

# setuptools_scm implements a file_finders entry point which returns all files
# tracked by SCM.
if [ ! -d .git ]; then
    git init
    git config user.email author@example.com
    git config user.name author
    git add .
    git commit -m 'release'
    git tag '%version'
fi

%build
%pyproject_build

%install
%pyproject_install

%check
# https://github.com/pyamg/pyamg/issues/342
%ifarch i586
%define _pytest_args -k 'not test_bellman_ford and not test_lloyd_cluster'
%endif
%pyproject_run -- bash -s <<-'ENDTESTS'
set -eux
mkdir empty
cd empty
python -m pytest -ra -Wignore --pyargs %mod_name %{?_pytest_args}
ENDTESTS

%files
%doc *.txt *.md
%python3_sitelibdir/pyamg/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/
%exclude %python3_sitelibdir/pyamg/tests
%exclude %python3_sitelibdir/pyamg/*/tests

%changelog
* Tue May 07 2024 Stanislav Levin <slev@altlinux.org> 5.1.0-alt2
- Fixed FTBFS (Pytest 8.1.1).

* Tue Mar 26 2024 Grigory Ustinov <grenka@altlinux.org> 5.1.0-alt1
- Automatically updated to 5.1.0.

* Tue Jul 04 2023 Grigory Ustinov <grenka@altlinux.org> 5.0.1-alt1
- Automatically updated to 5.0.1.

* Sat Apr 29 2023 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.

* Thu Sep 22 2022 Stanislav Levin <slev@altlinux.org> 4.2.3-alt1
- 4.0.0 -> 4.2.3.

* Wed Jan 15 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.0.0-alt1
- Version updated to 4.0.0
- porting on python3

* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt2
- Fixed build

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.1-alt1
- Version 2.2.1

* Sat Jul 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt2
- Avoid requirement on pythonX.Y(example)

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Fri Feb 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt2
- Moved examples into tests subpackage

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.5-alt1
- Initial build for Sisyphus

