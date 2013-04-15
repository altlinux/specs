%define oname luaexpat
Name: lua5-luaexpat
Version: 1.1
Release: alt1.qa1
Summary: SAX XML parser for Lua based on the Expat library
License: MIT
Group: Development/Other
Url: http://www.keplerproject.org/luaexpat/
Packager: Ildar Mulyukov <ildar@altlinux.ru>

Source: http://luaforge.net/frs/download.php/2469/luaexpat-1.1.tar
#.gz
Patch: %name-alt-build.patch

# Automatically added by buildreq on Mon Jun 21 2010
BuildRequires: libexpat-devel liblua5-devel

%description
LuaExpat is a SAX XML parser based on the Expat library.

LuaExpat is free software and uses the same license as Lua 5.1.

%prep
%setup -n %oname-%version
%patch -p1

%build
make \
	CFLAGS="%optflags_shared" \
	LUA_VERSION_NUM=501 \

%install
%make_install install \
	LUA_LIBDIR=%buildroot%_libdir/lua5 \
	LUA_DIR=%buildroot%_datadir/lua5

%files
%_libdir/lua5/*.so*
%_datadir/lua5/*
%doc README doc/* tests

%changelog
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Mon Jun 21 2010 Ildar Mulyukov <ildar@altlinux.ru> 1.1-alt1
- initial build for ALTLinux
