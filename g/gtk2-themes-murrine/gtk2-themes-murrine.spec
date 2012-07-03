Name: gtk2-themes-murrine
Version: 1.0
Release: alt1

Summary: Murrine GTK2 themes
Summary (ru_RU.UTF-8): Набор тем Murrine для GTK2
License: GPL
Group: Graphical desktop/GNOME
Url: http://www.cimitan.com/murrine/
Source0: %{name}-%{version}.tar.bz2
BuildArch: noarch
Requires: libgtk-engine-murrine >= 0.53.1

%description
Murrine theme pack for GNOME and XFCE. Included themes:
MurrinaStormCloud
MurrinaStormCloudSilver
MurrinaOransun
MurrinaOranche
MurrinaLoveGray
MurrinaGilouche
MurrinaFancySky
MurrinaFancySea
MurrinaFancySand
MurrinaFancyGrass
MurrinaFancyEarth
MurrinaFancyCandy
MurrinaFancyAncient
MurrinaAquaIsh

%description -l ru_RU.UTF-8
Набор тем Murrine(также известных как Murrina) для GNOME и XFCE.
В набор включены следующие темы:
MurrinaStormCloud
MurrinaStormCloudSilver
MurrinaOransun
MurrinaOranche
MurrinaLoveGray
MurrinaGilouche
MurrinaFancySky
MurrinaFancySea
MurrinaFancySand
MurrinaFancyGrass
MurrinaFancyEarth
MurrinaFancyCandy
MurrinaFancyAncient
MurrinaAquaIsh

%install
%__install -m755 -d $RPM_BUILD_ROOT/%_datadir/themes
%__tar xjf %SOURCE0 -C $RPM_BUILD_ROOT/%_datadir/themes

%files
%defattr(-, root, root, 0755)
%_datadir/*

%changelog
* Wed Nov 12 2008 Denis Koryavov <dkoryavov@altlinux.org> 1.0-alt1
- Initial build.