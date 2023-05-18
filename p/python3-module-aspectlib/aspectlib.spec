%define _unpackaged_files_terminate_build 1
%define pypi_name aspectlib
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 2.0.0
Release: alt1
Summary: An aspect-oriented programming, monkey-patch and decorators library
License: BSD
Group: Development/Python3
Url: https://pypi.org/project/aspectlib/
Vcs: https://github.com/ionelmc/python-aspectlib
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
%add_pyproject_deps_runtime_filter fields
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter hunter fields
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
An aspect-oriented programming, monkey-patch and decorators library.
It is useful when changing behavior in existing code is desired.
It includes tools for debugging and testing: simple mock/record and a complete capture/replay framework.

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
%pyproject_run_pytest -ra -Wignore

%files
%doc README.rst
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue May 02 2023 Stanislav Levin <slev@altlinux.org> 2.0.0-alt1
- 1.4.2 -> 2.0.0.

* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.4.2-alt3
- Build for python2 disabled.

* Thu May 30 2019 Stanislav Levin <slev@altlinux.org> 1.4.2-alt2
- Removed false dependency on `fields`.

* Fri Nov 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.2-alt1
- Initial build for ALT.
