Name: bird
Version: 1.3.4
Release: alt1
Summary: BIRD Internet Routing Daemon

Group: Networking/Other
License: GPL
URL: http://bird.network.cz

# Cloned from git://git.nic.cz/bird.git
Source: %name-%version.tar
Source1: %name.init
Patch: %name-%version-%release.patch

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: libreadline-devel libncurses-devel flex glibc-kernheaders OpenSP linuxdoc-tools

%description
BIRD is an Internet Routing Daemon designed to support all the routing
technology used in the today's Internet or planned to be used in near
future and to have a clean extensible architecture allowing new routing
protocols to be incorporated easily. Among other features, BIRD supports:

 * both IPv4 and IPv6 protocols
 * multiple routing tables
 * the Border Gateway Protocol (BGPv4)
 * the Routing Information Protocol (RIPv2)
 * the Open Shortest Path First protocol (OSPFv2)
 * a virtual protocol for exchange of routes between different routing
   tables on a single host
 * a command-line interface allowing on-line control and inspection of
   status of the daemon
 * soft reconfiguration (no need to use complex online commands to
   change the configuration, just edit the configuration file and notify
   BIRD to re-read it and it will smoothly switch itself to the new
   configuration, not disturbing routing protocols unless they are
   affected by the configuration changes)
 * a powerful language for route filtering

BIRD has been developed at the Faculty of Math and Physics, Charles
University, Prague, Czech Republic as a student project. It can be
freely distributed under the terms of the GNU General Public License.

%package -n bird6
Group: Networking/Other
Summary: BIRD Internet Routing Daemon, ipv6 enabled
Requires: %name = %version-%release
%description -n bird6
%summary

%prep
%setup
%patch -p1

%build
autoconf
./configure --prefix=%_usr --sysconfdir=%_sysconfdir --localstatedir=%_var \
	--enable-ipv6 --with-protocols=all
%make_build
mv bird bird6
mv birdc birdc6
%make clean
./configure --prefix=%_usr --sysconfdir=%_sysconfdir --localstatedir=%_var \
	--with-protocols=all
%make_build
pushd doc
    make prog.sgml
    ./sgml2html prog.sgml
    ./sgml2html bird.sgml
popd

%install
%make_install install \
	prefix=%buildroot%_prefix \
	sysconfdir=%buildroot%_sysconfdir \
	sbindir=%buildroot%_sbindir \
	localstatedir=%buildroot%_var

install -d %buildroot%_sbindir
install bird6 %buildroot%_sbindir
install birdc6 %buildroot%_sbindir

install -d %buildroot%_initdir
install %SOURCE1 %buildroot%_initdir/%name

%post
%post_service bird

%preun
%preun_service bird

%files
%_initdir/%name
%config(noreplace) %_sysconfdir/%name.conf
%_sbindir/%name
%_sbindir/%{name}c
%doc NEWS README TODO doc/*.html

%files -n bird6
%_sbindir/%{name}6
%_sbindir/%{name}c6

%changelog
* Mon Nov 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3.4-alt1
- New version 1.3.4

* Thu Oct 06 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3.3-alt1
- New version 1.3.3
- Source cloned from upstream git
- Build html docs from sgml

* Sun Nov 28 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.5-alt2
- Implemented reload() in the init script (CLoses: #24532)

* Mon Oct 18 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.5-alt1
- New version 1.2.5

* Tue Aug 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.4-alt1
- New version 1.2.4

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.3-alt1
- New version 1.2.3
- Move socket to /var/run
- Patch from upstream to fix bug in topology.c

* Fri Apr 16 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.2-alt1
- New version 1.2.2
- Add patches from debian to fix ipv6 build in io.c

* Wed Mar 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.1-alt1
- New version 1.2.1

* Sun Jan 17 2010 Vladimir Lettiev <crux@altlinux.ru> 1.2.0-alt1
- New version 1.2.0

* Tue Dec 29 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.7-alt1
- new release

* Tue Nov 03 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.5-alt1
- new release

* Sat Oct 17 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.4-alt1
- new release

* Mon Sep 07 2009 Vladimir Lettiev <crux@altlinux.ru> 1.1.2-alt1
- new release (29bcd04)

* Sun May 31 2009 Vladimir Lettiev <crux@altlinux.ru> 1.0.15-alt1
- new release (4c2507d)

* Wed Apr 29 2009 Vladimir Lettiev <crux@altlinux.ru> 1.0.14-alt1
- initial build

