%define ver_major 3.4
%define gst_api_ver 1.0
%def_enable libcoverart

Name: goobox
Version: %ver_major.2
Release: alt1

Summary: CD player and ripper for GNOME
License: LGPLv2+
Group: Sound

URL: http://people.gnome.org/~paobac/goobox/
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

# from configure.in
%define gtk_ver 3.6.0

Requires: dconf gnome-icon-theme

BuildRequires: gcc-c++ gnome-common intltool yelp-tools
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildRequires: libnotify-devel libSM-devel
BuildRequires: libmusicbrainz5-devel gst-plugins%gst_api_ver-devel
BuildRequires: libbrasero-devel libdiscid-devel
%{?_enable_libcoverart:BuildRequires: libcoverart-devel}

%description
Goobox is a CD player and ripper well integrated with the GNOME environment.

%prep
%setup
# fix libcoverart required version
subst 's|1\.0\.0beta1|1.0.0|' configure*

%build
%autoreconf
%configure \
	--disable-schemas-compile \
	%{subst_enable libcoverart}
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%name.desktop
%_iconsdir/hicolor/*x*/apps/%name.png
%_iconsdir/hicolor/scalable/apps/%name-symbolic.svg
%_datadir/glib-2.0/schemas/org.gnome.Goobox.gschema.xml
%_datadir/GConf/gsettings/goobox.convert
%_datadir/appdata/%name.appdata.xml
%doc AUTHORS NEWS README TODO


%changelog
* Mon Oct 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Feb 16 2015 Yuri N. Sedunov <aris@altlinux.org> 3.3.3-alt1
- 3.3.3

* Mon Dec 01 2014 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt2
- rebuilt against libmusicbrainz5.so.1

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Thu Mar 28 2013 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Sun Mar 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.1.2-alt1
- first build for people/gnome

