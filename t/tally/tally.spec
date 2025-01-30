%def_enable snapshot

%define _name tally
%define __name Tally
%define ver_major 0.4
%define rdn_name ca.vlacroix.%__name

# no tests
%def_disable check

Name: %_name
Version: %ver_major.1
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
Patch1: %name-0.4.1-alt-makefile.patch
Patch2: %name-0.4.1-alt-no_flatpak.patch

%define lua_ver 5.4

Requires: lua5.4 lgi%lua_ver typelib(Adw) = 1

BuildRequires(pre): rpm-build-lua
BuildRequires: lua%lua_ver-devel

%description
A counter for GNOME.

%prep
%setup
%patch1 -b .no_flatpak
%patch2 -b .no_flatpak

%build
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%_name
%_desktopdir/%rdn_name.desktop
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml

%doc README*

%changelog
* Thu Jan 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.1-alt1
- first build for Sisyphus (0.4.1-2-g9cae28f)
