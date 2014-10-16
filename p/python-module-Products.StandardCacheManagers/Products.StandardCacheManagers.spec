%define oname Products.StandardCacheManagers

Name: python-module-%oname
Version: 2.13.1
Release: alt1.git20140914
Summary: Cache managers for Zope 2
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.StandardCacheManagers/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/Products.StandardCacheManagers.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.component python-module-transaction
BuildPreReq: python-module-AccessControl
BuildPreReq: python-module-Products.PythonScripts

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.component

%description
This package provides two cache managers for Zope 2. A RAMCacheManager
and an Accelerated HTTP cache manager, which adds HTTP cache headers to
responses.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides two cache managers for Zope 2. A RAMCacheManager
and an Accelerated HTTP cache manager, which adds HTTP cache headers to
responses.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
export PYTHONPATH=$PWD/src
python setup.py test

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1.git20140914
- Snapshot from git
- Enabled testing

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1
- Initial build for Sisyphus

