Name: gnome-shell-extension-dash-to-panel
Version: 59
Release: alt1

%define sname dash-to-panel
%define eid dash-to-panel@jderose9.github.com

Summary: An icon taskbar for the Gnome Shell

BuildArch: noarch

License: GPL-2.0
Group:  Graphical desktop/GNOME
Url: https://github.com/home-sweet-gnome/dash-to-panel

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %sname-%version.tar

Requires: gnome-shell >= 45

%define gettext_domain dash-to-panel

BuildRequires: %_bindir/glib-compile-schemas sassc eslint

%description
An icon taskbar for the Gnome Shell.
This extension moves the dash into the gnome main panel so that the application launchers and system tray are combined into a single panel,
similar to that found in KDE Plasma and Windows 7+. A separate dock is no longer needed for easy access to running and favorited applications.

%prep
%setup  -n %sname-%version
%__subst  's/"version": [[:digit:]][[:digit:]]*/"version": %version/'  metadata.json;

%build
%make_build

%install
%makeinstall_std
%find_lang %gettext_domain

%files -f %gettext_domain.lang
%_datadir/gnome-shell/extensions/%eid/*
%doc README.md

%changelog
* Mon Sep 25 2023 Hihin Ruslan <ruslandh@altlinux.ru> 59-alt1
- version v59

* Sat Sep 23 2023 Hihin Ruslan <ruslandh@altlinux.ru> 56-alt2_git_2_d5790be
- Update from github commit d5790be

* Fri Sep 22 2023 Hihin Ruslan <ruslandh@altlinux.ru> 56-alt2_git_1_b86a1c9
- Update from github commit b86a1c9

* Fri Aug 25 2023 Hihin Ruslan <ruslandh@altlinux.ru> 56-alt1.1
- Fix group

* Thu Aug 24 2023 Hihin Ruslan <ruslandh@altlinux.ru> 56-alt1
- Initial build for Sisyphus
