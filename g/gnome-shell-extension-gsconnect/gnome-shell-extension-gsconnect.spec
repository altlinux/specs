%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 55
%define beta %nil
%define domain gsconnect@andyholmes.github.io
%define xdg_name org.gnome.Shell.Extensions.GSConnect

%def_enable webextension
%def_enable installed_tests
# network required
%def_disable check

Name: gnome-shell-extension-gsconnect
Version: %ver_major
Release: alt1

Summary: GSConnect is a implementation of KDE Connect for GNOME Shell
Group: Graphical desktop/GNOME
License: GPL-2.0
Url: https://github.com/andyholmes/%name

%{?_disable_webextension:BuildArch: noarch}

%if_disabled snapshot
Source: %url/archive/v%version%beta/%name-%version%beta.tar.gz
%else
Vcs: https://github.com/andyholmes/gnome-shell-extension-gsconnect.git
Source: %name-%version%beta.tar
%endif

Requires: gnome-shell >= 44
Requires: /usr/bin/ffmpeg /usr/bin/fusermount
Requires: /usr/bin/ssh-keygen /usr/bin/ssh-add
Requires: fuse-sshfs /usr/bin/openssl
Requires: libadwaita-gir >= 1.2

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-python3
BuildRequires: meson eslint libgio-devel libdbus-devel libgtk4-devel
%{?_enable_check:BuildRequires: xvfb-run %_bindir/gjs typelib(Gdk) = 3.0 typelib(Adw) = 1}

%add_python3_path %_datadir/gnome-shell/extensions/%domain %_datadir/nautilus-python/extensions
# imports.gi.St.Settings.get()
%add_typelib_req_skiplist typelib(get) typelib(Nemo)

%description
GSConnect is a complete implementation of KDE Connect for
GNOME Shell with Nautilus, Chrome and Firefox integration.

%package tests
Summary: Tests for the GSConnect
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed GSConnect Gnome Shell extension.

%prep
%setup -n %name-%version%beta

%build
%meson \
    %{?_disable_webextension:-Dwebextension=false} \
    %{?_disable_installed_tests:-Dinstalled_tests=false}
%meson_build

%install
%meson_install
%find_lang %xdg_name

%check
xvfb-run %__meson_test

%files -f %xdg_name.lang
%_desktopdir/%xdg_name.desktop
%_desktopdir/%xdg_name.Preferences.desktop
%_datadir/gnome-shell/extensions/%domain/
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/nautilus-python/extensions/nautilus-gsconnect.py
%_datadir/nautilus-python/extensions/__pycache__/*
%_iconsdir/hicolor/*/*/*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml

%if_enabled webextension
%_sysconfdir/chromium/native-messaging-hosts/org.gnome.shell.extensions.gsconnect.json
%_sysconfdir/opt/chrome/native-messaging-hosts/org.gnome.shell.extensions.gsconnect.json
%_libdir/mozilla/native-messaging-hosts/org.gnome.shell.extensions.gsconnect.json
%endif
%doc README.md

%if_enabled installed_tests
%files tests
%_datadir/installed-tests/gsconnect/
%_libexecdir/installed-tests/gsconnect/
%endif

%changelog
* Sun Mar 26 2023 Yuri N. Sedunov <aris@altlinux.org> 55-alt1
- 55

* Tue Oct 18 2022 Yuri N. Sedunov <aris@altlinux.org> 54-alt1
- 54

* Fri Mar 25 2022 Yuri N. Sedunov <aris@altlinux.org> 53-alt1
- 53

* Sun Mar 20 2022 Yuri N. Sedunov <aris@altlinux.org> 50-alt1
- 50

* Tue Oct 05 2021 Yuri N. Sedunov <aris@altlinux.org> 48-alt1
- 48

* Sun Jun 20 2021 Yuri N. Sedunov <aris@altlinux.org> 47-alt1
- 47

* Sun Apr 11 2021 Yuri N. Sedunov <aris@altlinux.org> 46-alt1
- updated to v46-6-g9d105bed

* Thu Oct 29 2020 Yuri N. Sedunov <aris@altlinux.org> 44-alt1
- 44

* Wed Sep 30 2020 Yuri N. Sedunov <aris@altlinux.org> 43-alt1
- 43

* Fri Aug 21 2020 Yuri N. Sedunov <aris@altlinux.org> 41-alt1
- 41

* Tue Jun 23 2020 Yuri N. Sedunov <aris@altlinux.org> 39-alt1
- 39

* Mon Jun 01 2020 Yuri N. Sedunov <aris@altlinux.org> 38-alt1
- 38

* Fri Apr 17 2020 Yuri N. Sedunov <aris@altlinux.org> 37-alt1
- 37

* Mon Mar 30 2020 Yuri N. Sedunov <aris@altlinux.org> 36-alt1
- 36

* Wed Mar 25 2020 Yuri N. Sedunov <aris@altlinux.org> 35-alt1
- updated to v35-3-g006e3a02

* Tue Mar 17 2020 Yuri N. Sedunov <aris@altlinux.org> 34-alt1
- updated to v34-4-ge21a0ef5

* Sun Jan 26 2020 Yuri N. Sedunov <aris@altlinux.org> 31-alt1
- 31

* Thu Dec 05 2019 Yuri N. Sedunov <aris@altlinux.org> 30-alt1
- 30

* Wed Nov 06 2019 Yuri N. Sedunov <aris@altlinux.org> 28-alt1
- 28

* Thu Oct 17 2019 Yuri N. Sedunov <aris@altlinux.org> 27-alt1
- 27

* Mon Jun 24 2019 Yuri N. Sedunov <aris@altlinux.org> 25-alt0.1
- first build for Sisyphus (0.25-rc2)

