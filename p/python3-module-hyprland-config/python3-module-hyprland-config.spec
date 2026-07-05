%global _unpackaged_files_terminate_build 1
%global module_name hyprland_config
%ifarch aarch64
%def_without check
%else
%def_with check
%endif

Name: python3-module-hyprland-config
Version: 0.9.11
Release: alt1
Summary: Round-trip parser and editor for Hyprland configuration files
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hyprland-config
VCS: https://github.com/BlueManCZ/hyprland-config

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-hypothesis
%endif

%description
This is a round-trip parser. It keeps comments, blank lines,
variable definitions, and formatting intact - editing one option
doesn't rewrite the rest of the file.

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
* Sun Jul 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.11-alt1
- Updated to version 0.9.11.

* Sun May 31 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.5-alt1
- Updated to version 0.9.5.

* Mon May 04 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.5-alt1
- Initial build for ALT.
