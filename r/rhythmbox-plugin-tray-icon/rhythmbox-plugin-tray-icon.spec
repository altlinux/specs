%define _unpackaged_files_terminate_build 1

Name: rhythmbox-plugin-tray-icon
Version: 2020.05.21
Release: alt1

Summary: A tray icon plugin for rhythmbox music player
License: GPL-3.0-or-later
Group: Graphical desktop/Other
URL: http://packages.linuxmint.com/pool/main/r/rhythmbox-plugin-tray-icon/

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

Requires: rhythmbox
Requires: typelib(Gtk)
Requires: typelib(Peas)
Requires: typelib(RB)
Requires: typelib(XApp)

Source: %name-%version.tar

Patch: %name-%version-%release.patch

%description
%summary

%prep
%setup
%patch -p1

%build
# nothing to build here

%install
mkdir -p %buildroot/%_libdir
cp -arv usr/lib/* %buildroot/%_libdir/

%files
%doc README.md LICENSE
%dir %_libdir/rhythmbox/plugins/rhythmbox-tray-icon/
%_libdir/rhythmbox/plugins/rhythmbox-tray-icon/tray_icon.plugin
%_libdir/rhythmbox/plugins/rhythmbox-tray-icon/tray_icon.py

%changelog
* Fri Oct 17 2025 Nikolay Strelkov <snk@altlinux.org> 2020.05.21-alt1
- Initial build for Sisyphus
