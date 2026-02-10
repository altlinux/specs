%define _unpackaged_files_terminate_build 1
%define pypi_name nkeys
%define mod_name nkeys

%def_with check

Name: python3-module-%pypi_name
Version: 0.2.1
Release: alt1

Summary: NATS Keys for Python
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/nkeys/
Vcs: https://github.com/nats-io/nkeys.py

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
A public-key signature system based on Ed25519 for the NATS ecosystem.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipenv Pipfile dev-packages
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Feb 10 2026 Egor Ignatov <egori@altlinux.org> 0.2.1-alt1
- First build for ALT.
