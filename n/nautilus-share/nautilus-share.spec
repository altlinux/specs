Name: nautilus-share
Version: 0.7.5
Release: alt1

Summary: Nautilus extension to share folder using Samba
License: GPL-2.0
Group: Graphical desktop/GNOME
Url: https://gitlab.gnome.org/coreyberla/nautilus-share

Vcs: https://gitlab.gnome.org/coreyberla/nautilus-share.git
Source: %url/-/archive/%version/%name-%version.tar.gz
Patch: %name-0.7.5-alt-interfaces_dir.patch
Patch1: %name-0.7.5-alt-po_build.patch

%define gtk4_ver 4.6
%define nautilus_ver 43

Requires: nautilus >= %nautilus_ver
Requires: samba >= 3.0.23
Requires: %name-common = %EVR

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: libgtk4-devel >= %gtk4_ver libnautilus-devel >= %nautilus_ver

%description
Application for the GNOME desktop integrated in Nautilus, that allows
simple use of Nautilus shares without signing in as root.

Features:
* A new entry in your Nautilus right-click menu with a
   nice icon.

* A simple dialog to share your folder, which allows you to choose a
   name and decide whether to make it read-only.

* Possibility to access it from the Properties tab of your folder.

* Possibility to see whether a share name already exists by simply
   typing it.

* Nautilus displays a palm icon to visually show you which folders are
   shared.

%package common
Summary: Common files for nautilus-share
Group: Graphical desktop/GNOME
BuildArch: noarch

%description common
Provides common files for nautilus-share.

%prep
%setup
%patch
%patch1
pushd po
ls *.po|cut -f1 -d. > LINGUAS
popd

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files common -f %name.lang
%_datadir/nautilus-share/*
%doc AUTHORS ChangeLog README INSTALL

%files
%_libdir/nautilus/extensions-4/lib%name.so

%changelog
* Thu Nov 24 2022 Yuri N. Sedunov <aris@altlinux.org> 0.7.5-alt1
- 0.7.5 (ported to libnautilus-extension-4/Meson build system)

* Tue Nov 13 2018 Evgeny Sinelnikov <sin@altlinux.org> 0.7.3-alt1.qa1
- Rebuild due it was already built but no source id has been recorded

* Fri Sep 2 2011 Alex Negulescu <alecs@altlinux.org> 0.7.3-alt1
- Initial build, 0.7.3-alt1.
