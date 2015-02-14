%define oname Products.RichDocument

Name: python-module-%oname
Version: 3.6
Release: alt2.dev0.git20140821
Summary: Allows users to upload images directly into the document during editing
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.RichDocument/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.RichDocument.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-nose
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.TinyMCE
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-plone.outputfilters
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-Products.SimpleAttachment

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.SimpleAttachment
%py_requires Products.Archetypes Products.CMFCore Products.TinyMCE
%py_requires Products.ATContentTypes Products.CMFPlone zope.component
%py_requires Products.CMFDynamicViewFTI Products.LinguaPlone
%py_requires plone.outputfilters zope.interface zope.i18nmessageid

%description
RichDocument is a document type which provides the same fields as the
standard Plone Document/Page type, but allows users to upload images
directly into the document during editing.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
RichDocument is a document type which provides the same fields as the
standard Plone Document/Page type, but allows users to upload images
directly into the document during editing.

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

%check
python setup.py test

%files
%doc *.md docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6-alt2.dev0.git20140821
- Added necessary requirements
- Enabled testing

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6-alt1.dev0.git20140821
- Initial build for Sisyphus

