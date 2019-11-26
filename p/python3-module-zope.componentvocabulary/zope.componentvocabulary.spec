%define oname zope.componentvocabulary

Name: python3-module-%oname
Version: 2.0.0
Release: alt4

Summary: Component vocabularies
License: ZPLv2.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zope.componentvocabulary/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_requires zope zope.component zope.i18nmessageid zope.interface
%py3_requires zope.schema zope.security


%description
This package contains various vocabularies.

%package tests
Summary: Tests for zope.componentvocabulary
Group: Development/Python3
Requires: %name = %version-%release
%py3_requires zope.component

%description tests
This package contains tests for zope.componentvocabulary.

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

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/*/tests


%changelog
* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.0.0-alt4
- python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 2.0.0-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt3
- Version 2.0.0

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt2.a1
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1.a1
- Version 2.0.0a1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.1-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus

