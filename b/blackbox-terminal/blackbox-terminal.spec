%define xdg_name com.raggesilver.BlackBox
%define _name blackbox

Name: blackbox-terminal
Version: 0.14.0
Release: alt9.git53be998

Summary: A beautiful GTK 4 terminal
License: GPL-3.0
Group: Terminals

Url: https://gitlab.gnome.org/raggesilver/blackbox
Source: %name-%version.tar
Patch1: blackbox-0.14.0-alt-xvt-compatibility.patch
Patch2: blackbox-0.14.0-alt-gio-print.patch
Packager: Vladimir Didenko <cow@altlinux.org>

Provides: xvt
Provides: x-terminal-emulator
# Executable file name conflict
Conflicts: blackbox

%define vte_ver 0.69.0

Requires(pre): libvte3 >= %vte_ver
Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-macros-alternatives
BuildRequires: meson
BuildRequires: vala
BuildRequires: libgio-devel
BuildRequires: libgtk4-devel
BuildRequires: libvte3-devel >= %vte_ver
BuildRequires: libadwaita-devel
BuildRequires: libmarblepq-vala
BuildRequires: libpcre2-devel libxml2-devel
BuildRequires: librsvg-devel
BuildRequires: libjson-glib-devel
BuildRequires: libgraphene-devel
BuildRequires: libgee0.8-devel

%description
A beautiful GTK 4 terminal.

%prep
%setup
%autopatch -p1

%build
%meson -Dblackbox_is_flatpak=false -Ddevel=false
%meson_build

%install
%meson_install

# alternatives (gnome-terminal -- 39)
mkdir -p %buildroot%_altdir
cat >%buildroot%_altdir/%_name <<EOF
%_bindir/xvt	%_bindir/%_name	38
%_bindir/x-terminal-emulator	%_bindir/%_name	38
EOF

%find_lang %_name

%files -f %_name.lang
%doc COPYING README.md
%_bindir/%_name
%_altdir/%_name
%_datadir/%_name
%_datadir/metainfo/%xdg_name.metainfo.xml
%_desktopdir/%xdg_name.desktop
%_datadir/glib-2.0/schemas/*
%_iconsdir/hicolor/*/actions/*.svg
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Wed Aug 7 2024 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt9.git53be998
- New version

* Tue Mar 5 2024 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt8.gitd693b92
- Fix undefined reference build issue

* Mon Feb 26 2024 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt7.gitd693b92
- New version

* Mon Dec 25 2023 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt6.git55f34e7
- New version

* Mon Aug 21 2023 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt5.gitdc3417f
- Support -e option as alias for -c for xvt compatibility (closes: #47180)

* Wed Aug 9 2023 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt4.gitdc3417f
- Change alternatives priority to avoid conflict with gnome-terminal

* Wed Aug 9 2023 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt3.gitdc3417f
- Provide x-terminal-emulator (closes: #47180)
- Support alternatives

* Tue Aug 8 2023 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt2.gitdc3417f
- New version

* Tue Jul 18 2023 Vladimir Didenko <cow@altlinux.org> 0.14.0-alt1
- New version

* Thu Mar 9 2023 Vladimir Didenko <cow@altlinux.org> 0.13.2-alt1
- New version

* Thu Jan 19 2023 Vladimir Didenko <cow@altlinux.org> 0.13.1-alt1
- New version

* Tue Dec 6 2022 Vladimir Didenko <cow@altlinux.org> 0.12.2-alt1
- New version

* Mon Oct 24 2022 Vladimir Didenko <cow@altlinux.org> 0.12.1-alt2
- Fix text selection

* Wed Oct 5 2022 Vladimir Didenko <cow@altlinux.org> 0.12.1-alt1
- New version

* Mon Sep 19 2022 Vladimir Didenko <cow@altlinux.org> 0.12.0-alt1
- Initial build for Sisyphus
