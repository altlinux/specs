Name: cpuspeed
Version: 1.5
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: CPU Frequency adjusting daemon
License: GPLv2+
Group: System/Kernel and hardware

Url: http://carlthompson.net/Software/CPUSpeed
Source0: http://www.carlthompson.net/downloads/cpuspeed/cpuspeed-%version.tar.bz2
# TODO: initscript logic improvement (TARGET: 1.5-alt2)
Source1: cpuspeed.init
Source2: cpuspeed.conf

Patch1: cpuspeed-1.5-no-affected_cpus-fallback.patch

# Automatically added by buildreq on Wed Apr 18 2007
BuildRequires: gcc-c++

%description
cpuspeed is a daemon that dynamically changes the speed of your processor(s)
depending upon its current workload if CPU is capable (needs Intel Speedstep,
AMD PowerNow!, or similar support). It also supports enabling CPU frequency
scaling via in-kernel governors on Intel Centrino and AMD Athlon64/Opteron
platforms.

The program can also be configured to reduce the CPU clock speed if the CPU
temperature gets too high or if the computer's AC adapter is disconnected.

%prep
%setup
%patch1 -p1
%__subst 's/strip /# strip /' Makefile

%build
%make COPTS="%optflags"

%install
install -pD -m755 cpuspeed %buildroot/sbin/cpuspeed
install -pD -m755 %_sourcedir/cpuspeed.init %buildroot%_initdir/cpuspeed
install -pD -m644 %_sourcedir/cpuspeed.conf %buildroot%_sysconfdir/sysconfig/cpuspeed

%post
%post_service cpuspeed

%preun
%preun_service cpuspeed

%files
%doc CHANGES FEATURES USAGE
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/sysconfig/cpuspeed
/sbin/cpuspeed
%_initdir/cpuspeed

%changelog
* Thu Oct 23 2008 Victor Forsyuk <force@altlinux.org> 1.5-alt1
- 1.5

* Tue Sep 23 2008 Victor Forsyuk <force@altlinux.org> 1.2.1-alt3
- Fix ALT#17137.

* Tue Mar 11 2008 Victor Forsyuk <force@altlinux.org> 1.2.1-alt2
- Added condstop to initscript.

* Wed Apr 18 2007 Victor Forsyuk <force@altlinux.org> 1.2.1-alt1
- 1.2.1
- Fix summary.
- Apply optflags.
- Patch that allows to not count nice time as idle time.
- Add service management to installation scripts.

* Sat Apr 17 2004 Grigory Milev <week@altlinux.ru> 1.1-alt1
- Initial build.
