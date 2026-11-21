# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define app_id clipboard-indicator@tudmotu.com

Name: gnome-shell-extension-clipboard-indicator
Version: 73
Release: alt1
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
%makeinstall_std INSTALLPATH=%buildroot%_datadir/gnome-shell/extensions/%app_id

# fix install gsettings schemas
mkdir -p %buildroot%_datadir/glib-2.0/schemas
mv %buildroot%_datadir/gnome-shell/extensions/%app_id/schemas/*.xml \
	%buildroot%_datadir/glib-2.0/schemas
rm -vr %buildroot%_datadir/gnome-shell/extensions/%app_id/schemas

rm -v %buildroot%_datadir/gnome-shell/extensions/%app_id/README.md
rm -v %buildroot%_datadir/gnome-shell/extensions/%app_id/LICENSE.rst

%find_lang --with-gnome clipboard-indicator

%files -f clipboard-indicator.lang
%dir %_datadir/gnome-shell/extensions/%app_id
%_datadir/gnome-shell/extensions/%app_id/metadata.json
%_datadir/gnome-shell/extensions/%app_id/prefs.js
%_datadir/gnome-shell/extensions/%app_id/registry.js
%_datadir/gnome-shell/extensions/%app_id/stylesheet.css
%_datadir/gnome-shell/extensions/%app_id/compat.js
%_datadir/gnome-shell/extensions/%app_id/confirmDialog.js
%_datadir/gnome-shell/extensions/%app_id/constants.js
%_datadir/gnome-shell/extensions/%app_id/extension.js
%_datadir/gnome-shell/extensions/%app_id/keyboard.js
%dir %_datadir/gnome-shell/extensions/%app_id/locale
%dir %_datadir/gnome-shell/extensions/%app_id/locale/*
%dir %_datadir/gnome-shell/extensions/%app_id/locale/*/*
%_datadir/glib-2.0/schemas/*.xml
%doc README.md LICENSE.rst

%changelog
* Fri Nov 20 2026 Anton Midyukov <antohami@altlinux.org> 73-alt1
- New version 73.
- Update russian translation.

* Sat Sep 26 2026 Anton Midyukov <antohami@altlinux.org> 71-alt2
- add gnome-shell 51 support.

* Sun May 10 2026 Anton Midyukov <antohami@altlinux.org> 71-alt1
- New version 71.

* Tue May 05 2026 Anton Midyukov <antohami@altlinux.org> 70-alt1
- New version 70.
- Update Russian translations.

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
