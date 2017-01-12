%define _unpackaged_files_terminate_build 1
%define oname django-dfp

%def_with python3

Name: python-module-%oname
Version: 0.4.1
Release: alt1
Summary: DFP implementation for Django
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-dfp/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/praekelt/django-dfp.git
Source0: https://pypi.python.org/packages/e5/7b/dcce10c6192402aed8e0907b1f5e8b69d007066768d9c45085c9ce95f8cf/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
App that provides tags to fetch Google DFP ads.

%package -n python3-module-%oname
Summary: DFP implementation for Django
Group: Development/Python3

%description -n python3-module-%oname
App that provides tags to fetch Google DFP ads.

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

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20140721.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20140721
- Initial build for Sisyphus

