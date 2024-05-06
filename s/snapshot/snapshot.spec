%def_disable snapshot
%define ver_major 46
%define beta %nil
%define xdg_name org.gnome.Snapshot

%def_disable bootstrap
%def_enable check

Name: snapshot
Version: %ver_major.3
Release: alt1%beta

Summary: GNOME Camera
License: GPL-3.0-or-later
Group: Video
Url: https:/apps.gnome.org/Snapshot

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/snapshot.git
Source: %name-%version%beta.tar
%endif

%define glib_ver 2.76
%define pango_ver 1.51
%define gtk_ver 4.14
%define adwaita_ver 1.5
%define gst_ver 1.20

Provides: gnome-camera = %EVR
Requires: gst-plugins-base1.0 >= %gst_ver
Requires: gst-plugins-bad1.0 >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(gio-2.0) >= %glib_ver
BuildRequires: pkgconfig(pango) >= %pango_ver
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(gstreamer-video-1.0) >= %gst_ver
BuildRequires: pkgconfig(gstreamer-plugins-bad-1.0) >= %gst_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils clippy}

%description
A simple application to take pictures and videos from camera on your
computer, tablet, or phone.

%prep
%setup -n %name-%version%beta
# %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README*


%changelog
* Mon May 06 2024 Yuri N. Sedunov <aris@altlinux.org> 46.3-alt1
- 46.3

* Thu Apr 11 2024 Yuri N. Sedunov <aris@altlinux.org> 46.2-alt1
- 46.2

* Sun Mar 31 2024 Yuri N. Sedunov <aris@altlinux.org> 46.1-alt1
- 46.1

* Fri Mar 15 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Thu Dec 28 2023 Yuri N. Sedunov <aris@altlinux.org> 45.2-alt1
- 45.2

* Sat Dec 09 2023 Yuri N. Sedunov <aris@altlinux.org> 45.1-alt1
- 45.1
- enabled %%check

* Sat Sep 16 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Sat Jul 01 2023 Yuri N. Sedunov <aris@altlinux.org> 45-alt0.1.alpha
- first build for people/gnome (45.alpha)




