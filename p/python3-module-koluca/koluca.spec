Name: python3-module-koluca
Version: 0.2.1
Release: alt1

Summary: Korean lunar calendar to Gregorian converter
License: MIT
Group: Development/Python
Url: https://pypi.org/project/korean-lunar-calendar/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/korean_lunar_calendar
%python3_sitelibdir/korean_lunar_calendar-%version-*-info

%changelog
* Thu Sep 24 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.2.1-alt1
- initial
