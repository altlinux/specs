Name: gtk2-themes-aurora
Version: 1.5.1
Release: alt1

Summary: Aurora GTK2 themes
Summary (ru): Набор тем Aurora для GTK2
License: GPL
Group: Graphical desktop/GNOME
Source0: %{name}-%{version}.tar.bz2
BuildArch: noarch
Requires: libgtk-engine-aurora >= 1.5
Packager: Denis Koryavov <dkoryavov@altlinux.org>

%description
Aurora theme pack for GNOME and XFCE. Included themes:
Aurora
Aurora-Midnight
Aurora-looks
Aurora Luminix
Aurora e17 Detour
Aurora Borealis

%description -l ru
Набор тем Aurora для GNOME и XFCE.
В набор включены следующие темы:
Aurora
Aurora-Midnight
Aurora-looks
Aurora Luminix
Aurora e17 Detour
Aurora Borealis

%install
%__install -m755 -d $RPM_BUILD_ROOT/%_datadir/themes
%__tar xjf %SOURCE0 -C $RPM_BUILD_ROOT/%_datadir/themes

%files
%defattr(-, root, root, 0755)
%_datadir/*

%changelog
* Wed Apr 22 2009 Denis Koryavov <dkoryavov@altlinux.org> 1.5.1-alt1
- Version update to 1.5.1

* Wed Nov 26 2008 Denis Koryavov <dkoryavov@altlinux.org> 1.0-alt1
- Initial build.
