%define		theme DarkGlass_Reworked
Name:		kde-icon-theme-%theme
Version:	2.72
Release:	alt2
Summary:	A set of Icons for KDE
Summary(ru_RU.UTF-8): Набор иконок для KDE
License:	GPL
Group:		Graphical desktop/KDE
Url:		https://store.kde.org/p/1002589/
Provides:	kde-icon-theme
Conflicts:	kdeartwork-extra <= 3.1.0-alt2
Source0:	http://www.mentalrey.it/icon_set/%theme.tar.gz
Patch0:		%theme-nocompress.diff
BuildArch:	noarch

# Automatically added by buildreq on Thu Sep 25 2008 (-bi)
BuildRequires: ImageMagick

%description
Icons by http://www.mentalrey.it/.

%description -l ru_RU.UTF8
Набор иконок для KDE от http://www.mentalrey.it/.

%prep
%setup -q -n %theme
%patch0 -p1

%build
chmod -x ./index.desktop
./buildset

%install
mkdir -p %buildroot/%_iconsdir/%theme-Icons
cd %theme
%__cp -r * %buildroot/%_iconsdir/%theme-Icons/
rm -f %buildroot/%_iconsdir/%theme-Icons/buildset

%files
%_iconsdir/%theme-Icons

%changelog
* Wed Jun 06 2018 Grigory Ustinov <grenka@altlinux.org> 2.72-alt2
- Update URL.
- Add russian description (Closes: #22161).

* Thu Sep 25 2008 Motsyo Gennadi <drool@altlinux.ru> 2.72-alt1
- initial build for ALT Linux
