Name: python3-module-certifi
Version: 2024.8.30
Release: alt1

Summary: Python package for providing Mozilla's CA Bundle
License: MPL-2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/certifi/

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
This installable Python package contains a CA Bundle that you can
reference in your Python code. This is useful for verifying HTTP
requests, for example.

This is the same CA Bundle which ships with the Requests codebase, and
is derived from Mozilla Firefox's canonical set.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE *.rst
%python3_sitelibdir/certifi
%python3_sitelibdir/certifi-%version.dist-info

%changelog
* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.8.30-alt1
- 2024.8.30 released

* Thu Jun 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.5.7-alt1
- 2023.5.7 released

* Tue Oct 05 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2021.5.30-alt1
- 2021.5.30 released

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 2020.12.5-alt2
- Drop python2 support.

* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.12.5-alt1
- 2020.12.5 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 2020.6.20-alt1
- 2020.6.20 released

* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 2019.11.28-alt1
- 2019.11.28 released

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 2016.9.26-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2015.04.28-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2015.04.28-alt1
- Version 2015.04.28

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.05.14-alt1
- Initial build for Sisyphus

