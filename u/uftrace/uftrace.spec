Name: uftrace
Version: 0.9.4
Release: alt1

Summary: Function (graph) tracer for user-space

License: GPL-2.0
Group: Development/Debuggers
Url: https://github.com/namhyung/uftrace

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/namhyung/uftrace/archive/v%version.tar.gz
Source: %name-%version.tar

ExclusiveArch: x86_64 %ix86 aarch64

BuildRequires: libelf-devel
BuildRequires: libdw-devel

BuildRequires: pandoc

%description
The uftrace tool is to trace and analyze execution of a program written in
C/C++. It was heavily inspired by the ftrace framework of the Linux kernel
(especially function graph tracer) and supports userspace programs. It supports
various kind of commands and filters to help analysis of the program execution
and performance.

%prep
%setup

%build
%configure --libdir=%_libdir/%name
%make_build

%install
%makeinstall_std

%files
%_bindir/%name
%dir %_libdir/%name
%_libdir/%name/libmcount*.so
%_man1dir/%{name}*.1*
%_sysconfdir/bash_completion.d/%name
%doc COPYING
%doc README.md

%changelog
* Tue Oct 20 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt1
- new version 0.9.4 (with rpmrb script)

* Tue Oct 20 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- initial build for ALT Sisyphus

* Tue Oct  9 2018 ddiss@suse.com
- Upgrade to v0.9
  + argument update
  - automatic argument using DWARF debug info
    + add libdw-devel dependency
  + TUI implementation
  - graph, report and info commands using ncurses
  + filter changes
  - add --match option to select pattern matching method: regex or glob
  - add --no-event option to disable default events
  + i386 arch support
  + event update
  - add task events (fork/comm/exit) using Linux perf subsystem
  + trigger update
  - change 'read' trigger action to read events twice (at entry and exit)
  - add 'p' format for function pointer
  - add --auto-args option for automatic argument/return value
  - support enum type for auto-args
  + diff change
  - add 'compact' policy and make it default
  + graph change
  - add -f/--output-fields option to control output
  - show full graph when no function given
  - support fork+exec properly
  + script change
  - flush stdout buffer before fork
  - serialize execution using a mutex
  + Many bug fixes and improvements.
* Mon Oct 30 2017 ddiss@suse.com
- Initial commit
  + uftrace v0.8.1
