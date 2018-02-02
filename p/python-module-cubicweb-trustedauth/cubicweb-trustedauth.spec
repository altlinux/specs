%define oname cubicweb-trustedauth
Name: python-module-%oname
Version: 0.3.1
Release: alt1.1
Summary: Authentication plugin for cubicweb instances
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/cubicweb-trustedauth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools cubicweb

Requires: cubicweb

%description
This cube provides an authentication plugin which ensures proper
authentication of users behind a trusted reverse proxy (eg. Apache +
mod_ssl + mod_auth_kerb).

The idea is that if the CubicWeb application is behind a reverse proxy
that is responsible for authenticating users, the CubicWeb application
do trust this latter when it says the user is authenticated as "user".
This information is simply passed from the reverse proxy to the CubicWeb
application by an entry in the HTTP header.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%doc README
%python_sitelibdir/*
%_datadir/cubicweb/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1
- Initial build for Sisyphus

