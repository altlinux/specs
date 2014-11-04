%define oname pyramid_localize

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20140504
Summary: Package to provide translation methods for pyramid
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_localize/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/fizyk/pyramid_localize.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid python-module-pyramid_basemodel
BuildPreReq: python-module-tzf.pyramid_yml python-module-pyramid_mako
BuildPreReq: python-module-pytest_pyramid python-module-pytest-cov
BuildPreReq: python-module-mock python-module-babel
BuildPreReq: python-module-sphinx-devel python-module-inflect
BuildPreReq: python-module-pyramid_tm python-module-pysqlite2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid python3-module-pyramid_basemodel
BuildPreReq: python3-module-tzf.pyramid_yml python3-module-pyramid_mako
BuildPreReq: python3-module-pytest_pyramid python3-module-pytest-cov
BuildPreReq: python3-module-mock python3-module-babel
BuildPreReq: python3-module-pyramid_tm python3-module-markupsafe
%endif

%py_provides %oname
%py_requires tzf.pyramid_yml

%description
Package provides translation methods for pyramid, and means to reload
translations without stopping the application.

%package -n python3-module-%oname
Summary: Package to provide translation methods for pyramid
Group: Development/Python3
%py3_provides %oname
%py3_requires tzf.pyramid_yml

%description -n python3-module-%oname
Package provides translation methods for pyramid, and means to reload
translations without stopping the application.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Package provides translation methods for pyramid, and means to reload
translations without stopping the application.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Package provides translation methods for pyramid, and means to reload
translations without stopping the application.

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
rm -fR build
py.test
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
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20140504
- Initial build for Sisyphus

