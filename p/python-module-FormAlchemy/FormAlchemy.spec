%define oname FormAlchemy

%def_with python3

Name: python-module-%oname
Version: 1.5.3
Release: alt2.1
Summary: Greatly speeds development with SQLAlchemy mapped classes in a HTML forms environment
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/FormAlchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools python-module-six
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools python3-module-six
%endif

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

%package -n python3-module-%oname
Summary: Greatly speeds development with SQLAlchemy mapped classes in a HTML forms environment
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
FormAlchemy eliminates boilerplate by autogenerating HTML input fields
from a given model. FormAlchemy will try to figure out what kind of HTML
code should be returned by introspecting the model's properties and
generate ready-to-use HTML code that will fit the developer's
application.

Of course, FormAlchemy can't figure out everything, i.e, the developer
might want to display only a few columns from the given model. Thus,
FormAlchemy is also highly customizable.

%package -n python3-module-%oname-tests
Summary: Tests for FormAlchemy
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
FormAlchemy eliminates boilerplate by autogenerating HTML input fields
from a given model. FormAlchemy will try to figure out what kind of HTML
code should be returned by introspecting the model's properties and
generate ready-to-use HTML code that will fit the developer's
application.

Of course, FormAlchemy can't figure out everything, i.e, the developer
might want to display only a few columns from the given model. Thus,
FormAlchemy is also highly customizable.

This package contains tests for FormAlchemy.

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

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export LC_ALL=en_US.UTF-8

%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt docs
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.3-alt2
- Added module for Python 3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.3-alt1
- Version 1.5.3

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1
- Version 1.4.3

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.2-alt1
- Version 1.4.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1
- Initial build for Sisyphus

