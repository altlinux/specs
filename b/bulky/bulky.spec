%define _unpackaged_files_terminate_build 1

Name: bulky
Version: 4.0
Release: alt1

Summary: Bulk Renamer
License: GPL-3.0-or-later
Group: Graphical desktop/Other
URL: https://github.com/linuxmint/bulky

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

BuildArch: noarch

Source: %name-%version.tar

%description
Bulky is used to rename files and directories.

It's an XApp so it can work in any distribution and many desktop
environments (Cinnamon, MATE, GNOME, etc.).

Thunar already has its own built-in file renamer so Bulky is redundant
in Xfce.

%prep
%setup
sed -i "s/__DEB_VERSION__/%{version}/" usr/lib/bulky/bulky.py
sed -i 's|common-licenses/GPL|license/GPL-3.0-or-later|' usr/lib/bulky/bulky.py

%build
%make

%install
mkdir -p %buildroot/usr/
cp -arv usr/* %buildroot/usr/

%find_lang %name --all-name

%files -f %{name}.lang
%doc README.md
%_bindir/bulky
%dir %_libexecdir/bulky
%_libexecdir/bulky/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%_datadir/glib-2.0/schemas/*.gschema.xml
%dir %_datadir/bulky
%_datadir/bulky/*

%changelog
* Sun Nov 23 2025 Nikolay Strelkov <snk@altlinux.org> 4.0-alt1
- New version 4.0.

* Fri Oct 17 2025 Nikolay Strelkov <snk@altlinux.org> 3.9-alt1
- Initial build for Sisyphus
