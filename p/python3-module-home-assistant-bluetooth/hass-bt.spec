Name: python3-module-home-assistant-bluetooth
Version: 1.12.2
Release: alt1

Summary: Home Assistant Bluetooth Models and Helpers
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/home-assistant-bluetooth/

Source0: %name-%version-%release.tar
Source1: pyproject_deps.json

BuildArch: noarch

BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build

%description
%summary

%prep
%setup

%build
%pyproject_deps_resync_build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/home_assistant_bluetooth
%python3_sitelibdir/home_assistant_bluetooth-%version.dist-info

%changelog
* Fri Jul 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 1.12.2-alt1
- 1.12.2 released

* Thu Mar 14 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.12.0-alt1
- 1.12.0 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.10.0-alt1
- 1.10.0 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.9.2-alt1
- 1.9.2 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0-alt1
- 1.6.0 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released
