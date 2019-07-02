Name: bumper
Version: 0.1.13
Release: alt1

Summary: Bump (pin/manage) your dependency requirements with ease

License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/bumper/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: https://pypi.io/packages/source/b/%name/%name-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-intro
BuildRequires: python3-module-setuptools
%py3_use bumper-lib >= 0.2.17
%py3_use requests simplejson

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
subst "s|'setuptools-git'|'setuptools'|" setup.py

%build
%python3_build_debug

%install
%python3_install

%check
%python3_test

%files
%doc *.rst docs/*.rst
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon Jul 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.1.13-alt1
- new version (0.1.13) with rpmgs script
- switch to build from tarball, use python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.8-alt1.git20150215.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.8-alt1.git20150215
- Initial build for Sisyphus

