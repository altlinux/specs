%define oname mozsci

%def_with python3

Name: python-module-%oname
Version: 0.9.2
Release: alt1.git20150127
Summary: Data science tools from Moz
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/mozsci/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/seomoz/mozsci.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests gcc-c++
BuildPreReq: python-module-scipy libnumpy-devel python-modules-json
BuildPreReq: python-module-nose python-module-coverage
BuildPreReq: python-module-Cython python-module-simplejson
BuildPreReq: python-module-scikit-learn python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-scipy libnumpy-py3-devel
BuildPreReq: python3-module-nose python3-module-coverage
BuildPreReq: python3-module-Cython python3-module-simplejson
BuildPreReq: python3-module-scikit-learn python3-module-six
%endif

%py_provides %oname
%py_requires scipy numpy simplejson json sklearn six

%description
A grab bag of assorted Data science tools from Moz.

%package -n python3-module-%oname
Summary: Data science tools from Moz
Group: Development/Python3
%py3_provides %oname
%py3_requires scipy numpy simplejson json sklearn six

%description -n python3-module-%oname
A grab bag of assorted Data science tools from Moz.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md test
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md test
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.2-alt1.git20150127
- Initial build for Sisyphus

