Name: python3-module-getmac
Version: 0.9.6
Release: alt1

Summary: Python library to get the MAC address
License: MIT
Group: Development/Python
URL: https://pypi.org/project/getmac
VCS: https://github.com/ghostofgoes/getmac

Source0: %name-%version.tar
Source1: pyproject_deps.json

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
Pure-Python package to get the MAC address of network interfaces and hosts
on the local network.

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_pipreqfile tests/test-requirements.txt

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest tests

%files
%python3_sitelibdir/getmac
%python3_sitelibdir/getmac-%version.dist-info

%changelog
* Tue Oct 06 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.6-alt1
- 0.9.6 released

* Mon Nov 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.9.5-alt1
- 0.9.5 released

* Wed Jan 24 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.4-alt1
- 0.9.4 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.9.3-alt1
- 0.9.3 released

* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.3-alt1
- 0.8.3 released

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.8.2-alt1
- initial
