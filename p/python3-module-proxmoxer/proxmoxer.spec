%set_python3_req_method strict
%define _unpackaged_files_terminate_build 1
%define pypi_name proxmoxer
%def_with check

Name: python3-module-%pypi_name
Version: 2.1.0
Release: alt1

Summary: A Python wrapper for Proxmox REST API
License: MIT
Group: Development/Python3
Url: https://github.com/proxmoxer/proxmoxer
BuildArch: noarch

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(requests)
BuildRequires: python3(paramiko)

%if_with check
BuildRequires: python3(responses)
BuildRequires: python3(requests_toolbelt)
BuildRequires: python3(pytest)
BuildRequires: python3(openssh_wrapper)
%endif


%py3_provides %pypi_name

%add_python3_req_skip httplib # python3(http) is used instead this
%add_python3_req_skip urlparse # python3(urllib) is used instead this

%description
Proxmoxer is a python wrapper around the Proxmox REST API v2.
It currently supports the Proxmox services of Proxmox Virtual Environment (PVE),
Proxmox Mail Gateway (PMG), and Proxmox Backup Server (PBS).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%pypi_name-%version.dist-info
%doc README.rst LICENSE.txt

%changelog
* Tue Aug 13 2024 Alexander Makeenkov <amakeenk@altlinux.org> 2.1.0-alt1
- Updated to version 2.1.0.
- Enabled tests.

* Tue Jan 03 2023 Alexander Makeenkov <amakeenk@altlinux.org> 2.0.1-alt1
- Updated to version 2.0.1
- Use pyproject macroses for build
- Added py3_provides

* Thu Jul 23 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.1.1-alt4
- Used the strict dependency search method (closes: #38751)
- Fixed %%files section
- Package license and readme files

* Thu Jul 23 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.1.1-alt3
- Don't package tests

* Thu Jul 23 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.1.1-alt2
- Added conflicts with python3-module-pymta-tests and python3-module-m2r

* Thu Jul 16 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.1.1-alt1
- Updated to version 1.1.1
- Fixed url tag

* Fri Jan 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.2-alt5
- Porting on Python3.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt4
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt3
- NMU: remove %ubt from release

* Fri Jun 08 2018 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.0.2-alt2%ubt
- Fixed the dependencies and a bogus `Provides: python2.7(tests)`.

* Tue May 29 2018 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.0.2-alt1%ubt
- Initial build for ALTLinux Sisyphus
