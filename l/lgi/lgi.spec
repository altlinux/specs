Summary: Lua bindings to GObject libraries
Name: lgi
Version: 0.6.2
Release: alt1
License: MIT/X11
Group: System/Libraries
Url: http://github.com/pavouk/lgi
Source0: %name-%version.tar

BuildRequires: liblua5-devel gobject-introspection-devel

%description
Dynamic Lua binding to any library which is introspectable using
gobject-introspection. Allows using GObject-based libraries directly
from Lua.

If you need to support pre-gobject-introspection GTK (ancient GTK+ 2.x
releases), use Lua-Gnome.

%prep
%setup

%build
make
%install
%makeinstall_std PREFIX=%_prefix LUA_LIBDIR=%_libdir/lua5 LUA_SHAREDIR=%_datadir/lua5

%files
%_libdir/lua5/%name
%_datadir/lua5/%name.lua
%_datadir/lua5/%name

%doc README.md docs samples

%changelog
* Sun Dec  9 2012 Terechkov Evgenii <evg@altlinux.org> 0.6.2-alt1
- Initial build for ALT Linux Sisyphus
