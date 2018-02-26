%define oname zc.copy
Name: python-module-%oname
Version: 1.2
Release: alt2.1
Summary: Pluggable object copying (deprecated in favor of zope.copy)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.copy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.copy zope.copypastemove zope.location

%description
This package used to provide a pluggable replacement of ObjectCopier
class and locationCopy function from zope.copypastemove and
zope.location respectively. Currently, all its functionality is merged
to those packages and the new zope.copy package is provided that
contains the actual pluggable copying mechanism used to be in this
package with no dependencies except zope.interface.

This package now only provides backward-compatibility imports and should
not be used for new developments.

%package tests
Summary: Tests for zc.copy
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package used to provide a pluggable replacement of ObjectCopier
class and locationCopy function from zope.copypastemove and
zope.location respectively. Currently, all its functionality is merged
to those packages and the new zope.copy package is provided that
contains the actual pluggable copying mechanism used to be in this
package with no dependencies except zope.interface.

This package now only provides backward-compatibility imports and should
not be used for new developments.

This package contains tests for zc.copy.

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

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

