%define oname Products.SimpleAttachment
Name: python-module-%oname
Version: 4.4
Release: alt1.dev0.git20131218
Summary: Simple Attachments for Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.SimpleAttachment/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.SimpleAttachment.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-plone.app.blob
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-collective.testcaselayer
BuildPreReq: python-module-Products.RichDocument

%py_provides %oname
Requires: python-module-Zope2
%py_requires archetypes.schemaextender plone.app.blob

%description
Several Plone products have a need to handle simple attachments: content
types that do not have a workflow of their own but will reuse the
permissions on their container. SimpleAttachment implements simple file
and image attachment types that can serve this need.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing collective.testcaselayer Products.RichDocument

%description tests
Several Plone products have a need to handle simple attachments: content
types that do not have a workflow of their own but will reuse the
permissions on their container. SimpleAttachment implements simple file
and image attachment types that can serve this need.

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
%doc *.txt *.md
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4-alt1.dev0.git20131218
- Initial build for Sisyphus

