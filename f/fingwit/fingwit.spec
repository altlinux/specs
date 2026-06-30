%define _unpackaged_files_terminate_build 1

Name: fingwit
Version: 1.0.9
Release: alt1

Summary: Fingerprint Configuration Tool
License: GPL-3.0-or-later
Group: Graphical desktop/Other
URL: https://github.com/xapp-project/fingwit

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-build-python3
BuildRequires: meson
BuildRequires: cmake
BuildRequires: pkgconfig(pam)

%filter_from_requires /python3(PAM)/d
Requires: python3-module-PAM
Requires: typelib(XApp)
# to get /etc/pam.d/gdm-fingerprint
Requires: gdm-data

Requires: xapp-symbolic-icons

Source: %name-%version.tar

%description
Fingwit is used to configure fingerprint authentication.

It's an XApp so it can work in any distribution and many
desktop environments.

%prep
%setup
sed -i "s/common-auth/gdm-fingerprint/" fingwit
sed -i 's|common-licenses/GPL|license/GPL-3.0-or-later|' fingwit
sed -i 's|^Categories=.*|Categories=GTK;Settings;HardwareSettings;|' data/fingwit.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%files -f %{name}.lang
%doc README.md
%_bindir/fingwit
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%dir %_datadir/fingwit
%_datadir/fingwit/*
%_datadir/glib-2.0/schemas/*.gschema.xml
%dir %_libdir/fingwit
%_libdir/fingwit/pam_fingwit.py
%_libdir/security/pam_fingwit.so
%dir %_datadir/pam-configs
%_datadir/pam-configs/fingwit

%changelog
* Tue Jun 30 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.9-alt1
- New version 1.0.9.

* Fri Jan 09 2026 Nikolay Strelkov <snk@altlinux.org> 1.0.8-alt1
- New version 1.0.8.

* Sat Dec 13 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.7-alt1
- New version 1.0.7.

* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.6-alt1
- New version 1.0.6.

* Fri Oct 17 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.5-alt1
- Initial build for Sisyphus
