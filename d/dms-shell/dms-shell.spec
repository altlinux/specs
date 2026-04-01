%define _unpackaged_files_terminate_build 1
%global import_path github.com/AvengeMedia/DankMaterialShell/core

Name: dms-shell
Version: 1.4.4
Release: alt1

Summary: DankMaterialShell - Material 3 inspired shell for Wayland compositors
License: MIT
Group: Graphical desktop/Other

Url: https://github.com/AvengeMedia/DankMaterialShell
# Source-url: https://github.com/AvengeMedia/DankMaterialShell/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

Requires: accountsservice
Requires: dsearch
Requires: dgop
Requires: quickshell
Requires: matugen
Requires: qt6-multimedia
Requires: ppd-service
Requires: xdg-desktop-portal-gtk

# False positive
%filter_from_requires /niri/d
%filter_from_requires /hyprland/d

%description
DankMaterialShell (DMS) is a modern Wayland desktop shell built with Quickshell
and optimized for the niri, hyprland, sway, and dwl (MangoWC) compositors. Features notifications,
app launcher, wallpaper customization, and fully customizable with plugins.

Includes auto-theming for GTK/Qt apps with matugen, 20+ customizable widgets,
process monitoring, notification center, clipboard history, dock, control center,
lock screen, and comprehensive plugin system.

%prep
%setup -a1

%build

cp -r vendor ./core/

export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
%golang_build core/cmd/dms

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

install -d %buildroot%_datadir/bash-completion/completions
install -d %buildroot%_datadir/zsh/site-functions
install -d %buildroot%_datadir/fish/vendor_completions.d

dms completion bash > %buildroot%_datadir/bash-completion/completions/dms || :
dms completion zsh > %buildroot%_datadir/zsh/site-functions/_dms || :
dms completion fish > %buildroot%_datadir/fish/vendor_completions.d/dms.fish || :

install -Dm644 assets/systemd/dms.service %buildroot%_userunitdir/dms.service

install -Dm644 assets/dms-open.desktop %buildroot%_desktopdir/dms-open.desktop
install -Dm644 assets/danklogo.svg %buildroot%_iconsdir/hicolor/scalable/apps/danklogo.svg

install -dm755 %buildroot%_datadir/quickshell/dms
cp -r "quickshell/"* %buildroot%_datadir/quickshell/dms/

rm -rf %buildroot%_datadir/quickshell/dms/.git*
rm -f %buildroot%_datadir/quickshell/dms/.gitignore
rm -rf %buildroot%_datadir/quickshell/dms/.github
rm -rf %buildroot%_datadir/quickshell/dms/distro
rm -f %buildroot%_datadir/quickshell/dms/scripts/i18nsync.py
rm -f %buildroot%_datadir/quickshell/dms/translations/extract_settings_index.py
rm -f %buildroot%_datadir/quickshell/dms/translations/extract_translations.py
rm -f %buildroot%_datadir/quickshell/dms/translations/replace_qstr.py

echo "%version" > %buildroot%_datadir/quickshell/dms/VERSION

%files
%_bindir/dms
%_datadir/bash-completion/completions/dms
%_datadir/zsh/site-functions/_dms
%_datadir/fish/vendor_completions.d/dms.fish
%_datadir/quickshell/dms/
%_userunitdir/dms.service
%_desktopdir/dms-open.desktop
%_iconsdir/hicolor/scalable/apps/danklogo.svg

%changelog
* Tue Mar 31 2026 Boris Yumankulov <boria138@altlinux.org> 1.4.4-alt1
- initial build for ALT Sisyphus

