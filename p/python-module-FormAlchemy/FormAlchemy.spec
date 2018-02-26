%define oname FormAlchemy
Name: python-module-%oname
Version: 1.4.2
Release: alt1
Summary: Greatly speeds development with SQLAlchemy mapped classes in a HTML forms environment
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/FormAlchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_provides %oname

%description
FormAlchemy eliminates boilerplate by autogenerating HTML input fields
from a given model. FormAlchemy will try to figure out what kind of HTML
code should be returned by introspecting the model's properties and
generate ready-to-use HTML code that will fit the developer's
application.

Of course, FormAlchemy can't figure out everything, i.e, the developer
might want to display only a few columns from the given model. Thus,
FormAlchemy is also highly customizable.

%package tests
Summary: Tests for FormAlchemy
Group: Development/Python
Requires: %name = %version-%release

%description tests
FormAlchemy eliminates boilerplate by autogenerating HTML input fields
from a given model. FormAlchemy will try to figure out what kind of HTML
code should be returned by introspecting the model's properties and
generate ready-to-use HTML code that will fit the developer's
application.

Of course, FormAlchemy can't figure out everything, i.e, the developer
might want to display only a few columns from the given model. Thus,
FormAlchemy is also highly customizable.

This package contains tests for FormAlchemy.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt docs
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1
- Version 1.4.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

