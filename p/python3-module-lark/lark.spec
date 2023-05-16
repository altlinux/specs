%define _unpackaged_files_terminate_build 1
%define pypi_name lark
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.1.5
Release: alt1
Summary: A modern parsing library
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/lark
Vcs: https://github.com/lark-parser/lark
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch
%pyproject_runtimedeps_metadata
# pyinstaller's hook
%filter_from_requires /python3(PyInstaller\(\..*\)\?)/d
# file conflict on site-packages/lark/
Provides: python3-module-lark-parser = %EVR
Obsoletes: python3-module-lark-parser <= 0.11.3-alt1
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
%add_pyproject_deps_check_filter js2py
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Lark is a modern general-purpose parsing library for Python.
With Lark, you can parse any context-free grammar, efficiently, with very little
code.

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
%pyproject_run -- python -m tests

%files
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Fri May 05 2023 Stanislav Levin <slev@altlinux.org> 1.1.5-alt1
- Initial build for Sisyphus.
