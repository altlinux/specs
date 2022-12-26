%define oname pre-commit

Name:    python3-module-%oname
Version: 2.21.0
Release: alt1

Summary: A framework for managing and maintaining multi-language pre-commit hooks.

License: MIT
Group:   Development/Python3
URL:     https://github.com/pre-commit/pre-commit

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
# tests need lots of network, git and other stuff

%files
%doc *.md
%_bindir/%oname
%_bindir/%oname-validate-config
%_bindir/%oname-validate-manifest
%python3_sitelibdir/pre_commit
%python3_sitelibdir/pre_commit-%version-py%_python3_version.egg-info

%changelog
* Mon Dec 26 2022 Grigory Ustinov <grenka@altlinux.org> 2.21.0-alt1
- Automatically updated to 2.21.0.

* Fri Jul 15 2022 Grigory Ustinov <grenka@altlinux.org> 2.20.0-alt1
- Automatically updated to 2.20.0.

* Thu May 12 2022 Grigory Ustinov <grenka@altlinux.org> 2.19.0-alt1
- Automatically updated to 2.19.0.

* Thu Apr 14 2022 Grigory Ustinov <grenka@altlinux.org> 2.18.1-alt1
- Automatically updated to 2.18.1.

* Tue Mar 15 2022 Grigory Ustinov <grenka@altlinux.org> 2.17.0-alt1
- Automatically updated to 2.17.0.

* Tue Sep 07 2021 Grigory Ustinov <grenka@altlinux.org> 2.15.0-alt1
- Automatically updated to 2.15.0.

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
