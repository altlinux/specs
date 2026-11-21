%global        lua_version 5.5
%global        current_lua_version %lua_version
%global        pure_dir %_libexecdir/luarocks
%global        native_dir %_libdir/luarocks
%global        rocks_dir %pure_dir/rocks

Name:          rock-luarocks
Version:       3.13.0
Release:       alt1
Summary:       LuaRocks package manager for Lua 5.5
License:       MIT
Group:         Development/Tools
Url:           https://luarocks.org/
Vcs:           https://github.com/luarocks/luarocks.git
Source:        %name-%version.tar
Source1:       luarocks55.filetrigger
Patch:         named-tree-paths.patch
Patch1:        bootstrap-rockspec.patch
BuildRequires(pre): rpm-build-rocks >= 5.5.1-alt1
BuildRequires(pre): rpm-macros-alternatives
BuildRequires: cmake(lua) >= %lua_version
Requires:      lua >= %lua_version
Requires(pre): alternatives >= 0:0.2.0-alt0.12

%description
LuaRocks installs and manages Lua modules with their package metadata.
This build uses Lua 5.5 and the ALT system rocks tree.


%prep
%setup
%autopatch -p1

%build
./configure \
   --prefix=%prefix \
   --sysconfdir=%_sysconfdir \
   --lua-version=%lua_version \
   --with-lua-interpreter=lua%lua_version \
   --with-lua-include=%_includedir/lua%lua_version \
   --with-lua-lib=%_libdir
%make_build luadir=%pure_dir

pure_dir=%pure_dir
native_dir=%native_dir
cat >> build/config-%lua_version.lua <<EOF_CONFIG
lua_modules_path = "${pure_dir#%_prefix/}"
lib_modules_path = "${native_dir#%_prefix/}"
rocks_subdir = "${pure_dir#%_prefix/}/rocks"
gcc_rpath = false
EOF_CONFIG

%install
cp build/config-%lua_version.lua config-%lua_version.lua
printf '\nwrap_bin_scripts = false\n' >> build/config-%lua_version.lua
%make_build bootstrap DESTDIR=%buildroot
install -m644 config-%lua_version.lua %buildroot%_sysconfdir/luarocks/config-%lua_version.lua

install -d %buildroot%_altdir %buildroot%native_dir %buildroot%_rpmlibdir
printf '%%s\t%%s\t%%s\n' %_bindir/luarocks %_bindir/luarocks-%lua_version 55 > %buildroot%_altdir/%name
sed 's|@ROCKS_DIR@|%rocks_dir|g' %SOURCE1 > %buildroot%_rpmlibdir/luarocks55.filetrigger
chmod 755 %buildroot%_rpmlibdir/luarocks55.filetrigger
printf '%%%%dir %%s\n' %pure_dir %native_dir | sort -u > rock-dirs.files

%check
export LUA_PATH_5_5='%buildroot%pure_dir/?.lua;;'
export LUAROCKS_CONFIG_5_5=%buildroot%_sysconfdir/luarocks/config-%lua_version.lua
grep -Fx '#!%_bindir/lua%lua_version' %buildroot%_bindir/luarocks-%lua_version
%buildroot%_bindir/luarocks-%lua_version --version
%buildroot%_bindir/luarocks-%lua_version --tree=%buildroot%_prefix list --porcelain luarocks |
   grep -E '^luarocks[[:space:]]+%version-%rock_revision[[:space:]]+installed'


%files         -f rock-dirs.files
%doc COPYING README.md
%dir %_sysconfdir/luarocks
%config(noreplace) %_sysconfdir/luarocks/config-%lua_version.lua
%_bindir/luarocks-%lua_version
%_bindir/luarocks-admin-%lua_version
%_altdir/%name
%dir %rocks_dir
%ghost %rocks_dir/manifest
%rocks_dir/luarocks/
%pure_dir/luarocks/
%_rpmlibdir/luarocks55.filetrigger


%changelog
* Wed Nov 18 2026 Pavel Skrylev <majioa@altlinux.org> 3.13.0-alt1
- > used upstream versions without rock revisions in RPM capabilities.
- + built rock-luarocks 3.13.0 for Sisyphus with Lua 5.5
    and the ALT system rocks tree.
- + added an alternative for /usr/bin/luarocks pointing to the Lua 5.5 CLI.
- + added support for custom named-tree deployment paths.
- * required alternatives before installation.
- * used Lua and CMake capabilities in package dependencies.
- * bootstrapped locally and made download and archive tools optional.
- * generated rock dependencies with rpm-build-rocks from Lua.
