Name: cgdb
Summary: Frontend for GDB
Version: 0.6.4
Release: alt3
Url: http://cgdb.sourceforge.net/
License: GPL2
Group: Development/Debuggers

Packager: Alexey Gladkov <legion@altlinux.ru>

Source: %name-%version.tar.bz2
Patch0: cgdb-alt-fix-xfree.patch

Requires: gdb

# Automatically added by buildreq on Fri Sep 26 2008
BuildRequires: flex libncurses-devel libreadline-devel

%description
CGDB is a curses (terminal-based) interface to the GNU Debugger (GDB).
Its goal is to be lightweight and responsive; not encumbered with
unnecessary features. 

%prep
%setup -q
%patch0 -p1

%build
%configure
printf '#define HAVE_DEV_PTMX 1\n' >> config.h

%make_build

%install
%makeinstall_std

%files
%doc README NEWS
%_bindir/*
%_datadir/%name
%_infodir/*
%_man1dir/*

%changelog
* Thu Dec 17 2009 Alexey Gladkov <legion@altlinux.ru> 0.6.4-alt3
- Remove obsolete macros.

* Fri Sep 26 2008 Alexey Gladkov <legion@altlinux.ru> 0.6.4-alt2
- Fix requires.

* Fri Sep 26 2008 Alexey Gladkov <legion@altlinux.ru> 0.6.4-alt1
- initial build for ALT Linux Sisyphus
