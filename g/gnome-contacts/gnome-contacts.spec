%define ver_major 3.4

Name: gnome-contacts
Version: %ver_major.1
Release: alt1

Summary: Contacts manager for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://live.gnome.org/ThreePointOne/Features/Contacts

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.31.10
%define vala_ver 0.13.0
%define tp_glib_ver 0.17.5
%define folks_ver 0.6.4

BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel libtelepathy-glib-devel >= %tp_glib_ver
BuildRequires: libfolks-devel >= %folks_ver libvala-devel >= %vala_ver libnotify-devel libgnome-desktop3-devel
BuildRequires: libgnome-online-accounts-devel libgee-devel evolution-data-server-devel
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
%_datadir/applications/%name.desktop
%_datadir/glib-2.0/schemas/org.gnome.Contacts.gschema.xml
%doc AUTHORS README NEWS TODO

%changelog
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

