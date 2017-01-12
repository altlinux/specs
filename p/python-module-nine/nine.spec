%define _unpackaged_files_terminate_build 1
%define oname nine

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1
Summary: Python 2 / 3 compatibility, like six, but favouring Python 3
License: Public Domain
Group: Development/Python
Url: https://pypi.python.org/pypi/nine
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/31/0b/b86e3453dd85bf48eda37f842c91bc6f5ce2d5ffc451b6a88039340ed262/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Python 2 and 3 compatibility library, such that your code looks more
like Python 3.

%package -n python3-module-%oname
Summary: Python 2 / 3 compatibility, like six, but favouring Python 3
Group: Development/Python3

%description -n python3-module-%oname
Python 2 and 3 compatibility library, such that your code looks more
like Python 3.

%package -n python3-module-%oname-test
Summary: Test for nine
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-test
Python 2 and 3 compatibility library, such that your code looks more
like Python 3.

This package contains test for nine.

%package test
Summary: Test for nine
Group: Development/Python
Requires: %name = %EVR

%description test
Python 2 and 3 compatibility library, such that your code looks more
like Python 3.

This package contains test for nine.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files test
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-test
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.3-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt2
- Added module for Python 3

* Tue Sep 17 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus

