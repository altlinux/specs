%define modname lunit
%define luaver 5.3
%define luapkgdir %_datadir/lua/%luaver

%def_enable check

Name: lua-lunit
Version: 0.5
Release: alt2

Summary: Unit testing framework for Lua
Group: Development/Other
License: MIT
Url: https://nessie.de/mroth/%modname/index.html

Source: %url/%modname-%version.tar.gz
Source44: import.info

BuildArch: noarch

Requires: lua >= %luaver

%{?_enable_check:BuildRequires: lua >= %luaver}

%description
Lunit is a unit testing framework for lua, written in lua.

Lunit provides 26 assert functions, and a few misc functions for usage
in an easy unit testing framework.

Lunit comes with a test suite to test itself. The testsuite consists
of approximately 710 assertions.

%prep
%setup -n %modname-%version

%build
%install
mkdir -p %buildroot%_bindir
cp -p lunit %buildroot%_bindir

mkdir -p %buildroot%luapkgdir
cp -pr lunit{,-console}.lua %buildroot%luapkgdir

%check
./lunit lunit-tests.lua | tee testlog.txt
grep -q "0 failed, 0 errors" testlog.txt

%files
%doc LICENSE ANNOUNCE CHANGES DOCUMENTATION README* example.lua
%_bindir/lunit
%luapkgdir/*

%changelog
* Thu Jun 14 2018 Yuri N. Sedunov <aris@altlinux.org> 0.5-alt2
- rebuilt for lua-5.3

* Wed Oct 05 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.5-alt1_10
- converted for ALT Linux by srpmconvert tools

