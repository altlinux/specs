%define _unpackaged_files_terminate_build 1
%define oname zope.publisher

%def_with check

Name: python3-module-%oname
Epoch: 1
Version: 5.1.1
Release: alt1

Summary: The Zope publisher publishes Python objects on the web (Python3)
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.publisher
#Git: https://github.com/zopefoundation/zope.publisher.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-zope.browser
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.component-tests
BuildRequires: python3-module-zope.contenttype
BuildRequires: python3-module-zope.i18n
BuildRequires: python3-module-zope.interface-tests
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-zope.security
BuildRequires: python3-module-zope.security-tests
BuildRequires: python3-module-zope.deferredimport
BuildRequires: python3-module-zope.hookable
BuildRequires: python3-module-zope.deprecation
BuildRequires: python3-module-zope.event
%endif

%py3_requires zope.browser
%py3_requires zope.component
%py3_requires zope.configuration
%py3_requires zope.contenttype
%py3_requires zope.event
%py3_requires zope.exceptions
%py3_requires zope.i18n
%py3_requires zope.interface
%py3_requires zope.location
%py3_requires zope.proxy
%py3_requires zope.security
%py3_requires zope.deferredimport
%py3_requires zope.hookable
%py3_requires zope.deprecation

%description
zope.publisher allows you to publish Python objects on the web. It has
support for plain HTTP/WebDAV clients, web browsers as well as XML-RPC
and FTP clients. Input and output streams are represented by request and
response objects which allow for easy client interaction from Python.
The behaviour of the publisher is geared towards WSGI compatibility.

%package tests
Summary: Tests for zope.publisher
Group: Development/Python3
Requires: %name = %EVR
%py3_requires zope.testrunner
%py3_requires zope.testing
Requires: python3-module-zope.security-tests
Requires: python3-module-zope.component-tests
Requires: python3-module-zope.interface-tests

%description tests
This package contains tests for %oname.

%prep
%setup
%patch0 -p1

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
export PYTHONPATH=src
zope-testrunner3 --test-path=src -vv

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*

%changelog
* Fri Dec 20 2019 Nikolai Kostrigin <nickel@altlinux.org> 1:5.1.1-alt1
- NMU: 4.3.2 -> 5.1.1
- Remove python2 module build
- Remove ubt tag from changelog
- Enable check
- Remove obsolete fix-tests patch

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1:4.3.2-alt4
- NMU: remove rpm-build-ubt from BR:

* Tue Apr 09 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:4.3.2-alt3
- requires for tests fixed

* Thu Mar 14 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:4.3.2-alt2
- Tests fixed

* Mon Mar 05 2018 Stanislav Levin <slev@altlinux.org> 1:4.3.2-alt1
- 4.2.1 -> 4.3.2

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.2.1-alt1.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:4.2.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.2.1-alt1
- Version 4.2.1

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.1.0-alt1
- Version 4.1.0

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.0-alt2
- Version 4.0.0

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:4.0.0-alt1.a4
- Version 4.0.0a4 again

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.13.4-alt2
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.13.4-alt1
- Version 3.13.4

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a4
- Version 4.0.0a4

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.13.0-alt1
- Version 3.13.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.12.6-alt4.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt4
- Added necessary requirements for tests

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt3
- Added necessary requirements
- Excluded *.pth

* Thu May 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt2
- Set as archdep package

* Tue May 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.12.6-alt1
- Initial build for Sisyphus

