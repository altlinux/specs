%define theme wonderland

Name: kde-icon-theme-%theme
Version: 1.0
Release: alt1

Summary: A set of Icons for KDE
Summary (ru_RU.UTF-8): Наборы пиктограмм для KDE
License: GPL
Group: Graphical desktop/KDE
Url: http://www.redhat.com

BuildArch: noarch

Provides: kde-icon-theme
Provides: icons-%theme = %version-%release
Obsoletes: gnome-kde-icon-theme-wonderland
Conflicts: kdelibs <= 3.1.0-alt8 gnome-kde-icon-theme-wonderland

Source: %theme-%version.tar.bz2

%description
Wonderland icons, also known as BlueCurve for KDE.

%description -l ru_RU.UTF-8
Набор пиктограмм "Страна чудес", также известный как BlueCurve, для KDE.

%prep
%setup -q -n %theme-%version

%install
%__install -m755 -d $RPM_BUILD_ROOT%_iconsdir/%theme
%__mv * $RPM_BUILD_ROOT%_iconsdir/%theme

%files
%_iconsdir/*

    
%changelog
* Fri Feb 07 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- first build

