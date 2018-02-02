Name: bumper
Version: 0.1.8
Release: alt1.git20150215.1
Summary: Bump (pin/manage) your dependency requirements with ease
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/bumper/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/maxzheng/bumper.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-bumper-lib
BuildPreReq: python-module-requests python-module-simplejson

%py_requires bumper requests simplejson

%description
Bump (pin/manage) your dependency requirements with ease.

Feature Summary:

* Bumps dependencies in requirements.txt / pinned.txt to latest or
  specified version
* Versions are validated against published versions in PyPI
* Show detailed changelogs for pinned version bumps
* Automatically pin dependency requirements from detailed changelogs
* Easily extendible by writing your own bumper class

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc *.rst docs/*.rst
%_bindir/*
%python_sitelibdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.8-alt1.git20150215.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.git20150215
- Initial build for Sisyphus

