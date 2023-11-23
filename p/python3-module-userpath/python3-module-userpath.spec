%define _unpackaged_files_terminate_build 1
%define pypi_name userpath

%def_with check

Name: python3-module-%pypi_name
Version: 1.9.1
Release: alt1

Summary: Cross-platform tool for adding locations to the user PATH
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/userpath/
Vcs: https://github.com/ofek/userpath

BuildArch: noarch

Source0: %name-%version.tar
Source1: %pyproject_deps_config_name

%pyproject_runtimedeps_metadata
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%if_with check
%pyproject_builddeps_metadata
%pyproject_builddeps_check
%endif

%description
This is a tool for modifying a user's PATH.

%prep
%setup
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
%pyproject_run_pytest -k 'not TestDebian' -vra

%files
%doc LICENSE.txt README.md HISTORY.rst
%_bindir/%pypi_name
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 23 2023 Anton Zhukharev <ancieg@altlinux.org> 1.9.1-alt1
- Built for ALT Sisyphus.

