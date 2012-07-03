Name: iputils
%define timestamp 20101006
Version: %timestamp
Release: alt2

Summary: Utilities for IPv4/IPv6 networking
License: BSD-style
Group: Networking/Other
Url: http://www.skbuff.net/iputils
Packager: Afanasov Dmitry <ender@altlinux.org>

Source0: %url/%name-s%version.tar.bz2
Source1: bonding-0.2.tar.bz2
Source2: bonding-ifenslave.c
Source3: ping.control
Source4: ping6.control

Patch1: iputils-ss020927-owl-warnings.patch
Patch3: iputils-20001007-rh-bug23844.patch
Patch4: iputils-s20071127-alt-datalen-fix.patch
Patch5: iputils-s20101006-alt-droppriv.patch
Patch6: iputils-s20071127-owl-man.patch
# Parallel build of documentation:
Patch8: iputils-pmake.patch
# Disallow lazy binding for setuid binaries:
Patch9: iputils-bindnow.patch

Patch21: iputils-20020124-fc-countermeasures.patch
Patch22: iputils-20020927-fc-addrcache.patch
Patch23: iputils-20020927-fc-ia64_align.patch
Patch24: iputils-20020927-fc-unaligned.patch
Patch25: iputils-20020927-fc-ping-subint.patch

Patch30: iputils-fc-ping_cleanup.patch
# Cosmetic fix, remove \n in perror message:
Patch31: iputils-perror-newline.patch

Conflicts: netkit-base

PreReq: shadow-utils, control
Requires: ipv6calc, /var/resolv

# Automatically added by buildreq on Mon Sep 15 2008
BuildRequires: OpenSP docbook-style-dsssl libcap-devel perl-SGMLSpm
BuildRequires: libsysfs-devel libssl-devel

%description
The iputils package contains basic utilities for monitoring a network:
+ clockdiff - measures clock difference;
+ ping/ping6 - sends ICMP ECHO_REQUEST packets to network hosts;
+ arping - ping by ARP packets;
+ rdisc - classic router discovery daemon;
+ tracepath/tracepath6 - traces path to destination discovering MTU
along this path.

%prep
%setup -q -n %name-s%version -a1

rm -f bonding-0.2/ifenslave
mv -f bonding-0.2/README bonding-0.2/README.ifenslave
cp -a %_sourcedir/bonding-ifenslave.c bonding-0.2/ifenslave.c

%patch1 -p1
%patch22 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch8 -p1
%patch9 -p1

%patch21 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1

%patch30 -p1
%patch31 -p1

find -type f -name \*.orig -delete -print

%build
%make_build \
	CCOPT="%optflags -D_GNU_SOURCE -Wstrict-prototypes" \
	LDLIBS=
%make_build CFLAGS="%optflags" ifenslave -C bonding-0.2
%make_build man -C doc

%install
mkdir -p %buildroot{/{,s}bin,%_sbindir,%_man8dir}
install -p arping clockdiff %buildroot%_sbindir/
install -p -m700 ping %buildroot/bin/
install -p bonding-0.2/ifenslave %buildroot/sbin/
for n in ping6 tracepath tracepath6; do
	install -p -m755 "$n" %buildroot/bin/
done
install -p rdisc %buildroot%_sbindir/in.rdisc
ln -s in.rdisc %buildroot%_sbindir/rdisc
pushd doc
	install -pm644 arping.8 clockdiff.8 pg3.8 rdisc.8 \
		%buildroot%_man8dir/
	install -pD -m644 ping.1 %buildroot%_man1dir/ping.1
	install -pD -m644 tracepath.1 %buildroot%_man1dir/tracepath.1
	ln -s ping.1 %buildroot%_man1dir/ping6.1
	ln -s tracepath.1 %buildroot%_man1dir/tracepath6.1
popd
install -pD -m755 %_sourcedir/ping.control \
	%buildroot/etc/control.d/facilities/ping
install -pD -m755 %_sourcedir/ping6.control \
	%buildroot/etc/control.d/facilities/ping6

%pre
/usr/sbin/groupadd -r -f iputils
/usr/sbin/useradd -r -g iputils -d /dev/null -s /dev/null -n iputils >/dev/null 2>&1 ||:
/usr/sbin/groupadd -r -f netadmin

if [ $1 -ge 2 ]; then
	/usr/sbin/control-dump ping ping6
fi

%post
if [ $1 -ge 2 ]; then
	/usr/sbin/control-restore ping ping6
else
	/usr/sbin/control ping public
	/usr/sbin/control ping6 public
fi

%files
%config /etc/control.d/facilities/ping
%config /etc/control.d/facilities/ping6
%attr(700,root,root) %verify(not mode group) /bin/ping
%attr(700,root,root) %verify(not mode group) /bin/ping6
/bin/tracepath*
/sbin/ifenslave
%_sbindir/*
%_mandir/man?/*
%doc RELNOTES bonding*/README.*

%changelog
* Mon May 09 2011 Afanasov Dmitry <ender@altlinux.org> 20101006-alt2
- fix #25282 (thx to led@)
  + updated droppriv patch for support sysfs

* Sun Jan 23 2011 Afanasov Dmitry <ender@altlinux.org> 20101006-alt1
- version 20101006.

* Tue Sep 30 2008 Afanasov Dmitry <ender@altlinux.org> 20071127-alt4
- fix typo in control facilities descriptions

* Tue Sep 30 2008 Afanasov Dmitry <ender@altlinux.org> 20071127-alt3
- add descriptions for control facilities (fix #17321)

* Thu Sep 18 2008 Afanasov Dmitry <ender@altlinux.org> 20071127-alt2
- add bindnow patch for linking (thx to force@)
- more correct summary.
- fixed documentation build to be SMP-compatible.

* Mon Sep 15 2008 Afanasov Dmitry <ender@altlinux.org> 20071127-alt1
- version s20071127
- remove old patches
    + rh-owl-cache-reverse-lookups - replaced by fc-addrcache
    + owl-man - now man is distributed by sgml. remake patch against sgml 
      files
- add some fedora core patches
    + fc-countermeasures (print countermeasures warning in verbose only)
    + fc-addrcache
    + fc-ia64_align (call strdup on device name)
    + fc-unaligned (add warning to ping.c)
    + fc-open-max (read OPEN_MAX value from sysctl)
    + fc-ping_cleanup (more descriptive string about icmp replies)

* Wed Oct 03 2007 Dmitry V. Levin <ldv@altlinux.org> 20020927-alt5
- Do not check kernel headers.

* Tue May 22 2007 Michael Shigorin <mike@altlinux.org> 20020927-alt4.2
- moved rarpd to a package of its own;
  see http://secunia.com/advisories/25061/

* Sun Oct 15 2006 Michael Shigorin <mike@altlinux.org> 20020927-alt4.1
- use proper ifenslave.c (closes: #9695)
- disabled patch7 (doesn't apply; seems like ifenslave.c has
  changed enough so additional code review is needed to determine
  whether it's still needed or how to port it -- still unpatched
  new source is reportedly working, see the referenced bugreport)
- fixed patch5 (#7283, thanks kas@ for alert/patch^2)
- added ping6 control proposed by icesik@ (#9783)
- added Packager:

* Thu Nov 24 2005 Dmitry V. Levin <ldv@altlinux.org> 20020927-alt4
- Relocated manual pages for commands to 1st section.

* Mon Nov 14 2005 Dmitry V. Levin <ldv@altlinux.org> 20020927-alt3
- Removed traceroute6 in favour of the traceroute package.
- Removed backwards compatibillity symlinks from %_sbindir/.
- Removed verifying permissions and group owner for ping since it's
controlled by control(8) facility.

* Wed Aug 27 2003 Dmitry V. Levin <ldv@altlinux.org> 20020927-alt2
- Updated build dependencies, fixed build.
- Relocated ping6, tracepath, tracepath6 and traceroute6 binaries
  from /usr/sbin to /bin; added backwards compatibility symlinks.
- Keep ping at mode 700 ("restricted") in the package, but default
  it to "public" in %%post when the package is first installed.
  This avoids a race and fail-open behavior where a "restricted"
  ping could be "public" during package upgrades (Owl).

* Wed Oct 16 2002 Dmitry V. Levin <ldv@altlinux.org> 20020927-alt1
- Updated to ss020927 (fixes #0000711).
- Dropped ss001110-owl-warnings patch (no longer needed).
- Fixed datalen typo.
- Added group (netadmin) to restrict access to ping.
- Added control support for ping.

* Thu Apr 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020124-alt8
- arping: do drop_priv a bit later to keep functionality.
- clockdif: keep cap_net_raw capability.

* Tue Apr 09 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020124-alt7
- Updated droppriv patch (chroot to /var/resolv).

* Fri Apr 05 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020124-alt6
- Refined droppriv patch:
  + added file descriptors fix;
  + drop root also for tracepath and tracepath6.

* Thu Apr 04 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020124-alt5
- Moved ipv6calc to outstanding package.
- arping, clockdiff, ping, ping6, traceroute6: drop root also for root user.

* Tue Apr 02 2002 Dmitry V. Levin <ldv@alt-linux.org> 20020124-alt4
- Disabled build of ipv6calc-static.
- Fixed build without kernel-source installed.

* Wed Mar 27 2002 Alexander Bokovoy <ab@altlinux.ru> 20020124-alt3
- Fixed:
    + tftpd removed from installation binaries 

* Mon Mar 25 2002 Alexander Bokovoy <ab@altlinux.ru> 20020124-alt2
- IPUtils ss020124
- IP6Calc 0.39
- Documentation now is built using SGML tools
- Various patches updated

* Thu Jan 03 2002 Stanislav Ievlev <inger@altlinux.ru> 20010805-alt2
- fixed rights on manual pages (bug  #0000292)
- fixed bonding with new interface ( 2.4.x )

* Tue Aug 14 2001 Alexander Bokovoy <ab@altlinux.ru>   20010805-alt1
- IPUtils ss010805
- Fixed: 
    + ping-deadline patch. Ping has been re-designed to eliminate this problem
    + Compiler options
    + Owl patch for ping

* Tue May 08 2001 Stanislav Ievlev <inger@altlinux.ru> 20001110-ipl2mdk
- Merge with patches from OpenWall, RH and MDK

* Fri Jan 12 2001 Dmitry V. Levin <ldv@fandra.org> 20001110-ipl1mdk
- ss001110.

* Thu Oct 19 2000 Dmitry V. Levin <ldv@fandra.org> 20001011-ipl1mdk
- ss001011.
- RE adaptions.

* Tue Oct 10 2000 Jeff Johnson <jbj@redhat.com>
- update to ss001010.
- don't segfault as root with large buffers (#16677).

* Sun Oct  8 2000 Jeff Johnson <jbj@redhat.com>
- update to ss001007.

* Tue Aug  8 2000 Tim Waugh <twaugh@redhat.com>
- fix spelling mistake (#15714).

* Tue Aug  8 2000 Tim Waugh <twaugh@redhat.com>
- turn on -U on machines without TSC (#15223).

* Tue Aug  1 2000 Jeff Johnson <jbj@redhat.com>
- better doco patch (#15050).

* Tue Jul 25 2000 Jakub Jelinek <jakub@redhat.com>
- fix include-glibc/ to work with new glibc 2.2 resolver headers

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Sun Jun 18 2000 Jeff Johnson <jbj@redhat.com>
- FHS packaging.
- update to ss000418.
- perform reverse DNS lookup only once for same input.

* Sun Mar  5 2000 Jeff Johnson <jbj@redhat.com>
- include README.ifenslave doco.
- "ping -i N" was broke for N >= 3 (#9929).
- update to ss000121:
-- clockdiff: preserve raw socket errno.
-- ping: change error exit code to 1 (used to be 92,93, ...)
-- ping,ping6: if -w specified, transmit until -c limit is reached.
-- ping,ping6: exit code non-zero if some packets not received within deadline.

* Tue Feb 22 2000 Jeff Johnson <jbj@redhat.com>
- man page corrections (#9690).

* Wed Feb  9 2000 Jeff Johnson <jbj@jbj.org>
- add ifenslave.

* Thu Feb  3 2000 Elliot Lee <sopwith@redhat.com>
- List /usr/sbin/rdisc in %files list.

* Thu Jan 27 2000 Jeff Johnson <jbj@redhat.com>
- add remaining binaries.
- casts to remove compilation warnings.
- terminate if -w deadline is reached exactly (#8724).

* Fri Dec 24 1999 Jeff Johnson <jbj@redhat.com>
- create (only ping for now, traceroute et al soon).
