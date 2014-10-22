%define oname Products.AddRemoveWidget
Name: python-module-%oname
Version: 1.5.2
Release: alt1.dev0.git20131031
Summary: AddRemoveWidget + ComboBoxWidget for Plone
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.AddRemoveWidget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.AddRemoveWidget.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Archetypes python-module-nose
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
%py_requires Products.Archetypes Products.CMFCore

%description
This is a replacement for KeywordWidget which permits you to add items
from a vocabulary (and optionally new items) using a pair of selection
boxes with "add" and "remove" buttons to transfer items between them. It
overlaps in functionality with InAndOutWidget, but does not suffer from
InAndOut's requirement for all items in the "target" list to be
selection upon form submission. I believe InAndOut does not allow
textual items to be added by the user, though it does support adding of
referenced objects, which AddRemove does not. You are advised to test
both to find out which one is more suitable for your needs.

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
nosetests

%files
%doc *.rst docs/*
%python_sitelibdir/*

%changelog
* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.dev0.git20131031
- Initial build for Sisyphus

