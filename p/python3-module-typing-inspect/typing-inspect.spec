%define _unpackaged_files_terminate_build 1
%define pypi_name typing-inspect

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.0
Release: alt1
Summary: Runtime inspection of types defined in typing module
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/typing-inspect/
Vcs: https://github.com/ilevkivskyi/typing_inspect
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch0: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
# excluded by default filter
BuildRequires: python3-module-mypy-extensions
%endif

%description
The typing_inspect module defines experimental API for runtime inspection of
types defined in the Python standard typing module. Works with typing version
3.7.4 and later.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile test-requirements.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra -Wignore

%files
%doc README.md
%python3_sitelibdir/typing_inspect.py
%python3_sitelibdir/__pycache__/typing_inspect.cpython-*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu May 25 2023 Stanislav Levin <slev@altlinux.org> 0.9.0-alt1
- 0.8.0 -> 0.9.0.

* Thu Sep 15 2022 Stanislav Levin <slev@altlinux.org> 0.8.0-alt1
- 0.6.0 -> 0.8.0.

* Fri Apr 16 2021 Stanislav Levin <slev@altlinux.org> 0.6.0-alt1
- Initial build for Sisyphus.

