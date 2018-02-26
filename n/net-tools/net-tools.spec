Name: net-tools
Version: 1.60
Release: alt16

Summary: The basic tools for setting up networking
License: GPLv2+
Group: System/Configuration/Networking
Url: http://net-tools.berlios.de/

# http://download.berlios.de/net-tools/%name-%version.tar.bz2
# http://www.tazenda.demon.co.uk/phil/net-tools/%name-%version.tar.bz2
Source: net-tools-%version.tar
Source1: iptunnel.8
Source2: ipmaddr.8

Patch10: net-tools-1.60-rh-mii-ioctl.patch
Patch11: net-tools-1.60-rh-virtualname.patch
Patch12: net-tools-1.57-rh-bug22040.patch
Patch13: net-tools-1.60-rh-cycle.patch
Patch14: net-tools-1.60-rh-nameif.patch
Patch15: net-tools-1.60-rh-ipx.patch
Patch16: net-tools-1.60-rh-inet6-lookup.patch
Patch17: net-tools-1.60-rh-man.patch
Patch18: net-tools-1.60-rh-mii-gcc33.patch
Patch19: net-tools-1.60-rh-trailingblank.patch
Patch20: net-tools-1.60-rh-interface.patch
Patch21: net-tools-1.60-rh-siunits.patch
Patch22: net-tools-1.60-rh-gcc34.patch
Patch23: net-tools-1.60-rh-ulong.patch
Patch24: net-tools-1.60-rh-return.patch
Patch25: net-tools-1.60-rh-trunc.patch
Patch26: net-tools-1.60-rh-parse.patch
Patch27: net-tools-1.60-rh-netmask.patch
Patch28: net-tools-1.60-rh-bcast.patch
Patch29: net-tools-1.60-rh-mii-doc.patch
Patch30: net-tools-1.60-rh-num-ports.patch

Patch40: net-tools-1.57-alt-config.patch
Patch41: net-tools-1.59-alt-ipvs.patch
Patch42: net-tools-1.60-alt-nstrcmp.patch
Patch43: net-tools-1.60-alt-outformat.patch
Patch44: net-tools-1.60-alt-mii-tool-fflush.patch
Patch45: net-tools-1.60-alt-bound.patch
Patch46: net-tools-1.60-alt-without-hostname.patch
Patch47: net-tools-1.60-alt-ec_hw-NULL.patch

Patch50: net-tools-1.60-rh-netstat-duplicate-tcp.patch
Patch51: net-tools-1.60-rh-statalias.patch
Patch52: net-tools-1.60-rh-po.patch
Patch53: net-tools-1.60-rh-ifconfig-ib.patch
Patch54: net-tools-1.60-rh-netstat-ifaceopt.patch
Patch55: net-tools-1.60-rh-statistics.patch
Patch56: net-tools-1.60-rh-ifconfig.patch
Patch57: net-tools-1.60-rh-arp-bound.patch
Patch58: net-tools-1.60-rh-man-hostname.patch
Patch59: net-tools-1.60-rh-interface-bound.patch
Patch60: net-tools-1.60-rh-alt-netstat-inode.patch
Patch61: net-tools-1.60-rh-arp-fgets.patch
Patch62: net-tools-1.60-rh-man-ifconfig.patch
Patch63: net-tools-1.60-rh-x25-proc.patch
Patch64: net-tools-1.60-rh-man-arp.patch
Patch65: net-tools-1.60-rh-x25_address.patch
Patch66: net-tools-1.60-rh-netstat-skip.patch
Patch67: net-tools-1.60-rh-netstat-I.patch
Patch68: net-tools-1.60-rh-nameif-bound.patch
Patch69: net-tools-1.60-rh-arp-unaligned-access.patch
Patch70: net-tools-1.60-rh-alt-remove-node.patch
Patch71: net-tools-1.60-rh-alt-netstat-interface.patch
Patch72: net-tools-1.60-rh-statistics-bound.patch
Patch73: net-tools-1.60-rh-arp-a.patch
Patch74: net-tools-1.60-rh-ifconfig-clear-flag.patch
Patch75: net-tools-1.60-rh-man-metric-tunnel.patch
Patch76: net-tools-1.60-rh-netstat-probe.patch
Patch77: net-tools-1.60-rh-scanf-format.patch
Patch78: net-tools-1.60-rh-continuous-flush-stdout.patch
Patch79: net-tools-1.60-rh-ib-warning.patch
Patch80: net-tools-1.60-rh-alt-man-obsolete.patch
Patch81: net-tools-1.60-berlios-makefile.patch
Patch82: net-tools-1.60-rh-slattach-fchown.patch
Patch83: net-tools-1.60-rh-mii-refactor.patch
Patch84: net-tools-1.60-deb-large-indexes.patch

# due to hostname
Requires: coreutils >= 0:5.3.1-alt0.2

# due to resolve
Requires: hostinfo >= 0:2.2-alt2

# due to mii-tool and ether-wake
Requires: ethtool >= 1:2.6.33, etherwake

%description
This package contains the traditional tools needed for setting up
networking: ethers, route and others.
Most of them are obsolete.  For replacement check iproute2 package.

%prep
%setup -q
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1

%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1

%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1

find -type f -name \*.orig -delete

install -pm644 %_sourcedir/{ipmaddr,iptunnel}.8 man/en_US/

# Fix slattach lock dir (ALT#10179).
find -type f -print0 |xargs -r0 sed -i 's|/var/lock|&/serial|g' --

%build
export CFLAGS='%optflags'
yes '' |make config version.h
make

%install
mkdir -p %buildroot{/bin,/sbin,%_mandir/man{1,5,8}}
export CFLAGS='%optflags'
%make_install install BASEDIR=%buildroot

# User friendly symlinks.
for f in arp ifconfig route; do
	ln -s ../sbin/$f %buildroot/bin/
done

# rarp is obsolete.
find %buildroot -name 'rarp*' -delete

# /bin/hostname utility was relocated to coreutils.
find %buildroot \( -name hostname\* -or -name \*domainname\* \) -delete

# Obsolete manpages.
rm -r %buildroot%_mandir/*_*

#%find_lang --with-man '[a-z-]\+' --output %name.lang
%find_lang %name

%files -f %name.lang
/bin/*
/sbin/*
%_mandir/man?/*
%doc README* TODO

%changelog
* Wed Feb 03 2010 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt16
- Updated to FC 1.60-101.
- Moved obsolete mii-tool back to this obsolete package.
- Added user symlinks for arp, ifconfig and route.

* Sun Nov 30 2008 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt15
- slattach: Fixed lock directory (closes: #10179).

* Fri Nov 28 2008 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt14
- Updated to FC 1.60-91.
- Removed obsolete rarp.

* Sun Jan 07 2007 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt13
- Updated to FC 1.60-76.

* Tue May 17 2005 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt12
- Relocated mii-tool manpage as well.

* Mon May 16 2005 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt11
- Relocated mii-tool and ether-wake utilities to ethtool package (#6360).

* Tue Apr 19 2005 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt10
- Relocated resolve(1) utility to hostinfo package (#6360).

* Tue Apr 12 2005 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt9
- Relocated hostname(1) utility to coreutils package (#6360).

* Mon Jan 17 2005 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt8
- Applied more RH patches:
  siunits, gcc34, ulong, return, trunc,
  parse, netmask, bcast, mii-doc, num-ports.

* Fri Mar 12 2004 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt7
- Applied more RH patches:
  nameif, ipx, inet6-lookup, man,
  gcc33, trailingblank, interface.
- Updated patches:
  rh-virtualname, rh-cycle, alt-outformat.
- ether-wake: updated to v1.09 11/12/2003.

* Wed May 21 2003 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt6
- mii-tool: added fflush(3) call to the show_basic_mii() function,
  thanks to Yaroslav Rastrigin for the hint.

* Sun May 04 2003 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt5
- resolve: added IPv6 support and manpage.
- netstat: fixed "-nic" operation (rh).

* Mon Nov 18 2002 Stanislav Ievlev <inger@altlinux.ru> 1.60-alt4
- two patches from RH:
    * virtualname
    * bug22040
- fix output format length (outformat patch, bug  #0001105)

* Mon Jul 15 2002 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt3
- Fixed recent fix for nstrcmp (#0001056).

* Tue Jul 02 2002 Dmitry V. Levin <ldv@altlinux.org> 1.60-alt2
- Added resolve utility (from MySQL but fixed).
- Added wake-on-lan wakeup utility, ether-wake (by Donald Becker).
- Fixed nstrcmp() - replaced by slightly modified version of
  rpmvercmp() from rpmlib.
- Don't use SIOCDEVPRIVATE for MII ioctls (rh).

* Thu Apr 19 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.60-alt1
- 1.60

* Sat Feb 24 2001 Dmitry V. Levin <ldv@fandra.org> 1.59-ipl2mdk
- Added ipvs patch.

* Sun Feb 18 2001 Dmitry V. Levin <ldv@fandra.org> 1.59-ipl1mdk
- 1.59

* Wed Nov 08 2000 Dmitry V. Levin <ldv@fandra.org> 1.57-ipl2mdk
- Enable all protocol options.
- Build and install mii-tool.
- Add more manpages and documentation.

* Tue Jun 13 2000 Dmitry V. Levin <ldv@fandra.org> 1.57-ipl1mdk
- 1.57
- RE and Fandra adaptions.

* Tue Apr  4 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.55-1mdk
- 1.55

* Fri Mar 31 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.54-1mdk
- Spec-helper clean-up.
- Merge with rh-patchs.
- use find_lang macros for locales.
- Adjust groups.

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- %%lang in man/-locale.
- big spec cleanup.

* Sun Aug 29 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 1.53:	- fixes several buffer overruns
	- adds german man pages
	- adds french ethers.5 translation
	- adds estonian
- fix up .spec

* Mon Jul 12 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Build release (8mdk).

* Sat Jul 10 1999 Pablo Saratxaga <pablo@mandrakesoft.com>
- moved french manpages from fr_FR to fr
- compressed all man pages
- added french, spanish and wallon descriptions

* Fri Jun 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Fix potentional bufer overruns.
- patch to recognize ESP and GRE protocols for VPN masquerade
  <jhardin@wolfenet.com>.

* Wed Apr 28 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Update to 1.52

* Tue Apr 13 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add patch from RedHat6.0.
- Update to 1.51.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- add de locale
- handle RPM_OPT_FLAGS

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 1.50.
- added slattach/plipconfig/ipmaddr/iptunnel commands.
- enabled translated man pages.

* Tue Dec 15 1998 Jakub Jelinek <jj@ultra.linux.cz>
- update to 1.49.

* Sat Dec  5 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.48.

* Thu Nov 12 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.47.

* Wed Sep  2 1998 Jeff Johnson <jbj@redhat.com>
- update to 1.46

* Thu Jul  9 1998 Jeff Johnson <jbj@redhat.com>
- build root
- include ethers.5

* Thu Jun 11 1998 Aron Griffis <agriffis@coat.com>
- upgraded to 1.45
- patched hostname.c to initialize buffer
- patched ax25.c to use kernel headers

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Feb 27 1998 Jason Spangler <jasons@usemail.com>
- added config patch

* Fri Feb 27 1998 Jason Spangler <jasons@usemail.com>
- changed to net-tools 1.432
- removed old glibc 2.1 patch

* Wed Oct 22 1997 Erik Troan <ewt@redhat.com>
- added extra patches for glibc 2.1

* Tue Oct 21 1997 Erik Troan <ewt@redhat.com>
- included complete set of network protocols (some were removed for
  initial glibc work)

* Wed Sep 03 1997 Erik Troan <ewt@redhat.com>
- updated glibc patch for glibc 2.0.5

* Thu Jun 19 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- updated to 1.33
