%define mname gocept
%define oname %mname.filestore
%def_disable check

Name: python-module-%oname
Version: 0.3
Release: alt2
Summary: Provides maildir like access to files
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/gocept.filestore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-module-setuptools-tests python-module-nose
#BuildPreReq: python-module-zope.deferredimport
#BuildPreReq: python-module-zope.interface
#BuildPreReq: python-module-zope.testing
BuildRequires: python-module-nose python-module-pytest python-module-zope.deferredimport python-module-zope.testing

%py_provides %oname
%py_requires %mname zope.deferredimport zope.interface

%description
The filestore is an easy way to to process files with multiple processes
without needing locks.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
The filestore is an easy way to to process files with multiple processes
without needing locks.

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
python setup.py test
nosetests -v

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.3-alt2
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1
- Initial build for Sisyphus

