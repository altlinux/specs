%define themename K-Style

Name: gnome-icon-theme-k-style
Version: 1.0
Release: alt1

Summary: A set of icons for the GNOME 2 desktop
Summary (ru_RU.UTF-8): Набор пиктограмм для Gnome 2.
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source0: %themename.tar.bz2
BuildArch: noarch
Conflicts: gnome-icon-themes-k-style
Obsoletes: gnome-icon-themes-k-style

%description
Alternative set of K-Style icons for Gnome featuring the default KDE 2 look.

%description -l ru_RU.UTF-8
Альтернативный набор пиктограмм "Стиль-К" для Gnome, похожий на KDE 2. 

%prep
%setup -q -n %themename

%install
%__install -m755 -d $RPM_BUILD_ROOT%_iconsdir/%themename
%__mv * $RPM_BUILD_ROOT%_iconsdir/%themename


%files
%_iconsdir/*

%changelog
* Fri Feb 07 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- first build

