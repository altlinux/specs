Name: python3-module-home-assistant-intents
Version: 2025.10.1
Release: alt1

Summary: Intents for Home Assistant
License: CC-BY-4.0
Group: Development/Python
Url: https://pypi.org/project/home-assistant-intents
VCS: https://github.com/OHF-Voice/intents

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_metadata_extra dev

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
O=home_assistant_intents/data
mkdir -p $O && python3 script/merged_output.py $O

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/home_assistant_intents
%python3_sitelibdir/home_assistant_intents-%version.dist-info

%changelog
* Thu Oct 16 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2025.10.1-alt1
- 2025.10.1 released

* Wed Jan 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 2025.1.1-alt1
- 2025.1.1 released

* Mon Nov 11 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.11.6-alt1
- 2024.11.6 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.9.4-alt1
- 2024.9.4 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.7.3-alt1
- 2024.7.3 released

* Mon May 06 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 2024.4.24-alt1
- 2024.4.24 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2024.3.12-alt1
- 2024.3.12 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 2024.1.2-alt1
- 2024.1.2 released

* Fri Nov 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.10.16-alt1
- 2023.10.16 released

* Thu Sep 14 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.8.2-alt1
- 2023.8.2 released

* Mon Jul 10 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.6.28-alt1
- 2023.6.28 released

* Thu May 04 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.4.26-alt1
- 2023.4.26 released

* Mon Mar 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.2.28-alt1
- initial
