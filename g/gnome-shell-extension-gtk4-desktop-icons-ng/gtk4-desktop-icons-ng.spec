# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-gtk4-desktop-icons-ng
Version: 100.18
Release: alt2
Summary: Extension for the GNOME Shell that renders icons on the desktop

License: GPL-3.0-or-later
Group:  Graphical desktop/GNOME
Url: https://gitlab.com/smedius/desktop-icons-ng
Vcs: https://gitlab.com/smedius/desktop-icons-ng
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

Requires: gnome-shell >= 50.0
Requires: nautilus >= 3.38.0
Requires: file-roller >= 3.38.0
# https://bugzilla.altlinux.org/53044
Requires: libpoppler-gir
Requires: libgnome-autoar-gir
BuildRequires: %_bindir/glib-compile-schemas
BuildRequires: meson
BuildRequires: gtk-update-icon-cache

%description
Gtk4 Desktop Icons NG is an extension and a program together for the GNOME Shell
that renders icons on the desktop. It is a fork from DING.
Desktop Icons NG (DING) by Sergio Costas itself is a fork/rewrite of the
official 'Desktop Icons' extension, originally by Carlos Soriano.

This new Gtk4 extension was originally submitted upstream to the DING project as
a merge request. It was not merged for quite some time with development
continuing on both branches simultaneously. The branches started diverging
significantly, and further, the new commit's in the original DING branch were
not easily adaptable to changes already made in this gtk4 branch. That made it
very difficult to rebase and merge all the new changes to the original branch.

A mutual decision was therefore made to continue independent development of both
branches. Important bug fixes from branches are still back ported and
forward-ported between them. Therefore there are two extensions available, the
classic DING that uses Gtk 3, and this newer fork based on Gtk 4 and libadwaita.

This fork of DING is ported to use the Gtk4 toolkit, and now has been ported to
libadwaita. This, and the original DING can both be installed together, but only
one can be activated at a time in the extension Manager. They use different
install directories and GSettings schemas, therefore preferences set in one will
not carrry through to the other. This is to avoid trampling on the stable branch
and isolate errors from this branch.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang gtk4-ding

# remove apparmor config
rm -r %buildroot%_sysconfdir/apparmor.d

# remove unsupported locales
rm -r %buildroot%_datadir/locale/zh-Hans
rm -r %buildroot%_datadir/locale/zh-Hant

# override for systemd user units for fix user session end
mkdir -p %buildroot%_userunitdir/org.gnome.Shell@user.service.d
pushd %buildroot%_userunitdir/org.gnome.Shell@user.service.d
cat > gtk4-ding.conf << EOF
[Unit]
After=xdg-desktop-portal.service xdg-document-portal.service gvfs-daemon.service
EOF
popd

%files -f gtk4-ding.lang
%_datadir/gnome-shell/extensions/gtk4-ding@smedius.gitlab.com
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.gtk4-ding.gschema.xml
%_desktopdir/com.desktop.ding.desktop
%_iconsdir/hicolor/scalable/apps/com.desktop.ding.svg
%_userunitdir/org.gnome.Shell@user.service.d/gtk4-ding.conf
%doc DEBUGGING.md FEATURES.md HISTORY.md ISSUES.md README.md

%changelog
* Thu Jun 18 2026 Anton Midyukov <antohami@altlinux.org> 100.18-alt2
- Fix override for org.gnome.Shell.service on gnome 50.
- Runtime dependency on gnome-shell >= 50.

* Wed Mar 18 2026 Anton Midyukov <antohami@altlinux.org> 100.18-alt1
- New version 100.18.

* Thu Mar 05 2026 Anton Midyukov <antohami@altlinux.org> 100.17-alt2
- Add override for systemd user units for fix user session end (Closes: 57845).

* Wed Mar 04 2026 Anton Midyukov <antohami@altlinux.org> 100.17-alt1
- New version 100.17.

* Wed Oct 15 2025 Anton Midyukov <antohami@altlinux.org> 100.8-alt1
- New version 100.8-2.

* Mon Sep 15 2025 Anton Midyukov <antohami@altlinux.org> 100.6-alt1
- New version 100.6.

* Mon Jul 28 2025 Anton Midyukov <antohami@altlinux.org> 100.5-alt1
- New version 100.5.

* Sat Jul 19 2025 Anton Midyukov <antohami@altlinux.org> 100.4-alt1
- New version 100.4.

* Thu Jul 10 2025 Anton Midyukov <antohami@altlinux.org> 100.2-alt1
- New version 100.2.

* Tue Jun 03 2025 Anton Midyukov <antohami@altlinux.org> 100.1-alt1
- New version 100.1.

* Thu May 01 2025 Anton Midyukov <antohami@altlinux.org> 98-alt1
- New version 98.
- Fix multiple find file windows.

* Sun Apr 20 2025 Anton Midyukov <antohami@altlinux.org> 97-alt1
- New version 97.

* Wed Apr 09 2025 Anton Midyukov <antohami@altlinux.org> 96-alt1
- New version 96.

* Mon Mar 10 2025 Anton Midyukov <antohami@altlinux.org> 93-alt1
- New version 93.

* Wed Feb 19 2025 Anton Midyukov <antohami@altlinux.org> 92-alt1
- New version 92
- Add dependency on libgnome-autoar-gir

* Wed Feb 12 2025 Anton Midyukov <antohami@altlinux.org> 91-alt2
- Add dependency on libpoppler-gir (Closes: 53044)

* Sat Feb 08 2025 Anton Midyukov <antohami@altlinux.org> 91-alt1
- New version 91.

* Wed Jan 22 2025 Anton Midyukov <antohami@altlinux.org> 90-alt2
- Revert "Hard code for Ptyxis terminal for new Fedora"

* Wed Jan 22 2025 Anton Midyukov <antohami@altlinux.org> 90-alt1
- New version 90.

* Fri Jan 10 2025 Anton Midyukov <antohami@altlinux.org> 89-alt1
- New version 89.

* Thu Dec 19 2024 Anton Midyukov <antohami@altlinux.org> 87-alt1
- initial build
