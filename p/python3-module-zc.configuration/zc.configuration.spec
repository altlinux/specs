%define oname zc.configuration

Name: python3-module-%oname
Version: 1.2.0
Release: alt1

Summary: Extensions to zope.configuration
License: ZPLv1.1
Group: Development/Python3
Url: http://pypi.python.org/pypi/zc.configuration/

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_requires zope.testing zope.configuration


%description
The zc.configuration package used to provide the exclude directive for
inhibiting configuration. It was included in the zope.configuration and
this package currently provides a backward-compatibility imports and
tests that ensure that it will work for people who are already using
zc.configuration and not the newer zope.configuration.

This package may contain more configuration extensions in future, but
currently, it's not useful anymore as the only feature it provided, the
exclude directive was merged into the original zope.configuration
package.

%package tests
Summary: Tests for zc.configuration
Group: Development/Python3
Requires: %name = %version-%release

%description tests
The zc.configuration package used to provide the exclude directive for
inhibiting configuration. It was included in the zope.configuration and
this package currently provides a backward-compatibility imports and
tests that ensure that it will work for people who are already using
zc.configuration and not the newer zope.configuration.

This package may contain more configuration extensions in future, but
currently, it's not useful anymore as the only feature it provided, the
exclude directive was merged into the original zope.configuration
package.

This package contains tests for zc.configuration.

%package demo
Summary: demo for zc.configuration
Group: Development/Python3
Requires: %name = %version-%release

%description demo
The zc.configuration package used to provide the exclude directive for
inhibiting configuration. It was included in the zope.configuration and
this package currently provides a backward-compatibility imports and
tests that ensure that it will work for people who are already using
zc.configuration and not the newer zope.configuration.

This package may contain more configuration extensions in future, but
currently, it's not useful anymore as the only feature it provided, the
exclude directive was merged into the original zope.configuration
package.

This package contains demo for zc.configuration.

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
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/demo

%files tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*

%files demo
%python3_sitelibdir/*/*/demo


%changelog
* Tue Dec 10 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.0-alt1
- Version updated to 1.2.0
- build for python2 disabled

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.1-alt3.2
- Rebuild with python3.7.

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt3.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

