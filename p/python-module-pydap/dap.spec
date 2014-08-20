%define oname pydap

%def_with python3

Name: python-module-%oname
Version: 3.1.1
Release: alt1.git20131114
Summary: A Python library implementing the Data Access Protocol (DAP, aka OPeNDAP or DODS)
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/dap/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/robertodealmeida/pydap.git
Source: %oname-%version.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-httplib2
BuildPreReq: python-module-paste python-module-cheetah
BuildPreReq: python-module-Paver python-module-setuptools-tests
BuildPreReq: python-module-sphinx-devel libnumpy-devel
BuildPreReq: python-module-PasteScript python-module-PasteDeploy
BuildPreReq: python-module-genshi
%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-httplib2
BuildPreReq: python3-module-setuptools-tests libnumpy-py3-devel
BuildPreReq: python3-module-paste python3-module-Paver
BuildPreReq: python3-module-PasteScript python3-module-PasteDeploy
BuildPreReq: python3-module-genshi
%endif

Requires: python-modules-email
%py_requires paste.deploy

%description
Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array and
iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.

%package tests
Summary: Tests for Pydap
Group: Development/Python
Requires: %name = %EVR

%description tests
Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array and
iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.

This package contains tests for Pydap.

%package pickles
Summary: Pickles for Pydap
Group: Development/Python

%description pickles
Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array and
iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.

This package contains pickles for Pydap.

%package docs
Summary: Documentation for Pydap
Group: Development/Documentation
BuildArch: noarch

%description docs
Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array and
iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.

This package contains documentation for Pydap.

%package -n python3-module-%oname
Summary: Python implementation of the Data Access Protocol (DAP)
Group: Development/Python3
%py3_requires paste.deploy rfc822py3

%description -n python3-module-%oname
Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array and
iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.

%package -n python3-module-%oname-tests
Summary: Tests for Pydap
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array and
iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.

This package contains tests for Pydap.

%prep
%setup

%if_with python3
cp -fR . ../python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
popd
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
paver build

%if_with python3
pushd ../python3
paver.py3 build
popd
%endif

%install
paver install --root=%buildroot
for i in $(find %buildroot%python_sitelibdir/%oname -type d); do
	touch $i/__init__.py
done

%if_with python3
pushd ../python3
paver.py3 install --root=%buildroot
popd
for i in $(find %buildroot%python3_sitelibdir/%oname -type d |\
	grep -v __pycache__)
do
	touch $i/__init__.py
done
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc README.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files tests
%python_sitelibdir/*/tests.*

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1.git20131114
- Version 3.1.1
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.2.6.7-alt1.svn20081222.3.1
- Rebuild with Python-2.7

* Sun Feb 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6.7-alt1.svn20081222.3
- Added .pth file

* Wed Nov 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6.7-alt1.svn20081222.2
- Rebuilt with python 2.6

* Sat Oct 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6.7-alt1.svn20081222.1
- Fixed loading of responses and plugins submodules

* Fri Oct 2 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6.7-alt1.svn20081222
- Initial build for Sisyphus

