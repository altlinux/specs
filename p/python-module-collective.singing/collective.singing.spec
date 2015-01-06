%define mname collective
%define oname %mname.singing
Name: python-module-%oname
Version: 0.7.3
Release: alt1.dev0.git20150105
Summary: A Zope 3 library for sending notifications and newsletters
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.singing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.singing.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-initgroups
BuildPreReq: python-module-zope.sendmail
BuildPreReq: python-module-zope.keyreference
BuildPreReq: python-module-zope.app.keyreference
BuildPreReq: python-module-zope.app.catalog
BuildPreReq: python-module-zope.app.i18n
BuildPreReq: python-module-zc.queue
BuildPreReq: python-module-zc.lockfile
BuildPreReq: python-module-plone.z3cform-tests
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.app.container
BuildPreReq: python-module-zope.app.intid
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.index
BuildPreReq: python-module-zope.app.pagetemplate
BuildPreReq: python-module-zope.browserpage
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-z3c.form-tests
BuildPreReq: python-module-zope.testing

%py_provides %oname
%py_requires %mname zope.sendmail zope.keyreference zope.app.catalog
%py_requires zope.app.keyreference zope.app.i18n zc.queue zc.lockfile
%py_requires plone.memoize zope.interface zope.publisher zope.schema
%py_requires zope.i18n zope.component zope.i18nmessageid zope.container
%py_requires zope.app.container zope.app.intid zope.intid zope.event
%py_requires zope.lifecycleevent zope.index zope.app.pagetemplate
%py_requires zope.browserpage zope.annotation zope.app.component
%py_requires zope.deprecation z3c.form

%description
Singing is a Zope 3 library for sending notifications and newsletters.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.z3cform.tests zope.component.testing zope.testing
%py_requires z3c.form.testing
%add_python_req_skip queue

%description tests
Singing is a Zope 3 library for sending notifications and newsletters.

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

pushd %mname/singing
cp -fR *.txt *.zcml locales %buildroot%python_sitelibdir/%mname/singing/
install -p -m644 browser/*.pt browser/*.txt browser/*.zcml \
	%buildroot%python_sitelibdir/%mname/singing/browser/
popd

%check
python setup.py test
py.test collective/singing/tests.py
py.test collective/singing/browser/tests.py

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*
%exclude %python_sitelibdir/%mname/*/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*
%python_sitelibdir/%mname/*/*/tests.*

%changelog
* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.3-alt1.dev0.git20150105
- 0.7.3.dev0

* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.2-alt1.git20141114
- Initial build for Sisyphus

