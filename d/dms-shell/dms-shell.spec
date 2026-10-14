%define _unpackaged_files_terminate_build 1
%global import_path github.com/AvengeMedia/DankMaterialShell/core

Name: dms-shell
Version: 1.6.3
Release: alt1

Summary: DankMaterialShell - Material 3 inspired shell for Wayland compositors
License: MIT
Group: Graphical desktop/Other

Url: https://github.com/AvengeMedia/DankMaterialShell
# Source-url: https://github.com/AvengeMedia/DankMaterialShell/releases/download/v%version/dms-source.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

ExcludeArch: i586

Requires: accountsservice
Requires: dsearch
Requires: quickshell
Requires: matugen
Requires: qt6-multimedia
Requires: ppd-service
Requires: xdg-desktop-portal-gtk

# False positive
%filter_from_requires /niri/d
%filter_from_requires /hyprland/d
%filter_from_requires /Hyprland/d

%description
DankMaterialShell (DMS) is a modern Wayland desktop shell built with Quickshell
and optimized for the niri, hyprland, sway, and dwl (MangoWC) compositors. Features notifications,
app launcher, wallpaper customization, and fully customizable with plugins.

Includes auto-theming for GTK/Qt apps with matugen, 20+ customizable widgets,
process monitoring, notification center, clipboard history, dock, control center,
lock screen, and comprehensive plugin system.

%prep
%setup -a1
sed -i -e '/@update-desktop-database/d' -e '/@gtk-update-icon-cache/d' Makefile

%build

cp -r vendor ./core/
%make -C core sync-shell

export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
export TAGS="distro_binary withshell"
export LDFLAGS="-X main.Version=%version"
%golang_build core/cmd/dms

%install
export BUILDDIR="$PWD/.build"
%makeinstall_std \
    PREFIX=%_prefix \
    BUILD_DIR="$BUILDDIR/bin" \
    SYSTEMD_USER_DIR=%buildroot%_userunitdir

%files
%_bindir/dms
%_datadir/bash-completion/completions/dms
%_datadir/zsh/site-functions/_dms
%_datadir/fish/vendor_completions.d/dms.fish
%_userunitdir/dms.service
%_desktopdir/com.danklinux.dms.desktop
%_desktopdir/com.danklinux.dms.notepad.desktop
%_desktopdir/dms-open.desktop
%_iconsdir/hicolor/scalable/apps/danklogo.svg

%changelog
* Tue Oct 13 2026 Boris Yumankulov <boria138@altlinux.org> 1.6.3-alt1
- new version 1.6.3
- remove dgop runtime dependency (monitoring library is built into dms)
- use upstream make install for package files

* Mon Aug 03 2026 Boris Yumankulov <boria138@altlinux.org> 1.5.3-alt1
- new version 1.5.3

* Thu Jul 23 2026 Boris Yumankulov <boria138@altlinux.org> 1.5.2-alt1
- new version 1.5.2 (ALT bug: 59886)

* Tue May 19 2026 Boris Yumankulov <boria138@altlinux.org> 1.4.6-alt2
- add Hyprland to filter_from_require (ALT bug: 59253)

* Wed Apr 29 2026 Boris Yumankulov <boria138@altlinux.org> 1.4.6-alt1
- new version 1.4.6
- delete notification dev scripts from package

* Sat Apr 11 2026 Boris Yumankulov <boria138@altlinux.org> 1.4.4.1-alt1
- new version 1.4.4.1

* Tue Mar 31 2026 Boris Yumankulov <boria138@altlinux.org> 1.4.4-alt1
- initial build for ALT Sisyphus
