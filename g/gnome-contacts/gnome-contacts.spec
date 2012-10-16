%define ver_major 3.6
%define _libexecdir %_prefix/libexec
%define gst_api_ver 1.0
%def_with cheese

Name: gnome-contacts
Version: %ver_major.1
Release: alt1

Summary: Contacts manager for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://live.gnome.org/ThreePointOne/Features/Contacts

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.31.10
%define gtk_ver 3.4.0
%define vala_ver 0.17.2
%define tp_glib_ver 0.17.5
%define folks_ver 0.7.3
%define eds_ver 3.5.3
%define cheese_ver 3.5.90

BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver libtelepathy-glib-devel >= %tp_glib_ver
BuildRequires: libfolks-devel >= %folks_ver libvala-devel >= %vala_ver libnotify-devel libgnome-desktop3-devel
BuildRequires: libgnome-online-accounts-devel libgee-devel evolution-data-server-devel >= %eds_ver
%{?_with_cheese:BuildRequires: gstreamer%gst_api_ver-devel libcheese-devel >= %cheese_ver}
BuildRequires: intltool

%description
%name is a standalone contacts manager for GNOME desktop.

%prep
%setup -q

%build
%configure
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_libexecdir/gnome-contacts-search-provider
%_datadir/applications/%name.desktop
%_datadir/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%_datadir/dbus-1/services/org.gnome.Contacts.SearchProvider.service
%_datadir/gnome-shell/search-providers/gnome-contacts-search-provider.ini
%doc AUTHORS README NEWS

%changelog
* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue May 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Thu Oct 20 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Wed Oct 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0.1-alt1
- 3.2.0.1

* Fri Sep 09 2011 Yuri N. Sedunov <aris@altlinux.org> 0.1.4.1-alt1
- first build for Sisyphus

