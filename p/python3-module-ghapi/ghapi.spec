%define _unpackaged_files_terminate_build 1
%define pypi_name ghapi
%define mod_name ghapi

Name: python3-module-%pypi_name
Version: 1.0.6
Release: alt1

Summary: A third-party Python library and CLI client for the GitHub API

License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/ghapi/
VCS: https://github.com/AnswerDotAI/ghapi/

BuildArch: noarch

Source: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
ghapi includes tab-completion, integrated documentation and
automatic pagination of responses.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%files
%_bindir/completion-ghapi
%_bindir/gh-create-workflow
%_bindir/ghpath
%_bindir/ghraw
%_bindir/%pypi_name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Feb 12 2025 Anastasia Doronina <swaggyglice@altlinux.org> 1.0.6-alt1
- Initial Build for Sisyphus.
