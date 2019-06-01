%define oname appier_extras

Name: python-module-%oname
Version: 0.19.4
Release: alt1

Summary: Appier Framework Extra Elements

License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/appier_extras/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: https://pypi.io/packages/source/a/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%description
Set of extra elements for Appier Framework infra-structure.

%package -n python3-module-%oname
Summary: Appier Framework Extra Elements
Group: Development/Python3

%description -n python3-module-%oname
Set of extra elements for Appier Framework infra-structure.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
rm -rf %_bindir/markdown

%files -n python3-module-%oname
%python3_sitelibdir/*

%changelog
* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 0.19.4-alt1
- new version 0.19.4 (with rpmrb script)
- python3 only

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.11-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.4-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.4-alt1
- Version 0.3.4

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.19-alt1
- Initial build for Sisyphus

