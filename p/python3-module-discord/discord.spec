%define _unpackaged_files_terminate_build 1
%define pypi_name discord
%define mod_name discord_py

%def_with check

Name: python3-module-%pypi_name
Version: 2.5.2
Release: alt1
Summary: An API wrapper for Discord written in Python.
License: MIT 
Group: Development/Python3
Url: https://github.com/Rapptz/discord.py
Vcs: https://pypi.org/project/discord-py/

BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(aiohttp)
#BuildRequires: python3-module-audioop-lts

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
A modern, easy to use, feature-rich, and async ready API wrapper
for Discord written in Python.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
#pyproject_run_pytest

%files
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Sun Aug 10 2025 Pavel Shilov <zerospirit@altlinux.org> 2.5.2-alt1
- Initial build for Sisyphus.