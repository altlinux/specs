%define _unpackaged_files_terminate_build 1
%define oname dnslib

%def_with python3

Name: python-module-%oname
Version: 0.9.6
Release: alt1
Summary: Simple library to encode/decode DNS wire-format packets
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/dnslib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/d2/49/d9430826e6678cab9675e343c795e3e0c3ca568b9dfcc145b5d5490c3b17/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
A library to encode/decode DNS wire-format packets supporting both
Python 2.7 and Python 3.2+.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
A library to encode/decode DNS wire-format packets supporting both
Python 2.7 and Python 3.2+.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Simple library to encode/decode DNS wire-format packets
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A library to encode/decode DNS wire-format packets supporting both
Python 2.7 and Python 3.2+.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
A library to encode/decode DNS wire-format packets supporting both
Python 2.7 and Python 3.2+.

This package contains tests for %oname.
%endif

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

%check
python setup.py test -v
VERSIONS=python ./run_tests.sh -v
%if_with python3
pushd ../python3
python3 setup.py test -v
VERSIONS=python3 ./run_tests.sh -v
popd
%endif

%files
%doc README*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%if_with python3
%files -n python3-module-%oname
%doc README*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test*
%exclude %python3_sitelibdir/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test*
%python3_sitelibdir/*/*/test*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.6-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1
- Initial build for Sisyphus

