%define mname collective.viewlet
%define oname %mname.pythonscript
Name: python-module-%oname
Version: 0.2
Release: alt1.dev0.git20141114
Summary: Viewlet rendering collection of items returned by customizable Python scripts
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.viewlet.pythonscript/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.viewlet.pythonscript.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-unittest2
BuildPreReq: python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-collective.portlet.pythonscript-tests
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.component

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.CMFPlone Products.GenericSetup
%py_requires Products.statusmessages archetypes.schemaextender
%py_requires collective.portlet.pythonscript zope.interface zope.schema

%description
This add-on product adds ability to use 'Script (Python)' objects as
source of items to display in a Plone viewlet.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.component
%py_requires collective.portlet.pythonscript.tests

%description tests
This add-on product adds ability to use 'Script (Python)' objects as
source of items to display in a Plone viewlet.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires collective

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

install -p -m644 src/collective/viewlet/__init__.py \
	%buildroot%python_sitelibdir/collective/viewlet/

%check
python setup.py test

%files
%doc *.txt *.md
%python_sitelibdir/collective/viewlet/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/viewlet/*/test*
%exclude %python_sitelibdir/collective/viewlet/*/*/test*
%exclude %python_sitelibdir/collective/viewlet/__init__.py*

%files tests
%python_sitelibdir/collective/viewlet/*/test*
%python_sitelibdir/collective/viewlet/*/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/collective/viewlet
%python_sitelibdir/collective/viewlet/__init__.py*

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev0.git20141114
- Initial build for Sisyphus

