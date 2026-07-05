%global _unpackaged_files_terminate_build 1
%global module_name hyprland_state
%def_with check

Name: python3-module-hyprland-state
Version: 0.4.3
Release: alt1
Summary: Live state interface for Hyprland
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hyprland-state
VCS: https://github.com/BlueManCZ/hyprland-state

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-hyprland-config
BuildRequires: python3-module-hyprland-schema
BuildRequires: python3-module-hyprland-socket
BuildRequires: python3-module-hyprland-monitors
%endif

%description
Live state interface for Hyprland - read, write,
and inspect the running compositor's configuration.

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
* Sun Jul 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.3-alt1
- Updated to version 0.4.3.

* Sun May 31 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.2-alt1
- Updated to version 0.4.2.

* Sun May 10 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.1-alt1
- Updated to version 0.2.1.

* Mon May 04 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.0-alt1
- Initial build for ALT.
