Name:		gtk2-themes-SlicknesS-black
Summary:	SlicknesS-black GTK2 theme
Version:	0.9
Release:	alt1
License:	GPLv2+
Url:		http://xfce-look.org/content/show.php?action=content&content=73210
Source:		73210-SlicknesS-black.tar.gz
Group:		Graphical desktop/GNOME
Packager:	Motsyo Gennadi <drool@altlinux.ru>

BuildArch:	noarch

%description
SlicknesS Black is a very black modification of a SlicknesS theme

%prep
%setup -c

%install
mkdir -p %buildroot%_datadir/themes
cp -a "./SlicknesS-black" %buildroot%_datadir/themes/SlicknesS-black

%files
%dir %_datadir/themes/SlicknesS-black
%_datadir/themes/SlicknesS-black/*

%changelog
* Fri Apr 12 2013 Motsyo Gennadi <drool@altlinux.ru> 0.9-alt1
- initial build for ALT Linux
