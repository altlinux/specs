%define themename NoiaWarm

Name: gnome-icon-theme-noia-warm
Version: 1.0
Release: alt3

Summary: A set of icons for GNOME 2
Summary (ru_RU.UTF-8): Набор пиктограмм для Gnome 2
License: GPL
Group: Graphical desktop/GNOME
Url: http://www.carlitus.net
Source: %themename.tar.bz2
BuildArch: noarch

%description
"Warm" Noia icons for Gnome.

%description -l ru_RU.UTF-8
"Тёплая" версия набора пиктограмм "Девушка" для Gnome 2.

%prep
%setup -q -n %themename

%install
%__install -m755 -d $RPM_BUILD_ROOT%_iconsdir/%themename
%__mv * $RPM_BUILD_ROOT%_iconsdir/%themename

%files
%_iconsdir/*

%changelog
* Wed Aug 18 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt3
- Fixed for GNOME 2.6

* Sat Sep 27 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt2
- 3 missing icons added

* Tue Apr 22 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- first build
