%define pypi_name jupyterhub-systemdspawner

%def_without check

Name:    python3-module-%pypi_name
Version: 1.0.2
Release: alt1

Summary: Spawn JupyterHub single-user notebook servers with systemd
License: BSD-3-Clause
Group:   Development/Python3
URL:     https://github.com/jupyterhub/systemdspawner

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
The systemdspawner enables JupyterHub to spawn single-user notebook servers
using systemd.

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
%python3_sitelibdir/systemdspawner
%python3_sitelibdir/%{pyproject_distinfo jupyterhub_systemdspawner}

%changelog
* Wed Jan 29 2025 Andrey Cherepanov <cas@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
