%global _unpackaged_files_terminate_build 1
%global module_name hyprland_socket
%def_with check

Name: python3-module-hyprland-socket
Version: 0.12.2
Release: alt1
Summary: Typed Python library for Hyprland IPC via Unix sockets
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/hyprland-socket
VCS: https://github.com/BlueManCZ/hyprland-socket

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-hatchling

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
Typed Python library for Hyprland IPC via Unix sockets.
Covers both read and write operations - querying state,
applying settings live, batch commands, and monitoring events.

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
* Sun Jul 05 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.12.2-alt1
- Updated to version 0.12.2.

* Sun May 31 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.12.1-alt1
- Updated to version 0.12.1.

* Sun May 10 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.10.0-alt1
- Updated to version 0.10.0.

* Sun May 03 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.9.1-alt1
- Initial build for ALT.
