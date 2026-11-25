%define _unpackaged_files_terminate_build 1
%define base_id app.drey.PaperPlane

Name: paper-plane
Version: 0.1.0.beta.6
Release: alt1

Summary: Chat over Telegram on a modern and elegant client
License: GPL-3.0
Group: Networking/Instant messaging
Url: https://github.com/vitlav/paper-plane
Vcs: https://github.com/vitlav/paper-plane

ExcludeArch: %ix86

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Source2: config.toml

Patch1: 0006-fix-login-Use-buttons-styled-as-links-for-the-login-.patch
Patch2: 0007-fix-chat-history-Do-not-depend-on-a-patched-GTK.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: rust-cargo
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(shumate-1.0)
BuildRequires: pkgconfig(tdjson) >= 1.8.65
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
%patch1 -p1
%patch2 -p1
install -vD %SOURCE2 .cargo/config.toml

%build
%meson
%meson_build -v

%install
%meson_install
%find_lang --with-gnome %name

# remove unsupported by glibc locale
rm %buildroot%_datadir/locale/zh_Hans/LC_MESSAGES/paper-plane.mo

%files -f %name.lang
%_bindir/%name
%_desktopdir/%base_id.desktop
%_datadir/glib-2.0/schemas/%base_id.gschema.xml
%_iconsdir/hicolor/scalable/apps/%base_id.svg
%_iconsdir/hicolor/symbolic/apps/%base_id-symbolic.svg
%_datadir/metainfo/%base_id.metainfo.xml
%_datadir/%name/

%changelog
* Mon Nov 02 2026 Vitaly Lipatov <lav@altlinux.ru> 0.1.0.beta.6-alt1
- New version 0.1.0-beta.6 from the maintained fork
  https://github.com/vitlav/paper-plane.
- Ported to tdlib-rs and TDLib 1.8.65 (closes: #56829).
- Merged upstream pull requests: translations, replies chat, secret chat
  style, updated gtk-rs/libadwaita-rs dependencies.
- Fixed crash on quit and kept --test-dc sessions apart from production.
- Removed dependence on patched GTK and fixed login links.

* Mon Oct 27 2025 Anton Zhukharev <ancieg@altlinux.org> 0.1.0.beta.5-alt2.20.gab48a3e
- Applied workaround to not patch gtk4 (ALT#48770).

* Thu Oct 10 2024 Anton Zhukharev <ancieg@altlinux.org> 0.1.0.beta.5-alt1.20.gab48a3e
- Updated to ab48a3e.

* Mon Nov 20 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt0.5.beta5
- first build for Sisyphus
