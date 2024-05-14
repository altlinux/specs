# define suffix for easy backporing bird-2.x to stable branches as bird2 package
# for build as bird - use gear.specsubst.suffix %nil
# for build as bird2 - use gear.specsubst.suffix 2
# gear-create-tag -s suffix=%nil or gear-create-tag -s suffix=2
%define _suffix %nil
%define _localstatedir %_var
%define protocols all

Name: bird%_suffix
Version: 2.15.1
Release: alt2
Summary: BIRD Internet Routing Daemon

Group: Networking/Other
License: GPLv2
URL: http://bird.network.cz

VCS: https://gitlab.nic.cz/labs/bird
Source: %name-%version.tar
Source1: bird.init
Source2: bird.service

%if 0%_suffix != 0
Conflicts: bird
%else
Obsoletes: bird2 < %EVR
Provides: bird2 = %EVR
%endif

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

%prep
%setup

%build
%autoreconf
%configure  --with-runtimedir=/run/bird \
	    --sysconfdir=%_sysconfdir/bird \
	    --with-protocols=%protocols \
	    #
%make_build all


%install
%makeinstall_std
install -d %buildroot%_localstatedir/lib/bird %buildroot%_tmpfilesdir  %buildroot%_sysconfdir/bird/bird.d
install -pD -m755 %SOURCE1 %buildroot%_initdir/bird
install -pD -m644 %SOURCE2 %buildroot%_unitdir/bird.service

# create temporary directory
mkdir -p %buildroot%_tmpfilesdir
cat > %buildroot%_tmpfilesdir/bird.conf << _EOF_
d /run/bird 0750 _bird _bird -
_EOF_

# add bird.d configuration directory
cat >> %buildroot%_sysconfdir/bird/bird.conf << _EOF_
include "/etc/bird/bird.d/*.conf";
_EOF_

%check
make test

%pre
%_sbindir/groupadd -r -f _bird 2> /dev/null ||:
%_sbindir/useradd -r -n -g _bird -d /var/lib/bird -s /dev/null -c "BIRD Routing Daemon System User" _bird 2> /dev/null ||:

%post
%post_service bird

%preun
%preun_service bird

%files
%doc NEWS README doc/bird.conf.example*
%_initdir/bird
%_unitdir/bird.service
%dir %_sysconfdir/bird
%dir %_sysconfdir/bird/bird.d
%config(noreplace) %_sysconfdir/bird/bird.conf
%_tmpfilesdir/bird.conf
%dir %attr(0750,_bird,_bird) %_localstatedir/lib/bird
%_sbindir/bird
%_sbindir/birdc
%_sbindir/birdcl

%changelog
* Tue May 14 2024 Sergey Y. Afonin <asy@altlinux.org> 2.15.1-alt2
- removed expect-group option from init.d/bird (ALT #50356)

* Thu May 02 2024 Anton Farygin <rider@altlinux.ru> 2.15.1-alt1
- 2.15.1

* Thu Jul 06 2023 Sergey Y. Afonin <asy@altlinux.org> 2.13.1-alt2
- init.d/bird:
  + fixed typo in stop()
  + added test of configuration before restart and reload

* Sun Jun 25 2023 Anton Farygin <rider@altlinux.ru> 2.13.1-alt1
- 2.13 -> 2.13.1

* Sat Jun 17 2023 Anton Farygin <rider@altlinux.ru> 2.13-alt2
- 2.0.7-> 2.13
- set package name "bird" for sisyphus and bird2 for branches with bird-1.6.8
  and add correct "obsoletes/provides/conflicts" between bird and bird2 packages
- moved bird.conf to /etc/bird/bird.conf
- added /etc/bird/bird.d configuration directory
- run under unprivileged _bird user and group
- enabled tests

* Sat Feb 27 2021 Anton Farygin <rider@altlinux.org> 2.0.7-alt1
- 2.0.7

* Thu Jun 11 2020 Anton Farygin <rider@altlinux.ru> 1.6.8-alt1
- 1.6.8

* Thu Sep 12 2019 Anton Farygin <rider@altlinux.ru> 1.6.7-alt1
- 1.6.7 (Fixes: CVE-2019-16159)

* Tue May 21 2019 Anton Farygin <rider@altlinux.ru> 1.6.4-alt5
- added upstream patch against errors with clang build

* Wed Jan 16 2019 Anton Farygin <rider@altlinux.ru> 1.6.4-alt2
- cleared from %%ubt macros

* Thu Mar 22 2018 Anton Farygin <rider@altlinux.ru> 1.6.4-alt1
- new version

* Wed Jan 11 2017 Anton Farygin <rider@altlinux.ru> 1.6.3-alt1
- new version

* Thu Dec 08 2016 Anton Farygin <rider@altlinux.ru> 1.6.2-alt1
- 1.6.2
- added % macros for easy backporting to stable branches

* Sun Oct 25 2015 Vladimir Lettiev <crux@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Tue Sep 09 2014 Alexey Shabalin <shaba@altlinux.ru> 1.4.4-alt1
- 1.4.4
- add separate bird6 service
- add systemd unit files

* Thu Aug 28 2014 Andriy Stepanov <stanv@altlinux.ru> 1.4.3-alt2
- add status entry for init script

* Tue Apr 22 2014 Vladimir Lettiev <crux@altlinux.ru> 1.4.3-alt1
- New version 1.4.3

* Mon Nov 25 2013 Vladimir Lettiev <crux@altlinux.ru> 1.4.0-alt1
- New version 1.4.0
- Packed light client birdcl{,6}

* Sun Jan 13 2013 Vladimir Lettiev <crux@altlinux.ru> 1.3.9-alt1
- New version 1.3.9

* Thu Oct 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.3.8-alt1
- New version 1.3.8

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

