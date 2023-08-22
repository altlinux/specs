%def_with check

%define  modulename cfgv

Name:    python3-module-%modulename
Version: 3.4.0
Release: alt1

Summary: Validate configuration and produce human readable error messages

License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/cfgv
VCS:     https://github.com/asottile/cfgv

Packager: Grigory Ustinov <grenka@altlinux.org>

BuildArch: noarch

Source:  %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-coverage
BuildRequires: python3-module-covdefaults
%endif

%description
%summary.

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
%python3_sitelibdir/%modulename.py
%python3_sitelibdir/__pycache__
%python3_sitelibdir/%modulename-%version.dist-info

%changelog
* Tue Aug 22 2023 Grigory Ustinov <grenka@altlinux.org> 3.4.0-alt1
- Automatically updated to 3.4.0.
- Build with check.

* Tue Sep 07 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.1-alt1
- Automatically updated to 3.3.1.

* Sun Jun 06 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.0-alt1
- Automatically updated to 3.3.0.

* Sun Nov 08 2020 Grigory Ustinov <grenka@altlinux.org> 3.2.0-alt1
- Initial build for Sisyphus.
