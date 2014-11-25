%define oname zc.sentrywsgi

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1
Summary: Sentry configuration middleware
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/zc.sentrywsgi
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-corbeau
BuildPreReq: python-module-raven python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools-tests python3-module-corbeau
BuildPreReq: python3-module-raven python3-module-requests
%endif

%py_provides %oname
%py_requires zc corbeau raven requests

%description
This is a thin wrapper around the raven middleware which ensures SSL
validation is performed and logging configuration is also applied.

%package -n python3-module-%oname
Summary: Sentry configuration middleware
Group: Development/Python3
%py3_provides %oname
%py3_requires zc corbeau raven requests

%description -n python3-module-%oname
This is a thin wrapper around the raven middleware which ensures SSL
validation is performed and logging configuration is also applied.

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/zc/*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/zc/*
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

