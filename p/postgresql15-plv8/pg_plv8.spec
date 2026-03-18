%define pg_ver 15
%define enable_llvm %(if pg_server_config --configure | grep -q LLVM_CONFIG ; then echo 1; else echo 0; fi)

Name: postgresql%pg_ver-plv8
Version: 3.2.4
Release: alt2

Summary: PLV8 - A Procedural Language in Javascript powered by V8
License: PostgreSQL
Group: Databases
Url: https://github.com/plv8/plv8

Source: %name-%version.tar
Source101: v8-cmake.tar
Patch0: %name-%version-%release.patch

BuildRequires: lld19.1-devel llvm19.1-devel clang19.1-devel cmake /proc
BuildRequires: postgresql%pg_ver-server-devel
Requires: postgresql%pg_ver-server

ExcludeArch: %e2k %ix86 loongarch64

%description
PLV8 is a shared library that provides a PostgreSQL procedural language powered
by V8 Javascript Engine. With this program you can write in Javascript your
function that is callable from SQL.

%prep
%setup
tar -xf %SOURCE101 -C deps/v8-cmake
%patch0 -p1

%build
%make CC=clang-19 CXX=clang++-19 LLVM_CONFIG=/usr/bin/llvm-config-19

%install
%makeinstall_std

%files
%doc docs/*
%_libdir/pgsql/*.so
%if %{enable_llvm}
%_libdir/pgsql/bitcode/*
%endif
%_datadir/pgsql/extension/*

%changelog
* Wed Mar 18 2026 Alexei Takaseev <taf@altlinux.org> 3.2.4-alt2
- Use LLVM if it used in PostgreSQL

* Wed Jul 30 2025 Alexei Takaseev <taf@altlinux.org> 3.2.4-alt1
- 3.2.4

* Tue Apr 15 2025 Alexei Takaseev <taf@altlinux.org> 3.2.3-alt1
- Initial build for ALT Linux
