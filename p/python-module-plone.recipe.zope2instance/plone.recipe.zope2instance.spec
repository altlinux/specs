%define mname plone.recipe
%define oname %mname.zope2instance
Name: python-module-%oname
Version: 4.2.17
Release: alt1.dev0.git20141101
Summary: Buildout recipe for creating a Zope 2 instance
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.recipe.zope2instance/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.recipe.zope2instance.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zc.buildout-tests
BuildPreReq: python-module-mailinglogger
BuildPreReq: python-module-zc.recipe.egg

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires ZODB3 zc.buildout zc.recipe.egg

%description
This recipe creates and configures a Zope 2 instance in parts. It also
installs a control script, which is like zopectl, in the bin/ directory.
The name of the control script is the the name of the part in buildout.
By default various runtime and log information will be stored inside the
var/ directory.

Note: This recipe is not intended to setup a Zope 2 WSGI based instance
and will not work for this use-case. There's no special recipe required
to setup WSGI any longer and you can use simple template recipes
instead.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zc.buildout.testing

%description tests
This recipe creates and configures a Zope 2 instance in parts. It also
installs a control script, which is like zopectl, in the bin/ directory.
The name of the control script is the the name of the part in buildout.
By default various runtime and log information will be stored inside the
var/ directory.

Note: This recipe is not intended to setup a Zope 2 WSGI based instance
and will not work for this use-case. There's no special recipe required
to setup WSGI any longer and you can use simple template recipes
instead.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires plone

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 src/plone/recipe/__init__.py \
	%buildroot%python_sitelibdir/plone/recipe/

%check
python setup.py test
rm -fR build
py.test

%files
%doc *.txt *.rst
%python_sitelibdir/plone/recipe/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/recipe/*/tests
%exclude %python_sitelibdir/plone/recipe/__init__.py*

%files tests
%python_sitelibdir/plone/recipe/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/plone/recipe
%python_sitelibdir/plone/recipe/__init__.py*

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.17-alt1.dev0.git20141101
- Initial build for Sisyphus

