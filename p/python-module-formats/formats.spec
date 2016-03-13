%define oname formats

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20150211.1
Summary: Support multiple formats with ease
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/formats/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/redodo/formats.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname
%py_requires json

%description
Formats will provide you with a consistent API to parse and compose
data.

You could of course use the register method to register your own parser,
but decorators are much more fun!

%package -n python3-module-%oname
Summary: Support multiple formats with ease
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Formats will provide you with a consistent API to parse and compose
data.

You could of course use the register method to register your own parser,
but decorators are much more fun!

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
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.md *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20150211.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20150211
- Initial build for Sisyphus

