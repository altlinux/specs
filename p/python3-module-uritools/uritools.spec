%define  oname uritools

%def_with check

Name:    python3-module-%oname
Version: 6.0.1
Release: alt1

Summary: URI parsing, classification and composition

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/uritools
VCS:     https://github.com/tkem/uritools

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

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
%pyproject_run_pytest

%files
%doc LICENSE *.rst
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Tue Jan 27 2026 Grigory Ustinov <grenka@altlinux.org> 6.0.1-alt1
- Automatically updated to 6.0.1.

* Tue May 06 2025 Grigory Ustinov <grenka@altlinux.org> 5.0.0-alt1
- Automatically updated to 5.0.0.

* Wed May 29 2024 Grigory Ustinov <grenka@altlinux.org> 4.0.3-alt1
- Automatically updated to 4.0.3.

* Mon Sep 11 2023 Grigory Ustinov <grenka@altlinux.org> 4.0.2-alt1
- Automatically updated to 4.0.2.

* Mon Jan 09 2023 Grigory Ustinov <grenka@altlinux.org> 4.0.1-alt1
- Automatically updated to 4.0.1.

* Tue Jun 28 2022 Grigory Ustinov <grenka@altlinux.org> 4.0.0-alt1
- Initial build for Sisyphus.
