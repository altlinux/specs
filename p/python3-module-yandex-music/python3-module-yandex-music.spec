%define _unpackaged_files_terminate_build 1
%define pypi_name yandex-music
%define mod_name yandex_music

Name: python3-module-%pypi_name
Version: 2.2.0
Release: alt1

Summary: Library for the Yandex.Music API
License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/yandex-music/
Vcs: https://github.com/MarshalX/yandex-music-api

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools

%description
This library provides a Python interface for the undocumented and
self-hosted Yandex Music API. It is compatible with Python 3.8+ and
supports both synchronous and asynchronous (asyncio) code.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install
rm -rf %buildroot%python3_sitelibdir/tests

%files
%doc README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Sat Nov 01 2025 Tatyana Gagina <treza@altlinux.org> 2.2.0-alt1
- Packaged for ALT Sisyphus.
