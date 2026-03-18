# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-dash-to-panel
Version: 73
Release: alt1

%define sname dash-to-panel
%define eid dash-to-panel@jderose9.github.com

Summary: An icon taskbar for the Gnome Shell

BuildArch: noarch

License: GPL-2.0
Group:  Graphical desktop/GNOME
Url: https://github.com/home-sweet-gnome/dash-to-panel
Vcs: https://github.com/home-sweet-gnome/dash-to-panel

Source: %name-%version.tar
Patch: %name-%version-%release.patch

Requires: gnome-shell >= 47.0

%define gettext_domain dash-to-panel

BuildRequires: %_bindir/glib-compile-schemas sassc eslint

%description
An icon taskbar for the Gnome Shell.
This extension moves the dash into the gnome main panel so that the application
launchers and system tray are combined into a single panel,
similar to that found in KDE Plasma and Windows 7+. A separate dock is no longer
needed for easy access to running and favorited applications.

%prep
%setup
%__subst  's/"version": [[:digit:]][[:digit:]]*/"version": %version/'  metadata.json;
%autopatch -p1

%build
%make_build

%install
%makeinstall_std
%find_lang %gettext_domain

# remove docs from directory of extension
rm %buildroot%_datadir/gnome-shell/extensions/%eid/COPYING
rm %buildroot%_datadir/gnome-shell/extensions/%eid/README.md

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%eid/*
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.dash-to-panel.gschema.xml
%doc README.md COPYING

%changelog
* Wed Mar 18 2026 Anton Midyukov <antohami@altlinux.org> 73-alt1
- New version 73.

* Tue Dec 30 2025 Anton Midyukov <antohami@altlinux.org> 72-alt2
- Update russian translations.

* Wed Oct 15 2025 Anton Midyukov <antohami@altlinux.org> 72-alt1
- New version 72.

* Mon Sep 15 2025 Anton Midyukov <antohami@altlinux.org> 70-alt1
- New version 70.

* Tue Jul 29 2025 Anton Midyukov <antohami@altlinux.org> 68-alt5.119a5928.1
- update russian translation

* Fri Jul 11 2025 Anton Midyukov <antohami@altlinux.org> 68-alt4.ae5bc044.1
- new snapshot

* Thu May 22 2025 Anton Midyukov <antohami@altlinux.org> 68-alt3.fa8fabd.1
- update russian translation

* Mon May 19 2025 Anton Midyukov <antohami@altlinux.org> 68-alt2.fa8fabd.1
- new snapshot
- update russian translation

* Wed Mar 12 2025 Anton Midyukov <antohami@altlinux.org> 68-alt1
- New version 68.

* Tue Mar 11 2025 Anton Midyukov <antohami@altlinux.org> 67-alt2
- src/taskbar.js: do not call setDonateApp
- src/prefs.js: remove donate page
- src/extension.js: do not show udate version notification
- Update RU translation

* Mon Mar 10 2025 Anton Midyukov <antohami@altlinux.org> 67-alt1
- New version 67.

* Wed Jan 22 2025 Anton Midyukov <antohami@altlinux.org> 65-alt1
- New version 65.
- Remove Packager

* Sat Dec 21 2024 Anton Midyukov <antohami@altlinux.org> 64-alt1
- spec: fix install glibc schema
- Update .gear/rules for build from git tag, generate patch
- spec: Unpackaged files in buildroot should terminate build
- spec: Split lines in %description by length less than 80 characters
- Save .gear/upstream/remotes

* Fri Nov 29 2024 Hihin Ruslan <ruslandh@altlinux.ru> 64-alt0_1_git_db12bb
- Update from git from commit db12bb

* Fri Sep 20 2024 Hihin Ruslan <ruslandh@altlinux.ru> 63-alt0_1_git_0d14d7
- Update from git from commit 0d14d7

* Mon Mar 25 2024 Hihin Ruslan <ruslandh@altlinux.ru> 61-alt1
- Version v61

* Wed Mar 20 2024 Hihin Ruslan <ruslandh@altlinux.ru> 60-alt1_1_git_42eba9
- Update from git from commit 42eba9

* Mon Feb 05 2024 Hihin Ruslan <ruslandh@altlinux.ru> 60-alt1.1
- Fix spec

* Mon Feb 05 2024 Hihin Ruslan <ruslandh@altlinux.ru> 60-alt1
- Version v60

* Mon Sep 25 2023 Hihin Ruslan <ruslandh@altlinux.ru> 59-alt1
- Version v59

* Sat Sep 23 2023 Hihin Ruslan <ruslandh@altlinux.ru> 56-alt2_git_2_d5790be
- Update from github commit d5790be

* Fri Sep 22 2023 Hihin Ruslan <ruslandh@altlinux.ru> 56-alt2_git_1_b86a1c9
- Update from github commit b86a1c9

* Fri Aug 25 2023 Hihin Ruslan <ruslandh@altlinux.ru> 56-alt1.1
- Fix group

* Thu Aug 24 2023 Hihin Ruslan <ruslandh@altlinux.ru> 56-alt1
- Initial build for Sisyphus
