%define oname admesh

Name: python3-module-%oname
Version: 0.98.9
Release: alt1
Summary: Python bindings for ADMesh, STL maipulation library
License: GPLv2+
Group: Development/Python3
Url: https://pypi.python.org/pypi/admesh/
Vcs: https://github.com/admesh/python-admesh.git

Source: %name-%version.tar
Patch: python3-module-admesh-0.98.9-alt-tox_testing_fix.patch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): gcc-c++
BuildRequires(pre): libadmesh-devel
BuildRequires: python3-devel
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-module-Cython
BuildRequires: python3-module-pytest

%description
This module provides bindings for the ADMesh library. It lets you
manipulate 3D models in binary or ASCII STL format and partially repair
them if necessary.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.rst
%python3_sitelibdir/*

%changelog
* Thu Jul 10 2023 Aleksei Kalinin <kaa@altlinux.org> 0.98.9-alt1
- Version 0.98.9 updated from upstream.
- Drop Python 2 support.
- Fix tox.ini testing instructions.
- Simple .spec refactoring.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.98.3-alt1.git20150225
- Initial build for Sisyphus

