%define        nomen lgi

Summary:       Lua bindings to GObject libraries rock
Name:          rock-lgi
Version:       0.9.2.134
Release:       alt0.1
License:       MIT
Group:         System/Libraries
Url:           https://github.com/lgi-devs/lgi
Vcs:           https://github.com/lgi-devs/lgi.git

Source:        %name-%version.tar
Patch:         disable.test.patch
Patch1:        rockspec.patch
BuildRequires(pre): rpm-build-rocks >= 5.5.1-alt1
BuildRequires(pre): rpm-macros-meson
BuildRequires: cmake
BuildRequires: dbus
BuildRequires: meson
BuildRequires: xvfb-run
BuildRequires: /usr/bin/dbus-launch
BuildRequires: gir(Gtk) = 3.0
BuildRequires: cmake(lua) >= 5.5
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libffi)
BuildRequires: rocks(luarocks) >= 3.13.0
Requires:      gobject-introspection
Requires:      lua >= 5.5
Requires:      rocks(luarocks) >= 3.13.0

%description
Dynamic Lua binding to any library which is introspectable using
gobject-introspection. Allows using GObject-based libraries directly
from Lua.

If you need to support pre-gobject-introspection GTK (ancient GTK+ 2.x
releases), use Lua-Gnome.


%package       devel
Summary:       Dependencies for building the LGI native module
Group:         Development/Other
Requires:      %name = %EVR
Requires:      cmake(lua) >= 5.5
Requires:      pkgconfig(gmodule-2.0)
Requires:      pkgconfig(gobject-introspection-1.0)
Requires:      pkgconfig(libffi)

%description   devel
Development dependencies for building the native LGI module.


%prep
%setup
%autopatch -p1

%build
%meson \
   -Dlua-pc=lua5.5 \
   -Dlua-bin=lua5.5
%meson_build

%install
LIBS="$(pkg-config --libs lua5.5)" \
   %rocks_make lgi-%version-1.rockspec
rm -f %buildroot%rock_specdir/manifest
printf '%%%%dir %%s\n' %rock_libexecdir/%nomen %rock_libdir/%nomen | sort -u > lgi-dirs.files

%check
xvfb-run %meson_test
test -f %buildroot%rock_specdir/lgi/%version-1/rock_manifest
(
   cd %buildroot
   LUA_PATH_5_5='%buildroot%rock_libexecdir/?.lua;%buildroot%rock_libexecdir/?/init.lua;;' \
   LUA_CPATH_5_5='%buildroot%rock_libdir/?.so;;' \
      lua5.5 -e 'local lgi = require("lgi"); assert(lgi.GLib and lgi.Gio and lgi.GioUnix and lgi.cairo)'
)


%files         -f lgi-dirs.files
%doc LICENSE README.md docs samples
%rock_libdir/%nomen/*.so
%rock_libexecdir/%nomen.lua
%rock_libexecdir/%nomen/*.lua
%rock_libexecdir/%nomen/override/
%rock_specdir/%nomen/

%files         devel


%changelog
* Wed Nov 18 2026 Pavel Skrylev <majioa@altlinux.org> 0.9.2.134-alt0.1
- + built rock-lgi 0.9.2.134 for Sisyphus with Lua 5.5.
- + added rock-lgi-devel with the native module build dependencies.
- * generated the RPM rock capability from the installed rockspec.
- * used the MIT license identifier.
