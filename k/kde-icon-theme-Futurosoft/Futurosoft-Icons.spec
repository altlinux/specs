%define theme Futurosoft
Name: kde-icon-theme-%theme
Version: 0.5.2
Release: alt2
Summary: A set of Icons for KDE
Summary(ru_RU.UTF-8): Набор иконок для KDE
License: GPL
Group: Graphical desktop/KDE
Url: https://store.kde.org/p/1002561/
Provides: kde-icon-theme
Conflicts: kdeartwork-extra <= 3.1.0-alt2
Source: %theme-Icons-%version.tar.gz
BuildArch: noarch

%description
Icons by Futurosoft.
This icons is inspirated in Vista.

%description -l ru_RU.UTF8
Набор иконок для KDE, созданный Futurosoft под впечатлением от Vista.

%prep
%setup -q -c

%install
mkdir -p %buildroot/%_iconsdir/%theme-Icons
cd '%theme Icons %version'
%__cp -r * %buildroot/%_iconsdir/%theme-Icons/

%files
%_iconsdir/%theme-Icons

%changelog
* Wed Jun 06 2018 Grigory Ustinov <grenka@altlinux.org> 0.5.2-alt2
- Update URL.
- Add russian description (Closes: #22162).

* Tue Jul 31 2007 Motsyo Gennadi <drool@altlinux.ru> 0.5.2-alt1
- new version

* Fri May 18 2007 Motsyo Gennadi <drool@altlinux.ru> 0.5.1-alt1
- initial build for Sisyphus

* Mon Feb 26 2007 Motsyo Gennadi <drool@altlinux.ru> 0.5.1-alt0.M24.1
- initial build for ALT Linux 2.4 Master
