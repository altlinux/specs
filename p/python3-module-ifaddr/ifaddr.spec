Name: python3-module-ifaddr
Version: 0.2.0
Release: alt2

Summary: Python library to enumerate own IP addressess
License: MIT
Group: Development/Python
URL: https://pypi.org/project/ifaddr
VCS: https://github.com/ifaddr/ifaddr

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata

%description
Enumerates all IP addresses on all network adapters of the system

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
%python3_sitelibdir/ifaddr
%python3_sitelibdir/ifaddr-%version.dist-info

%changelog
* Thu Feb 05 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.0-alt2
- switch to metadata runtime deps (closes: 57776)

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.0-alt1
- 0.2.0 released

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.7-alt1
- 0.1.7 released

* Thu Nov 28 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.1.6-alt1
- initial
