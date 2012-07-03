Name: ttysnoop
Version: 0.12d
Release: alt1

Summary: Program to snoop on a TTY through another
License: distributable
Group: Terminals

Source: ftp://metalab.unc.edu/pub/Linux/utils/terminal/%name-%version.tar.gz
Patch: ttysnoop_0.12d-3.diff.gz
Packager: Michael Shigorin <mike@altlinux.org>

Summary(pl):	Program s³u¿acy do kontrolowania jednej konsoli za pomoc± innej

%define _sbindir /sbin

%description
The package allows you to snoop on login tty's through another
tty-device or pseudo-tty. The snoop-tty becomes a 'clone' of the
original tty, redirecting both input and output from/to it.

%description -l pl
Pakiet ten pozwala na podgl±danie i kontrolowanie loginowych tty
poprzez inne urz±dzenie tego typu lub pseudo-tty. Urz±dzenie
kontroluj±ce stajê siê klonem pierwotnego tty, przekierowuj±c strumieñ
wej¶cia/wyj¶cia do niej.

%prep
%setup
%patch -p1

%build
make OPT="%optflags"

%install
install -pDm755 ttysnoop	%buildroot%_sbindir/ttysnoop
install -pDm755 ttysnoops	%buildroot%_sbindir/ttysnoops
install -pDm644 ttysnoop.8	%buildroot%_man8dir/ttysnoop.8
install -pDm640 snooptab.dist	%buildroot%_sysconfdir/snooptab
echo ".so ttysnoop.8" > %buildroot%_man8dir/ttysnoops.8
install -d %buildroot%_spooldir/%name

%files
%_sbindir/*
%attr(640,root,root) %config(noreplace) %_sysconfdir/snooptab
%attr(700,root,root) %dir %_var/spool/%name
%doc README
%_man8dir/*

%changelog
* Sun Apr 12 2009 Michael Shigorin <mike@altlinux.org> 0.12d-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)
- applied Debian patch (as is)
