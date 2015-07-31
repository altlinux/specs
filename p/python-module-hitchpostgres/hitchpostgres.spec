%define oname hitchpostgres

%def_with python3

Name: python-module-%oname
Version: 0.6.1
Release: alt1.git20150723
Summary: Plugin to run Postgres using the Hitch testing framework
License: AGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/hitchpostgres/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hitchtest/hitchpostgres.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-hitch python-module-hitchserve
BuildPreReq: python-module-hitchtest python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-hitch python3-module-hitchserve
BuildPreReq: python3-module-hitchtest python3-module-requests
%endif

%py_provides %oname
%py_requires hitch hitchserve hitchtest

%description
HitchPostgres is a plugin for the Hitch test framework that lets you run
and interact with Postgres in an isolated way as part of a test.

Before starting the service, it runs the initdb command to create all
required data files for a postgresql database in the .hitch directory.
This means that whatever you do, you will not interfere with the system
postgres files. The system postgres does not even have to be running.

After starting the service, it creates any users and databases specified
that may be required for your app to start.

During the test it provides convenience functions psql, pg_dump and
pg_restore so that you can interact with the database using IPython or
in your test.

%if_with python3
%package -n python3-module-%oname
Summary: Plugin to run Postgres using the Hitch testing framework
Group: Development/Python3
%py3_provides %oname
%py3_requires hitch hitchserve hitchtest

%description -n python3-module-%oname
HitchPostgres is a plugin for the Hitch test framework that lets you run
and interact with Postgres in an isolated way as part of a test.

Before starting the service, it runs the initdb command to create all
required data files for a postgresql database in the .hitch directory.
This means that whatever you do, you will not interfere with the system
postgres files. The system postgres does not even have to be running.

After starting the service, it creates any users and databases specified
that may be required for your app to start.

During the test it provides convenience functions psql, pg_dump and
pg_restore so that you can interact with the database using IPython or
in your test.
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
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
* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150723
- Initial build for Sisyphus

