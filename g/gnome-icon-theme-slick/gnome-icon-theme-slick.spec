%define themename Slick

Name: gnome-icon-theme-slick
Version: 1.0
Release: alt2

Summary: Additonal set of icons for the GNOME 2 desktop
Summary (ru_RU.UTF-8): Дополнительный набор пиктограмм для Gnome 2.
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source0: %themename.tar.bz2
BuildArch: noarch

%description
Alternative set of icons for Gnome based on the KDE Slick style.

%description -l ru_RU.UTF-8
Альтернативный набор пиктограмм для Gnome на основе стиля Slick из KDE.

%prep
%setup -q -n %themename

%install
%__install -m755 -d $RPM_BUILD_ROOT%_iconsdir/%themename
%__mv * $RPM_BUILD_ROOT%_iconsdir/%themename


%files
%_iconsdir/*

%changelog
* Wed Aug 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt2
- updated for GNOME 2.6

* Fri Feb 07 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- first build, OO icons



