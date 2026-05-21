Name: python3-module-aiohttp-asyncmdnsresolver
Version: 0.2.0
Release: alt1

Summary: Resolver for aiohttp with mDNS support
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/aiohttp-asyncmdnsresolver/
VCS: https://github.com/aio-libs/aiohttp-asyncmdnsresolver

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
%pyproject_deps_resync_check_pipreqfile requirements/test.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts=

%files
%python3_sitelibdir/aiohttp_asyncmdnsresolver
%python3_sitelibdir/aiohttp_asyncmdnsresolver-%version.dist-info

%changelog
* Thu May 21 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.0-alt1
- 0.2.0 released

* Tue Oct 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.1.1-alt1
- 0.1.1 released
