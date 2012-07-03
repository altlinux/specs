%define themename Crystal

Name: gnome-icon-themes-crystal
Version: 1.0
Release: alt1

Summary: Additonal sets of icons for the GNOME 2 desktop
Summary (ru_RU.UTF-8): Дополнительные наборы пиктограмм для Gnome 2.
License: GPL
Group: Graphical desktop/GNOME
Url: http://art.gnome.org
Source0: %themename.tar.bz2
BuildArch: noarch
Conflicts: gnome-icon-themes-k-style
Obsoletes: gnome-icon-themes-k-style

%description
Alternative sets of icons for Gnome featuring the KDE look for
cross-desktop consistency: Crystal, Crystal-Green, Crystal-Orange, 
Crystal-Red, Crystal-Violet, Crystal-Yellow and IceCrystal.

%description -l ru_RU.UTF-8
Альтернативные наборы пиктограмм для Gnome, похожие на темы KDE и
помогающие достичь единообразия рабочей среды: Кристалл, Зелёный 
кристалл, Оранжевый кристалл, Красный кристалл, Фиолетовый кристалл,
Жёлтый кристалл и Ледяной кристалл.

%prep
%setup -q -n %themename

%install
%__install -m755 -d $RPM_BUILD_ROOT%_iconsdir
%__mv * $RPM_BUILD_ROOT%_iconsdir


%files
%_iconsdir/*

%changelog
* Fri Feb 07 2003 Vyacheslav Dikonov <slava@altlinux.ru> 1.0-alt1
- first build

