%define oname sqlauth
Name: python-module-%oname
Version: 0.1.56
Release: alt1.git20141127
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
BuildPreReq: python-module-tabulate

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
* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.56-alt1.git20141127
- Version 0.1.56

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.54-alt1.git20141126
- Version 0.1.54

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.52-alt1.git20141126
- Version 0.1.52

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.50-alt1.git20141126
- Version 0.1.50

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.47-alt1.git20141126
- Version 0.1.47

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.31-alt1.git20141125
- Version 0.1.31

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.17-alt1.git20141124
- Initial build for Sisyphus

