%global pypi_name iso8601

%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1

Summary: Simple module to parse ISO 8601 dates

Group: Development/Python3
License: MIT
URL: https://pypi.org/project/iso8601
VCS: https://github.com/micktwomey/pyiso8601

Source0: %name-%version.tar

BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-poetry

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-hypothesis
%endif

BuildArch: noarch

%description
This module parses the most common forms of ISO 8601 date strings (e.g.
2007-01-14T20:34:22+00:00) into datetime objects.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.rst
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info/
%exclude %python3_sitelibdir/%pypi_name/test_iso8601.py
%exclude %python3_sitelibdir/%pypi_name/__pycache__/test_iso8601.cpython*

%changelog
* Fri Jan 31 2025 Grigory Ustinov <grenka@altlinux.org> 2.1.0-alt1
- Automatically updated to 2.1.0.

* Sun Jan 28 2024 Grigory Ustinov <grenka@altlinux.org> 0.1.16-alt2
- Moved on modern pyproject macros.

* Thu Jul 22 2021 Stanislav Levin <slev@altlinux.org> 0.1.16-alt1
- 0.1.11 -> 0.1.16.
- Enabled testing.

* Mon Oct 17 2016 Alexey Shabalin <shaba@altlinux.ru> 0.1.11-alt1
- 0.1.11

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.10-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 29 2014 Lenar Shakirov <snejok@altlinux.ru> 0.1.10-alt1
- 0.1.10
- Enable python3

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.1.4-alt1
- Initial release for Sisyphus (based on Fedora)
