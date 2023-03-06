Name: python3-module-home-assistant-intents
Version: 2023.2.28
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
BuildRequires: python3(build)
BuildRequires: python3(hassil)
BuildRequires: python3(yaml)

%description
%summary

%prep
%setup

%build
O=package/home_assistant_intents/data
mkdir -p $O
python3 -m script.intentfest merged_output $O
cd package
%pyproject_build

%install
cd package
%pyproject_install

%files
%python3_sitelibdir/home_assistant_intents
%python3_sitelibdir/home_assistant_intents-%version.dist-info

%changelog
* Mon Mar 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2023.2.28-alt1
- initial
