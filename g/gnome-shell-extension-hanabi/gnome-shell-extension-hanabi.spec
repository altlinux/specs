%define _unpackaged_files_terminate_build 1
%define ext_id hanabi-extension@jeffshee.github.io
%define ext_schema_id io.github.jeffshee.hanabi-extension

Name: gnome-shell-extension-hanabi
Version: 1
Release: alt9
Epoch: 1

Summary: Live Wallpaper for GNOME
Summary(ru_RU.UTF-8): Живые обои для GNOME
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://github.com/jeffshee/gnome-ext-hanabi
Vcs: https://github.com/jeffshee/gnome-ext-hanabi.git

BuildArch: noarch

Source: %name-%version.tar
Source1: node_modules.tar

Patch1: prefs-1-alt-fixs.patch

Requires: gnome-shell >= 42.0

BuildRequires(pre): rpm-macros-meson rpm-build-nodejs
BuildRequires: meson node npm
BuildRequires: %_bindir/glib-compile-schemas

%description
Extension for using videos as live wallpaper for GNOME Shell.

If the screen is black. Enabling options 'Force gtk4paintablesink'
or 'Force GtkMediaFile' in the extension settings can help.

%description -l ru_RU.UTF-8
Расширение для использования видео в качестве живых обоев в GNOME Shell.

Если экран черный. Включение опции 'Force gtk4paintablesink'
или 'Force GtkMediaFile' в настройках расширения может помочь.

%prep
%setup -a1

# fixed tooltips
%patch1 -p0

%build
%meson
%meson_build

%install
%meson_install
%find_lang %ext_id

%check
%meson_test

%files -f %ext_id.lang
%_datadir/glib-2.0/schemas/%ext_schema_id.gschema.xml
%_datadir/gnome-shell/extensions/%ext_id/
%doc README.md

%changelog
* Tue Jun 09 2026 Aleksandr Shamaraev <shad@altlinux.org> 1:1-alt9
- updated to git.074982d14d

* Mon Jun 08 2026 Aleksandr Shamaraev <shad@altlinux.org> 1:1-alt8
- updated to git.1ba3be9474

* Mon May 11 2026 Aleksandr Shamaraev <shad@altlinux.org> 1:1-alt7
- updated to git.033dc86a65

* Sat Mar 21 2026 Aleksandr Shamaraev <shad@altlinux.org> 1:1-alt6
- fixed patch

* Fri Mar 20 2026 Aleksandr Shamaraev <shad@altlinux.org> 1:1-alt5
- fixed for GNOME 50

* Sat Feb 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 1:1-alt4
- fixed Gjs-CRITICAL for run Hanabi in GNOME 49.3

* Sat Jan 31 2026 Aleksandr Shamaraev <shad@altlinux.org> 1:1-alt3
- fixed tooltips (ALT #53929)

* Thu Jan 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 1:1-alt2
- updated to git.3a9a9060

* Fri Dec 26 2025 Aleksandr Shamaraev <shad@altlinux.org> 1:1-alt1.476a2953.1
- Update to git.476a2953.
- Fix: work on Gnome 49

* Mon Sep 15 2025 Vladimir Vaskov <rirusha@altlinux.org> 1:1-alt1.20fe84dc.1
- New snapshot.
- Switched to snapshot version instaed of date tag.

* Fri Mar 28 2025 Vladimir Vaskov <rirusha@altlinux.org> 20250307-alt1
- Initial build.
