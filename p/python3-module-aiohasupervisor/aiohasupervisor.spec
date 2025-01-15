Name: python3-module-aiohasupervisor
Version: 0.2.2
Release: alt1

Summary: Client Library for Home Assistant Supervisor
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/propcache/

Source0: %name-%version-%release.tar

BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/aiohasupervisor
%python3_sitelibdir/aiohasupervisor-%version.dist-info

%changelog
* Wed Jan 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.2-alt1
- 0.2.2 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.2.1-alt1
- 0.2.1 released
