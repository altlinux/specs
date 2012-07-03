%define oname z3c.recipe.paster
Name: python-module-%oname
Version: 0.5.3
Release: alt3.1
Summary: Zope3 paste deploy setup recipe
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.recipe.paster/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.recipe paste paste.deploy paste.script ZConfig
%py_requires zc.recipe.egg zope.app.wsgi zope.app.debug zope.schema
%py_requires zope.interface

%description
The z3c.recipe.paster:serve generates a paste deploy serve scripts and
configuration files for starting a paste deploy based Zope 3 setup. The
paste deploy *.ini file content can get defined in the buildout.cfg
file.

Note, you have to define an entry_point in your projects setup.py file
for using a application_factory via the section name.

%package tests
Summary: Tests for Zope3 paste deploy setup recipe
Group: Development/Python
Requires: %name = %version-%release
%py_requires transaction ZODB3 pytz zc.lockfile zc.recipe.filestorage
%py_requires zdaemon zope.annotation zope.app.appsetup
%py_requires zope.authentication zope.app.publication zope.browser
%py_requires zope.broken zope.cachedescriptors zope.component
%py_requires zope.configuration zope.container zope.copy
%py_requires zope.deferredimport zope.dottedname zope.error zope.event
%py_requires zope.exceptions zope.filerepresentation zope.i18n
%py_requires zope.i18nmessageid zope.processlifetime
%py_requires zope.lifecycleevent zope.location zope.minmax zope.proxy
%py_requires zope.publisher zope.session zope.site zope.size
%py_requires zope.testing zc.buildout zope.traversing zope.security

%description tests
The z3c.recipe.paster:serve generates a paste deploy serve scripts and
configuration files for starting a paste deploy based Zope 3 setup. The
paste deploy *.ini file content can get defined in the buildout.cfg
file.

Note, you have to define an entry_point in your projects setup.py file
for using a application_factory via the section name.

This package contains tests for Zope3 paste deploy setup recipe.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.3-alt3.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt3
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt2
- Fixed requirements

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1
- Initial build for Sisyphus

