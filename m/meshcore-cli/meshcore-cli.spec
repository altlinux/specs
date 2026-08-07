%define _unpackaged_files_terminate_build 1
%define pypi_name meshcore-cli
%define mod_name meshcore_cli

Name: meshcore-cli
Version: 1.5.0
Release: alt1
Summary: Command line interface to MeshCore node
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/meshcore-cli
VCS: https://github.com/meshcore-dev/meshcore-cli.git

BuildArch: noarch
AutoProv: nopython3

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(hatchling)

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(pytest-asyncio)
BuildRequires: python3(meshcore)
BuildRequires: python3(prompt_toolkit)
BuildRequires: python3(requests)
%endif

%description
meshcore-cli is a tool that connects to your companion radio node over BLE, TCP
or Serial and lets you interact with it from a terminal using a command line
interface.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.*
%_bindir/%name
%_bindir/meshcli
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Aug 05 2026 Vasiliy Doylov <neko@altlinux.org> 1.5.0-alt1
- Initial build for ALT.
