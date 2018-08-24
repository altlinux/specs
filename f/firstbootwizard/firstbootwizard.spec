Name: firstbootwizard
Version: 0.0.3
Release: alt1

Summary: System setup utility when boot first (oem-mode)
Group: Networking/IRC
License: GPLv2

Url: http://git.altlinux.org/gears/f/firstboot

Source0: %name-%version.tar

BuildRequires(pre): rpm-macros-qt5
BuildRequires: gcc-c++
BuildRequires: qt5-declarative-devel qt5-tools-devel

%description
Booting in firstboot mode will let the final user configure
the system to her preference and create her actual account.

%prep
%setup

%build
%qmake_qt5
%make_build

%install
%makeinstall_std INSTALL_ROOT=%buildroot

%files
%_bindir/%name
%dir %_datadir/%name
%_datadir/%name/*.ts

%changelog
* Fri Aug 24 2018 Pavel Akopov <pak@altlinux.org> 0.0.3-alt1
- update to version 0.0.3

* Thu Aug 23 2018 Pavel Akopov <pak@altlinux.org> 0.0.2-alt1
- update to version 0.0.2

* Tue Aug 21 2018 Pavel Akopov <pak@altlinux.org> 0.0.1-alt1
- initial build

