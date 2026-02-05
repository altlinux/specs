%define _name LuaGObject
%define lua_ver 5.4

%def_disable check

Name: %_name%lua_ver
Version: 0.10.5
Release: alt1

Summary: Lua-5.4 bindings to GObject libraries
License: MIT
Group: System/Libraries
Url: https://github.com/vtrlx/LuaGObject

Vcs: https://github.com/vtrlx/LuaGObject.git

Source: %_name-%version.tar

%filter_from_requires /^lua%lua_ver(bytes)/d
%filter_from_requires /^lua%lua_ver(%_name\.lua_gobject_core)/d
%filter_from_requires /^lua%lua_ver(%_name\.override\.)/d

BuildRequires(pre): rpm-macros-meson rpm-macros-lua
BuildRequires: meson rpm-build-lua %_bindir/lua%lua_ver
BuildRequires: liblua%lua_ver-devel
BuildRequires: pkgconfig(libffi) pkgconfig(cairo-gobject)
BuildRequires: gobject-introspection-devel >= 1.80
BuildRequires: /usr/bin/dbus-run-session

%description
LuaGObject is a library which dynamically generates Lua bindings to
libraries which support GObject-Introspection such as Adwaita, GTK,
GLib, Gio, Pango, and many more. It also generates bindings to Cairo,
necessary for certain Gtk functionality.

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
* Thu Feb 05 2026 Yuri N. Sedunov <aris@altlinux.org> 0.10.5-alt1
- 0.10.5

* Wed Jan 21 2026 Yuri N. Sedunov <aris@altlinux.org> 0.10.4-alt1
- 0.10.4

* Tue Dec 30 2025 Yuri N. Sedunov <aris@altlinux.org> 0.10.3-alt1
- 0.10.3

* Mon Dec 08 2025 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- first build for Sisyphus (0.10.2-3-g3133643)


