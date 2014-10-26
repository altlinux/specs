%define oname Products.ATReferenceBrowserWidget
Name: python-module-%oname
Version: 3.0.1
Release: alt1.git20120103
Summary: ATReferenceBrowserWidget is reference widget for Archetypes
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ATReferenceBrowserWidget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.ATReferenceBrowserWidget.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-archetypes.referencebrowserwidget
BuildPreReq: python-module-zope.deprecation
BuildPreReq: python-module-unittest2

%py_provides %oname
Requires: python-module-Zope2
%py_requires archetypes.referencebrowserwidget zope.deprecation

%description
ATReferenceBrowserWidget is an add-on to Archtetypes. It adds a new
reference widget that allows you to search or browse the portal when
creating references. This new widget inherits from the standard
reference widget so you can use all it's properties.

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
%python_sitelibdir/*

%changelog
* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.git20120103
- Initial build for Sisyphus

