%define ver_major 3.22
%define plugins_ver 11
%define _libexecdir %_prefix/libexec
%define xdg_name org.gnome.Software

%def_enable gtkspell
%def_enable gudev
%def_enable gnome_desktop
%def_enable polkit
%def_disable firmware
%def_disable flatpak
%def_disable ostree
%def_disable limba
%def_disable packagekit

Name: gnome-software
Version: %ver_major.6
Release: alt0.1

Summary: Software manager for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Software

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.46
%define gtk_ver 3.20
%define appstream_glib_ver 0.6.5
%define json_glib_ver 1.1.1
%define soup_ver 2.52
%define packagekit_ver 1.1.0
%define gnome_desktop_ver 3.18
%define fwupd_ver 0.7.0
%define flatpak_ver 0.6.12
%define limba_ver 0.5.6

BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libappstream-glib-devel >= %appstream_glib_ver
BuildRequires: libjson-glib-devel >= %json_glib_ver
BuildRequires: libsoup-devel >= %soup_ver
BuildRequires: gnome-common rpm-build-xdg intltool yelp-tools xsltproc docbook-style-xsl
BuildRequires: libsqlite3-devel libsecret-devel gsettings-desktop-schemas-devel
BuildRequires: librpm-devel
%{?_enable_gudev:BuildRequires: libgudev-devel}
%{?_enable_gtkspell:BuildRequires: libgtkspell3-devel}
%{?_enable_gnome_desktop:BuildRequires: libgnome-desktop3-devel >= %gnome_desktop_ver}
%{?_enable_polkit:BuildRequires: libpolkit-devel}
%{?_enable_firmware:BuildRequires: libfwupd-devel >= %fwupd_ver}
%{?_enable_flatpak:BuildRequires: libflatpak-devel >= %flapak_ver}
%{?_enable_ostree:BuildRequires: libostree-devel >= %flapak_ver}
%{?_enable_limba:BuildRequires: liblimba-devel >= %limba_ver}
%{?_enable_packagekit:BuildRequires: libpackage-kit-devel >= %packagekit_ver}

%description
GNOME Software is for installing, removing and updating software.

%prep
%setup

%build
%configure \
	--disable-static \
	--disable-schemas-compile \
	%{subst_enable gtkspell} \
	%{subst_enable gudev} \
	%{?_enable_gnome_desktop:--enable-gnome-desktop} \
	%{subst_enable polkit} \
	%{subst_enable firmware} \
	%{subst_enable flatpak} \
	%{subst_enable ostree} \
	%{subst_enable limba} \
	%{subst_enable packagekit}
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_xdgconfigdir/autostart/%name-service.desktop
%_bindir/%name
%_libdir/gs-plugins-%plugins_ver/
%_desktopdir/%name-local-file.desktop
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/%name/
%_datadir/gnome-shell/search-providers/%xdg_name-search-provider.ini
%_iconsdir/hicolor/*x*/*/%xdg_name.png
%_iconsdir/hicolor/scalable/apps/%xdg_name-symbolic.svg
%_datadir/glib-2.0/schemas/org.gnome.software.gschema.xml
%_datadir/appdata/%xdg_name.appdata.xml
%_man1dir/%name.1.*
%doc AUTHORS README NEWS

#devel
%_includedir/%name/
%_pkgconfigdir/%name.pc
%_datadir/gtk-doc/html/%name/

%changelog
* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.6-alt0.1
- 3.22.6

* Mon Jan 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt0.1
- 3.22.5

* Fri Dec 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt0.1
- first preview for Sisyphus


