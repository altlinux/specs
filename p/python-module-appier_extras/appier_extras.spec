%define oname appier_extras

%def_with python3

Name: python-module-%oname
Version: 0.8.11
Release: alt1
Summary: Appier Framework Extra Elements
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/appier_extras/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/5e/75/363964c18cc4c1f41f44a6b76b100bcb20c5145ffc4396b2f786faece696/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Set of extra elements for Appier Framework infra-structure.

%package -n python3-module-%oname
Summary: Appier Framework Extra Elements
Group: Development/Python3

%description -n python3-module-%oname
Set of extra elements for Appier Framework infra-structure.

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
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.11-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Version 0.3.4

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.19-alt1
- Initial build for Sisyphus

