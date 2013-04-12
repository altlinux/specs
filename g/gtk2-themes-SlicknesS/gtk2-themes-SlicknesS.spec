Name:		gtk2-themes-SlicknesS
Summary:	SlicknesS GTK2 theme
Version:	2.2.2
Release:	alt1
License:	GPLv2+
Url:		http://xfce-look.org/content/show.php/SlicknesS?content=71993
Source:		SlicknesS_by_Th3R0b.tar.gz
Group:		Graphical desktop/GNOME
Packager:	Motsyo Gennadi <drool@altlinux.ru>

BuildArch:	noarch

%description
A dark (black & white) theme for GTK2

%prep
%setup -c

%install
mkdir -p %buildroot%_datadir/themes
cp -a "./SlicknesS" %buildroot%_datadir/themes/SlicknesS

%files
%dir %_datadir/themes/SlicknesS
%_datadir/themes/SlicknesS/*

%changelog
* Fri Apr 12 2013 Motsyo Gennadi <drool@altlinux.ru> 2.2.2-alt1
- initial build for ALT Linux
