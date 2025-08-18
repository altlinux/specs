%define _unpackaged_files_terminate_build 1
%define luarocks_revision 1
# Disable on bootstrap.
%def_with check

Name: lua5.4-module-busted
Version: 2.2.0
Release: alt2_lr%luarocks_revision

Summary: Busted is a unit testing framework with a focus on being easy to use
License: MIT
Group: Development/Other
Url: https://lunarmodules.github.io/busted/
Vcs: https://github.com/lunarmodules/busted
BuildArch: noarch

Source: %name-%version.tar

# This patch has been applied in next upstream version which is not released yet.
# Fixes strict requirment of lua_cliargs 3.0.
Patch: lua-module-busted-2.2.0-alt-rockspec-fixes.patch
# Fixes assets regex path.
Patch1: lua-module-busted-2.2.0-alt-fixtures_fix.patch

# self-dependency
%filter_from_requires /lua5.4(busted\..*)/d
# Optional dependency provided by luajit which is currently supported only by lua5.1.
# Links to information about compatibility:
# https://github.com/LuaJIT/LuaJIT/issues/929
# https://luajit.org/install.html
%if "%(rpmvercmp '5.4' '5.1')" > "0"
%filter_from_requires /lua5.4(ffi)/d
%endif

BuildRequires(pre): rpm-macros-lua
BuildRequires: lua5.4-luarocks
BuildRequires: lua5.4-module-lua_cliargs
BuildRequires: lua5.4-module-luasystem
BuildRequires: lua5.4-module-dkjson
BuildRequires: lua5.4-module-say
BuildRequires: lua5.4-module-luassert
BuildRequires: lua5.4-module-lua-term
BuildRequires: lua5.4-module-penlight
BuildRequires: lua5.4-module-mediator_lua
%if_with check
BuildRequires: lua5.4-module-busted
BuildRequires: lua5.4-module-luacov
%endif

Provides: luarocks5.4(busted) = %EVR

%description
Busted is a unit testing framework with a focus on being easy to use.
Supports Lua >= 5.1, luajit >= 2.0.0, and moonscript.

Check out the official docs for extended info.

Busted test specs read naturally without being too verbose. You can
even chain asserts and negations, such as assert.is_not.equal. Nest
blocks of tests with contextual descriptions using describe, and add
tags to blocks so you can run arbitrary groups of tests.

An extensible assert library allows you to extend and craft your own
assert functions specific to your case with method chaining. A modular
output library lets you add on your own output format, along with the
default pretty and plain terminal output, JSON with and without
streaming, and TAP-compatible output that allows you to run busted
specs within most CI servers.

%package -n bash-completion-busted
Summary: Bash completion for busted
Group: Shells
BuildArch: noarch
Requires: %name
Requires: bash-completion

%description -n bash-completion-busted
Contains bush completion for busted.

%package -n zsh-completion-busted
Summary: zsh completion for busted
Group: Shells
BuildArch: noarch
Requires: zsh
Requires: %name

%description -n zsh-completion-busted
Contains zsh completion for busted.

%prep
%setup
%autopatch -p1

# 2.2.0-alt1_lr1
# Replace lua with appropriate intrepreter/.
sed -i "s|#!/usr/bin/env lua|#!/usr/bin/env lua5.4|g" bin/busted
sed -i "s|#!/usr/bin/env lua|#!/usr/bin/env lua5.4|g" spec/lua.lua

%build
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	rockspecs/busted-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

# Fix paths.
sed -i 's|%buildroot||g' %buildroot%_bindir/busted

# Completions.
install -dp %buildroot%_datadir/bash-completion/completions/
install -dp %buildroot%_datadir/zsh/site-functions/
install -p -m 644 completions/bash/busted.bash %buildroot%_datadir/bash-completion/completions/busted
install -p -m 644 completions/zsh/_busted %buildroot%_datadir/zsh/site-functions/_busted

%check
luarocks-5.4 test --test-type busted \
	rockspecs/busted-%version-%luarocks_revision.rockspec

%files
%doc LICENSE
%_bindir/busted
%luarocks_dbdir/busted
%lua_modulesdir_noarch/busted

%files -n bash-completion-busted
%_datadir/bash-completion/completions/busted

%files -n zsh-completion-busted
%_datadir/zsh/site-functions/_busted

%changelog
* Wed Aug 13 2025 Sergey Zhidkih <rx1513@altlinux.org> 2.2.0-alt2_lr1
- Enable tests.

* Wed Apr 30 2025 Sergey Zhidkih <rx1513@altlinux.org> 2.2.0-alt1_lr1
- Initital build.
