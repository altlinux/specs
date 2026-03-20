# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-add-to-desktop
Version: 16
Release: alt0.1
Summary: An easy way to create desktop app shortcuts in GNOME
License: GPL-3.0-or-later
Group:  Graphical desktop/GNOME
Url: https://github.com/Tommimon/add-to-desktop
Vcs: https://github.com/Tommimon/add-to-desktop.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

Requires: gnome-shell-extension-gtk4-desktop-icons-ng

%description
This simple extension tries to make easier the GNOME process to create
a desktop shortcut for apps.

The idea is simple: instead of searching for the .desktop files through
multiple folders let's use the application launcher that already groups
all our apps.

This extension adds a new line to the app context menu in the application
launcher, the new entry ('Add to Desktop') if clicked automatically creates
a desktop shortcut to the app.

%prep
%setup
%autopatch -p1

%build
# build locale
for f in po/*; do
	name=${f:3:${#f}-6}
	mkdir -p locale/"$name"/LC_MESSAGES
	msgfmt "$f" --output-file=locale/"$name"/LC_MESSAGES/add-to-desktop.mo
done

%install
mkdir -p %buildroot%_datadir/gnome-shell/extensions/add-to-desktop@tommimon.github.com
install -m644 *.js metadata.json %buildroot%_datadir/gnome-shell/extensions/add-to-desktop@tommimon.github.com/
cp -r locale %buildroot%_datadir/

%find_lang add-to-desktop

%files -f add-to-desktop.lang
%_datadir/gnome-shell/extensions/add-to-desktop@tommimon.github.com
%doc README.md LICENSE

%changelog
* Fri Mar 20 2026 Anton Midyukov <antohami@altlinux.org> 16-alt0.1
- Add gnome 50 support.

* Sun Sep 28 2025 Anton Midyukov <antohami@altlinux.org> 15-alt1
- New version 15.

* Fri Apr 11 2025 Anton Midyukov <antohami@altlinux.org> 14-alt1
- initial build
