%define oname pyramid_celery

%def_with python3

Name: python-module-%oname
Version: 2.0.0
Release: alt1.git20150203
Summary: Celery integration with pyramid
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pyramid_celery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sontek/pyramid_celery.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pyramid-tests python-module-celery
BuildPreReq: python-module-mock python-module-pytest-cov
BuildPreReq: python-module-redis-py
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pyramid-tests python3-module-celery
BuildPreReq: python3-module-mock python3-module-pytest-cov
BuildPreReq: python3-module-redis-py
%endif

%py_provides %oname
Conflicts: python-module-praekelt_pyramid_celery
%py_requires pyramid celery

%description
Pyramid configuration with celery integration. Allows you to use pyramid
.ini files to configure celery and have your pyramid configuration
inside celery tasks.

%if_with python3
%package -n python3-module-%oname
Summary: Celery integration with pyramid
Group: Development/Python3
%py3_provides %oname
Conflicts: python3-module-praekelt_pyramid_celery
%py3_requires pyramid celery

%description -n python3-module-%oname
Pyramid configuration with celery integration. Allows you to use pyramid
.ini files to configure celery and have your pyramid configuration
inside celery tasks.
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
python setup.py test
export PYTHONPATH=$PWD
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.rst CHANGES.txt examples
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst CHANGES.txt examples
%python3_sitelibdir/*
%endif

%changelog
* Tue Mar 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.git20150203
- Initial build for Sisyphus

