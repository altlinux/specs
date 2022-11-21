%define translations_name xapp

%define libxappsdir /usr/lib/xapps

Name: xapps
Version: 2.4.1
Release: alt1

Summary: Libraries and common resources for XApps
License: %gpl3only
Group: Graphical desktop/GNOME
Url: https://github.com/linuxmint/xapps
Packager: Vladimir Didenko <cow@altlinux.org>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

AutoReqProv: nopython
%define __python %nil

Requires: lib%name = %version-%release
BuildRequires(pre): rpm-build-licenses rpm-build-gnome rpm-build-python3

# From configure.in
BuildPreReq: intltool >= 0.35
BuildPreReq: libgtk+3-devel >= 3.3.6
BuildPreReq: glib2-devel >= 2.35.0
BuildPreReq: libgio-devel >= 2.28.0
BuildPreReq: gtk-doc >= 1.4
BuildPreReq: gnome-common >= 2.8.0
BuildPreReq: gsettings-desktop-schemas-devel >= 3.5.91

BuildRequires: meson
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel libgnomekbd-devel
BuildRequires: vala-tools
BuildRequires: python3-module-pygobject3-devel
BuildRequires: libdbus-devel libdbusmenu-gtk3-devel

%add_python3_path %libxappsdir

%description
Libraries and common resources for XApps

%package -n %name-schemas
Summary: A collection of GSettings schemas for XApps
Group: Graphical desktop/GNOME
BuildArch: noarch

%description -n %name-schemas
A collection of GSettings schemas for XApps

%package -n %name-utils
Summary: A collection of utils for XApps
Group: Graphical desktop/GNOME
BuildArch: noarch

%description -n %name-utils
A collection of utils for XApps

%package -n %name-icons
Summary: XApps icons
Group: Graphical desktop/GNOME
BuildArch: noarch

%description -n %name-icons
XApps icons.

%package -n lib%name
Summary: XApps core libraries
Group: Graphical desktop/GNOME
Requires: %name-schemas

%description -n lib%name
XApps libraries.

%package -n lib%name-devel
Summary: XApps development libraries and includes
Group: Development/GNOME and GTK+
Requires: lib%name = %version-%release

%description -n lib%name-devel
XApps development libraries and includes

%package -n lib%name-gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the %name library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the %name
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the %name library

%package -n python3-module-%name-overrides
Summary: Python3 Xapp overrides Library
Group: Development/Python3

%description -n python3-module-%name-overrides
Python3 Xapp pverrides Library

%package -n %name-applet-constants
Summary: Common constants for XApps applets
Group: Graphical desktop/GNOME

%description -n %name-applet-constants
Common constants for XApps applets

%package -n xapp-sn-watcher
Summary: XApp Status Notifier Watcher
Group: Graphical desktop/GNOME

%description -n xapp-sn-watcher
XApp Status Notifier Watcher

%package -n mate-xapp-status-applet
Summary: XAppStatusIcon applet for mate panel
Group: Graphical desktop/GNOME
Requires: %name-applet-constants
BuildArch: noarch

%description -n mate-xapp-status-applet
XAppStatusIcon applet for mate panel

%prep
%setup -q -n %name-%version
%patch -p1

%build
%meson -D deprecated_warnings=false
%meson_build

%install
%meson_install

install -m 0755 -d %buildroot%_x11sysconfdir/profile.d
mv %buildroot%_x11sysconfdir/xinit/xinitrc.d/80xapp-gtk3-module.sh %buildroot%_x11sysconfdir/profile.d/xapp-gtk3-module.sh

%find_lang %translations_name

# This module name is too generic. I don't want to make it visible for
# the whole system
%filter_from_requires /python3[(]applet_constants[)]/d
%filter_from_provides /python3[(]applet_constants[)]/d

%files -n %name-schemas
%_datadir/glib-2.0/schemas/org.x.apps.*.xml

%files -n %name-icons
%_datadir/icons/hicolor/scalable/*/*

%files -n %name-utils
%_bindir/xfce4-set-wallpaper
# TODO: this scripts don't work without modifications in Alt Linux. Need to fix.
%exclude %_bindir/pastebin
%exclude %_bindir/upload-system-info


%files -n lib%name -f %translations_name.lang
%_libdir/*.so.*
%_libdir/gtk-3.0/modules/*.so
%_x11sysconfdir/profile.d/*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_vapidir/xapp.vapi
%_vapidir/xapp.deps
%_datadir/glade/catalogs/xapp-glade-catalog.xml

%files -n lib%name-gir
%_typelibdir/*

%files -n lib%name-gir-devel
%_girdir/*

%files -n python3-module-%name-overrides
%python3_sitelibdir/gi/overrides/XApp.py
%python3_sitelibdir/gi/overrides/__pycache__/*

%files -n %name-applet-constants
%dir %libxappsdir
%libxappsdir/applet_constants.*
%dir %libxappsdir/__pycache__/
%libxappsdir/__pycache__/*

%files -n xapp-sn-watcher
%_sysconfdir/xdg/autostart/xapp-sn-watcher.desktop
%_prefix/lib/xapps/sn-watcher/xapp-sn-watcher
%_datadir/dbus-1/services/org.x.StatusNotifierWatcher.service

%files -n mate-xapp-status-applet
%libxappsdir/mate-xapp-status-applet.py
%_datadir/dbus-1/services/org.mate.panel.applet.MateXAppStatusAppletFactory.service
%_datadir/mate-panel/applets/org.x.MateXAppStatusApplet.mate-panel-applet

%changelog
* Fri Nov 18 2022 Vladimir Didenko <cow@altlinux.org> 2.4.1-alt1
- 2.4.1

* Mon Sep 5 2022 Vladimir Didenko <cow@altlinux.org> 2.2.15-alt1
- 2.2.15

* Tue Aug 2 2022 Vladimir Didenko <cow@altlinux.org> 2.2.14-alt1
- 2.2.14

* Thu Jul 21 2022 Vladimir Didenko <cow@altlinux.org> 2.2.13-alt1
- 2.2.13

* Tue Jul 12 2022 Vladimir Didenko <cow@altlinux.org> 2.2.12-alt1
- 2.2.11

* Tue Jun 21 2022 Vladimir Didenko <cow@altlinux.org> 2.2.11-alt1
- 2.2.11

* Fri Jun 10 2022 Vladimir Didenko <cow@altlinux.org> 2.2.10-alt1
- 2.2.10

* Wed Jan 12 2022 Vladimir Didenko <cow@altlinux.org> 2.2.8-alt1
- 2.2.8

* Wed Dec 15 2021 Vladimir Didenko <cow@altlinux.org> 2.2.6-alt1
- 2.2.6

* Thu Nov 25 2021 Vladimir Didenko <cow@altlinux.org> 2.2.5-alt1
- 2.2.5

* Tue Nov 9 2021 Vladimir Didenko <cow@altlinux.org> 2.2.4-alt1
- 2.2.4

* Mon Aug 2 2021 Vladimir Didenko <cow@altlinux.org> 2.2.3-alt1
- 2.2.3-1-ge40a44c

* Mon Jun 28 2021 Vladimir Didenko <cow@altlinux.org> 2.2.2-alt1
- 2.2.2

* Wed Jun 16 2021 Vladimir Didenko <cow@altlinux.org> 2.2.1-alt1
- 2.2.1

* Fri May 28 2021 Vladimir Didenko <cow@altlinux.org> 2.2.0-alt1
- 2.2.0

* Wed Mar 10 2021 Vladimir Didenko <cow@altlinux.org> 2.0.7-alt1
- 2.0.7

* Tue Jan 12 2021 Vladimir Didenko <cow@altlinux.org> 2.0.6-alt1
- 2.0.6

* Mon Dec 21 2020 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt1
- 2.0.4-4-g4a0eb55

* Fri Dec 11 2020 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- 2.0.3

* Fri Nov 27 2020 Vladimir Didenko <cow@altlinux.org> 2.0.0-alt1
- 2.0.0

* Fri Sep 25 2020 Vladimir Didenko <cow@altlinux.org> 1.8.10-alt1
- 1.8.10

* Thu Sep 3 2020 Vladimir Didenko <cow@altlinux.org> 1.8.9-alt1
- 1.8.9

* Thu Jul 2 2020 Vladimir Didenko <cow@altlinux.org> 1.8.8-alt1
- 1.8.8

* Tue Jun 9 2020 Vladimir Didenko <cow@altlinux.org> 1.8.7-alt1
- 1.8.7

* Mon May 25 2020 Vladimir Didenko <cow@altlinux.org> 1.8.6-alt1
- 1.8.6

* Thu May 21 2020 Vladimir Didenko <cow@altlinux.org> 1.8.5-alt1
- 1.8.5

* Sat May 16 2020 Vladimir Didenko <cow@altlinux.org> 1.8.4-alt2
- add dependency on xapps-schemas to libxapps package

* Thu May 14 2020 Vladimir Didenko <cow@altlinux.org> 1.8.4-alt1
- 1.8.4

* Tue Feb 11 2020 Vladimir Didenko <cow@altlinux.org> 1.6.10-alt1
- 1.6.10

* Tue Jan 14 2020 Vladimir Didenko <cow@altlinux.org> 1.6.9-alt1
- 1.6.9

* Tue Dec 17 2019 Vladimir Didenko <cow@altlinux.org> 1.6.8-alt1
- 1.6.8

* Wed Dec 11 2019 Vladimir Didenko <cow@altlinux.org> 1.6.7-alt1
- 1.6.7

* Mon Dec 2 2019 Vladimir Didenko <cow@altlinux.org> 1.6.5-alt1
- 1.6.5

* Thu Nov 28 2019 Vladimir Didenko <cow@altlinux.org> 1.6.3-alt1
- 1.6.3

* Fri Nov 22 2019 Vladimir Didenko <cow@altlinux.org> 1.6.2-alt1
- 1.6.2

* Mon Nov 18 2019 Vladimir Didenko <cow@altlinux.org> 1.6.1-alt1
- 1.6.1
- remove Python 2 sub-package

* Thu Sep 12 2019 Vladimir Didenko <cow@altlinux.org> 1.4.9-alt1
- 1.4.9

* Wed Jul 10 2019 Vladimir Didenko <cow@altlinux.org> 1.4.8-alt1
- 1.4.8

* Tue Jun 25 2019 Vladimir Didenko <cow@altlinux.org> 1.4.7-alt1
- 1.4.7

* Tue Dec 25 2018 Vladimir Didenko <cow@altlinux.org> 1.4.5-alt1
- 1.4.5

* Tue Dec 4 2018 Vladimir Didenko <cow@altlinux.org> 1.4.4-alt1
- 1.4.4

* Tue Nov 20 2018 Vladimir Didenko <cow@altlinux.org> 1.4.2-alt1
- 1.4.2

* Wed Oct 31 2018 Vladimir Didenko <cow@altlinux.org> 1.4.0-alt1
- 1.4.0

* Fri Sep 14 2018 Vladimir Didenko <cow@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Sep 6 2018 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1.1
- Rebuild with pygobject 3.30

* Sat Apr 28 2018 Vladimir Didenko <cow@altlinux.org> 1.2.0-alt1
- 1.2.0-1-g6b33ff3

* Fri Oct 27 2017 Vladimir Didenko <cow@altlinux.org> 1.0.4-alt1
- 1.0.4

* Thu May 18 2017 Vladimir Didenko <cow@altlinux.org> 1.0.3-alt1
- 1.0.3

* Wed Nov 23 2016 Vladimir Didenko <cow@altlinux.org> 1.0.2-alt1
- 1.0.2-3-g4b700fe

* Tue Sep 27 2016 Vladimir Didenko <cow@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
