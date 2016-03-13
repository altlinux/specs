%define oname botocore-tornado

%def_with python3

Name: python-module-%oname
Version: 0.93.0
Release: alt1.git20150225.1
Summary: AsyncHTTPClient based subclass of botocore
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/botocore-tornado/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/qudos-com/botocore-tornado.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-botocore python-module-tornado
BuildPreReq: python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-botocore python3-module-tornado
BuildPreReq: python-tools-2to3
%endif

%py_provides botocore_tornado
%py_requires botocore tornado logging

%description
This module provides subclasses of botocore classes that use the tornado
AsyncHTTPClient to make requests. As far as possible, the api is kept
the same as the botocore api, the only difference is that Operation.call
returns a Future that is resolved when the http request is complete.

%package -n python3-module-%oname
Summary: AsyncHTTPClient based subclass of botocore
Group: Development/Python3
%py3_provides botocore_tornado
%py3_requires botocore tornado logging

%description -n python3-module-%oname
This module provides subclasses of botocore classes that use the tornado
AsyncHTTPClient to make requests. As far as possible, the api is kept
the same as the botocore api, the only difference is that Operation.call
returns a Future that is resolved when the http request is complete.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.93.0-alt1.git20150225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.93.0-alt1.git20150225
- Version 0.93.0

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.85.0.3-alt1.git20150130
- Initial build for Sisyphus

