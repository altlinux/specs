%define oname appier_extras

Name: python3-module-%oname
Version: 0.19.4
Release: alt2

Summary: Appier Framework Extra Elements

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/appier_extras/

# Source-url: https://pypi.io/packages/source/a/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
Set of extra elements for Appier Framework infra-structure.

%prep
%setup

%build
%python3_build

%install
%python3_install
rm -rf %_bindir/markdown

%files
%python3_sitelibdir/*

%changelog
* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 0.19.4-alt2
- Rename package, spec cleanup.

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

