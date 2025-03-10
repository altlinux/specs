%define pypi_name pulsemixer

%def_without check

Name:    python3-module-%pypi_name
Version: 1.5.1
Release: alt1

Summary: CLI and curses mixer for PulseAudio
License: MIT
Group:   Development/Python3
Url:     https://pypi.org/project/pulsemixer/
Vcs:     https://github.com/GeorgeFilipkin/pulsemixer

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

BuildArch: noarch

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc LICENSE README.*
%_bindir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri Jan 24 2025 Sergey Palcheh <minergenon@altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus
