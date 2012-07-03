%define oname luafilesystem
Name: lua5-luafilesystem
Version: 1.5.0_2_gae5a05d
Release: alt1
Summary: Lua library to complement functions related to file systems
License: MIT
Group: Development/Other
Url: http://www.keplerproject.org/luafilesystem/
Packager: Ildar Mulyukov <ildar@altlinux.ru>

#git://github.com/keplerproject/luafilesystem.git
Source: %oname-%version.tar
Patch: %name-alt-build.patch

# Automatically added by buildreq on Mon Jun 21 2010
BuildRequires: liblua5-devel

%description
LuaFileSystem is a Lua library developed to complement the set of functions
related to file systems offered by the standard Lua distribution.

LuaFileSystem offers a portable way to access the underlying directory
structure and file attributes.

LuaFileSystem is free software and uses the same license as Lua 5.1.

%prep
%setup -n %oname
%patch -p1

%build
make

%install
mkdir -p \
	%buildroot%_libdir/lua5/
install -p src/*.so %buildroot%_libdir/lua5/

%files
%_libdir/lua5/*.so
%doc README doc/* tests

%changelog
* Mon Jun 21 2010 Ildar Mulyukov <ildar@altlinux.ru> 1.5.0_2_gae5a05d-alt1
- initial build for ALTLinux
