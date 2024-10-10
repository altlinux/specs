%define _unpackaged_files_terminate_build 1
%define base_id app.drey.PaperPlane

Name: paper-plane
Version: 0.1.0.beta.5
Release: alt1.20.gab48a3e

Summary: Chat over Telegram on a modern and elegant client
License: GPL-3.0
Group: Networking/Instant messaging
Url: https://github.com/paper-plane-developers/paper-plane
Vcs: https://github.com/paper-plane-developers/paper-plane

ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(shumate-1.0)
BuildRequires: pkgconfig(tdjson)
BuildRequires: blueprint-compiler
BuildRequires: librlottie-devel
BuildRequires: clang-devel

%description
Paper Plane is an alternative Telegram client. It uses libadwaita for its user
interface and strives to meet the design principles of the GNOME desktop.

Paper Plane is still under development and not yet feature-complete. However,
the following things are already working:
* The use of multiple accounts at the same time.
* Viewing text messages, images, stickers and files.
* Sending text messages and images.
* Replying to messages.
* Searching for groups and persons.

%prep
%setup -a1
%autopatch -p1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build -v

%install
%meson_install
%find_lang --with-gnome %name
echo '%%lang(zh) %_datadir/locale/zh_Hans/LC_MESSAGES/paper-plane.mo' >> %name.lang

%files -f %name.lang
%_bindir/%name
%_desktopdir/%base_id.desktop
%_datadir/glib-2.0/schemas/%base_id.gschema.xml
%_iconsdir/hicolor/scalable/apps/%base_id.svg
%_iconsdir/hicolor/symbolic/apps/%base_id-symbolic.svg
%_datadir/metainfo/%base_id.metainfo.xml
%_datadir/%name/

%changelog
* Thu Oct 10 2024 Anton Zhukharev <ancieg@altlinux.org> 0.1.0.beta.5-alt1.20.gab48a3e
- Updated to ab48a3e.

%changelog
* Mon Nov 20 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt0.5.beta5
- first build for Sisyphus
