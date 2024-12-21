# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-dash-to-panel
Version: 64
Release: alt1

%define sname dash-to-panel
%define eid dash-to-panel@jderose9.github.com

Summary: An icon taskbar for the Gnome Shell

BuildArch: noarch

License: GPL-2.0
Group:  Graphical desktop/GNOME
Url: https://github.com/home-sweet-gnome/dash-to-panel
Vcs: https://github.com/home-sweet-gnome/dash-to-panel

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

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

# fix install glibc schema
mkdir -p %buildroot%_datadir/glib-2.0/schemas
mv %buildroot%_datadir/gnome-shell/extensions/%eid/schemas/*.xml \
	%buildroot%_datadir/glib-2.0/schemas
rm -vr %buildroot%_datadir/gnome-shell/extensions/%eid/schemas

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%eid/*
%_datadir/glib-2.0/schemas/org.gnome.shell.extensions.dash-to-panel.gschema.xml
%doc README.md

%changelog
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
