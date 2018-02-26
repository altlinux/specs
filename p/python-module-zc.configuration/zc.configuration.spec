%define oname zc.configuration
Name: python-module-%oname
Version: 1.1
Release: alt2.1
Summary: Extensions to zope.configuration
License: ZPLv1.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.configuration/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.testing zope.configuration

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
Group: Development/Python
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
Group: Development/Python
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
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*
%exclude %python_sitelibdir/*/*/demo

%files tests
%python_sitelibdir/*/*/tests.*

%files demo
%python_sitelibdir/*/*/demo

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

