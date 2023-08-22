%define _unpackaged_files_terminate_build 1
%define pypi_name readtime

%def_with check

Name: python3-module-%pypi_name
Version: 3.0.0
Release: alt1

Summary: Calculates the time some text takes the average human to read
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/readtime/
Vcs: https://github.com/alanhamlett/readtime

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
Calculates the time some text takes the average human to read,
based on Medium's read time forumula.

%prep
%setup
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
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md AUTHORS
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Aug 22 2023 Anton Zhukharev <ancieg@altlinux.org> 3.0.0-alt1
- Built for ALT Sisyphus.

