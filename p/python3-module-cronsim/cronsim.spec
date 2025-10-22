Name: python3-module-cronsim
Version: 2.7
Release: alt1

Summary: A cron expression parser and evaluator
License: BSD-3-Clause
Group: Development/Python
Url: https://pypi.org/project/cronsim
VCS: https://github.com/cuu508/cronsim

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -v tests

%files
%python3_sitelibdir/cronsim
%python3_sitelibdir/cronsim-%version.dist-info

%changelog
* Wed Oct 22 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.7-alt1
- 2.7 released

* Wed Jan 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2.6-alt1
- 2.6 released
