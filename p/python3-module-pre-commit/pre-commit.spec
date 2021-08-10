%define  modulename pre-commit

Name:    python3-module-%modulename
Version: 2.14.0
Release: alt1

Summary: A framework for managing and maintaining multi-language pre-commit hooks.

License: MIT
Group:   Development/Python3
URL:     https://github.com/pre-commit/pre-commit

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
%doc *.md
%_bindir/*
%python3_sitelibdir/pre_commit
%python3_sitelibdir/*.egg-info

%changelog
* Tue Aug 10 2021 Grigory Ustinov <grenka@altlinux.org> 2.14.0-alt1
- Automatically updated to 2.14.0.

* Sat May 29 2021 Grigory Ustinov <grenka@altlinux.org> 2.13.0-alt1
- Automatically updated to 2.13.0.

* Wed Apr 21 2021 Grigory Ustinov <grenka@altlinux.org> 2.12.1-alt1
- Automatically updated to 2.12.1.

* Wed Mar 17 2021 Grigory Ustinov <grenka@altlinux.org> 2.11.1-alt1
- Automatically updated to 2.11.1.

* Mon Mar 01 2021 Grigory Ustinov <grenka@altlinux.org> 2.10.1-alt1
- Automatically updated to 2.10.1.

* Fri Dec 11 2020 Grigory Ustinov <grenka@altlinux.org> 2.9.3-alt1
- Automatically updated to 2.9.3.

* Tue Dec 01 2020 Grigory Ustinov <grenka@altlinux.org> 2.9.2-alt1
- Automatically updated to 2.9.2.

* Sun Nov 08 2020 Grigory Ustinov <grenka@altlinux.org> 2.8.2-alt1
- Initial build for Sisyphus.
