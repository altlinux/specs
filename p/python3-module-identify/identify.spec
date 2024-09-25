%define  oname identify

%def_with check

Name:    python3-module-%oname
Version: 2.6.1
Release: alt1

Summary: File identification library for Python

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/identify
VCS:     https://github.com/pre-commit/identify

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source:  %name-%version.tar

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-covdefaults
BuildRequires: python3-module-ukkonen
BuildRequires: python3-module-cffi
%endif

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc LICENSE *.md
%_bindir/identify-cli
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed Sep 25 2024 Grigory Ustinov <grenka@altlinux.org> 2.6.1-alt1
- Automatically updated to 2.6.1.

* Mon Jul 08 2024 Grigory Ustinov <grenka@altlinux.org> 2.6.0-alt1
- Automatically updated to 2.6.0.

* Mon Apr 22 2024 Grigory Ustinov <grenka@altlinux.org> 2.5.36-alt1
- Automatically updated to 2.5.36.

* Mon Feb 26 2024 Grigory Ustinov <grenka@altlinux.org> 2.5.35-alt1
- Automatically updated to 2.5.35.

* Mon Dec 25 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.33-alt1
- Automatically updated to 2.5.33.

* Mon Oct 30 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.31-alt1
- Automatically updated to 2.5.31.

* Mon Oct 02 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.30-alt1
- Automatically updated to 2.5.30.

* Mon Sep 18 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.29-alt1
- Automatically updated to 2.5.29.

* Tue Sep 12 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.28-alt1
- Automatically updated to 2.5.28.

* Tue Aug 22 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.27-alt1
- Automatically updated to 2.5.27.

* Mon Jul 24 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.26-alt1
- Automatically updated to 2.5.26.

* Thu Jul 20 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.25-alt1
- Automatically updated to 2.5.25.

* Fri May 05 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.24-alt1
- Automatically updated to 2.5.24.

* Wed Apr 26 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.23-alt1
- Automatically updated to 2.5.23.

* Sun Mar 26 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.22-alt1
- Automatically updated to 2.5.22.

* Fri Mar 17 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.21-alt1
- Automatically updated to 2.5.21.

* Mon Mar 13 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.20-alt1
- Automatically updated to 2.5.20.

* Thu Mar 09 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.19-alt1
- Automatically updated to 2.5.19.

* Tue Feb 14 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.18-alt1
- Automatically updated to 2.5.18.

* Tue Feb 07 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.17-alt1
- Automatically updated to 2.5.17.

* Wed Jan 25 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.15-alt1
- Automatically updated to 2.5.15.

* Thu Jan 12 2023 Grigory Ustinov <grenka@altlinux.org> 2.5.13-alt1
- Automatically updated to 2.5.13.

* Thu Dec 22 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.11-alt1
- Automatically updated to 2.5.11.

* Mon Dec 19 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.10-alt1
- Automatically updated to 2.5.10.

* Wed Nov 30 2022 Grigory Ustinov <grenka@altlinux.org> 2.5.9-alt1
- Automatically updated to 2.5.9.
- Build with check.

* Thu Nov 26 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.10-alt1
- Automatically updated to 1.5.10.

* Sun Nov 08 2020 Grigory Ustinov <grenka@altlinux.org> 1.5.9-alt1
- Initial build for Sisyphus.
