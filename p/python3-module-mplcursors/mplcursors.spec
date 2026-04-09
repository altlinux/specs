Name: python3-module-mplcursors
Version: 0.7.1
Release: alt1

Summary: Interactive data selection cursors for Matplotlib
License: Zlib
Group: Development/Python
Url: https://pypi.org/project/mplcursors
VCS: https://github.com/anntzer/mplcursors

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra test

%description
%summary

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/mplcursors
%python3_sitelibdir/mplcursors-%version.dist-info

%changelog
* Thu Apr 09 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7.1-alt1
- 0.7.1 released

* Tue Oct 21 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.7-alt1
- 0.7 released

* Fri Apr 18 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.6-alt1
- 0.6 released

