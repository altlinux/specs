%define oname hgdistver

%def_with python3

Name: python-module-%oname
Version: 0.23
Release: alt1
Summary: Utility to generate python package version infos from mercurial/git tags
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/hgdistver/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: git mercurial
BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
Requires: git mercurial

%description
This module is a simple drop-in to support setup.py in mercurial and git
based projects.

Alternatively it can be a setup time requirement.

It extracts the last Tag as well as the distance to it in commits from
the scm, and uses these to calculate a version number.

%package -n python3-module-%oname
Summary: Utility to generate python package version infos from mercurial/git tags
Group: Development/Python3
%py3_provides %oname
Requires: git mercurial

%description -n python3-module-%oname
This module is a simple drop-in to support setup.py in mercurial and git
based projects.

Alternatively it can be a setup time requirement.

It extracts the last Tag as well as the distance to it in commits from
the scm, and uses these to calculate a version number.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23-alt1
- Initial build for Sisyphus

