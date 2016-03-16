%define oname z3c.caching

%def_with python3

Name: python-module-%oname
Version: 2.0a1
Release: alt3.1
Summary: Caching infrastructure for web apps
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.caching/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

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

%package -n python3-module-%oname
Summary: Caching infrastructure for web apps
Group: Development/Python3
%py3_requires zope.interface zope.component zope.event
%py3_requires zope.lifecycleevent zope.browser

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for Caching infrastructure for web apps
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires nose

%description -n python3-module-%oname-tests
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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0a1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0a1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0a1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0a1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0a1-alt1
- Initial build for Sisyphus

