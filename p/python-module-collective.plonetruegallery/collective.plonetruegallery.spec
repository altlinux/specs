%define mname collective
%define oname %mname.plonetruegallery
Name: python-module-%oname
Version: 3.4.6
Release: alt1.dev0.git20141128
Summary: Implements a very customizable and sophisticated gallery
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.plonetruegallery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.plonetruegallery.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.ptg.galleria
BuildPreReq: python-module-plone.app.collection
BuildPreReq: python-module-plone.app.contentmenu
BuildPreReq: python-module-plone.app.form
BuildPreReq: python-module-plone.app.imaging
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.querystring
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.folder
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-transaction
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.testing

%py_provides %oname
%py_requires %mname collective.ptg.galleria plone.app.collection
%py_requires plone.app.contentmenu plone.app.form plone.app.imaging
%py_requires plone.app.portlets plone.app.querystring plone.app.z3cform
%py_requires plone.app.vocabularies plone.folder plone.memoize z3c.form
%py_requires plone.portlets plone.uuid plone.z3cform Products.Archetypes
%py_requires Products.ATContentTypes Products.CMFCore Products.CMFPlone
%py_requires Products.GenericSetup zope.component zope.i18nmessageid
%py_requires zope.interface zope.schema

%description
collective.plonetruegallery is a Plone product that implements a very
customizable and sophisticated gallery.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.testing

%description tests
collective.plonetruegallery is a Plone product that implements a very
customizable and sophisticated gallery.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

# There is a file in the package named .DS_Store or .DS_Store.gz, 
# the file name used by Mac OS X to store folder attributes.  
# Such files are generally useless in packages and were usually accidentally 
# included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name '*.DS_Store' -o -name '*.DS_Store.gz' \) -print -delete

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.6-alt1.dev0.git20141128
- Version 3.4.6.dev0

* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.5-alt2.dev.git20140605
- Applied python-module-collective.plonetruegallery-3.4.5-alt1.dev.git20140605.diff

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.5-alt1.dev.git20140605
- Initial build for Sisyphus

