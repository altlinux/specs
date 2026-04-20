%define _unpackaged_files_terminate_build 1
%define app_id io.gitlab.ilshat_apps.gitpulsar

Name: gitpulsar
Version: 0.7.0
Release: alt1

Summary: GNOME-native Git GUI written in Rust with GTK4/libadwaita
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME

URL: https://gitlab.com/ilshat-apps/gitpulsar
VCS: https://gitlab.com/ilshat-apps/gitpulsar
Source: %name-%version.tar
Source1: %name-vendor.tar

BuildRequires: rust-cargo
BuildRequires: rpm-macros-rust
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: oniguruma-devel
BuildRequires: libssl-devel

Requires: icon-theme-hicolor

%description
GitPulsar is a GNOME-native Git GUI written in Rust with GTK4/libadwaita.
It helps you work with Git repositories through a clean, visual interface.

%prep
%setup -a1
%rust_prep

%build
%rust_build

%install
%rust_install gitpulsar-gtk
install -Dm644 data/%app_id.desktop %buildroot%_datadir/applications/%app_id.desktop
sed -i 's|Icon=%app_id|Icon=%_datadir/icons/hicolor/scalable/apps/%app_id.svg|' \
    %buildroot%_datadir/applications/%app_id.desktop
install -Dm644 data/%app_id.metainfo.xml %buildroot%_datadir/metainfo/%app_id.metainfo.xml
install -Dm644 data/icons/hicolor/scalable/apps/%app_id.svg \
    %buildroot%_iconsdir/hicolor/scalable/apps/%app_id.svg
install -Dm644 data/icons/hicolor/scalable/actions/branch-compare-symbolic.svg \
    %buildroot%_iconsdir/hicolor/scalable/actions/branch-compare-symbolic.svg
install -Dm644 data/icons/hicolor/scalable/actions/branch-fork-symbolic.svg \
    %buildroot%_iconsdir/hicolor/scalable/actions/branch-fork-symbolic.svg
install -Dm644 data/icons/hicolor/scalable/actions/commit-symbolic.svg \
    %buildroot%_iconsdir/hicolor/scalable/actions/commit-symbolic.svg
install -Dm644 data/icons/hicolor/scalable/actions/git-symbolic.svg \
    %buildroot%_iconsdir/hicolor/scalable/actions/git-symbolic.svg
install -Dm644 data/icons/hicolor/scalable/actions/history-undo-symbolic.svg \
    %buildroot%_iconsdir/hicolor/scalable/actions/history-undo-symbolic.svg
install -Dm644 data/icons/hicolor/scalable/actions/pull-request-merged-symbolic.svg \
    %buildroot%_iconsdir/hicolor/scalable/actions/pull-request-merged-symbolic.svg
install -Dm644 data/icons/hicolor/scalable/actions/pull-request-symbolic.svg \
    %buildroot%_iconsdir/hicolor/scalable/actions/pull-request-symbolic.svg
install -Dm644 data/icons/hicolor/scalable/actions/tag-outline-symbolic.svg \
    %buildroot%_iconsdir/hicolor/scalable/actions/tag-outline-symbolic.svg

%files
%_bindir/gitpulsar-gtk
%_desktopdir/%app_id.desktop
%_datadir/metainfo/%app_id.metainfo.xml
%_iconsdir/hicolor/scalable/apps/%app_id.svg
%_iconsdir/hicolor/scalable/actions/*.svg

%changelog
* Sun Apr 19 2026 Anton Osipov <radiolamp@altlinux.org> 0.7.0-alt1
- Initial build.
