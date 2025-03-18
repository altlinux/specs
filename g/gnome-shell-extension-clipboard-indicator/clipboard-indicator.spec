# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gnome-shell-extension-clipboard-indicator
Version: 66
Release: alt3
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
%find_lang clipboard-indicator

%files -f clipboard-indicator.lang
%_datadir/gnome-shell/extensions/clipboard-indicator@tudmotu.com
%doc README.rst

%changelog
* Tue Mar 18 2025 Anton Midyukov <antohami@altlinux.org> 66-alt3
- Update metadata.json for GNOME 48 support

* Fri Feb 28 2025 Anton Midyukov <antohami@altlinux.org> 66-alt2
- Update Russian translation

* Sat Feb 08 2025 Anton Midyukov <antohami@altlinux.org> 66-alt1
- New version 66.

* Fri Dec 20 2024 Anton Midyukov <antohami@altlinux.org> 65-alt1
- initial build
