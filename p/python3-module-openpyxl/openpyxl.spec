%define oname openpyxl

Name:    python3-module-%oname
Version: 3.1.3
Release: alt1

Summary: A Python library to read/write Excel 2010 xlsx/xlsm files

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/openpyxl

Source: %name-%version.tar

BuildArch: noarch

%py3_requires et_xmlfile
%py3_provides %oname

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
openpyxl is a Python library to read/write Excel 2010 xlsx/xlsm files.

It was born from lack of existing library to read/write natively from
Python the Office Open XML format.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENCE.rst README.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sun Jun 02 2024 Grigory Ustinov <grenka@altlinux.org> 3.1.3-alt1
- Build new version.

* Tue Dec 26 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.2-alt1
- Build new version.

* Mon Jan 09 2023 Anton Vyatkin <toni@altlinux.org> 3.0.10-alt1
- new version 3.0.10

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 2.6.2-alt3
- Fixed FTBFS.

* Thu Sep 17 2020 Grigory Ustinov <grenka@altlinux.org> 2.6.2-alt2
- Drop python2 support.

* Mon Aug 26 2019 Georgy A Bystrenin <gkot@altlinux.org> 2.6.2-alt1
- New version 2.6.2
- Add test
- Fix spec for a new way to run test

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.4.1-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 07 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4.1-alt2
- Updated build dependencies.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1
- automated PyPI update

* Wed Jun 08 2016 Andrey Cherepanov <cas@altlinux.org> 2.3.5-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3.0-alt1.b1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.3.0-alt1.b1.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.b1
- Version 2.3.0-b1

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.4-alt1
- Initial build for Sisyphus

