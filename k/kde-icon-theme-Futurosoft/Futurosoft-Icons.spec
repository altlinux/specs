%define theme Futurosoft
Name: kde-icon-theme-%theme
Version: 0.5.2
Release: alt1
Summary: A set of Icons for KDE
License: GPL
Group: Graphical desktop/KDE
Url: http://www.kde-look.org/content/show.php?content=50667
Provides: kde-icon-theme
Conflicts: kdeartwork-extra <= 3.1.0-alt2
Source: %theme-Icons-%version.tar.gz
BuildArch: noarch

%description
Icons by Futurosoft.
This icons is inspirated in Vista.

%prep
%setup -q -c

%install
mkdir -p %buildroot/%_iconsdir/%theme-Icons
cd '%theme Icons %version'
%__cp -r * %buildroot/%_iconsdir/%theme-Icons/

%files
%_iconsdir/%theme-Icons

%changelog
* Tue Jul 31 2007 Motsyo Gennadi <drool@altlinux.ru> 0.5.2-alt1
- new version

* Fri May 18 2007 Motsyo Gennadi <drool@altlinux.ru> 0.5.1-alt1
- initial build for Sisyphus

* Mon Feb 26 2007 Motsyo Gennadi <drool@altlinux.ru> 0.5.1-alt0.M24.1
- initial build for ALT Linux 2.4 Master
