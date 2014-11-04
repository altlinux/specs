%define oname pyramid_fullauth

%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt1.git20141102
Summary: Provide full authentication / authorisation implementation for pyramid apps
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_fullauth/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/fizyk/pyramid_fullauth.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: libmysqlclient-devel python-module-pyaml
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid python-module-pyramid_localize
BuildPreReq: python-module-pyramid_mako python-module-tzf.pyramid_yml
BuildPreReq: python-module-pyramid_basemodel python-module-mock
BuildPreReq: python-module-pytest_pyramid python-module-pytest-cov
BuildPreReq: python-module-velruse python-module-mysql
BuildPreReq: python-module-pytest-dbfixtures python-module-psycopg2
BuildPreReq: python-module-openid python-module-pyramid_tm
BuildPreReq: python-module-sphinx-devel python-module-inflect
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid python3-module-pyramid_localize
BuildPreReq: python3-module-pyramid_mako python3-module-tzf.pyramid_yml
BuildPreReq: python3-module-pyramid_basemodel python3-module-mock
BuildPreReq: python3-module-pytest_pyramid python3-module-pytest-cov
BuildPreReq: python3-module-openid python3-module-pyramid_tm
BuildPreReq: python3-module-markupsafe
%endif

%py_provides %oname
%py_requires tzf.pyramid_yml

%description
Pyramid fullauth's goal is to provide full plug-in registration
functionality for pyramid, with user managing.

%package -n python3-module-%oname
Summary: Provide full authentication / authorisation implementation for pyramid apps
Group: Development/Python3
%py3_provides %oname
%py3_requires tzf.pyramid_yml

%description -n python3-module-%oname
Pyramid fullauth's goal is to provide full plug-in registration
functionality for pyramid, with user managing.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Pyramid fullauth's goal is to provide full plug-in registration
functionality for pyramid, with user managing.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Pyramid fullauth's goal is to provide full plug-in registration
functionality for pyramid, with user managing.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141102
- Initial build for Sisyphus

