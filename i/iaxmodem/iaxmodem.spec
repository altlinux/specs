Name: iaxmodem
Version: 1.2.0
Release: alt1
Summary: IAX software fax modem
License: GPL
Group: Communications

Url: http://iaxmodem.sourceforge.net

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name.tar
Source2: %name.init
Source3: %name-sysconfig
Source4: %name.ttyIAX

Patch: %name.as-needed.patch
Patch1: %name.pidfile.patch

# Automatically added by buildreq on Sat May 07 2011 (-bb)
# optimized out: elfutils libX11-devel libstdc++-devel xorg-xproto-devel
BuildRequires: gcc-c++ glibc-devel-static libaudiofile-devel libfftw3-devel libfltk-devel libtiff-devel libxml2-devel

%description
%summary

%prep
%setup -c
%patch0 -p2
%patch1 -p0

%build
./build static

%install
install -D -m755 %name %buildroot%_sbindir/%name
install -D -m644 %name.1 %buildroot%_man1dir/%name.1
install -D -m755 %SOURCE2 %buildroot%_initdir/%name
install -D -m644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -D -m644 %SOURCE4 %buildroot%_sysconfdir/%name/ttyIAX
mkdir -p %buildroot%_sysconfdir/%name
mkdir -p %buildroot/var/log/%name
mkdir -p %buildroot/var/run/%name
mkdir -p %buildroot/var/log/%name
touch %buildroot/var/log/%name/%name

%preun
%preun_service iaxmodem

%post
%post_service iaxmodem

%files
%_sbindir/%name
%_man1dir/*
%_initdir/%name
%config(noreplace) %_sysconfdir/%name/*
%_sysconfdir/sysconfig/%name
%dir /var/log/%name
%dir /var/run/%name
%dir /var/log/%name
%dir %_sysconfdir/%name
%doc TODO README FAQ CHANGES *.ttyIAX

%ghost /var/log/%name/%name

%changelog
* Sat May 07 2011 Denis Smirnov <mithraen@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat May 07 2011 Denis Smirnov <mithraen@altlinux.ru> 1.1.1-alt4
- fix EOL in config file (ALT #25577)
- fix path to lockfile (ALT #25578)
- add post_service/preun_service (ALT #25576)

* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 1.1.1-alt3
- auto rebuild

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 1.1.1-alt2
- cleanup spec

* Mon Jul 28 2008 Denis Smirnov <mithraen@altlinux.ru> 1.1.1-alt1
- update to 1.1.1
- fix unaligned errors in libiax2 (Gus Bourg)
- improve training in spandsp V.27ter receive (Steve Underwood)
- fix a potential crash (divide by zero) in spandsp V.17 receive (Steve
  Underwood)

* Sun Mar 30 2008 Denis Smirnov <mithraen@altlinux.ru> 1.1.0-alt1
- update to 1.1.0
- kill -HUP now makes the modems wait to restart when they're on-hook
- improve IAX2 call rejection when the modem is busy by using
- REJECT instead of ACCEPT+CONGSTN+HANGUP
- add "nodaemon" config file feature
- add "iax2debug" and "dspdebug" config file features
- update spandsp to 20080110 snapshot
- update libiax2 to current iaxclient/lib/libiax2 + patches

* Thu Nov 29 2007 Denis Smirnov <mithraen@altlinux.ru> 0.3.2-alt1
- support dialing of DTMF and commas
- fix receive aborts when carrier is connected
- fix +FRH:3 from appearing at improper times
- set hang-up timer on unexpected disconnections as well
- stop fast looping on registration rejection
- fix numerous training issues with V.17 rx
- update spandsp to snapshot 20070802

* Thu Nov 29 2007 Denis Smirnov <mithraen@altlinux.ru> 0.3.1-alt1
- add -F option to prevent detachment (Francesco P. Sileno)
- update spandsp to snapshot 20070619
- fix possible initial failure to register

* Mon Jun 11 2007 Denis Smirnov <mithraen@altlinux.ru> 0.3.0-alt1
- skip non-regular files in %_sysconfdir/iaxmodem (Julien BLACHE)
- take caution against bad refresh negotiations from the server
- update spandsp to snapshot 20070502 (adds V.17 rx support)
- improve the ability to detect quiet signalling (spandsp: fsk min_power)
- improve the sensitivity to carrier loss (spandsp: power_meter)
- improve tcflushing when getty not reading pty and buffer fills,  prevents
  fast looping when buffer is filled

* Wed Apr 18 2007 Denis Smirnov <mithraen@altlinux.ru> 0.2.1-alt1
- upstream update 0.2.0->0.2.1

* Tue Feb 20 2007 Denis Smirnov <mithraen@altlinux.ru> 0.2.0-alt1
- upstream update 0.1.14->0.2.0

* Thu Jan 11 2007 Denis Smirnov <mithraen@altlinux.ru> 0.1.14-alt5
- LSB initscript
- start after Asterisk if installed
- do not requires bash for initscript

* Fri Oct 27 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1.14-alt4
- update initscript (thanks to Ivan Kurbanov)
- add sysconfig (thanks to Ivan Kurbanov)
- patch for creating pidfile in /var/run/iaxmodem/
- add log dir for iaxmodem
- add default config (thanks to Ivan Kurbanov)

* Wed Oct 25 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1.14-alt3
- create log dir

* Wed Oct 25 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1.14-alt2
- fix requires
- add initscript

* Tue Oct 24 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1.14-alt1
- first build for Sisyphus
