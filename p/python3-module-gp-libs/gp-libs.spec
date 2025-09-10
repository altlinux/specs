%define _unpackaged_files_terminate_build 1
%define pypi_name gp-libs
%def_with check

Name: python3-module-%pypi_name
Version: 0.0.13
Release: alt1

Summary: Incubator for pytest and sphinx helpers for git-pull python projects 
License: MIT
Group: Development/Python3
Url: https://gp-libs.git-pull.com/
Vcs: https://github.com/git-pull/gp-libs
BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name
Patch: %name-%version-alt.patch

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-macros-pyproject
BuildRequires: rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: python3-module-sphinx-tests
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
Incubating / dogfooding some sphinx extensions and pytest plugins on
git-pull projects, e.g. cihai, vcs-python, or tmux-python.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_depgroup testing
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run -- bash -s <<-'ENDTESTS'
# Tests are hardcoded to load source files of this module from the src/. You
# can see that in the pyproject.toml file in the pytest settings section.
PYTHONPATH=src python3 -m pytest
ENDTESTS

%files
%doc README.md LICENSE
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%python3_sitelibdir/doctest_docutils.py
%python3_sitelibdir/docutils_compat.py
%python3_sitelibdir/gp_libs.py
%python3_sitelibdir/linkify_issues.py
%python3_sitelibdir/pytest_doctest_docutils.py
%python3_sitelibdir/__pycache__/doctest_docutils.*
%python3_sitelibdir/__pycache__/docutils_compat.*
%python3_sitelibdir/__pycache__/gp_libs.*
%python3_sitelibdir/__pycache__/linkify_issues.*
%python3_sitelibdir/__pycache__/pytest_doctest_docutils.*

%changelog
* Wed Sep 10 2025 Alexandr Shashkin <dutyrok@altlinux.org> 0.0.13-alt1
- Initial build for ALT Sisyphus.

