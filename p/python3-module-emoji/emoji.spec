Name: python3-module-emoji
Version: 1.6.3
Release: alt1

Summary: Emoji for Python
License: BSD
Group: Development/Python
Url: https://pypi.org/project/emoji/

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
%python3_sitelibdir/emoji
%python3_sitelibdir/emoji-%version-*-info

%changelog
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
