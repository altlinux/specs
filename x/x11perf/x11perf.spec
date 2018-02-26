Name: x11perf
Version: 1.5.4
Release: alt1

Summary: x11perf application - X11 server performance test program
License: MIT
Group: System/X11

Url: http://cgit.freedesktop.org/xorg/app/x11perf/
Source: http://xorg.freedesktop.org/releases/individual/app/x11perf-%version.tar.bz2

# Automatically added by buildreq on Mon Aug 01 2011
BuildRequires: libXext-devel libXft-devel libXmu-devel

%description
The x11perf program runs one or more performance tests and reports how
fast an X server can execute the tests.

%prep
%setup

%build
%configure
%make_build V=1

%install
%makeinstall_std

%files
%_bindir/*
%_libdir/X11/x11perfcomp/
%_man1dir/*

%changelog
* Mon Aug 01 2011 Victor Forsiuk <force@altlinux.org> 1.5.4-alt1
- 1.5.4

* Thu Mar 03 2011 Victor Forsiuk <force@altlinux.org> 1.5.3-alt1
- 1.5.3

* Sun Jun 10 2007 Michael Shigorin <mike@altlinux.org> 1.4.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD, rev. 1.16)
- spec cleanup
