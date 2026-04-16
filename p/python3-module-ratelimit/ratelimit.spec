Name: python3-module-ratelimit
Version: 2.2.1
Release: alt1

Summary: API Rate Limit Decorator
License: MIT
Group: Development/Python
URL: https://pypi.org/project/ratelimit
VCS: https://github.com/tomasbasham/ratelimit

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

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
%pyproject_run_pytest -o addopts=

%files
%python3_sitelibdir/ratelimit
%python3_sitelibdir/ratelimit-%version.dist-info

%changelog
* Thu Apr 16 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.2.1-alt1
- 2.2.1 released

