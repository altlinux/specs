%define oname pre_commit_hooks
Name: python-module-%oname
Version: 0.4.0
Release: alt1.git20150227
Summary: Some out-of-the-box hooks for pre-commit
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pre_commit_hooks/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pre-commit/pre-commit-hooks.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-autopep8
BuildPreReq: python-module-flake8 python-module-plumbum pyflakes
BuildPreReq: python-module-yaml python-module-simplejson
BuildPreReq: python-module-coverage python-module-mock
BuildPreReq: python-module-pre_commit git

%py_provides %oname
%py_requires autopep8 plumbum flake8 yaml simplejson

%description
Some out-of-the-box hooks for pre-commit.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Some out-of-the-box hooks for pre-commit.

This package contains tests for %oname.

%prep
%setup

git config --global user.email "real at altlinux.org"
git config --global user.name "REAL"

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
rm -fR build
py.test -vv

%files
%doc CHANGELOG *.md
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests*

%files tests
%python_sitelibdir/*/tests*

%changelog
* Thu Mar 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20150227
- Initial build for Sisyphus

