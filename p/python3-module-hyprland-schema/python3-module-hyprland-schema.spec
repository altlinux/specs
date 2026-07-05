%global _unpackaged_files_terminate_build 1
%global module_name hyprland_schema
%def_with check

Name: python3-module-hyprland-schema
Version: 0.6.3
Release: alt1
Summary: Typed Python schema for every Hyprland configuration option
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hyprland-schema
VCS: https://github.com/BlueManCZ/hyprland-schema

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: ruff
BuildRequires: python3-module-pytest
%endif

%description
Typed Python schema for every Hyprland configuration option - with defaults,
ranges, and descriptions. Generated from Hyprland's ConfigDescriptions.hpp.
Zero runtime dependencies - stdlib only.

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
* Sun Jul 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.3-alt1
- Updated to version 0.6.3.

* Sun May 31 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.6.1-alt1
- Updated to version 0.6.1.

* Sun May 03 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.0-alt1
- Initial build for ALT.
