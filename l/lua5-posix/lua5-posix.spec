Name: lua5-posix
Version: 5.1.1
Release: alt1
Epoch: 1

Summary: POSIX library for Lua
License: MIT
Group: Development/Other

URL: http://luaforge.net/projects/luaposix/
Source: luaposix-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Mon Sep 28 2009
BuildRequires: liblua5-devel lua5

%description
This is a POSIX library for Lua which provides access to many POSIX features
to Lua programs.

%prep
%setup -q -n luaposix-%version
%patch -p1

%build
gcc -shared %optflags %optflags_shared lposix.c -o posix.so -llua -Wl,-z,defs
lua -e 'require "posix"; print(posix.version)'

%install
install -pD -m755 posix.so %buildroot%_libdir/lua5/posix.so

%files
%doc ChangeLog README
%_libdir/lua5/posix.so

%changelog
* Mon Sep 28 2009 Alexey Tourbin <at@altlinux.ru> 1:5.1.1-alt1
- updated to 5.1.1
- disabled mkstemp patch for now

* Tue May 16 2006 Alexey Tourbin <at@altlinux.ru> 2006-alt1
- new version for lua-5.1 from http://lua-users.org/lists/lua-l/2006-04/msg00162.html

* Mon May 09 2005 Alexey Tourbin <at@altlinux.ru> 2003.11.07-alt2
- removed posix.lua, compat-5.1.lua should be used instead

* Sat Sep 18 2004 Alexey Tourbin <at@altlinux.ru> 2003.11.07-alt1
- initial revision
