%define oname furl

%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt1.git20141118.1
Summary: URL manipulation made simple
License: Public domain
Group: Development/Python
Url: https://pypi.python.org/pypi/furl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gruns/furl.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-orderedmultidict
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-orderedmultidict
%endif

%py_provides %oname

%description
furl is a small Python library that makes manipulating URLs simple.

%package -n python3-module-%oname
Summary: URL manipulation made simple
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
furl is a small Python library that makes manipulating URLs simple.

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
touch tests/__init__.py
python setup.py test
%if_with python3
pushd ../python3
touch tests/__init__.py
python3 setup.py test
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.git20141118.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141118
- Version 0.4.0
- Added module for Python 3

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.95-alt1.git20140717
- Initial build for Sisyphus

