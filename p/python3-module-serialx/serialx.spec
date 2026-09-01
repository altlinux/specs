Name: python3-module-serialx
Version: 1.9.0
Release: alt1

Summary: Serial communication library
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/serialx
VCS: https://github.com/puddly/serialx

Source0: %name-%version.tar
Source1: pyproject_deps.json
Source2: crates.tar

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildRequires(pre): rpm-build-pyproject >= 0.2.0
BuildRequires: /dev/pts, socat
%add_pyproject_deps_check_filter codespell
%add_pyproject_deps_check_filter prek
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra dev
%pyproject_builddeps_check

%python3_set_limited_api 3.10

%description
%summary

%prep
%setup -a2
%ifdef bootstrap
cargo vendor
tar cf %SOURCE2 .cargo vendor
%endif

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts=  tests

%files
%python3_sitelibdir/serialx
%python3_sitelibdir/serialx-%version.dist-info

%changelog
* Tue Sep 01 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.9.0-alt1
- 1.9.0 released

* Tue Jul 28 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.2-alt1
- 1.8.2 released

* Wed Jul 22 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 1.8.0-alt1
- 1.8.0 released

