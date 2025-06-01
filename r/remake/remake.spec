%define _unpackaged_files_terminate_build 1

Name: remake
Version: 4.3+dbg1.6
Release: alt1

Summary: GNU make fork with improved error reporting and debugging
License: GPL-3.0
Group: Development/Other
Url: https://salsa.debian.org/debian/remake

Source: %name-%version.tar

BuildRequires: libreadline-devel

%description
Modernized version of GNU make utility that adds improved error
reporting, the ability to trace execution in a comprehensible way, and
a debugger. Some of the features of the debugger are:

* see the target call stack
* set breakpoints on targets
* show and set variables
* execute arbitrary "make" code
* issue shell commands while stopped in the middle of execution
* inspect target descriptions
* write a file with the commands of the target expanded

%prep
%setup
patch -p1 < debian/patches/disable-doc-build.patch

%build
export CFLAGS="%{optflags} -fcommon"
%autoreconf
%configure --disable-nls --enable-maintainer-mode
%make_build

%install
%makeinstall_std

%check
%make_build check

%files
%doc *.md
%_bindir/*
%_man1dir/*
%exclude %_includedir/gnuremake.h

%changelog
* Sun Jun 01 2025 Nikolay Strelkov <snk@altlinux.org> 4.3+dbg1.6-alt1
- Initial build for Sisyphus
