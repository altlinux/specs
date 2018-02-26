%define oname z3c.caching
Name: python-module-%oname
Version: 2.0a1
Release: alt2.1
Summary: Caching infrastructure for web apps
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.caching/2.0a1
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface zope.component zope.event
%py_requires zope.lifecycleevent zope.browser

%description
Caching of web pages is a complicated process: there are many possible
policies to choose from, and the right policy can depend on factors such
as who is making the request, the URL is being retrieved and resource
negotiation settings such as accepted languages and encodings.

Hardcoding caching logic in an application is not desirable, especially
for reusable code. It is also not possible to allow an administrator to
manually configure the caching headers for every resource in an
application. This packages tries to address this problem by providing a
cache ruleset framework: it allows implementors to specify a ruleset for
every component. Administrators can then define a policy which dictates
the correct caching behaviour for each ruleset.

%package tests
Summary: Tests for Caching infrastructure for web apps
Group: Development/Python
Requires: %name = %version-%release
%py_requires nose

%description tests
Caching of web pages is a complicated process: there are many possible
policies to choose from, and the right policy can depend on factors such
as who is making the request, the URL is being retrieved and resource
negotiation settings such as accepted languages and encodings.

Hardcoding caching logic in an application is not desirable, especially
for reusable code. It is also not possible to allow an administrator to
manually configure the caching headers for every resource in an
application. This packages tries to address this problem by providing a
cache ruleset framework: it allows implementors to specify a ruleset for
every component. Administrators can then define a policy which dictates
the correct caching behaviour for each ruleset.

This package contains tests for Caching infrastructure for web apps.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0a1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0a1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0a1-alt1
- Initial build for Sisyphus

