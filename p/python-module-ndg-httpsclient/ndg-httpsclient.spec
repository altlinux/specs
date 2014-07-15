%define oname ndg-httpsclient

%def_with python3

Name: python-module-%oname
Version: 0.3.2
Release: alt2

Summary: Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
License: BSD
Group: Development/Python

Url: https://pypi.python.org/pypi/ndg-httpsclient/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python
BuildPreReq: python-module-setuptools python-module-epydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%setup_python_module %oname

Requires: python-module-ndg = %EVR

%description
This is a HTTPS client implementation for httplib and urllib2 based on
PyOpenSSL. PyOpenSSL provides a more fully featured SSL implementation
over the default provided with Python and importantly enables full
verification of the SSL peer.

%package -n python3-module-%oname
Summary: Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
Group: Development/Python3
Requires: python3-module-ndg = %EVR

%description -n python3-module-%oname
This is a HTTPS client implementation for httplib and urllib2 based on
PyOpenSSL. PyOpenSSL provides a more fully featured SSL implementation
over the default provided with Python and importantly enables full
verification of the SSL peer.

%package -n python3-module-%oname-tests
Summary: Tests for ndg-httpsclient
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This is a HTTPS client implementation for httplib and urllib2 based on
PyOpenSSL. PyOpenSSL provides a more fully featured SSL implementation
over the default provided with Python and importantly enables full
verification of the SSL peer.

This package contains tests for ndg-httpsclient.

%package -n python3-module-ndg
Summary: Core module of ndg
Group: Development/Python3

%description -n python3-module-ndg
This package contains core module of ndg.

%package tests
Summary: Tests for ndg-httpsclient
Group: Development/Python
Requires: %name = %EVR

%description tests
This is a HTTPS client implementation for httplib and urllib2 based on
PyOpenSSL. PyOpenSSL provides a more fully featured SSL implementation
over the default provided with Python and importantly enables full
verification of the SSL peer.

This package contains tests for ndg-httpsclient.

%package docs
Summary: Documentation for ndg-httpsclient
Group: Development/Documentation

%description docs
This is a HTTPS client implementation for httplib and urllib2 based on
PyOpenSSL. PyOpenSSL provides a more fully featured SSL implementation
over the default provided with Python and importantly enables full
verification of the SSL peer.

This package contains documentation for ndg-httpsclient.

%package -n python-module-ndg
Summary: Core module of ndg
Group: Development/Python

%description -n python-module-ndg
This package contains core module of ndg.

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
sed -i 's|urllib2|urllib.request|' \
	ndg/httpsclient/https.py \
	ndg/httpsclient/urllib2_build_opener.py
sed -i 's|from urllib2|from urllib.request|' \
	ndg/httpsclient/utils.py
%python3_build_debug
popd
%endif

%make -C documentation

%install
%if_with python3
pushd ../python3
%python3_install
touch %buildroot%python3_sitelibdir/ndg/__init__.py
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install
touch %buildroot%python_sitelibdir/ndg/__init__.py

rm -f documentation/Makefile

%files
%doc LICENSE
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/ndg/__init__.py*

%files tests
%python_sitelibdir/*/*/test

%files docs
%doc documentation/*

%files -n python-module-ndg
%python_sitelibdir/ndg/__init__.py*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE
%_bindir/*.py3
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/ndg/__init__.py
%exclude %python3_sitelibdir/ndg/__pycache__/__init__.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test

%files -n python3-module-ndg
%python3_sitelibdir/ndg/__init__.py
%python3_sitelibdir/ndg/__pycache__/__init__.*
%endif

%changelog
* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2
- Added module for Python 3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus

