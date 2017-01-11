%define _unpackaged_files_terminate_build 1
%define oname jellyfish

%def_with python3

Name: python-module-%oname
Version: 0.5.6
Release: alt1
Summary: A library for doing approximate and phonetic matching of strings
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jellyfish/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/sunlightlabs/jellyfish.git
Source0: https://pypi.python.org/packages/94/48/ddb1458d966f0a84e472d059d87a9d1527df7768a725132fc1d810728386/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Jellyfish is a python library for doing approximate and phonetic
matching of strings.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Jellyfish is a python library for doing approximate and phonetic
matching of strings.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: A library for doing approximate and phonetic matching of strings
Group: Development/Python3

%description -n python3-module-%oname
Jellyfish is a python library for doing approximate and phonetic
matching of strings.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Jellyfish is a python library for doing approximate and phonetic
matching of strings.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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
%exclude %python_sitelibdir/*/test.*

%files tests
%python_sitelibdir/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/test.*
%exclude %python3_sitelibdir/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/test.*
%python3_sitelibdir/*/*/test.*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.5.6-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20140812.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20140812
- Initial build for Sisyphus

