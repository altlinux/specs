%define _unpackaged_files_terminate_build 1
%define pypi_name displayctl

%def_with check

Name: python3-module-%pypi_name
Version: 1.2.2
Release: alt1
Summary: Display Configuration Manager for GNOME
License: MIT
Group: Graphics
Url: https://pypi.org/project/displayctl
Vcs: https://github.com/sorenisanerd/displayctl
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(build)
BuildRequires: python3(dbus)
BuildRequires: python3(hatchling)
BuildRequires: python3(hatchling)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(dbus)
%endif
Requires: python3(dbus)

%py3_provides %pypi_name

%description
Display Configuration Manager for GNOME

%prep
%setup -q

%build
%pyproject_build

%install
%pyproject_install

%check
%if_with check
%pyproject_run_pytest -v
%endif

%files
%doc README.md
%_bindir/%pypi_name
%python3_sitelibdir/%{pypi_name}/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 04 2026 Pavel Shilov <zerospirit@altlinux.org> 1.2.2-alt1
- Initial build for Sisyphus.