%define oname Products.AutocompleteWidget
Name: python-module-%oname
Version: 1.4.0
Release: alt1.git20140915
Summary: Archetypes autocomplete widget with support for String-, Lines- and ReferenceFields
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.AutocompleteWidget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.AutocompleteWidget.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.Archetypes Products.CMFPlone

%description
Archetypes autocomplete widget with support for String-, Lines- and
ReferenceFields.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/Products
cp -fR Products/AutocompleteWidget \
	%buildroot%python_sitelibdir/Products/
cp -fR *.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info

%changelog
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.0-alt1.git20140915
- Initial build for Sisyphus

