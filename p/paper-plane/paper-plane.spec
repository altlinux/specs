%def_enable snapshot
%define ver_major 0.1
%define beta .beta5
%define rdn_name app.drey.PaperPlane

%def_disable bootstrap
%def_enable check

Name: paper-plane
Version: %ver_major.0
Release: alt0.5%beta

Summary: Telegram client for GNOME desktop
License: GPL-3.0
Group: Networking/Instant messaging
Url: https://github.com/paper-plane-developers/paper-plane

%if_disabled snapshot
Source: %url/archive/v%version/%name-%version%beta.tar.gz
%else
Vcs: https://github.com/paper-plane-developers/paper-plane.git
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

ExclusiveArch: x86_64 aarch64

%define glib_ver 2.76
%define gtk_ver 4.12
%define adwaita_ver 1.4
%define td_ver 1.8.19
%define gst_ver 1.20

Requires: gst-plugins-base1.0 >= %gst_ver
Requires: gst-plugins-bad1.0 >= %gst_ver

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson rust-cargo
BuildRequires: /usr/bin/appstream-util desktop-file-utils
BuildRequires: blueprint-compiler typelib(Adw)
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: pkgconfig(shumate-1.0)
BuildRequires: pkgconfig(tdjson) >= %td_ver
BuildRequires: pkgconfig(dbus-1)
%{?_enable_check:BuildRequires: clippy}

BuildRequires: pkgconfig(rlottie)
# for bindgen
BuildRequires: clang-devel

%description
Paper Plane is an alternative Telegram client.
It uses libadwaita for its user interface and strives to meet the design
principles of the GNOME desktop.

Paper Plane is still under development and not yet feature-complete.
However, the following things are already working:

- The use of multiple accounts at the same time.
- Viewing text messages, images, stickers and files.
- Sending text messages and images.
- Replying to messages.
- Searching for groups and persons.

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

# try to build with current tdlib
sed -i '/tdjson/s/==/>=/' meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test -t 2

%files -f %name.lang
%_bindir/%name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*


%changelog
* Mon Nov 20 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt0.5.beta5
- first build for Sisyphus


