%define oname Products.flickrgallery
Name: python-module-%oname
Version: 1.1.1
Release: alt2.git20141205
Summary: A Gallery product for Plone, powered by Flickr
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.flickrgallery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.flickrgallery.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-flickrapi
BuildPreReq: python-module-Products.DataGridField
BuildPreReq: python-module-collective.colorbox
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.DataGridField collective.colorbox flickrapi
%py_requires Products.CMFPlone Products.Archetypes Products.GenericSetup
%py_requires Products.ATContentTypes Products.CMFCore zope.interface

%description
A photogallery product which loads images from flickr It includes a
portlet which can be used to filter galleries by keyword.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing
%add_python_req_skip flickrengine flickrlib

%description tests
A photogallery product which loads images from flickr It includes a
portlet which can be used to filter galleries by keyword.

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

# It is the file in the package whose name matches the format emacs or vim uses 
# for backup and autosave files. It may have been installed by  accident.
find $RPM_BUILD_ROOT \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete
# failsafe cleanup if the file is declared as %%doc
find . \( -name '.*.swp' -o -name '#*#' -o -name '*~' \) -print -delete

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/*/*/*test*.py*

%files tests
%python_sitelibdir/Products/*/*/*/*test*.py*

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2.git20141205
- Applied python-module-Products.flickrgallery-1.1.1-alt1.git20141205.diff

* Tue Dec 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20141205
- Initial build for Sisyphus

