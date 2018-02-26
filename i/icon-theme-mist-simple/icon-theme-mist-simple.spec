%define themename mist-simple

Name: icon-theme-%themename
Version: 0.2
Release: alt1

Summary: Additonal set of icons for the Mist theme
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source0: %name-%version.tar
BuildArch: noarch
Packager: Eugene Prokopiev <enp@altlinux.ru>

Requires: icon-theme-mist

%description
Additonal set of icons for the Mist theme

%prep
%setup

%install
install -m755 -d $RPM_BUILD_ROOT%_iconsdir/%themename
mv * $RPM_BUILD_ROOT%_iconsdir/%themename


%files
%_iconsdir/*

%changelog
* Mon Jul 25 2011 Eugene Prokopiev <enp@altlinux.ru> 0.2-alt1
- use old gnome desktop icon

* Wed Apr 21 2010 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt1
- first build


