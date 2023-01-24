Name: python3-module-emoji
Version: 2.2.0
Release: alt1

Summary: Emoji for Python
License: BSD
Group: Development/Python
Url: https://pypi.org/project/emoji/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
py.test3 tests

%files
%python3_sitelibdir/emoji
%python3_sitelibdir/emoji-%version.dist-info

%changelog
* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.2.0-alt1
- 2.2.0 released

* Thu Jul 21 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.0.0-alt1
- 2.0.0 released

* Fri Mar 18 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.0-alt1
- 1.7.0 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.3-alt1
- 1.6.3 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.5.0-alt1
- 1.5.0 released

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.2.1-alt1
- 1.2.1 released

* Mon Sep 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt1
- 0.6.0 released

* Mon Jul 06 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.5.3-alt1
- initial
