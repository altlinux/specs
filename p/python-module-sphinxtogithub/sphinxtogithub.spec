%define oname sphinxtogithub
Name: python-module-%oname
Version: 1.1.0
Release: alt1.dev.git20131026.1
Summary: Script to prepare Sphinx html output for github pages
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sphinxtogithub/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/michaeljones/sphinx-to-github.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools

%py_provides %oname

%description
This project is designed to help you get around the github-pages Jekyll
behaviour of ignoring top level directories starting with an underscore.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.dev.git20131026.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.dev.git20131026
- Initial build for Sisyphus

