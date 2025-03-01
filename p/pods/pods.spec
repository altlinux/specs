%define APP_ID com.github.marhkb.Pods
#Validate clippy FAIL
%def_disable check

Name: pods
Version: 2.1.2
Release: alt2

Summary: Manage your Podman containers
License: GPL-3.0
Group: Graphical desktop/GNOME

Url: https://github.com/marhkb/pods
Vcs: https://github.com/marhkb/pods
Source0: %name-%version.tar
Source1: %name-vendor.tar
Source2: config.toml

Requires: podman

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: pkgconfig(glib-2.0) >= 2.66
BuildRequires: pkgconfig(gio-2.0) >= 2.66
BuildRequires: pkgconfig(gtk4) >= 4.16.0
BuildRequires: pkgconfig(libadwaita-1) >= 1.6
BuildRequires: pkgconfig(gtksourceview-5) >= 4.90
BuildRequires: pkgconfig(vte-2.91-gtk4) >= 0.70.0
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: libgio
%endif

ExcludeArch: %ix86

%description
Pods is a frontend for podman. It uses libadwaita for its user interface
and strives to meet the design principles of GNOME.

With Pods you can, among other things:

* Connect to local and remote Podman instances.
* Easily overview images, containers and pods.
* View prepared information about images, containers, and pods.
* Inspect images, containers and pods.
* View and search container logs.
* Monitor processes of containers and pods.
* Download images and build them using Dockerfiles.
* Create pods and containers.
* Control the lifecycle of containers
  and pods (in bulk) (start, stop, pause, etc.).
* Delete images, containers, and pods (in bulk).
* Prune images.
* Rename containers.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build

%install
%meson_install
# drop unknown languages, find known
rm -r %buildroot%_datadir/locale/zh_Hans
%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%APP_ID.desktop
%_datadir/glib-2.0/schemas/%APP_ID.gschema.xml
%_iconsdir/hicolor/*/apps/%{APP_ID}*.svg
%_datadir/metainfo/%APP_ID.metainfo.xml
%_datadir/%name

%changelog
* Fri Feb 28 2025 Oleg Shchavelev <oleg@altlinux.org> 2.1.2-alt2
- Fix debuginfo generation for release builds

* Fri Feb 28 2025 Oleg Shchavelev <oleg@altlinux.org> 2.1.2-alt1
- Initial build
