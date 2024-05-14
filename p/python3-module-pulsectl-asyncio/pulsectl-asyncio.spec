%define _unpackaged_files_terminate_build 1

%def_with check

%global pypi_name pulsectl-asyncio

Name: python3-module-%{pypi_name}
Version: 1.2.0
Release: alt1

Summary: Asyncio frontend for pulsectl, a Python bindings library for PulseAudio (libpulse)
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/pulsectl-asyncio
VCS: https://github.com/mhthies/pulsectl-asyncio
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pulsectl >= 23.5.2
BuildRequires: pulseaudio
BuildRequires: /proc
%endif

%description
This library provides an Python 3 asyncio interface on top of the
pulsectl library for monitoring and controlling the PulseAudio sound
server.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
echo 'passenv = HOME' >> ./tox.ini
%tox_check_pyproject

%files
%python3_sitelibdir/pulsectl_asyncio
%python3_sitelibdir/%{pyproject_distinfo pulsectl_asyncio}

%changelog
* Fri Apr 19 2024 Egor Ignatov <egori@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Oct 03 2023 Egor Ignatov <egori@altlinux.org> 1.1.1-alt1
- First build for ALT
