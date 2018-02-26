%define themename Beos

Name: gnome-icon-theme-beos
Version: 0.1
Release: alt1

Summary: Additonal set of icons for the GNOME 2 desktop
Summary (ru_RU.UTF-8): Дополнительный набор пиктограмм для Gnome 2.
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source0: %themename.tar.bz2
BuildArch: noarch

%description
Alternative set of BeOS-like icons for Gnome.

%description -l ru_RU.UTF-8
Альтернативный набор пиктограмм похожих на BeOS для Gnome.

%prep
%setup -q -n %themename

%install
%__install -m755 -d $RPM_BUILD_ROOT%_iconsdir/%themename
%__mv * $RPM_BUILD_ROOT%_iconsdir/%themename


%files
%_iconsdir/*

%changelog
* Wed Jan 29 2003 Vyacheslav Dikonov <slava@altlinux.ru> 0.1-alt1
- first build

