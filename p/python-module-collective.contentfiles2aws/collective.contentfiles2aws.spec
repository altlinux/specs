%define mname collective
%define oname %mname.contentfiles2aws
Name: python-module-%oname
Version: 1.3.0
Release: alt1.git20141212
Summary: Amazon S3 (AWS) storage for Plone content files
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.contentfiles2aws/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/martinschoel/collective.contentfiles2aws.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-boto
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.validation
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname boto Products.CMFCore Products.Archetypes plone.i18n
%py_requires Products.validation Products.ATContentTypes plone.indexer
%py_requires Products.statusmessages zope.component zope.interface
%py_requires zope.annotation zope.app.component zope.i18nmessageid

%description
The main purpose of the package to move content images and files to
amazon CDN, that allows to serve content to end users with high
performance and high availability. The package contains two content
types: AWSFile and AWSImage which work similar to the default Plone
ones. The main difference is that they store their content on amazon
simple storage instead of a Plone site. Also, the package contains a
patch for default content types like Image, File, and News Item.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
The main purpose of the package to move content images and files to
amazon CDN, that allows to serve content to end users with high
performance and high availability. The package contains two content
types: AWSFile and AWSImage which work similar to the default Plone
ones. The main difference is that they store their content on amazon
simple storage instead of a Plone site. Also, the package contains a
patch for default content types like Image, File, and News Item.

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
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20141212
- Initial build for Sisyphus

