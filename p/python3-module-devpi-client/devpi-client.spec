%define _unpackaged_files_terminate_build 1
%define pypi_name devpi-client
%define mod_name devpi

%def_with check

Name: python3-module-%pypi_name
Version: 7.2.1
Release: alt1.1
Summary: Manage devpi-server, Python packaging and testing
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/devpi-client
Vcs: https://github.com/devpi/devpi
BuildArch: noarch
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: python3-module-devpi-server
BuildRequires: python3-module-mock
BuildRequires: python3-module-pypitoken
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-instafail
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-tox
BuildRequires: python3-module-webtest

BuildRequires: python3-module-build
BuildRequires: python3-module-check-manifest
BuildRequires: python3-module-devpi-common
BuildRequires: python3-module-iniconfig
BuildRequires: python3-module-pkginfo
BuildRequires: python3-module-platformdirs
BuildRequires: python3-module-pluggy
BuildRequires: python3-module-requests
BuildRequires: python3-module-pip
BuildRequires: python3-module-flit-core
%endif

%description
The devpi command line tool is typically used in conjunction with devpi-server.
It allows to upload, test and install packages from devpi indexes.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
# symlink server plugins as it's made in upstream
ln -sf -t testing/ \
    %python3_sitelibdir/test_devpi_server/{functional,reqmock,simpypi}.py

# https://github.com/Pylons/pyramid/issues/3731
export PYTHONWARNINGS='ignore:pkg_resources is deprecated as an API.:UserWarning:pyramid.path'
%pyproject_run_pytest -ra

%files
%_bindir/devpi
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 7.2.1-alt1.1
- Demodernized packaging.

* Wed Mar 18 2026 Stanislav Levin <slev@altlinux.org> 7.2.1-alt1
- 7.2.0 -> 7.2.1.

* Mon Jun 02 2025 Stanislav Levin <slev@altlinux.org> 7.2.0-alt3
- Fixed FTBFS (setuptools 80.9.0).

* Mon May 05 2025 Stanislav Levin <slev@altlinux.org> 7.2.0-alt2
- fixed FTBFS (setuptools 75.8.1).

* Sat Dec 28 2024 Stanislav Levin <slev@altlinux.org> 7.2.0-alt1
- Initial build for Sisyphus.
