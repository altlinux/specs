%def_disable snapshot

%define _name tally
%define __name Tally
%define ver_major 0.7
%define rdn_name ca.vlacroix.%__name

# no tests
%def_disable check

Name: %_name
Version: %ver_major.3
Release: alt1

Summary: GNOME Counter
Group: Graphical desktop/GNOME
License: LGPL-3.0-or-later
Url: https://www.vlacroix.ca/apps/tally/

Vcs: https://github.com/vtrlx/tally.git

%if_disabled snapshot
Source: https://github.com/vtrlx/tally/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Patch1: %name-0.7.3-alt-makefile.patch
Patch2: %name-0.7.3-alt-no_flatpak.patch

%define lua_ver 5.4

Requires: lua5.4 LuaGObject%lua_ver typelib(Adw) = 1

BuildRequires(pre): rpm-build-lua
BuildRequires: clang
BuildRequires: lua%lua_ver-devel
BuildRequires: %_bindir/glib-compile-resources

%description
A counter for GNOME.

%prep
%setup
%patch1 -b .no_flatpak
%patch2 -b .no_flatpak

# #embed support from C23 required but it not available in our gcc-14
sed -i 's/cc/clang/' Makefile

%build
%add_optflags -std=c23
%make_build PREFIX=%_prefix

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml

%doc README*

%changelog
* Wed Jan 21 2026 Yuri N. Sedunov <aris@altlinux.org> 0.7.3-alt1
- 0.7.3

* Mon Dec 08 2025 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Tue Apr 01 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt1
- 0.5

* Thu Jan 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- first build for Sisyphus (0.4.1-2-g9cae28f)
