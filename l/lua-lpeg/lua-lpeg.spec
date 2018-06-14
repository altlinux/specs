%define modname lpeg

%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))")}
%define lualibdir %_libdir/lua/%luaver
%define luapkgdir %_datadir/lua/%luaver

%def_enable check

Name: lua-%modname
Version: 1.0.1
Release: alt1

Summary: Parsing Expression Grammars for Lua
Group: Development/Other
License: MIT
Url: http://www.inf.puc-rio.br/~roberto/%modname/

Source: %url/%modname-%version.tar.gz

BuildRequires: lua-devel >= %luaver
Requires: lua >= %luaver
Source44: import.info

%description
LPeg is a new pattern-matching library for Lua, based on Parsing Expression
Grammars (PEGs).

%prep
%setup -n %modname-%version

%build
%make_build COPT="%optflags"

%install
mkdir -p %buildroot%lualibdir
mkdir -p %buildroot%luapkgdir
install -p lpeg.so %buildroot%lualibdir/lpeg.so.%version
ln -s lpeg.so.%version %buildroot%lualibdir/lpeg.so
install -p -m0644 re.lua %buildroot%luapkgdir

%check
LD_LIBRARY_PATH=$PWD %make test

%files
%lualibdir/*
%luapkgdir/*
%doc HISTORY lpeg.html re.html lpeg-128.gif
%doc %attr(0644,root,root) test.lua

%changelog
* Thu Jun 14 2018 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1 (ALT #35032)

* Wed Oct 05 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.12.2-alt1_2
- converted for ALT Linux by srpmconvert tools

