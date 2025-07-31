%define _unpackaged_files_terminate_build 1
%define pypi_name netshow
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.2
Release: alt1
Summary: Lightweight, performant interactive network connection monitor with friendly service names.
License: MIT
Group: Monitoring
Url: https://github.com/taylorwilsdon/netshow
Vcs: https://pypi.org/project/netshow/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: lsof
BuildRequires: python3(hatchling)
BuildRequires: python3(psutil)
BuildRequires: python3(textual)
BuildRequires: python3-module-mdit-plugins

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
%name interactive, process-aware network monitoring for your terminal

%prep
%setup
%patch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
#These tests require network
%tox_check_pyproject

%files
%doc *.md
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Jul 31 2025 Pavel Shilov <zerospirit@altlinux.org> 0.2.2-alt1
- Initial build for Alt.

