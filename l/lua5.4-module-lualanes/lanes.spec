%define _unpackaged_files_terminate_build 1
%def_without check
%define luarocks_revision 0

Name: lua5.4-module-lualanes
Version: 4.0.0
Release: alt1_lr%luarocks_revision

Summary: Lanes is a lightweight, native, lazy evaluating multithreading library for Lua 5.1 to 5.4
License: MIT
Group: Development/Other
Url: https://lualanes.github.io/lanes/
Vcs: https://github.com/LuaLanes/lanes

# Self provided dependency.
%filter_from_requires /lua5.4(lanes_core)/d

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-lua
BuildRequires: gcc-c++
BuildRequires: lua5.4-luarocks
BuildRequires: liblua5.4-devel
BuildRequires: lua5.4-module-luasocket
# Dependency required for linda_perf test
BuildRequires: rpm-build-vm

%description
Lanes is a lightweight, native, lazy evaluating multithreading library
for Lua 5.1 to Lua 5.4. It allows efficient use of multicore processors
in Lua, by passing function calls into separate OS threads, and
separate Lua states.

No locking of the threads is needed, only launching and waiting for
(with an optional timeout) a thread to get ready. Efficient
communications between the running threads are possible either using
message passing or shared state models. Values passed can be anything
but coroutines (see detailed limitations in the manual).

Lua Lanes has been optimized for performance, and provides around
50-60%% speed increase when running heavily threaded applications on
dual core processors (compared to running a non-threaded plain Lua
implementation).

Starting with version 3.0, Lanes is compatible with LuaJIT 2.

%package doc
Summary: Documentation for lualanes
Group: Documentation
BuildArch: noarch

%description doc
Documentation for lualanes.

%prep
%setup

%build
export CFLAGS="-std=c++20"
luarocks-5.4 make --verbose --local --deps-mode all --pack-binary-rock \
	lanes-%version-%luarocks_revision.rockspec

%install
luarocks-5.4 install --verbose --local --deps-mode none \
	--no-manifest --tree %buildroot%prefix *.rock

%check
# Tell where to find installed modules.
export LUA_CPATH='%_libdir/lua/5.4/?.so'
export LUA_PATH='%_datadir/lua/5.4/?.lua'
# linda_perf test requires root previleges
vm-run --heredoc <<EOF
	%make_build test
EOF

%files
%doc COPYRIGHT
%luarocks_dbdir/lanes
%lua_modulesdir/lanes_core.so
%lua_modulesdir_noarch/lanes.lua

%files doc
%doc docs/*

%changelog
* Tue Mar 03 2026 Sergey Zhidkih <rx1513@altlinux.org> 4.0.0-alt1_lr0
- New version (4.0.0):
  + Switch to C++ implementation.

* Tue Feb 10 2026 Sergey Zhidkih <rx1513@altlinux.org> 3.17.2-alt2_lr0
- Fix FTBFS by removing dependency on luasocket-devel.

* Tue Dec 23 2025 Sergey Zhidkih <rx1513@altlinux.org> 3.17.2-alt1_lr0
- New version (3.17.2).

* Mon Apr 22 2025 Sergey Zhidkih <rx1513@altlinux.org> 3.17.1-alt1_lr0
- First build for alt.
