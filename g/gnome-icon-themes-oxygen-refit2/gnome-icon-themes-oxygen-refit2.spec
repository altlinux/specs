%define		icons		gnome-icon-theme-oxygen-refit2

Name: gnome-icon-themes-oxygen-refit2
Version: 2.3
Release: alt1

Summary: Additonal sets of icons for the GNOME 2 Desktop
Summary(ru_RU.UTF-8): Дополнительные наборы пиктограмм для GNOME 2
License: LGPL
Group: Graphical desktop/GNOME
Source0: OxygenRefit2-2.3.0.tar.bz2
Source1: OxygenRefit2-green-version.tar.bz2
Source2: OxygenRefit2-orange-version.tar.bz2
BuildArch: noarch

Requires: %{icons}-blue-version = %{version}-%{release}
Requires: %{icons}-green-version = %{version}-%{release}
Requires: %{icons}-orange-version = %{version}-%{release}

%description
Sets of icons for GNOME and XFCE based on original KDE4 icons - Oxygen. This package depends from
all versions of icons: blue,green,orange. It can be safely removed after install.

%description -l ru_RU.UTF-8
Набор пиктограмм для среды GNOME и XFCE основанный на оригинальном наборе
пиктограмм KDE4 - Oxygen. Данный пакет зависит от всех версий пиктограмм: синей,
зеленой и оранжевой. Сам пакет - виртуальный, его можно свободно удалить после установки.


%package -n %{icons}-blue-version
Summary:	Additional icons for GNOME
Summary(ru_RU.UTF-8): Дополнительный набор пиктограмм для GNOME 2
Group:		Graphical desktop/GNOME

%description -n %{icons}-blue-version
Sets of icons for GNOME and XFCE based on original KDE4 icons - Oxygen. This package contains a blue
version. 

%description -l ru_RU.UTF-8 -n %{icons}-blue-version
Набор пиктограмм для среды GNOME и XFCE основанный на оригинальном наборе
пиктограмм KDE4 - Oxygen. Данный пакет содержит синюю версию темы. 


%package -n %{icons}-green-version
Summary:	Additional icons for GNOME
Summary(ru_RU.UTF-8): Дополнительный набор пиктограмм для GNOME 2
Group:		Graphical desktop/GNOME

%description -n %{icons}-green-version
Sets of icons for GNOME and XFCE based on original KDE4 icons - Oxygen. This package contains a green
version. 

%description -l ru_RU.UTF-8 -n %{icons}-green-version
Набор пиктограмм для среды GNOME и XFCE основанный на оригинальном наборе
пиктограмм KDE4 - Oxygen. Данный пакет содержит зеленую версию темы. 


%package -n %{icons}-orange-version
Summary:	Additional icons for GNOME
Summary(ru_RU.UTF-8): Дополнительный набор пиктограмм для GNOME 2
Group:		Graphical desktop/GNOME

%description -n %{icons}-orange-version
Sets of icons for GNOME and XFCE based on original KDE4 icons - Oxygen. This package contains a orange
version. 

%description -l ru_RU.UTF-8 -n %{icons}-orange-version
Набор пиктограмм для среды GNOME и XFCE основанный на оригинальном наборе
пиктограмм KDE4 - Oxygen. Данный пакет содержит оранжевую версию темы. 


%prep 
%install
%__install -m755 -d $RPM_BUILD_ROOT%_iconsdir
%__tar xjf %SOURCE0 -C $RPM_BUILD_ROOT%_iconsdir
%__tar xjf %SOURCE1 -C $RPM_BUILD_ROOT%_iconsdir
%__tar xjf %SOURCE2 -C $RPM_BUILD_ROOT%_iconsdir

%__install -m755 -d $RPM_BUILD_ROOT%_docdir
%__mkdir $RPM_BUILD_ROOT%_docdir/%{icons}-blue-version
%__mv $RPM_BUILD_ROOT%_iconsdir/OxygenRefit2/COPYING $RPM_BUILD_ROOT%_docdir/%{icons}-blue-version/COPYING
%__mv $RPM_BUILD_ROOT%_iconsdir/OxygenRefit2/CREDITS $RPM_BUILD_ROOT%_docdir/%{icons}-blue-version/CREDITS
%__mv $RPM_BUILD_ROOT%_iconsdir/OxygenRefit2/ChangeLog $RPM_BUILD_ROOT%_docdir/%{icons}-blue-version/ChangeLog

%__mkdir $RPM_BUILD_ROOT%_docdir/%{icons}-green-version
%__mv $RPM_BUILD_ROOT%_iconsdir/OxygenRefit2-green-version/COPYING $RPM_BUILD_ROOT%_docdir/%{icons}-green-version/COPYING
%__mv $RPM_BUILD_ROOT%_iconsdir/OxygenRefit2-green-version/CREDITS $RPM_BUILD_ROOT%_docdir/%{icons}-green-version/CREDITS
%__mv $RPM_BUILD_ROOT%_iconsdir/OxygenRefit2-green-version/ChangeLog $RPM_BUILD_ROOT%_docdir/%{icons}-green-version/ChangeLog

%__mkdir $RPM_BUILD_ROOT%_docdir/%{icons}-orange-version
%__mv $RPM_BUILD_ROOT%_iconsdir/OxygenRefit2-orange-version/COPYING $RPM_BUILD_ROOT%_docdir/%{icons}-orange-version/COPYING
%__mv $RPM_BUILD_ROOT%_iconsdir/OxygenRefit2-orange-version/CREDITS $RPM_BUILD_ROOT%_docdir/%{icons}-orange-version/CREDITS
%__mv $RPM_BUILD_ROOT%_iconsdir/OxygenRefit2-orange-version/ChangeLog $RPM_BUILD_ROOT%_docdir/%{icons}-orange-version/ChangeLog

%files

%files -n %{icons}-blue-version
%_docdir/%{icons}-blue-version/* 
%_iconsdir/OxygenRefit2/*

%files -n %{icons}-green-version
%_docdir/%{icons}-green-version/*
%_iconsdir/OxygenRefit2-green-version/*

%files -n %{icons}-orange-version
%_docdir/%{icons}-orange-version/*
%_iconsdir/OxygenRefit2-orange-version/*

%changelog
* Fri Nov 7 2008 Denis Koryavov <dkoryavov@altlinux.org> 2.3-alt1
- initial build for Sisyphus
