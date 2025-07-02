%define _unpackaged_files_terminate_build 1
%define pypi_name distro
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.9.0
Release: alt1
Summary: An OS platform information API
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/distro/
Vcs: https://github.com/python-distro/distro
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
distro provides information about the OS distribution it runs on, such as a
reliable machine-readable ID, or version information.

It is the recommended replacement for Python's original
platform.linux_distribution function (removed in Python 3.8). It also provides
much more functionality which isn't necessarily Python bound, like a
command-line interface.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_tox tox.ini testenv
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc README.*
%_bindir/distro
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Jul 01 2025 Stanislav Levin <slev@altlinux.org> 1.9.0-alt1
- 1.8.0 -> 1.9.0.

* Mon Feb 20 2023 Alexander Stepchenko <geochip@altlinux.org> 1.8.0-alt1
- New version 1.8.0
- Add check section
- Add ALT Linux support

* Mon Oct 05 2020 Alexey Shabalin <shaba@altlinux.org> 1.5.0-alt2
- rename src.rpm package to python3-module-distro

* Fri Jul 03 2020 Vladimir Didenko <cow@altlinux.org> 1.5.0-alt1
- New version

* Mon Apr 08 2019 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- Initial build for Sisyphus
