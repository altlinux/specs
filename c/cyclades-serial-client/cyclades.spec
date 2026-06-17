Name: cyclades-serial-client
Version: 0.95
Release: alt1

Summary: Serial port client
License: GPL-2.0
Group: System/Kernel and hardware
Url: http://www.lysator.liu.se/~astrand/projects/cyclades-serial-client

Source: %name-%version.tgz
Patch1: cyclades-serial-client-termio.patch

# Automatically added by buildreq on Fri Jun 08 2007
BuildRequires: gcc-c++

%description
Network Serial port client software for Cyclades terminal servers
This is the client for network serial port emulation via the RFC 2217
protocol as used by Cyclades terminal servers and other products.  It
consists of a daemon that manages a pseudo-tty and a shared object to take
over the tcsetattr() and tcsendbreak() library calls to redirect their
functionality over the network.

%set_verify_elf_method textrel=relaxed

%prep
%setup
%autopatch -p1

%build
%add_optflags -fcommon
%autoreconf
%configure
%make

%install
%makeinstall_std

%files
%_target_libdir_noarch/lib*
%_sysconfdir/*
%_sbindir/*
%_man5dir/*
%_man8dir/*

%changelog
* Wed Jun 17 2026 Andrew A. Vasilyev <andy@altlinux.org> 0.95-alt1
- NMU: fix FTBFS with new glibc
- update to new version

* Fri Mar 26 2021 Slava Aseev <ptrnine@altlinux.org> 0.93-alt5
- fix build with gcc-10

* Mon Apr 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.93-alt4
- fix build

* Fri Aug 20 2010 Ilya Mashkin <oddity@altlinux.ru> 0.93-alt3
- fix requires

* Tue Jun 12 2007 Lunar Child <luch@altlinux.ru> 0.93-alt2
- fix changelog.

* Fri Jun 08 2007 Lunar Child <luch@altlinux.ru> 0.93-alt1
- Initial build for ALT Linux Sisyphus.
