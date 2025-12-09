Name: python3-module-socksio
Version: 1.0.0
Release: alt2

Summary: Client-side sans-I/O SOCKS proxy implementation
License: MIT
Group: Development/Python
Url: https://pypi.org/project/socksio
VCS: https://github.com/sethmlarson/socksio

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
%pyproject_run_pytest -o addopts=

%files
%python3_sitelibdir/socksio
%python3_sitelibdir/socksio-%version.dist-info

%changelog
* Tue Dec 09 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 1.0.0-alt2
- moved to pyproject

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.0-alt1
- 1.0.0 released
