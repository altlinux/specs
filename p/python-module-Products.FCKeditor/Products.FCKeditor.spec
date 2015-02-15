%define oname Products.FCKeditor
Name: python-module-%oname
Version: 2.6.6.3
Release: alt1
Summary: FCKEditor is an alternate WYSIWYG through-the-web editor for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.FCKeditor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.PloneArticle
BuildPreReq: python-module-Products.PloneExFile
BuildPreReq: python-module-Products.PythonScripts
BuildPreReq: python-module-Products.StandardCacheManagers
BuildPreReq: python-module-Products.PortalTransforms
BuildPreReq: python-module-plone.app.layout

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFPlone Products.Archetypes Products.CMFCore
%py_requires Products.ATContentTypes Products.PloneArticle
%py_requires Products.PloneExFile Products.PythonScripts
%py_requires Products.StandardCacheManagers Products.PortalTransforms
%py_requires plone.app.layout zope.interface
%add_findreq_skiplist %python_sitelibdir/Products/FCKeditor/_src/fckeditor/editor/dialog/fck_spellerpages/spellerpages/server-scripts/spellchecker.pl

%description
FCKEditor is an alternate WYSIWYG through-the-web editor for Plone. It
is offering control over styles, paragraph formatting, fonts, colors,
borders, image flash and file browsing/uploading, with a really good
Plone integration.

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.6.3-alt1
- Initial build for Sisyphus

