%global _unpackaged_files_terminate_build 1
%global module_name hyprland_monitors
%def_with check

Name: python3-module-hyprland-monitors
Version: 0.8.0
Release: alt1
Summary: Monitor management utilities for Hyprland
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hyprland-monitors
VCS: https://github.com/BlueManCZ/hyprland-monitors

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-hyprland-socket
%endif

%description
Monitor management utilities for Hyprland.
Scale computation, layout geometry, config line parsing, and
hardware capability detection for Hyprland monitor management.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%module_name
%python3_sitelibdir/%{pyproject_distinfo %module_name}

%changelog
* Sun Jul 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.0-alt1
- Updated to version 0.8.0.

* Sun May 31 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.7.0-alt1
- Updated to version 0.7.0.

* Sun May 10 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.5.0-alt1
- Updated to version 0.5.0.

* Sun May 03 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.0-alt1
- Initial build for ALT.
