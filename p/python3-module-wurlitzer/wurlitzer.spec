%define pypi_name wurlitzer

%def_with check

Name:    python3-module-%pypi_name
Version: 3.1.1
Release: alt1

Summary: Capture C-level stdout/stderr in Python
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/wurlitzer
VCS:     https://github.com/minrk/wurlitzer

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: /proc
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
%summary.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
py.test-3 test.py

%files
%doc LICENSE *.md
%python3_sitelibdir/%pypi_name.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Tue Jun 25 2024 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Automatically updated to 3.1.1.

* Tue Apr 30 2024 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- Automatically updated to 3.1.0.

* Tue Jun 13 2023 Grigory Ustinov <grenka@altlinux.org> 3.0.3-alt1
- Initial build for Sisyphus.
