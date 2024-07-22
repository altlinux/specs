%define pypi_name twilio

%def_without check

Name:    python3-module-%pypi_name
Version: 8.12.0
Release: alt1

Summary: A Python module for communicating with the Twilio API and generating TwiML.
License: MIT
Group:   Development/Python3
URL:     https://github.com/twilio/twilio-python

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%check
#%%tox_create_default_config
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Jul 22 2024 Andrey Cherepanov <cas@altlinux.org> 8.12.0-alt1
- Initial build for Sisyphus.
