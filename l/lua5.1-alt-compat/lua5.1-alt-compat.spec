Name: lua5.1-alt-compat
Version: 1.0
Release: alt1
Summary: Utility package for ALT Lua compatibility
License: GPL
Group: System/Libraries
Packager: Ildar Mulyukov <ildar@altlinux.ru>

#%%lua_modulesdir
Provides: %_libdir/lua/5.1
#%%lua_modulesdir_noarch
Provides: %_datadir/lua/5.1

%description
Utility package for ALT Lua compatibility

YOU GENERALLY DON'T NEED TO INSTALL IT

%install
for d in %_libdir/lua/ %_datadir/lua/ ; do
	mkdir -p %buildroot$d
	ln -s ../lua5 %buildroot$d/5.1
done

mkdir -p %buildroot%_rpmlibdir/
cat>%buildroot%_rpmlibdir/lua-files.req.list <<EOF
%_libdir/lua/5.1
%_datadir/lua/5.1
EOF

%files
%dir %_libdir/lua
%_libdir/lua/5.1
%dir %_datadir/lua
%_datadir/lua/5.1
%_rpmlibdir/lua-files.req.list

%changelog
* Wed Jan 05 2011 Ildar Mulyukov <ildar@altlinux.ru> 1.0-alt1
- initial build for ALT Linux Sisyphus
