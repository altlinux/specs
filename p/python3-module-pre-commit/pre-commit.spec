%define oname pre-commit

Name:    python3-module-%oname
Version: 3.8.0
Release: alt1

Summary: A framework for managing and maintaining multi-language pre-commit hooks

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/pre-commit
VCS:     https://github.com/pre-commit/pre-commit

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source:  %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# tests need lots of network, git and other stuff

%files
%doc LICENSE *.md
%_bindir/%oname
%python3_sitelibdir/pre_commit
%python3_sitelibdir/pre_commit-%version.dist-info

%changelog
* Mon Jul 29 2024 Grigory Ustinov <grenka@altlinux.org> 3.8.0-alt1
- Automatically updated to 3.8.0.

* Sun May 12 2024 Grigory Ustinov <grenka@altlinux.org> 3.7.1-alt1
- Automatically updated to 3.7.1.

* Mon Mar 25 2024 Grigory Ustinov <grenka@altlinux.org> 3.7.0-alt1
- Automatically updated to 3.7.0.

* Mon Feb 26 2024 Grigory Ustinov <grenka@altlinux.org> 3.6.2-alt1
- Automatically updated to 3.6.2.

* Tue Jan 23 2024 Grigory Ustinov <grenka@altlinux.org> 3.6.0-alt1
- Automatically updated to 3.6.0.

* Sat Oct 21 2023 Grigory Ustinov <grenka@altlinux.org> 3.5.0-alt1
- Automatically updated to 3.5.0.

* Mon Sep 04 2023 Grigory Ustinov <grenka@altlinux.org> 3.4.0-alt1
- Automatically updated to 3.4.0.

* Wed Jun 14 2023 Grigory Ustinov <grenka@altlinux.org> 3.3.3-alt1
- Automatically updated to 3.3.3.

* Thu May 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.3.2-alt1
- Automatically updated to 3.3.2.

* Wed May 03 2023 Grigory Ustinov <grenka@altlinux.org> 3.3.1-alt1
- Automatically updated to 3.3.1.

* Fri Apr 21 2023 Grigory Ustinov <grenka@altlinux.org> 3.2.2-alt1
- New version 3.2.2.

* Sun Mar 26 2023 Grigory Ustinov <grenka@altlinux.org> 3.2.1-alt1
- Automatically updated to 3.2.1.

* Sat Mar 18 2023 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt1
- Automatically updated to 3.2.0.

* Tue Feb 28 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Automatically updated to 3.1.1.

* Fri Feb 24 2023 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.

* Sun Feb 05 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.4-alt1
- Automatically updated to 3.0.4.

* Fri Jan 27 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt1
- Automatically updated to 3.0.1.

* Wed Jan 25 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.0-alt1
- Automatically updated to 3.0.0.

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
