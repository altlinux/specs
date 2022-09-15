Name: python3-module-psutil-home-assistant
Version: 0.0.1
Release: alt1

Summary: hass-specific psutil wrapper
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/psutil-home-assistant/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
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

%set_python3_req_method strict

%files
%python3_sitelibdir/psutil_home_assistant
%python3_sitelibdir/psutil_home_assistant-%version.dist-info

%changelog
* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.0.1-alt1
- 0.0.1 released
