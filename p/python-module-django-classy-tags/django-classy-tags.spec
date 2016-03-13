%define oname django-classy-tags

%def_with python3

Name: python-module-%oname
Version: 0.5.1
Release: alt2.1
Summary: Class based template tags for Django
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/django-classy-tags/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch

Source: %oname-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Class based template tags for Django.

%package -n python3-module-%oname
Summary: Class based template tags for Django
Group: Development/Python3

%description -n python3-module-%oname
Class based template tags for Django.

%package -n python3-module-%oname-tests
Summary: tests for Django classytags
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Class based template tags for Django.

This package contains tests for Django classytags.

%package tests
Summary: tests for Django classytags
Group: Development/Python
Requires: %name = %version-%release

%description tests
Class based template tags for Django.

This package contains tests for Django classytags.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/*
%exclude %python_sitelibdir/classytags/test*

%files tests
%python_sitelibdir/classytags/test*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/classytags/test*
%exclude %python3_sitelibdir/classytags/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/classytags/test*
%python3_sitelibdir/classytags/*/test*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2
- Added module for Python 3

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1
- Version 0.5.1

* Wed Feb 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4

* Fri Dec 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4.1-alt1
- Version 0.3.4.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.3.1-alt1.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3.1-alt1
- Version 0.3.3.1

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

