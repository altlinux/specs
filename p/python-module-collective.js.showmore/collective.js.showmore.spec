%define mname collective.js
%define oname %mname.showmore
Name: python-module-%oname
Version: 1.0
Release: alt1.a4.1
Summary: JS add-on to show/hide parts of a page
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.showmore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools

%py_provides %oname
%py_requires %mname

%description
collective.js.showmore provides a JQuery plugin.

The plugin hides a set of nodes and replaces them with a "Show more..."
link. When the link is clicked, the hidden nodes are made visible again.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
collective.js.showmore provides a JQuery plugin.

The plugin hides a set of nodes and replaces them with a "Show more..."
link. When the link is clicked, the hidden nodes are made visible again.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
install -d %buildroot%python_sitelibdir/collective/js
cp -fR collective/js/showmore \
	%buildroot%python_sitelibdir/collective/js/
cp -fR *.egg-info %buildroot%python_sitelibdir/

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/collective/js/showmore
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/js/showmore/tests

%files tests
%python_sitelibdir/collective/js/showmore/tests

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0-alt1.a4.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a4
- Initial build for Sisyphus

