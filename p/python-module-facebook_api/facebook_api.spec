%define oname facebook_api

Name: python-module-%oname
Version: 0.1.10
Release: alt1

Summary: Facebook API

License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/facebook_api/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: https://pypi.io/packages/source/f/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description
Facebook API.

%package -n python3-module-%oname
Summary: Facebook API
Group: Development/Python3

%description -n python3-module-%oname
Facebook API.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files -n python3-module-%oname
%python3_sitelibdir/*

%changelog
* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.1.10-alt1
- new version 0.1.10 (with rpmrb script)
- python3 only

* Tue Apr 30 2019 Grigory Ustinov <grenka@altlinux.org> 0.1.4-alt1.2
- Rebuild with python3.7.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1
- Initial build for Sisyphus

