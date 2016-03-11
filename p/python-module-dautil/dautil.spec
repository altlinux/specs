%define oname dautil

%def_with python3

Name: python-module-%oname
Version: 0.0.1
Release: alt1.a18.2
Summary: Data analysis utilities
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/dautil
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests ipython
BuildPreReq: python-module-appdirs python-module-landslide xvfb-run
BuildPreReq: python-module-nose python-module-nose-parameterized
BuildPreReq: python-module-pandas python-module-joblib
BuildPreReq: python-module-pycairo
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests ipython3
BuildPreReq: python3-module-appdirs python3-module-landslide xvfb-run
BuildPreReq: python3-module-nose python3-module-nose-parameterized
BuildPreReq: python3-module-pandas python3-module-joblib
BuildPreReq: python3-module-pycairo
%endif

%py_provides %oname
%py_requires appdirs landslide joblib

%description
Data analysis utilities.

http://pythonhosted.org/dautil/

%if_with python3
%package -n python3-module-%oname
Summary: Data analysis utilities
Group: Development/Python3
%py3_provides %oname
%py3_requires appdirs landslide joblib

%description -n python3-module-%oname
Data analysis utilities.

http://pythonhosted.org/dautil/
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
export LC_ALL=en_US.UTF-8
xvfb-run python setup.py test -v
%if_with python3
pushd ../python3
xvfb-run python3 setup.py test -v
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Mon Feb 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.1-alt1.a18.2
- rebuild with rpm-build-python3-0.1.9
  (to conform to the new Python3 deps and location "policy")

* Mon Aug 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.a18
- Initial build for Sisyphus

