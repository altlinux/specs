%define oname appier_extras

Name: python3-module-%oname
Version: 0.26.0
Release: alt1

Summary: Appier Framework Extra Elements

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.python.org/pypi/appier_extras
VCS: https://github.com/hivesolutions/appier-extras

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Set of extra elements for Appier Framework infra-structure.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%_bindir/markdown

%files
%doc *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Thu May 23 2024 Grigory Ustinov <grenka@altlinux.org> 0.26.0-alt1
- Automatically updated to 0.26.0.

* Tue Feb 06 2024 Grigory Ustinov <grenka@altlinux.org> 0.25.1-alt1
- Automatically updated to 0.25.1.

* Mon Jan 08 2024 Grigory Ustinov <grenka@altlinux.org> 0.25.0-alt1
- Automatically updated to 0.25.0.

* Wed May 17 2023 Grigory Ustinov <grenka@altlinux.org> 0.24.9-alt1
- Build new version.

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

