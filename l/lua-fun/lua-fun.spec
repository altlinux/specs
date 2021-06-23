%define luaver 5.3
%define luapkgdir %{_datadir}/lua/%{luaver}
# LuaJIT is compatible with Lua 5.1 and uses the same directory for modules
%global ljpkgdir %{_datadir}/lua/5.1

Name: lua-fun
Version: 0.1.3
Release: alt2
Summary: Functional programming library for Lua
Group: Development/Other
License: MIT
URL: https://github.com/rtsisyk/luafun
Source0: https://github.com/rtsisyk/luafun/archive/%{version}/luafun-%{version}.tar.gz
BuildArch: noarch
BuildRequires: /usr/bin/luajit
BuildRequires: lua >= 5.1
Requires: lua >= 5.1
Source44: import.info

%package -n luajit-fun
Group: Development/Other
Summary: Functional programming library for LuaJIT

%description -n lua-fun
Lua Fun is a high-performance functional programming library for Lua
designed with LuaJIT's trace compiler in mind.

Lua Fun provides a set of more than 50 programming primitives typically
found in languages like Standard ML, Haskell, Erlang, JavaScript, Python and
even Lisp. High-order functions such as map, filter, reduce, zip, etc.,
make it easy to write simple and efficient functional code.

This package provides a module for Lua %{luaver}.

%description -n luajit-fun
Lua Fun is a high-performance functional programming library for Lua
designed with LuaJIT's trace compiler in mind.

Lua Fun provides a set of more than 50 programming primitives typically
found in languages like Standard ML, Haskell, Erlang, JavaScript, Python and
even Lisp. High-order functions such as map, filter, reduce, zip, etc.,
make it easy to write simple and efficient functional code.

This package provides a module for LuaJIT.

%prep
%setup -q -n luafun-%{version}

%build
# nothing to do

%install
# Install for Lua
mkdir -p %{buildroot}%{luapkgdir}
cp -av fun.lua %{buildroot}%{luapkgdir}/fun.lua
# Install for LuaJIT
mkdir -p %{buildroot}%{ljpkgdir}
cp -av fun.lua %{buildroot}%{ljpkgdir}/fun.lua

%check
cd tests
luajit ./runtest *.lua
lua ./runtest *.lua

%files -n lua-fun
%{luapkgdir}/fun.lua
%doc README.md CONTRIBUTING.md
%doc COPYING.md

%files -n luajit-fun
%{ljpkgdir}/fun.lua
%doc README.md CONTRIBUTING.md
%doc COPYING.md

%changelog
* Wed Jun 23 2021 Vladimir Didenko <cow@altlinux.org> 0.1.3-alt2
- luajit-fun doesn't need luajit binary as a dependency

* Wed Oct 05 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1.3-alt1_2
- converted for ALT Linux by srpmconvert tools
