%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname ndg-httpsclient

%def_with python3

Name: python-module-%oname
Version: 0.4.2
#Release: alt2.1.1

Summary: Provides enhanced HTTPS support for httplib and urllib2 using PyOpenSSL
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/ndg-httpsclient/
Packager: Python Development Team <python@packages.altlinux.org>

Source0: https://pypi.python.org/packages/a2/a7/ad1c1c48e35dc7545dab1a9c5513f49d5fa3b5015627200d2be27576c2a0/ndg_httpsclient-%{version}.tar.gz

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-module-setuptools python-module-epydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

%setup_python_module %oname

Requires: python-module-ndg = %EVR

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-docutils python-module-genshi python-module-jinja2 python-module-pytz python-module-snowballstemmer python-module-sphinx python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-epydoc python-module-setuptools python-module-html5lib python3-module-setuptools rpm-build-python3 time

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
%setup -q -n ndg_httpsclient-%{version}

%if_with python3
rm -rf ../python3
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
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 ndg/__init__.py %buildroot%python_sitelibdir/ndg/
%if_with python3
pushd ../python3
install -p -m644 ndg/__init__.py %buildroot%python3_sitelibdir/ndg/
popd
%endif

rm -f documentation/Makefile

%files
%doc PKG-INFO
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
%doc PKG-INFO
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
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.2-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt2.1.1.1
- (AUTO) subst_x86_64.

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 07 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.4.0-alt2
- NMU: added python-module-setuptools to BRs.

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.0-alt1.1
- NMU: Use buildreq for BR.

* Mon Aug 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1
- Version 0.4.0

* Fri Mar 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1
- Version 0.3.3

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2
- Added module for Python 3

* Wed Apr 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus

