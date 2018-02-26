%define themename d3a-icons

Name: gnome-icon-theme-d3a
Version: 20051403
Release: alt1

Summary: Additonal set of icons for the GNOME 2 desktop
Summary (ru_RU.UTF-8): Набор значков для Gnome 2.
License: Other
Group: Graphical desktop/GNOME
Url: http://gnome-look.org
Source0: %themename.tar.gz
BuildArch: noarch

%description
A set of icons for Gnome. Original icons created by Milosz Wlazlo,
additional mimetypes' icons by Nicola Pizurica.

%description -l ru_RU.UTF-8
Набор значков для Gnome. Оригинальные значки нарисованы Милошем Влазло,
дополнительные значки для типов файлов нарисовал Никола Пизурица.

%prep
%setup -q -n %themename

%install
%__install -m755 -d %buildroot%_iconsdir/d3a
%__mv * %buildroot%_iconsdir/d3a

%files
%_iconsdir/*

%changelog
* Fri Nov 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 20051403-alt1
- Initial Sisyphus package.

