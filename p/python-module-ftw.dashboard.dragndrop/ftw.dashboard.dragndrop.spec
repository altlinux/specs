%define mname ftw.dashboard
%define oname %mname.dragndrop
Name: python-module-%oname
Version: 1.5.5
Release: alt1.dev0.git20141107
Summary: ftw.dashboard.dragndrop adds dragndrop functionality to the dashboard
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.dashboard.dragndrop/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.dashboard.dragndrop.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2 python-module-transaction
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.traversing

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires zope.component zope.interface zope.publisher plone.portlets
%py_requires plone.theme plone.app.contentmenu plone.app.layout
%py_requires plone.app.portlets Products.GenericSetup Products.CMFCore
%py_requires Products.statusmessages collective.js.jqueryui

%description
ftw.dashboard.dragndrop adds persistent dragndrop functionality to the
standard plone dashboard.

Features:

* Drag'n'drop: All dashboard portlets can be moved with drag'n'drop from
  column to column and reordered in the column.
* Folding: Dashboard porlets are foldable.
* Edit portlet icon: Dashboard portlets have an icon on the top (pencil)
  for editing the portlet.
* close/remove portlet: Dashboard portlets have an icon on the top
  (cross) for removing the portlet from the dashboard.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing plone.app.testing zope.configuration
%py_requires zope.event zope.traversing

%description tests
ftw.dashboard.dragndrop adds persistent dragndrop functionality to the
standard plone dashboard.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires ftw

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

install -p -m644 ftw/dashboard/__init__.py \
	%buildroot%python_sitelibdir/ftw/dashboard/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/ftw/dashboard/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/ftw/dashboard/*/test*
%exclude %python_sitelibdir/ftw/dashboard/__init__.py*

%files tests
%python_sitelibdir/ftw/dashboard/*/test*

%files -n python-module-%mname
%dir %python_sitelibdir/ftw/dashboard
%python_sitelibdir/ftw/dashboard/__init__.py*

%changelog
* Thu Dec 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.5-alt1.dev0.git20141107
- Initial build for Sisyphus

