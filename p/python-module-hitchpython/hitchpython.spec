%define oname hitchpython

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.git20150727
Summary: Hitch plug-in to test python programs, including Celery and Django
License: AGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/hitchpython/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hitchtest/hitchpython.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-hitchserve python-module-hitchtest
BuildPreReq: python-module-python-build python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-hitchserve python3-module-hitchtest
BuildPreReq: python3-module-python-build python3-module-requests
%endif

%py_provides %oname
%py_requires hitchserve hitchtest python_build

%description
HitchPython is a plugin for the Hitch test framework that lets you test
python programs. Specifically, it includes code to:

* Download, build and create a virtualenv from all versions of python.
* Run a Django runserver service using hitchserve.
* Run a Celery service using hitchserve.

%if_with python3
%package -n python3-module-%oname
Summary: Hitch plug-in to test python programs, including Celery and Django
Group: Development/Python3
%py3_provides %oname
%py3_requires hitchserve hitchtest python_build

%description -n python3-module-%oname
HitchPython is a plugin for the Hitch test framework that lets you test
python programs. Specifically, it includes code to:

* Download, build and create a virtualenv from all versions of python.
* Run a Django runserver service using hitchserve.
* Run a Celery service using hitchserve.
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
* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20150727
- Initial build for Sisyphus

