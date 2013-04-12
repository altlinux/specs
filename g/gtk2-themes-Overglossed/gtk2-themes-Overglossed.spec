Name:		gtk2-themes-Overglossed
Summary:	Overglossed GTK2 theme
Version:	0.4
Release:	alt1
License:	GPLv2+
Url:		http://xfce-look.org/content/show.php/Overglossed?content=74813
Source:		74813-Overglossed.tar.gz
Group:		Graphical desktop/GNOME
Packager:	Motsyo Gennadi <drool@altlinux.ru>

BuildArch:	noarch

%description
Overglossed is a very overglossed theme for GTK2

%prep
%setup -c

%install
mkdir -p %buildroot%_datadir/themes
cp -a "./Overglossed" %buildroot%_datadir/themes/Overglossed

%files
%dir %_datadir/themes/Overglossed
%_datadir/themes/Overglossed/*

%changelog
* Fri Apr 12 2013 Motsyo Gennadi <drool@altlinux.ru> 0.4-alt1
- initial build for ALT Linux
