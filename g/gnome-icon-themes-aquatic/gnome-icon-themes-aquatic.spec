%define themename Aquatic

Name: gnome-icon-themes-aquatic
Version: 1.0
Release: alt2

Summary: Additonal sets of icons for the GNOME 2 desktop
Summary (ru_RU.UTF-8): Дополнительные наборы пиктограмм для Gnome 2.
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source0: %themename.tar.bz2
BuildArch: noarch

%description
Alternative sets of icons for Gnome in the spirit of Aqua:
World-Of-Aqua, Snow-Apple.

%description -l ru_RU.UTF-8
Альтернативные наборы пиктограмм для Gnome в стиле Аква:
Мир Aqua, Apple-снежный.

%prep
%setup -q -n %themename

%install
%__install -m755 -d $RPM_BUILD_ROOT%_iconsdir
%__mv * $RPM_BUILD_ROOT%_iconsdir


%files
%_iconsdir/*

%changelog
* Fri Feb 07 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt2
- fixes

* Wed Jan 29 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- first build

