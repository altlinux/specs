%define _unpackaged_files_terminate_build 1
%define pypi_name taskiq-pipelines
%define mod_name taskiq_pipelines

%def_with check

Name: python3-module-%pypi_name
Version: 0.1.2
Release: alt1

Summary: Task pipelining for taskiq
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/taskiq-pipelines/
Vcs: https://github.com/taskiq-python/taskiq-pipelines

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
Taskiq pipelines is a fire-and-forget at its limit.

Imagine you have a really tough functions and you want to call them
sequentially one after one, but you don't want to wait for them to
complete. taskiq-pipeline solves this for you.

%prep
%setup
%autopatch -p1
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%if_with check
%pyproject_deps_resync_check_poetry dev
%endif

# Upstream sets version via CI/CD and we need to set it itself.
sed -i '/^version =/s/".*"/"%version"/' pyproject.toml

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -vra

%files
%doc LICENSE README.md
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Aug 05 2024 Anton Zhukharev <ancieg@altlinux.org> 0.1.2-alt1
- Updated to 0.1.2.

* Mon Sep 04 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.1-alt1
- Updated to 0.1.1.

* Wed Jun 14 2023 Anton Zhukharev <ancieg@altlinux.org> 0.1.0-alt1
- New version.

* Sat May 13 2023 Anton Zhukharev <ancieg@altlinux.org> 0.0.3-alt1
- Tnitial build for ALT Sisyphus.

