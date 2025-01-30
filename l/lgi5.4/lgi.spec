%define _name lgi
%define lua_ver 5.4

%def_disable check

Name: %_name%lua_ver
Version: 0.9.2
Release: alt1

Summary: Lua-5.4 bindings to GObject libraries
License: MIT
Group: System/Libraries
Url: https://github.com/lgi-devs/lgi

Vcs: https://github.com/lgi-devs/lgi.git

Source: %_name-%version.tar

%filter_from_requires /^lua%lua_ver(bytes)/d
%filter_from_requires /^lua%lua_ver(lgi\.override\.)/d


BuildRequires(pre): rpm-macros-meson rpm-macros-lua
BuildRequires: meson rpm-build-lua %_bindir/lua%lua_ver
BuildRequires: liblua%lua_ver-devel
BuildRequires: pkgconfig(libffi) pkgconfig(cairo-gobject)
BuildRequires: gobject-introspection-devel
BuildRequires: /usr/bin/dbus-run-session

%description
Dynamic Lua binding to any library which is introspectable using
gobject-introspection. Allows using GObject-based libraries directly
from Lua.

If you need to support pre-gobject-introspection GTK (ancient GTK+ 2.x
releases), use Lua-Gnome.

%prep
%setup -n %_name-%version

%build
%meson -Dlua-pc=lua%lua_ver \
    -Dlua-bin=%_bindir/lua%lua_ver
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%lua54_modulesdir/%_name/
%lua54_modulesdir_noarch/%_name.lua
%lua54_modulesdir_noarch/%_name/
%doc README.md docs samples

%changelog
* Thu Jan 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- first build for Sisyphus (0.9.2-116-ga412921)


