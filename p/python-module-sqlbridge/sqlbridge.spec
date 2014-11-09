%define oname sqlbridge

%def_without python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20141107
Summary: Basic database connectivity for Autobahn web sockets
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlbridge/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lgfausak/sqlbridge.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-autobahn python-module-twisted-core
BuildPreReq: python-module-txpostgres python-module-psycopg2
BuildPreReq: python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-autobahn python3-module-twisted-core
BuildPreReq: python3-module-txpostgres python3-module-psycopg2
BuildPreReq: python3-module-six
%endif

%py_provides %oname
%py_requires twisted.python

%description
A simple database access component for Autobahn. This component builds
bridges to database backends making them accessible to Autobahn via
topics. The component can be used in its raw form to build custom
Autobahn deployments, or, the convenience scripts that haver been
included can be used to connect an sqlbridge to an already operating
Autobahn router. There are three test scripts included in this
distribution, sqlrouter, sqlbridge and sqlcmd.

%package -n python3-module-%oname
Summary: Basic database connectivity for Autobahn web sockets
Group: Development/Python3
%py3_provides %oname
%py3_requires twisted.python

%description -n python3-module-%oname
A simple database access component for Autobahn. This component builds
bridges to database backends making them accessible to Autobahn via
topics. The component can be used in its raw form to build custom
Autobahn deployments, or, the convenience scripts that haver been
included can be used to connect an sqlbridge to an already operating
Autobahn router. There are three test scripts included in this
distribution, sqlrouter, sqlbridge and sqlcmd.

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

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20141107
- Initial build for Sisyphus

