%define pypi_name promobot-sdk

Name: python3-module-%pypi_name
Version: 0.6.11
Release: alt1

Summary: Promobot Python SDK (manipulator MEdu)
License: MIT
Group: Development/Python3

Url: https://test.pypi.org/project/pm-python-sdk/

BuildArch: noarch

Source: %name-%version.tar


BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools


%description
Python SDK for controlling the Promobot (MEdu) manipulator: connecting
to the robot, taking control, and executing movement and gripper commands

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.md
%doc LICENSE
%python3_sitelibdir/sdk/
%python3_sitelibdir/pm_python_sdk-%version.dist-info/


%changelog
* Tue Mar 17 2026 Valentin Sokolov <sova@altlinux.org> 0.6.11-alt1
- Update to version 0.6.11

* Tue Jan 13 2026 Valentin Sokolov <sova@altlinux.org> 0.6.9-alt1
- Update to version 6.9

* Wed Dec 03 2025 Valentin Sokolov <sova@altlinux.org> 0.6.8-alt1
- Update to version 6.8

* Wed Nov 19 2025 Valentin Sokolov <sova@altlinux.org> 0.6.7-alt1
- Initial build for Sisyphus
