%define _unpackaged_files_terminate_build 1

Name: thingy
Version: 1.2.1
Release: alt1

Summary: Document Manager
License: GPL-3.0-or-later
Group: Graphical desktop/Other
URL: https://github.com/linuxmint/thingy

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
Thingy is used to quickly access recent and favorite documents.

It's an XApp so it can work in any distribution and many desktop
environments (Cinnamon, MATE, Xfce, GNOME, etc.).

%prep
%setup
sed -i "s/__DEB_VERSION__/%{version}/" usr/lib/thingy/thingy.py
sed -i 's|common-licenses/GPL|license/GPL-3.0-or-later|' usr/lib/thingy/thingy.py
sed -i 's|^Categories=.*|Categories=GTK;System;FileTools;|' generate_desktop_files usr/share/applications/thingy.desktop

%build
%make

%install
mkdir -p %buildroot/usr/
cp -arv usr/* %buildroot/usr/

%find_lang %name --all-name

%files -f %{name}.lang
%doc README.md
%_bindir/thingy
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%dir %_libexecdir/thingy
%_libexecdir/thingy/*
%_datadir/glib-2.0/schemas/*.gschema.xml
%dir %_datadir/thingy
%_datadir/thingy/*

%changelog
* Fri Oct 17 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus
