%define _unpackaged_files_terminate_build 1
%define oname facebook-ads-api

%def_with python3

Name: python-module-%oname
Version: 0.3.0
Release: alt1
Summary: Python client for the Facebook Ads API
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/facebook-ads-api/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/narrowcast/facebook-ads-api.git
Source0: https://pypi.python.org/packages/01/af/d2d7b9e3c07e5a0085f0b4218af1a28db8b52b2b5ba409901c6654296296/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python-tools-2to3
%endif

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python-modules-encodings python-modules-logging python3 python3-base
BuildRequires: python-devel python-tools-2to3 rpm-build-python3 time

%description
Python client for the Facebook Ads API.

%package -n python3-module-%oname
Summary: Python client for the Facebook Ads API
Group: Development/Python3

%description -n python3-module-%oname
Python client for the Facebook Ads API.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.52-alt1.git20141125.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.52-alt1.git20141125.1
- NMU: Use buildreq for BR.

* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.52-alt1.git20141125
- Version 0.1.52

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.51-alt1.git20141024
- Version 0.1.51

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.46-alt1.git20140916
- Initial build for Sisyphus

