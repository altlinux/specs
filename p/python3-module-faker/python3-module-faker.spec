%define  modulename faker
# https://github.com/joke2k/faker/issues/1575
%def_without check

Name:    python3-module-%modulename
Version: 13.3.4
Release: alt1

Summary: Faker is a Python package that generates fake data for you.
License: MIT
Group:   Development/Python3
URL:     https://github.com/joke2k/faker

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-text-unidecode
BuildRequires: python3-module-validators
BuildRequires: python3-module-freezegun
BuildRequires: python3-module-random2
%endif

BuildArch: noarch

Source:  %modulename-%version.tar

%description
%summary

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install

%check
# Exclude tests that require the faker.sphinx module
py.test3 --ignore-glob='tests/sphinx/*'

%files
%_bindir/%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
* Thu Apr 14 2022 Grigory Ustinov <grenka@altlinux.org> 13.3.4-alt1
- Automatically updated to 13.3.4.

* Thu Mar 24 2022 Grigory Ustinov <grenka@altlinux.org> 13.3.3-alt1
- Automatically updated to 13.3.3.

* Tue Mar 15 2022 Grigory Ustinov <grenka@altlinux.org> 13.3.2-alt1
- Automatically updated to 13.3.2.

* Thu Mar 10 2022 Grigory Ustinov <grenka@altlinux.org> 13.3.1-alt1
- Automatically updated to 13.3.1.

* Sat Feb 05 2022 Grigory Ustinov <grenka@altlinux.org> 12.1.0-alt1
- Automatically updated to 12.1.0.

* Mon Jan 17 2022 Grigory Ustinov <grenka@altlinux.org> 11.3.0-alt1
- Automatically updated to 11.3.0.

* Tue Nov 30 2021 Grigory Ustinov <grenka@altlinux.org> 9.9.0-alt1
- Automatically updated to 9.9.0.

* Tue Nov 23 2021 Grigory Ustinov <grenka@altlinux.org> 9.8.3-alt1
- Automatically updated to 9.8.3.

* Tue Oct 12 2021 Grigory Ustinov <grenka@altlinux.org> 9.3.1-alt1
- Automatically updated to 9.3.1.

* Thu Oct 07 2021 Grigory Ustinov <grenka@altlinux.org> 9.0.0-alt1
- Automatically updated to 9.0.0.

* Tue Sep 07 2021 Grigory Ustinov <grenka@altlinux.org> 8.12.1-alt1
- Automatically updated to 8.12.1.

* Mon Aug 09 2021 Grigory Ustinov <grenka@altlinux.org> 8.11.0-alt1
- Automatically updated to 8.11.0.

* Tue Jul 13 2021 Grigory Ustinov <grenka@altlinux.org> 8.10.1-alt1
- Automatically updated to 8.10.1.

* Wed Jul 07 2021 Grigory Ustinov <grenka@altlinux.org> 8.9.1-alt1
- Automatically updated to 8.9.1.

* Thu Jul 01 2021 Grigory Ustinov <grenka@altlinux.org> 8.9.0-alt1
- Automatically updated to 8.9.0.

* Sun Jun 27 2021 Grigory Ustinov <grenka@altlinux.org> 8.8.2-alt1
- Automatically updated to 8.8.2.

* Fri Jun 18 2021 Grigory Ustinov <grenka@altlinux.org> 8.8.1-alt1
- Automatically updated to 8.8.1.

* Sat Jun 05 2021 Grigory Ustinov <grenka@altlinux.org> 8.5.1-alt1
- Automatically updated to 8.5.1.

* Fri May 28 2021 Grigory Ustinov <grenka@altlinux.org> 8.4.0-alt1
- Automatically updated to 8.4.0.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 8.2.1-alt1
- Automatically updated to 8.2.1.

* Sat May 15 2021 Grigory Ustinov <grenka@altlinux.org> 8.1.4-alt1
- Automatically updated to 8.1.4.

* Wed May 12 2021 Grigory Ustinov <grenka@altlinux.org> 8.1.3-alt1
- Automatically updated to 8.1.3.

* Sun May 09 2021 Grigory Ustinov <grenka@altlinux.org> 8.1.2-alt1
- Automatically updated to 8.1.2.

* Mon Apr 26 2021 Grigory Ustinov <grenka@altlinux.org> 8.1.1-alt1
- Automatically updated to 8.1.1.

* Thu Apr 22 2021 Grigory Ustinov <grenka@altlinux.org> 8.1.0-alt1
- Automatically updated to 8.1.0.

* Sat Apr 03 2021 Grigory Ustinov <grenka@altlinux.org> 7.0.1-alt1
- Initial build for Sisyphus.
