%def_without doc

Name: lua5.1-module-event
Version: 0.4.6
Release: alt1

Source: luaevent-%version.tar

License: MIT
Url: https://github.com/harningt/luaevent/
Summary: Bindings of libevent to Lua
Group: Development/Other

# Make sure CFLAGS/LDFLAGS are respected.
Patch0: lua-event-0.4.3-respect-cflags.patch
# Conditionalize env calls which are gone in modern lua
Patch1: luaevent-0.4.3-envfix.patch

BuildRequires: lua5.1 liblua5.1-devel libevent-devel >= 1.4

%description
Lua bindings for libevent, an asynchronous event notification library
that provides a mechanism to execute a callback function when a specific
event occurs on a file descriptor or after a timeout has been reached.

%if_with doc
%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch
BuildRequires: ikiwiki

%description doc
This package contains documentation for developing applications that
use Lua bindings for libevent, an asynchronous event notification library
that provides a mechanism to execute a callback function when a specific
event occurs on a file descriptor or after a timeout has been reached.
%endif

%prep
%setup -n luaevent-%version
%patch0 -p1
%patch1 -p1 -b .envfix
# Remove 0-byte file.
rm -f doc/modules/luaevent.mdwn

%build
export CFLAGS="%optflags"
%make_build

%if_with doc
/bin/sh makeDocs.sh
%endif

%install
%makeinstall_std \
	INSTALL_DIR_LUA=%lua_modulesdir_noarch \
	INSTALL_DIR_BIN=%lua_modulesdir \
	#

%check
lua5.1 -e \
  'package.cpath="%buildroot%lua_modulesdir/?.so;"..package.cpath;
   package.path="%buildroot%lua_modulesdir_noarch/?.lua;"..package.path;
   dofile("test/basic.lua");'

%files
%doc doc/COPYING CHANGELOG README doc/COROUTINE_MANAGEMENT doc/PLAN
%dir %lua_modulesdir/luaevent/
%lua_modulesdir/luaevent/core.so
%lua_modulesdir_noarch/luaevent.lua

%if_with doc
%files doc
%doc html/*
%endif

%changelog
* Sun Jul 03 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.4.6-alt1
- Initial build for ALT Sisyphus based on Fedora package.
