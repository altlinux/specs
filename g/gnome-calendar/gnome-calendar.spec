%def_disable snapshot

%define xdg_name org.gnome.Calendar
%define ver_major 3.26
%define _libexecdir %_prefix/libexec

%def_enable gtk_doc

Name: gnome-calendar
Version: %ver_major.3
Release: alt1

Summary: Calendar application for GNOME
License: %gpl2plus
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Calendar

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-build-licenses rpm-build-gnome

%define glib_ver 2.44.0
%define gtk_ver 3.22.0
%define ical_ver 1.0.1
%define eds_ver 3.18.0
%define gsds_ver 3.21.2

BuildPreReq: meson intltool yelp-tools libappstream-glib-devel
BuildPreReq: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildPreReq: libical-devel >= %ical_ver libicu-devel
BuildRequires: libgnome-online-accounts-devel vala-tools
BuildRequires: gobject-introspection-devel
BuildRequires: evolution-data-server-devel >= %eds_ver
BuildRequires: gsettings-desktop-schemas-devel >= %gsds_ver
%{?_enable_gtk_doc:BuildRequires: gtk-doc}

%description
Calendar is a calendar application for GNOME.

%package devel-doc
Summary: Development documentation for GNOME Calendar
Group: Development/GNOME and GTK+
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package provides Calendar reference manual.


%prep
%setup

%build
%meson \
    -Denable-schemas-compile=false \
    %{?_enable_gtk_doc:-Denable-gtk-doc=true}
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini
%_desktopdir/%xdg_name.desktop
#%_man1dir/*
%_datadir/glib-2.0/schemas/org.gnome.calendar.gschema.xml
%_datadir/glib-2.0/schemas/org.gnome.calendar.enums.xml
%_iconsdir/hicolor/*x*/apps/%xdg_name.png
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc NEWS README.md

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%name
%endif

%changelog
* Wed Jan 17 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt2
- updated to 3.26.2-19-g954c48d
- built against libical.so.3

* Thu Oct 05 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Thu Sep 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Fri Jun 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Mon Apr 24 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Wed Mar 01 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Tue Dec 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Sun Oct 02 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed Sep 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.4-alt1
- 3.20.4

* Wed Aug 31 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Thu Apr 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Mar 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2.1-alt2
- rebuilt against libical.so.2

* Thu Dec 24 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2.1-alt1
- 3.18.2.1

* Wed Dec 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Sat Oct 17 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Thu Apr 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Fri Dec 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.15.3.1-alt1
- first build for people/gnome


