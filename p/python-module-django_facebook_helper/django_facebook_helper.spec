%define oname django_facebook_helper

%def_with python3

Name: python-module-%oname
Version: 0.3.7
Release: alt1.1
Summary: A Django application for helping in facebook login an managing
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django_facebook_helper/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
A Django application for helping in facebook login an managing.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A Django application for helping in facebook login an managing.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A Django application for helping in facebook login an managing
Group: Development/Python3

%description -n python3-module-%oname
A Django application for helping in facebook login an managing.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A Django application for helping in facebook login an managing.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
export LC_ALL=en_US.UTF-8

%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%files
%python_sitelibdir/%{oname}*
%exclude %python_sitelibdir/%oname/tests.py*

%files tests
%python_sitelibdir/%oname/tests.py*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%{oname}*
%exclude %python3_sitelibdir/%oname/tests.py
%exclude %python3_sitelibdir/%oname/__pycache__/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests.py
%python3_sitelibdir/%oname/__pycache__/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.7-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Sep 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.7-alt1
- Initial build for Sisyphus

