%define oname zope.app.module
Name: python-module-%oname
Version: 3.5.0
Release: alt2.1
Summary: Zope 3 persistent code/module support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.module/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.interface zope.component zope.container
%py_requires zope.schema zope.filerepresentation ZODB3 zodbcode

%description
Persistent Python modules allow us to develop and store Python modules
in the ZODB in contrast to storing them on the filesystem. You might
want to look at the zodbcode package for the details of the
implementation. In Zope 3 we implemented persistent modules as
utilities. These utilities are known as module managers that manage the
source code, compiled module and name of the module. We then provide a
special module registry that looks up the utilities to find modules.

%package tests
Summary: Tests for zope.app.module
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
Persistent Python modules allow us to develop and store Python modules
in the ZODB in contrast to storing them on the filesystem. You might
want to look at the zodbcode package for the details of the
implementation. In Zope 3 we implemented persistent modules as
utilities. These utilities are known as module managers that manage the
source code, compiled module and name of the module. We then provide a
special module registry that looks up the utilities to find modules.

This package contains tests for zope.app.module.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

