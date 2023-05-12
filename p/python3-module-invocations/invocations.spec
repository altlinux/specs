%define _unpackaged_files_terminate_build 1
%define pypi_name invocations
%define mod_name %pypi_name

# disable for bootstrap (loop invocations <-> pytest-relaxed)
%def_with check

Name: python3-module-%pypi_name
Version: 3.2.0
Release: alt1
Summary: Common/best-practice Invoke tasks and collections
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/invocations
Vcs: https://github.com/pyinvoke/invocations
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: /dev/pts
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Invocations is a collection of reusable Invoke tasks, task collections and
helper functions. Originally sourced from the Invoke project's own
project-management tasks file, they are now highly configurable and used across
a number of projects, with the intent to become a clearinghouse for implementing
common best practices.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile dev-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- inv test -o=-Wignore

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri May 12 2023 Stanislav Levin <slev@altlinux.org> 3.2.0-alt1
- 3.1.0 -> 3.2.0.

* Fri May 05 2023 Stanislav Levin <slev@altlinux.org> 3.1.0-alt2
- Enabled testing.

* Wed May 03 2023 Stanislav Levin <slev@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus.
