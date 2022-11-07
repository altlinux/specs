Name: python3-module-home-assistant-bluetooth
Version: 1.6.0
Release: alt1

Summary: Home Assistant Bluetooth Models and Helpers
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/home-assistant-bluetooth/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(poetry-core)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/home_assistant_bluetooth
%python3_sitelibdir/home_assistant_bluetooth-%version.dist-info

%changelog
* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.0-alt1
- 1.6.0 released

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.4.0-alt1
- 1.4.0 released
