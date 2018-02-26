%define oname django-classy-tags
Name: python-module-%oname
Version: 0.3.4.1
Release: alt1
Summary: Class based template tags for Django
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/django-classy-tags/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

Source: %oname-%version.tar

BuildPreReq: python-devel python-module-setuptools

%description
Class based template tags for Django.

%package tests
Summary: tests for Django classytags
Group: Development/Python
Requires: %name = %version-%release

%description tests
Class based template tags for Django.

This package contains tests for Django classytags.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/classytags/test*

%files tests
%python_sitelibdir/classytags/test*

%changelog
* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4.1-alt1
- Version 0.3.4.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3.1-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3.1-alt1
- Version 0.3.3.1

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

