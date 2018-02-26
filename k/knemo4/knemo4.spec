Name: knemo4
Version: 0.7.2
Release: alt1

Summary: KNemo - the KDE Network Monitor
License: GPL
Group: Monitoring

Url: http://kde-apps.org/content/show.php?content=12956
Source: knemo-%version.tar

BuildRequires(pre): kde-common-devel
BuildRequires: gcc-c++ kde4libs-devel libXScrnSaver-devel libXau-devel libXcomposite-devel libXdamage-devel
BuildRequires: libXdmcp-devel libXft-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel
BuildRequires: libwireless-devel libxkbfile-devel net-tools wireless-tools xorg-xf86vidmodeproto-devel
BuildRequires: libnl-devel

%description
KNemo offers a network monitor similar to the one found in Windows.
For every network interface it displays an icon in the systray.

%prep
%setup -n knemo-%version

%build
%K4build

%install
%K4install
%K4find_lang knemo --with-kde

%files -f knemo.lang
%doc AUTHORS ChangeLog README
%_K4bindir/*
%_K4lib/*.so
%_K4xdg_apps/*.desktop
%_K4start/*.desktop
%_K4apps/knemo/*
%_K4srv/*
%_K4iconsdir/hicolor/*/apps/*.png
%_K4iconsdir/hicolor/*/status/*.png
%_K4iconsdir/hicolor/scalable/apps/knemo.svgz
%_K4conf_update/*

%changelog
* Tue Oct 18 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 0.7.2-alt1
- 0.7.2

* Wed Apr 13 2011 Aeliya Grevnyov <gray_graff@altlinux.org> 0.7.1-alt1
- 0.7.1
- move to standart place

* Tue Aug 03 2010 Aeliya Grevnyov <gray_graff@altlinux.org> 0.6.3-alt1
- 0.6.3
- kde4_alternate_placement (ALT #23455)
- real maintainer

* Sun Apr 11 2010 Michael Shigorin <mike@altlinux.org> 0.6.2-alt1
- 0.6.2 (closes: #23247)
- NB: this package needs a real maintainer

* Fri Mar 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Wed Oct 17 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.4.8-alt2
- added knemo-0.4.8-alt-sysfs-by-default.patch (close #13149)

* Wed May 30 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.4.8-alt1
- 0.4.8

* Mon Apr 02 2007 Valery Inozemtsev <shrek@altlinux.ru> 0.4.7-alt1
- 0.4.7

* Wed Oct 04 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.4.6-alt1
- 0.4.6

* Mon Aug 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.4.5-alt1
- 0.4.5

* Mon Aug 07 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.4.3-alt1
- 0.4.3

* Sat Jun 17 2006 Valery Inozemtsev <shrek@altlinux.ru> 0.4.2-alt1
- initial release

