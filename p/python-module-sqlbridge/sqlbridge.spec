%define oname sqlbridge

%def_without python3

Name: python-module-%oname
Version: 0.1.68
Release: alt2.git20141218.1
Summary: Basic database connectivity for Autobahn web sockets
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlbridge/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lgfausak/sqlbridge.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-autobahn python-module-twisted-core
BuildPreReq: python-module-txpostgres python-module-psycopg2
BuildPreReq: python-module-six python-module-taskforce
BuildPreReq: python-module-inotifyx python-module-yaml
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-autobahn python3-module-twisted-core
BuildPreReq: python3-module-txpostgres python3-module-psycopg2
BuildPreReq: python3-module-six python3-module-taskforce
BuildPreReq: python3-module-inotifyx python3-module-yaml
%endif

%py_provides %oname
Requires: %oname-common = %EVR
%py_requires twisted.python

%description
A simple database access component for Autobahn. This component builds
bridges to database backends making them accessible to Autobahn via
topics. The component can be used in its raw form to build custom
Autobahn deployments, or, the convenience scripts that haver been
included can be used to connect an sqlbridge to an already operating
Autobahn router. There are three test scripts included in this
distribution, sqlrouter, sqlbridge and sqlcmd.

%package -n %oname-common
Summary: Common config files for %oname
Group: System/Configuration/Other

%description -n %oname-common
A simple database access component for Autobahn. This component builds
bridges to database backends making them accessible to Autobahn via
topics. The component can be used in its raw form to build custom
Autobahn deployments, or, the convenience scripts that haver been
included can be used to connect an sqlbridge to an already operating
Autobahn router. There are three test scripts included in this
distribution, sqlrouter, sqlbridge and sqlcmd.

This package contains common config files for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Basic database connectivity for Autobahn web sockets
Group: Development/Python3
%py3_provides %oname
Requires: %oname-common = %EVR
%py3_requires twisted.python

%description -n python3-module-%oname
A simple database access component for Autobahn. This component builds
bridges to database backends making them accessible to Autobahn via
topics. The component can be used in its raw form to build custom
Autobahn deployments, or, the convenience scripts that haver been
included can be used to connect an sqlbridge to an already operating
Autobahn router. There are three test scripts included in this
distribution, sqlrouter, sqlbridge and sqlcmd.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

install -d %buildroot%_sysconfdir
mv %buildroot%prefix/%oname %buildroot%_sysconfdir/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%files -n %oname-common
%dir %_sysconfdir/%oname
%config %_sysconfdir/%oname/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.68-alt2.git20141218.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.68-alt2.git20141218
- Fixed build

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.68-alt1.git20141218
- Version 0.1.68

* Mon Dec 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.65-alt1.git20141130
- Version 0.1.65

* Fri Nov 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.59-alt1.git20141127
- Version 0.1.59

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.54-alt1.git20141127
- Version 0.1.54

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.50-alt1.git20141124
- Version 0.1.50

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.49-alt1.git20141123
- Version 0.1.49

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.45-alt1.git20141121
- Version 0.1.45

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.40-alt1.git20141120
- Version 0.1.40

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.33-alt1.git20141117
- Version 0.1.33

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.14-alt1.git20141113
- Version 0.1.14

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.11-alt1.git20141112
- Version 0.1.11

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.9-alt1.git20141111
- Version 0.1.9

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20141107
- Initial build for Sisyphus

