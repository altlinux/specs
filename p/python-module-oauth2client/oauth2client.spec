%define oname oauth2client

%def_with python3

Name: python-module-%oname
Version: 1.4.1
Release: alt1.git20141115

Summary: OAuth 2.0 client library
License: Apache Software License
Group: Development/Python

Url: https://pypi.python.org/pypi/oauth2client/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-module-setuptools-tests python-modules-json
BuildPreReq: python-module-httplib2 python-module-pyasn1
BuildPreReq: python-module-pyasn1-modules python-module-rsa
BuildPreReq: python-module-keyring python-module-mox
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-httplib2 python3-module-pyasn1
BuildPreReq: python3-module-pyasn1-modules python3-module-rsa
BuildPreReq: python3-module-keyring python3-module-mox
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %oname

%description
The oauth2client is a client library for OAuth 2.0.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
The oauth2client is a client library for OAuth 2.0.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: OAuth 2.0 client library
Group: Development/Python3
%add_python3_req_skip google

%description -n python3-module-%oname
The oauth2client is a client library for OAuth 2.0.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc CHANGELOG *.md
%python_sitelibdir/*

%files docs
%doc docs/epy/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Nov 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.git20141115
- Version 1.4.1

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1.git20141031
- Version 1.3.2

* Tue Oct 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1.git20141027
- Version 1.3.1

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added module for Python 3

* Wed Sep 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Version 1.2

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

