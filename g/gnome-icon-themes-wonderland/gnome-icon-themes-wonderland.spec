%define themename Wonderland

Name: gnome-icon-themes-wonderland
Version: 1.0
Release: alt2

Summary: Additional sets of icons for GNOME 2
Summary (ru_RU.UTF-8): Наборы пиктограмм для Gnome 2
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source0: %themename.tar.bz2
BuildArch: noarch
Conflicts: gnome-kde-icon-theme-wonderland
Obsoletes: gnome-kde-icon-theme-wonderland

%description
Wonderland icons, also known as BlueCurve, and Bluesphere for Gnome.

%description -l ru_RU.UTF-8
Наборы пиктограмм "Страна чудес" (также известный как BlueCurve) и
Bluesphere для Gnome.

%prep
%setup -q -n %themename

%install
%__install -m755 -d $RPM_BUILD_ROOT%_iconsdir
%__mv * $RPM_BUILD_ROOT%_iconsdir


%files
%_iconsdir/*

%changelog
* Wed Aug 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt2
- updated from redhat-artwork-0.97

* Fri Feb 07 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- first build

