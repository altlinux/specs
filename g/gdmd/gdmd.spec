Name: gdmd
Version: 0.26.0
Release: alt1
Summary: DMD-like wrapper for GDC
License: GPL-3.0-or-later
Group: Development/Other
Url: https://github.com/D-Programming-GDC/gdmd
VCS: https://github.com/D-Programming-GDC/gdmd
BuildArch: noarch

Source: %name-%version.tar

Requires: gcc-gdc
Requires: perl-base

%description
GDMD is a wrapper script for GDC (the D language frontend for GCC)
that emulates the DMD command-line interface. This allows build systems
and tools designed for DMD to work with GDC without modification.

%prep
%setup

%install
mkdir -p %buildroot%_bindir %buildroot%_man1dir
%makeinstall_std prefix=%_prefix

%files
%doc README.md ChangeLog
%_bindir/gdmd
%_man1dir/gdmd.1*

%changelog
* Thu Feb 19 2026 Anton Farygin <rider@altlinux.org> 0.26.0-alt1
- initial build for ALT Linux
