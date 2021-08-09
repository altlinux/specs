%define  modulename faker

Name:    python3-module-%modulename
Version: 8.11.0
Release: alt1

Summary: Faker is a Python package that generates fake data for you.
License: MIT
Group:   Development/Python3
URL:     https://github.com/joke2k/faker

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

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

%files
%_bindir/%modulename
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%doc *.md

%changelog
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
