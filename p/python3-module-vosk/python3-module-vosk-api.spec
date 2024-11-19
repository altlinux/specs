%define _unpackaged_files_terminate_build 1
%define mod_name %pypi_name
%define pypi_name vosk

%def_with check

Name: python3-module-%pypi_name
Version: 0.3.50
Release: alt1
Summary: Offline speech recognition API for Android, iOS, Raspberry Pi and servers with Python, Java, C# and Node 
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/alphacep/vosk-api
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(cffi)
BuildRequires: python3(requests)
BuildRequires: python3(websockets)
BuildRequires: python3(wheel)
BuildRequires: python3(srt)

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
%summary

%prep
%setup

%build
cd python
%pyproject_build

%install
cd python
%pyproject_install

%check
#pyproject_run_pytest

%files
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version.dist-info
%_bindir/%pypi_name-transcriber/

%changelog
* Tue Nov 12 2024 Pavel Shilov <zerospirit@altlinux.org> 0.3.50-alt1
- initial build for Sisyphus
