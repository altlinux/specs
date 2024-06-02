%define _unpackaged_files_terminate_build 1
%define oname appier

Name: python3-module-%oname
Version: 1.34.2
Release: alt1

Summary: Appier Framework

License: Apache-2.0
Group: Development/Python3
URL: https://pypi.python.org/pypi/appier
VCS: https://github.com/hivesolutions/appier

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
Simple WSGI based framework for easy REST API creation. It aims at
creating simple infra-structure for the consulting work that is being
developed by the Hive Solutions team.

%package tests
Summary: Tests for Appier Framework
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description tests
Simple WSGI based framework for easy REST API creation. It aims at
creating simple infra-structure for the consulting work that is being
developed by the Hive Solutions team.

This package contains tests for Appier Framework.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.rst *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info
%exclude %python3_sitelibdir/*/test

%files tests
%python3_sitelibdir/*/test

%changelog
* Sun Jun 02 2024 Grigory Ustinov <grenka@altlinux.org> 1.34.2-alt1
- Automatically updated to 1.34.2.

* Sat Jun 01 2024 Grigory Ustinov <grenka@altlinux.org> 1.34.0-alt1
- Automatically updated to 1.34.0.

* Wed May 29 2024 Grigory Ustinov <grenka@altlinux.org> 1.33.5-alt1
- Automatically updated to 1.33.5.

* Fri May 10 2024 Grigory Ustinov <grenka@altlinux.org> 1.33.4-alt1
- Automatically updated to 1.33.4.

* Thu May 02 2024 Grigory Ustinov <grenka@altlinux.org> 1.33.3-alt1
- Automatically updated to 1.33.3.

* Mon Apr 22 2024 Grigory Ustinov <grenka@altlinux.org> 1.33.2-alt1
- Automatically updated to 1.33.2.

* Sun Apr 14 2024 Grigory Ustinov <grenka@altlinux.org> 1.33.0-alt1
- Automatically updated to 1.33.0.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 1.32.0-alt1
- Automatically updated to 1.32.0.

* Mon Jan 08 2024 Grigory Ustinov <grenka@altlinux.org> 1.31.5-alt1
- Automatically updated to 1.31.5.

* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 1.31.4-alt1
- Automatically updated to 1.31.4.

* Thu Jul 20 2023 Grigory Ustinov <grenka@altlinux.org> 1.31.2-alt1
- Automatically updated to 1.31.2.

* Sun Jun 11 2023 Grigory Ustinov <grenka@altlinux.org> 1.31.1-alt1
- Automatically updated to 1.31.1.

* Wed May 17 2023 Grigory Ustinov <grenka@altlinux.org> 1.30.1-alt1
- Build new version.

* Tue Jul 27 2021 Grigory Ustinov <grenka@altlinux.org> 1.18.25-alt2
- Rename package, spec cleanup.

* Sat Jun 01 2019 Vitaly Lipatov <lav@altlinux.ru> 1.18.25-alt1
- new version 1.18.25 (with rpmrb script)
- python3 only (uses yield from)

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1
- automated PyPI update

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.1-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.0-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.11-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.25-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.25-alt1
- Version 0.8.25

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.19-alt1
- Version 0.8.19

* Mon Sep 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.15-alt1
- Initial build for Sisyphus

