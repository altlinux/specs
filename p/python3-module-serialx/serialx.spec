Name: python3-module-serialx
Version: 1.15.0
Release: alt1

Summary: Serial communication library
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/serialx
VCS: https://github.com/puddly/serialx

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject >= 0.2.0
BuildRequires: /dev/pts, /proc, socat
%add_pyproject_deps_check_filter codespell
%add_pyproject_deps_check_filter prek
%add_pyproject_deps_check_filter 'uv$'
%add_pyproject_deps_check_filter '^types-'
%add_pyproject_deps_check_filter 'pytest-github-actions-annotate-failures'
%add_pyproject_deps_check_filter 'setuptools-rust'
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup dev
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts= tests

%files
%python3_sitelibdir/serialx
%python3_sitelibdir/serialx-%version.dist-info

%changelog
* Fri Oct 23 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.15.0-alt1
- 1.15.0 released

* Mon Oct 19 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.14.0-alt1
- 1.14.0 released

* Tue Oct 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.11.0-alt1
- 1.11.0 released

* Mon Sep 21 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.10.0-alt1
- 1.10.0 released

* Tue Sep 01 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.0-alt1
- 1.9.0 released

* Tue Jul 28 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.2-alt1
- 1.8.2 released

* Wed Jul 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.0-alt1
- 1.8.0 released

