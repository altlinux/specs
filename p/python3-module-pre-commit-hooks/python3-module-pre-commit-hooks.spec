%define _unpackaged_files_terminate_build 1
%define pypi_name pre-commit-hooks
%define mod_name pre_commit_hooks

%def_with check

Name: python3-module-%pypi_name
Version: 6.0.0
Release: alt1
Summary: Some out-of-the-box hooks for pre-commit
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/pre-commit-hooks/
Vcs: https://github.com/pre-commit/pre-commit-hooks.git
BuildArch: noarch
Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%if_with check
BuildRequires: git
BuildRequires: git-lfs
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
%summary.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_pipreqfile requirements-dev.txt
%endif

%build
%pyproject_build

%install
%pyproject_install

%check
git init .
export GIT_AUTHOR_NAME="test"
export GIT_COMMITTER_NAME="test"
export GIT_AUTHOR_EMAIL="test@example.com"
export GIT_COMMITTER_EMAIL="test@example.com"
%pyproject_run_pytest -vra

%files
%_bindir/*
%doc README.*
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu Feb 12 2026 Martynenko Evgeniy <enimalojd@altlinux.org> 6.0.0-alt1
- Initial build for ALT.
