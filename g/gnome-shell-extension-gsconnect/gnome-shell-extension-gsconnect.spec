%def_disable snapshot

%define ver_major 30
%define beta %nil
%define domain gsconnect@andyholmes.github.io
%define xdg_name org.gnome.Shell.Extensions.GSConnect
%define _libexecdir %_prefix/libexec

%def_disable webextension

Name: gnome-shell-extension-gsconnect
Version: %ver_major
Release: alt1

Summary: GSConnect is a implementation of KDE Connect for GNOME Shell
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://github.com/andyholmes/%name

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version%beta/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif

Requires: gnome-shell >= 3.24
Requires: /usr/bin/ffmpeg /usr/bin/fusermount
Requires: /usr/bin/ssh-keygen /usr/bin/ssh-add
Requires: fuse-sshfs /usr/bin/openssl

BuildRequires(pre): meson rpm-build-gir rpm-build-python3
BuildRequires: libgio-devel libdbus-devel

%add_python3_path %_datadir/nautilus-python/extensions

%description
GSConnect is a complete implementation of KDE Connect for
GNOME Shell with Nautilus, Chrome and Firefox integration.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_disable_webextension:-Dwebextension=false}
%meson_build

%check
%meson_test

%install
%meson_install
%find_lang %xdg_name

%files -f %xdg_name.lang
%_desktopdir/%xdg_name.desktop
%_desktopdir/%xdg_name.Preferences.desktop
%_datadir/gnome-shell/extensions/%domain/
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/nautilus-python/extensions/nautilus-gsconnect.py
%_datadir/nautilus-python/extensions/__pycache__/*
%_iconsdir/hicolor/*/*/*.svg

%if_enabled webextension
%_sysconfdir/chromium/native-messaging-hosts/org.gnome.shell.extensions.gsconnect.json
%_sysconfdir/opt/chrome/native-messaging-hosts/org.gnome.shell.extensions.gsconnect.json
%_libdir/mozilla/native-messaging-hosts/org.gnome.shell.extensions.gsconnect.json
%endif

%doc README.md

%changelog
* Thu Dec 05 2019 Yuri N. Sedunov <aris@altlinux.org> 30-alt1
- 30

* Wed Nov 06 2019 Yuri N. Sedunov <aris@altlinux.org> 28-alt1
- 28

* Thu Oct 17 2019 Yuri N. Sedunov <aris@altlinux.org> 27-alt1
- 27

* Mon Jun 24 2019 Yuri N. Sedunov <aris@altlinux.org> 25-alt0.1
- first build for Sisyphus (0.25-rc2)

