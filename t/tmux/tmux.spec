Summary: Terminal multiplexer
Name: tmux
Version: 1.6
Release: alt1
Source0: http://downloads.sourceforge.net/%name/%name-%version.tar.gz
License: BSD
Group: Terminals
Url: http://tmux.sourceforge.net/

# Automatically added by buildreq on Tue Mar 16 2010
BuildRequires: libevent1.4-devel libncurses-devel

%description
tmux is a "terminal multiplexer". It allows a number of terminals (or
windows) to be accessed and controlled from a single terminal. It is
intended to be a simple, modern, BSD-licensed alternative to programs
such as GNU screen.

%prep
%setup
./configure

%build
CFLAGS="-I/usr/include/asm" %make_build

%install
install -D -m 755 %name %buildroot%_bindir/%name
install -D -m 644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc FAQ NOTES TODO CHANGES examples/
%_bindir/*
%_man1dir/*

%changelog
* Fri Feb 10 2012 Fr. Br. George <george@altlinux.ru> 1.6-alt1
- Autobuild version bump to 1.6

* Wed Jul 20 2011 Fr. Br. George <george@altlinux.ru> 1.5-alt1
- Autobuild version bump to 1.5

* Sun Jun 19 2011 Fr. Br. George <george@altlinux.ru> 1.4-alt1
- Autobuild version bump to 1.4

* Wed Jul 28 2010 Fr. Br. George <george@altlinux.ru> 1.3-alt1
- Version up

* Wed Mar 17 2010 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Version up

* Tue Nov 10 2009 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Version up

* Wed Sep 23 2009 Fr. Br. George <george@altlinux.ru> 1.0-alt1
- Version up

* Fri Jul 10 2009 Fr. Br. George <george@altlinux.ru> 0.9-alt1
- Version up

* Fri Jul 10 2009 Fr. Br. George <george@altlinux.ru> 0.8-alt1
- Initial build from MDV

* Sun May 03 2009 Lev Givon <lev@mandriva.org> 0.8-1mdv2010.0
+ Revision: 371132
- Update to 0.8.

* Wed Feb 11 2009 Lev Givon <lev@mandriva.org> 0.7-1mdv2009.1
+ Revision: 339511
- Update to 0.7.

* Tue Jan 20 2009 Lev Givon <lev@mandriva.org> 0.6-1mdv2009.1
+ Revision: 331825
- import tmux

