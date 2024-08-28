%global _unpackaged_files_terminate_build 1

Name: gf
Version: 0
Release: alt1

Summary: A GDB frontend for Linux
License: MIT
Group: Development/Debuggers
Url: https://github.com/nakst/gf

Source: %name-%version.tar

Requires: gdb

BuildRequires: gcc-c++
BuildRequires: gdb
BuildRequires: libX11-devel
BuildRequires: libfreetype-devel

%description
%summary.

%prep
%setup

%build
cp extensions_v5/extensions.cpp .
./build.sh

%install
install -pD -m755 gf2 %buildroot%_bindir/gf2
install -pD -m644 extensions_v5/gf_profiling.c %buildroot%_includedir/gf/gf_profiling.c

%files
%doc README.md
%doc extensions_v5/profiler_instructions.txt
%_bindir/gf2
%_includedir/gf/

%changelog
* Wed Aug 28 2024 Alexander Stepchenko <geochip@altlinux.org> 0-alt1
- Initial build for ALT.
