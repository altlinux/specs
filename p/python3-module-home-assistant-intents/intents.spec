Name: python3-module-home-assistant-intents
Version: 2024.7.3
Release: alt1

Summary: Intents for Home Assistant
License: CC-BY-4.0
Group: Development/Python
Url: https://pypi.org/project/home-assistant-intents/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(hassil)
BuildRequires: python3(yaml)

%description
%summary

%prep
%setup
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
