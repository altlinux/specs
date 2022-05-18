Name: python3-module-holidays
Version: 0.13
Release: alt1

Summary: Holidays calculator
License: BSD
Group: Development/Python
Url: https://pypi.org/project/holidays/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
A fast, efficient Python library for generating country, province and state
specific sets of holidays on the fly. It aims to make determining whether
a specific date is a holiday as fast and flexible as possible.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/holidays
%python3_sitelibdir/holidays-%version-*-info

%changelog
* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13-alt1
- 0.13 released

* Thu Sep 24 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.3-alt1
- initial

