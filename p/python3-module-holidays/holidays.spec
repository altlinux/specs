Name: python3-module-holidays
Version: 0.16
Release: alt1

Summary: Holidays calculator
License: BSD
Group: Development/Python
Url: https://pypi.org/project/holidays/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
A fast, efficient Python library for generating country, province and state
specific sets of holidays on the fly. It aims to make determining whether
a specific date is a holiday as fast and flexible as possible.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/holidays
%python3_sitelibdir/holidays-%version.dist-info

%changelog
* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16-alt1
- 0.16 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.2-alt1
- 0.14.2 released

* Wed May 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.13-alt1
- 0.13 released

* Thu Sep 24 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.10.3-alt1
- initial
