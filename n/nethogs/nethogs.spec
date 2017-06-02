Name: nethogs
Version: 0.8.5
Release: alt1

Summary: net top
License: GPL
Group: Monitoring

Url: https://github.com/raboof/nethogs
Source0: %name-%version.tar
Source1: nethogs.control
#Patch2: nethogs-0.8.0-alt-pid32.patch
Packager: Michael Shigorin <mike@altlinux.org>

# Automatically added by buildreq on Tue Apr 07 2009
BuildRequires: gcc-c++ libncurses-devel libpcap-devel
BuildRequires: /proc

Summary(pl.UTF-8): Sieciowy top

%description
NetHogs is a small 'net top' tool. Instead of breaking the traffic
down per protocol or per subnet, like most such tools do, it groups
bandwidth by process - and does not rely on a special kernel module to
be loaded. So if there's suddenly a lot of network traffic, you can
fire up NetHogs and immediately see which PID is causing this, and if
it's some kind of spinning process, kill it.

%description -l pl.UTF-8
NetHogs to małe narzędzie sieciowe w stylu programu top. Zamiast
rozbijania ruchu na protokoły lub podsieci, jak robi większość
narzędzi, grupuje pasmo według procesów - i nie polega przy tym na
specjalnym module jądra. Jeśli nagle jest duży ruch w sieci, można
uruchomić NetHogs i od razu zobaczyć, który PID to powoduje i
ewentualnie go zabić.

%prep
%setup -n %name-%version
#%patch2 -p1

%build
%make PREFIX=%_usr GCC="g++" CFLAGS="%optflags -I%_includedir/ncurses"

%install
install -pDm755 src/%name %buildroot%_sbindir/%name
install -pDm644 doc/%name.8 %buildroot%_man8dir/%name.8
install -pDm755 %SOURCE1 %buildroot%_controldir/%name

%pre
%_sbindir/groupadd -r -f netadmin >/dev/null 2>&1
%pre_control %name

%post
%post_control -s netadmin %name

%files
%doc Changelog README.md
%_sbindir/*
%_man8dir/*
%config %_controldir/%name

%changelog
* Fri Jun 02 2017 Michael Shigorin <mike@altlinux.org> 0.8.5-alt1
- built for sisyphus (closes: #33524), thanks Oleg!
- BR: /proc for tests

* Thu Jun 01 2017 Oleg Zenin <zenin_o@ihep.ru> 0.8.5-alt0
- Makefile and get(e)uid patches (cf. 0.8.0-alt3) appear
  to have been merged into the upstream.

* Fri Oct 14 2011 Michael Shigorin <mike@altlinux.org> 0.8.0-alt3
- replaced my kludge with a patch by vx8400/gmail.com (thx!)

* Wed Oct 12 2011 Michael Shigorin <mike@altlinux.org> 0.8.0-alt2
- kludged 16-bit pid assertion (doesn't bail out but shows
  a question mark instead of non-zero pids anyways)

* Sat Sep 24 2011 Michael Shigorin <mike@altlinux.org> 0.8.0-alt1
- 0.8.0
- updated debian patches

* Fri Oct 30 2009 Michael Shigorin <mike@altlinux.org> 0.7.0-alt2
- added debian patches to fix *UID check (closes: #18421)
- relocated binary to %_sbindir

* Tue Apr 07 2009 Michael Shigorin <mike@altlinux.org> 0.7.0-alt1
- 0.7.0
- removed patch

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 0.6.1-alt1
- initial build for ALT Linux Sisyphus (spec from PLD)
- added control(8) support
- spec cleanup

