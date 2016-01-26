%define mname hurry
%define oname %mname.workflow
%def_disable check

Name: python-module-%oname
Version: 0.14
Release: alt2.dev0.git20130322
Summary: A simple but quite nifty workflow system for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/hurry.workflow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/hurry.workflow.git
Source: %name-%version.tar

BuildRequires: python-module-pytest python-module-zope.annotation python-module-zope.lifecycleevent python-module-zope.security python-module-zope.testrunner

#BuildPreReq: python-module-setuptools-tests
#BuildPreReq: python-module-ZODB3
#BuildPreReq: python-module-zope.interface
#BuildPreReq: python-module-zope.component-tests
#BuildPreReq: python-module-zope.event
#BuildPreReq: python-module-zope.security
#BuildPreReq: python-module-zope.annotation
#BuildPreReq: python-module-zope.lifecycleevent
#BuildPreReq: python-module-zope.testing

%py_provides %oname
#%py_requires %mname zope.interface zope.component ZODB3 zope.event
#%py_requires zope.security zope.annotation zope.lifecycleevent

%description
hurry.workflow is a simple workflow system. It can be used to implement
stateful multi-version workflows for Zope Toolkit applications.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
#%py_requires zope.testing zope.component.testing

%description tests
hurry.workflow is a simple workflow system. It can be used to implement
stateful multi-version workflows for Zope Toolkit applications.

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
export PYTHONPATH=$PWD/src
python src/hurry/workflow/tests.py -v

%files
%doc *.txt
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.14-alt2.dev0.git20130322
- Rebuild with "def_disable check"
- Cleanup buildreq

* Mon Feb 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1.dev0.git20130322
- Initial build for Sisyphus

