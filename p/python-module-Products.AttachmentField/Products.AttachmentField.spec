%define oname Products.AttachmentField
Name: python-module-%oname
Version: 1.4.6
Release: alt1.git20120911
Summary: AttachmentField/Widget for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.AttachmentField/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.AttachmentField.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.OpenXml
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-Products.MimetypesRegistry
BuildPreReq: python-module-plone.app.upgrade
BuildPreReq: python-module-zope.contenttype
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.OpenXml Products.Archetypes Products.CMFCore
%py_requires Products.PortalTransforms Products.MimetypesRegistry
%py_requires plone.app.upgrade zope.interface zope.contenttype

%description
An Archetype field that manages file attachments, to be used in place
of a FileField.

AttachmentField allows you to index and preview various kinds of
documents, such as MSOffice (Word, Excel, Powerpoint), PDF and more in
your Archetypes based content types.

%prep
%setup

%build
%python_build_debug

%install
rm -f Products/AttachmentField/converters/MSWord/win32/bin/*
install -d %buildroot%python_sitelibdir/Products
cp -fR Products/AttachmentField %buildroot%python_sitelibdir/Products/
cp -fR *.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.6-alt1.git20120911
- Initial build for Sisyphus

