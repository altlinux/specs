%define		icons		icon-theme-gnome-colors

Name: icon-themes-gnome-colors
Version: 3.6
Release: alt1

Summary: Additonal sets of icons for the GNOME and Xfce
Summary(ru_RU.UTF-8): Набор пиктограмм GNOME colors для GNOME и Xfce
License: GPL
URL: http://www.gnome-look.org/content/show.php?content=82562
Packager: Denis Koryavov <dkoryavov@altlinux.org>

Group: Graphical desktop/GNOME
Source0: gnome-colors-brave-%{version}.tar.gz
Source1: gnome-colors-human-%{version}.tar.gz
Source2: gnome-colors-noble-%{version}.tar.gz
Source3: gnome-colors-wine-%{version}.tar.gz
Source4: gnome-colors-wise-%{version}.tar.gz
Source5: gnome-colors-doc-%{version}.tar.gz
BuildArch: noarch

Requires: %{icons}-brave = %{version}-%{release}
Requires: %{icons}-human = %{version}-%{release}
Requires: %{icons}-noble = %{version}-%{release}
Requires: %{icons}-wine  = %{version}-%{release}
Requires: %{icons}-wise  = %{version}-%{release}

%description
Sets of icons for GNOME and XFCE based on original icons - Tango. This package depends from
all versions of icons: Brave, Human, Noble, Wine, Wise. It can be safely removed after install.

%description -l ru_RU.UTF-8
Набор пиктограмм GNOME colors для среды GNOME и XFCE основанный на оригинальном наборе
пиктограмм Tango. Данный пакет зависит от всех версий пиктограмм c палитрами 
Brave, Human, Noble, Wine и Wise. Сам пакет - виртуальный, его можно свободно 
удалить после установки.


%package -n %{icons}-brave
Summary:	Additional icons for GNOME and Xfce
Summary(ru_RU.UTF-8): Дополнительный набор пиктограмм для GNOME 2 и Xfce
Group:		Graphical desktop/GNOME

%description -n %{icons}-brave
Sets of icons for GNOME and XFCE based on original Tango. This package contains version 
with a Brave palette.

%description -l ru_RU.UTF-8 -n %{icons}-brave
Набор пиктограмм для среды GNOME и XFCE основанный на оригинальном наборе
пиктограмм Tango. Данный пакет содержит версию пиктограмм GNOME colors с палитрой Brave.


%package -n %{icons}-human
Summary:	Additional icons for GNOME and Xfce
Summary(ru_RU.UTF-8): Дополнительный набор пиктограмм для GNOME и Xfce
Group:		Graphical desktop/GNOME

%description -n %{icons}-human
Sets of icons for GNOME and XFCE based on original Tango. This package contains version 
with a Human palette.

%description -l ru_RU.UTF-8 -n %{icons}-human
Набор пиктограмм для среды GNOME и XFCE основанный на оригинальном наборе
пиктограмм Tango. Данный пакет содержит версию пиктограмм GNOME colors с палитрой Human. 


%package -n %{icons}-noble
Summary:	Additional icons for GNOME and Xfce
Summary(ru_RU.UTF-8): Дополнительный набор пиктограмм для GNOME и Xfce
Group:		Graphical desktop/GNOME

%description -n %{icons}-noble
Sets of icons for GNOME and XFCE based on original Tango. This package contains version 
with a Noble palette.. 

%description -l ru_RU.UTF-8 -n %{icons}-noble
Набор пиктограмм для среды GNOME и XFCE основанный на оригинальном наборе
пиктограмм Tango. Данный пакет содержит версию пиктограмм GNOME colors с палитрой Noble.


%package -n %{icons}-wine
Summary:	Additional icons for GNOME and Xfce
Summary(ru_RU.UTF-8): Дополнительный набор пиктограмм для GNOME и Xfce
Group:		Graphical desktop/GNOME

%description -n %{icons}-wine
Sets of icons for GNOME and XFCE based on original Tango. This package contains version 
with a Wine palette.. 

%description -l ru_RU.UTF-8 -n %{icons}-wine
Набор пиктограмм для среды GNOME и XFCE основанный на оригинальном наборе
пиктограмм Tango. Данный пакет содержит версию пиктограмм GNOME colors с палитрой Wine.

%package -n %{icons}-wise
Summary:	Additional icons for GNOME and Xfce
Summary(ru_RU.UTF-8): Дополнительный набор пиктограмм для GNOME и Xfce
Group:		Graphical desktop/GNOME

%description -n %{icons}-wise
Sets of icons for GNOME and XFCE based on original Tango. This package contains version 
with a Wise palette.. 

%description -l ru_RU.UTF-8 -n %{icons}-wise
Набор пиктограмм для среды GNOME и XFCE основанный на оригинальном наборе
пиктограмм Tango. Данный пакет содержит версию пиктограмм GNOME colors с палитрой Wise.

%prep 
%install
%__install -m755 -d $RPM_BUILD_ROOT%_iconsdir

%__tar xzf %SOURCE0 -C $RPM_BUILD_ROOT%_iconsdir
%__mv $RPM_BUILD_ROOT%_iconsdir/gnome-colors-brave-%{version} $RPM_BUILD_ROOT%_iconsdir/gnome-colors-brave

%__tar xzf %SOURCE1 -C $RPM_BUILD_ROOT%_iconsdir
%__mv $RPM_BUILD_ROOT%_iconsdir/gnome-colors-human-%{version} $RPM_BUILD_ROOT%_iconsdir/gnome-colors-human

%__tar xzf %SOURCE2 -C $RPM_BUILD_ROOT%_iconsdir
%__mv $RPM_BUILD_ROOT%_iconsdir/gnome-colors-noble-%{version} $RPM_BUILD_ROOT%_iconsdir/gnome-colors-noble

%__tar xzf %SOURCE3 -C $RPM_BUILD_ROOT%_iconsdir
%__mv $RPM_BUILD_ROOT%_iconsdir/gnome-colors-wine-%{version} $RPM_BUILD_ROOT%_iconsdir/gnome-colors-wine

%__tar xzf %SOURCE4 -C $RPM_BUILD_ROOT%_iconsdir
%__mv $RPM_BUILD_ROOT%_iconsdir/gnome-colors-wise-%{version} $RPM_BUILD_ROOT%_iconsdir/gnome-colors-wise


%__tar xzf %SOURCE5 -C $RPM_BUILD_ROOT%_iconsdir
%__cp $RPM_BUILD_ROOT%_iconsdir/gnome-colors-doc-%{version}/* $RPM_BUILD_ROOT%_iconsdir/gnome-colors-brave
%__cp $RPM_BUILD_ROOT%_iconsdir/gnome-colors-doc-%{version}/* $RPM_BUILD_ROOT%_iconsdir/gnome-colors-human
%__cp $RPM_BUILD_ROOT%_iconsdir/gnome-colors-doc-%{version}/* $RPM_BUILD_ROOT%_iconsdir/gnome-colors-noble
%__cp $RPM_BUILD_ROOT%_iconsdir/gnome-colors-doc-%{version}/* $RPM_BUILD_ROOT%_iconsdir/gnome-colors-wine
%__cp $RPM_BUILD_ROOT%_iconsdir/gnome-colors-doc-%{version}/* $RPM_BUILD_ROOT%_iconsdir/gnome-colors-wise
%__rm -rf $RPM_BUILD_ROOT%_iconsdir/gnome-colors-doc-%{version}

%files

%files -n %{icons}-brave
%_iconsdir/gnome-colors-brave/*

%files -n %{icons}-human
%_iconsdir/gnome-colors-human/*

%files -n %{icons}-noble
%_iconsdir/gnome-colors-noble/*

%files -n %{icons}-wine
%_iconsdir/gnome-colors-wine/*

%files -n %{icons}-wise
%_iconsdir/gnome-colors-wise/*

%changelog
* Thu May 21 2009 Denis Koryavov <dkoryavov@altlinux.org> 3.6-alt1
- First build for Sisyphus
