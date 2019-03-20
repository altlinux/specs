%define _unpackaged_files_terminate_build 1

Name: x11perf
Version: 1.6.1
Release: alt1

Summary: x11perf application - X11 server performance test program
License: MIT
Group: System/X11

Url: https://gitlab.freedesktop.org/xorg/test/x11perf.git

Source: %name-%version.tar.gz

BuildRequires: libXext-devel
BuildRequires: libXft-devel
BuildRequires: libXmu-devel
BuildRequires: xorg-util-macros

%description
The x11perf program runs one or more performance tests and reports how
fast an X server can execute the tests.

%prep
%setup

%build
%autoreconf
%configure
%make_build V=1

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/X11/x11perfcomp/
%_man1dir/*

%changelog
* Wed Mar 20 2019 Fr. Br. George <george@altlinux.ru> 1.6.1-alt1
- Autobuild version bump to 1.6.1

* Fri Feb 15 2019 Egor Zotov <egorz@altlinux.org> 1.6.0-alt1.git5e8ed9b
- Update to current upstream version.

* Mon Aug 01 2011 Victor Forsiuk <force@altlinux.org> 1.5.4-alt1
- 1.5.4

* Thu Mar 03 2011 Victor Forsiuk <force@altlinux.org> 1.5.3-alt1
- 1.5.3

* Sun Jun 10 2007 Michael Shigorin <mike@altlinux.org> 1.4.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD, rev. 1.16)
- spec cleanup
