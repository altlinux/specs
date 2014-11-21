%define mname collective.portlet
%define oname %mname.pythonscript
Name: python-module-%oname
Version: 1.2.2
Release: alt1.dev.git20130911
Summary: Portlet rendering collection of items returned by customizable Python scripts
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.portlet.pythonscript/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.portlet.pythonscript.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.CMFPlone Products.GenericSetup
%py_requires Products.statusmessages zope.interface zope.schema

%description
This add-on product adds ability to use 'Script (Python)' objects as
source of items to display in a 'Python Script Portlet'.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.component

%description tests
This add-on product adds ability to use 'Script (Python)' objects as
source of items to display in a 'Python Script Portlet'.

This package contains tests for %oname

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

install -p -m644 src/collective/portlet/__init__.py \
	%buildroot%python_sitelibdir/collective/portlet/

%check
python setup.py test

%files
%doc *.txt *.md docs/*
%python_sitelibdir/collective/portlet/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/portlet/*/test*
%exclude %python_sitelibdir/collective/portlet/*/*/test*
%exclude %python_sitelibdir/collective/portlet/__init__.py*

%files tests
%python_sitelibdir/collective/portlet/*/test*
%python_sitelibdir/collective/portlet/*/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/collective/portlet
%python_sitelibdir/collective/portlet/__init__.py*

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.dev.git20130911
- Initial build for Sisyphus

