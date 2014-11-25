%define oname sqlauth
Name: python-module-%oname
Version: 0.1.17
Release: alt1.git20141124
Summary: Authentication and Authorization via SQL for Autobahn
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlauth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lgfausak/sqlauth.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-autobahn python-module-sqlbridge
BuildPreReq: python-module-six python-module-taskforce
BuildPreReq: python-module-inotifyx python-module-yaml

%py_provides %oname
%py_requires twisted.python autobahn sqlbridge

%description
SQL authentication and authorization for Autobahn web sockets.

%prep
%setup

%build
%python_build_debug

%install
%python_install

install -d %buildroot%_sysconfdir
mv %buildroot%prefix/%oname %buildroot%_sysconfdir/

%check
python setup.py test

%files
%doc *.md docs/*
%_bindir/*
%config(noreplace) %_sysconfdir/*
%python_sitelibdir/*

%changelog
* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.17-alt1.git20141124
- Initial build for Sisyphus

