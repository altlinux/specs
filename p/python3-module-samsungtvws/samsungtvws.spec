Name: python3-module-samsungtvws
Version: 3.0.5
Release: alt1

Summary: Python library for remote controlling Samsung TV sets
License: MIT
Group: Development/Python
URL: https://pypi.org/project/samsungtvws
VCS: https://github.com/xchwarze/samsung-tv-ws-api

Source0: %name-%version.tar
Source1: pyproject_deps.json

BuildArch: noarch
Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata
%pyproject_runtimedeps_metadata_extra async
%pyproject_runtimedeps_metadata_extra encrypted

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
Python library for remote controlling Samsung TV sets via a TCP/IP connection.
It currently supports modern TVs with Ethernet or Wi-Fi connectivity.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile requirements.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -o addopts=

%files
%doc APPLICATIONS.md COMMANDS.md README.md
%_bindir/samsungtv
%python3_sitelibdir/samsungtvws
%python3_sitelibdir/samsungtvws-%version.dist-info

%changelog
* Mon Jun 01 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 3.0.5-alt1
- 3.0.5 released

* Thu Feb 12 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 2.7.0-alt1
- 2.7.0 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.0-alt1
- 2.6.0 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- initial
