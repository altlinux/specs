# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-clipboard-indicator
Version: 69
Release: alt2
Summary: Clipboard manager for GNOME Shell
License: MIT
Group:  Graphical desktop/GNOME
Url: https://github.com/Tudmotu/gnome-shell-extension-clipboard-indicator
Vcs: https://github.com/Tudmotu/gnome-shell-extension-clipboard-indicator
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildArch: noarch

Requires: gnome-shell >= 47.0
BuildRequires: %_bindir/glib-compile-schemas

%description
The most popular, reliable and feature-rich clipboard manager for GNOME with
over 1M downloads.

%prep
%setup
%autopatch -p1

%build
%make_build

%install
%makeinstall_std

# fix install gsettings schemas
mkdir -p %buildroot%_datadir/glib-2.0/schemas
mv %buildroot%_datadir/gnome-shell/extensions/clipboard-indicator@tudmotu.com/schemas/*.xml \
	%buildroot%_datadir/glib-2.0/schemas
rm -vr %buildroot%_datadir/gnome-shell/extensions/clipboard-indicator@tudmotu.com/schemas

# fix install translations
mv %buildroot%_datadir/gnome-shell/extensions/clipboard-indicator@tudmotu.com/locale \
	%buildroot%_datadir/
# cleanup translation sources
find %buildroot%_datadir/locale \
	-name *.po -exec rm {} \;

# remove docs from directory of extension
rm %buildroot%_datadir/gnome-shell/extensions/clipboard-indicator@tudmotu.com/*.rst

%find_lang clipboard-indicator

%files -f clipboard-indicator.lang
%_datadir/gnome-shell/extensions/clipboard-indicator@tudmotu.com
%_datadir/glib-2.0/schemas/*.xml
%doc README.rst LICENSE.rst

%changelog
* Sat Mar 21 2026 Anton Midyukov <antohami@altlinux.org> 69-alt2
- metadata.json: add gnome-shell 50 support.

* Sun Sep 28 2025 Anton Midyukov <antohami@altlinux.org> 69-alt1
- New version 69.

* Mon May 19 2025 Anton Midyukov <antohami@altlinux.org> 68-alt5
- fix install translations

* Mon May 19 2025 Anton Midyukov <antohami@altlinux.org> 68-alt4
- clipboard-indicator: fix install gsettings schemas
- Update russian translations

* Thu May 15 2025 Anton Midyukov <antohami@altlinux.org> 68-alt3
- Update russian translations (Closes: 54303)

* Fri May 02 2025 Anton Midyukov <antohami@altlinux.org> 68-alt2
- Update russian translations

* Sat Apr 05 2025 Anton Midyukov <antohami@altlinux.org> 68-alt1
- New version 68.

* Tue Mar 18 2025 Anton Midyukov <antohami@altlinux.org> 66-alt3
- Update metadata.json for GNOME 48 support

* Fri Feb 28 2025 Anton Midyukov <antohami@altlinux.org> 66-alt2
- Update Russian translation

* Sat Feb 08 2025 Anton Midyukov <antohami@altlinux.org> 66-alt1
- New version 66.

* Fri Dec 20 2024 Anton Midyukov <antohami@altlinux.org> 65-alt1
- initial build
