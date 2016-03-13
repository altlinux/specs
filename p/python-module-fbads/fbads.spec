%define oname fbads

%def_with python3

Name: python-module-%oname
Version: 0.3.6
Release: alt1.1
Summary: Python client for the Facebook Ads API
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/fbads/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Python client for the Facebook Ads API. Works with the new ads schema
(ad sets). Under development!

%package -n python3-module-%oname
Summary: Python client for the Facebook Ads API
Group: Development/Python3

%description -n python3-module-%oname
Python client for the Facebook Ads API. Works with the new ads schema
(ad sets). Under development!

%prep
%setup

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
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.6-alt1
- Initial build for Sisyphus

