%define _unpackaged_files_terminate_build 1
%define mod_name %pypi_name
%define pypi_name pyttsx3

%def_with check

Name: python3-module-%pypi_name

Version: 2.98
Release: alt1.1
Summary: Offline Text To Speech (TTS) converter for Python 
License: MPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/pyttsx3/
Vcs: https://github.com/nateshmbhat/pyttsx3
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: espeak
BuildRequires: ffmpeg
BuildRequires: libespeak
BuildRequires: alsa-utils

%py3_provides %pypi_name

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info
%exclude %python3_sitelibdir/%pypi_name/drivers/nsss.py
%exclude %python3_sitelibdir/%pypi_name/drivers/sapi5.py

%changelog
* Mon Jan 13 2025 Pavel Shilov <zerospirit@altlinux.org> 2.98-alt1.1
- add build requires alsa-utils for tests

* Tue Nov 12 2024 Pavel Shilov <zerospirit@altlinux.org> 2.98-alt1
- initial build for Sisyphus
