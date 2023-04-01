%define oname z3c.caching

%def_with check

Name: python3-module-%oname
Version: 3.0
Release: alt1

Summary: Caching infrastructure for web apps
License: ZPL-2.1
Group: Development/Python3
Url: https://pypi.org/project/z3c.caching/
Vcs: https://github.com/zopefoundation/z3c.caching

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%if_with check
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.browser
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.lifecycleevent
%endif

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
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

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
%python3_build

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif

%check
%tox_check

%files
%doc *.txt *.rst *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Sat Apr 01 2023 Anton Vyatkin <toni@altlinux.org> 3.0-alt1
- New version 3.0.

* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.2-alt1
- version updated to 2.2
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.0a1-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0a1-alt3.1.1
- (AUTO) subst_x86_64.

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

