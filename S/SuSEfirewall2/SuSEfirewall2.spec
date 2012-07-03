Name: SuSEfirewall2
Version: 3.6_SVNr195
Release: alt1
License: GPL
Group: Security/Networking
Packager: Evgenii Terechkov <evg@altlinux.ru>

Provides: personal-firewall SuSEfirewall
Obsoletes: personal-firewall SuSEfirewall

Summary: Stateful Packet Filter Using iptables and netfilter

Source: %name-%version.tar.bz2

BuildArch: noarch

BuildPreReq: perl-Net-DNS

%description
SuSEfirewall2 implements a packet filter to allow system administrators
to protect their computer and network by restricting the possibility of
other hosts connecting to them. This potentially saves you from
suffering under the design flaws and vulnerabilities that are found in
various daemons.

SuSEfirewall2 uses the iptables and netfilter packet filtering
infrastructure, which allows a flexible rule setup and the creation of
a stateful firewall, because it keeps track of connections and has the
notion of related connections.

For simply protecting a single host from attacks, you can set
SuSEfirewall2 in QUICK mode or use the personal-firewall configuration
file. Note that SuSEfirewall2 now includes the personal-firewall
functionality.

%prep
%setup

%build
%install
sed -i 's|/etc/init.d|%_initdir|' Makefile
make DESTDIR="%buildroot" install

install -m 644  %name.sysconfig %buildroot%_sysconfdir/sysconfig/%name
install -d -m 755 %buildroot%_datadir/%name/services

%post
# convert old broadcast variables from <= 9.2 if needed
file=%_sysconfdir/sysconfig/scripts/%name-oldbroadcast
if [ -e %_sysconfdir/sysconfig/%name -a -e $file ]; then
    (
	. %_sysconfdir/sysconfig/%name
	have_old_allow=
	have_old_ignore=
	if [ -n "$FW_ALLOW_FW_BROADCAST" -a "$FW_ALLOW_FW_BROADCAST" != "int" ]; then
	    have_old_allow=1
	fi
	if [ -n "$FW_IGNORE_FW_BROADCAST" -a "$FW_IGNORE_FW_BROADCAST" != "no" ]; then
	    have_old_ignore=1
	fi
	if [ -n "$have_old_allow" -o -n "$have_old_ignore" ]; then
	    alias warning=:
	    . $file
	    convert_old_broadcast
	fi
	sedpattern=
	if [ -n "$have_old_allow" ]; then
	    sedpattern="s/^FW_ALLOW_FW_BROADCAST_INT=.*/FW_ALLOW_FW_BROADCAST_INT=\"$FW_ALLOW_FW_BROADCAST_INT\"/"
	    sedpattern="$sedpattern;s/^FW_ALLOW_FW_BROADCAST_EXT=.*/FW_ALLOW_FW_BROADCAST_EXT=\"$FW_ALLOW_FW_BROADCAST_EXT\"/"
	    sedpattern="$sedpattern;s/^FW_ALLOW_FW_BROADCAST_DMZ=.*/FW_ALLOW_FW_BROADCAST_DMZ=\"$FW_ALLOW_FW_BROADCAST_DMZ\"/"
	fi
	if [ -n "$have_old_ignore" ]; then
	    sedpattern="$sedpattern;s/^FW_IGNORE_FW_BROADCAST_INT=.*/FW_IGNORE_FW_BROADCAST_INT=\"$FW_IGNORE_FW_BROADCAST_INT\"/"
	    sedpattern="$sedpattern;s/^FW_IGNORE_FW_BROADCAST_EXT=.*/FW_IGNORE_FW_BROADCAST_EXT=\"$FW_IGNORE_FW_BROADCAST_EXT\"/"
	    sedpattern="$sedpattern;s/^FW_IGNORE_FW_BROADCAST_DMZ=.*/FW_IGNORE_FW_BROADCAST_DMZ=\"$FW_IGNORE_FW_BROADCAST_DMZ\"/"
	fi
	if [ -n "$sedpattern" ]; then
	    sed -i "$sedpattern" %_sysconfdir/sysconfig/%name && echo "old broadcast variables converted"
	fi
	# %%{remove_and_set -n %name FW_IGNORE_FW_BROADCAST FW_ALLOW_FW_BROADCAST}
    )
fi

if [ -e %_sysconfdir/sysconfig/%name ] && grep -q '^FW_MASQ_DEV="\$FW_DEV_EXT"$' %_sysconfdir/sysconfig/%name; then
   sed -i 's/^FW_MASQ_DEV="\$FW_DEV_EXT"$/FW_MASQ_DEV="zone:ext"/' %_sysconfdir/sysconfig/%name && echo "FW_MASQ_DEV converted"
fi

%files
%config(noreplace) %_sysconfdir/sysconfig/%name
%config(noreplace) %_sysconfdir/sysconfig/%name.d/scripts/%name-custom
%_sysconfdir/sysconfig/%name.d
%_datadir/%name/services
%_sysconfdir/sysconfig/%name.d/scripts
/sbin/%name

%doc LICENCE EXAMPLES FAQ README
%doc *.html *.css
%doc %name.sysconfig

%changelog
* Sat Feb 28 2009 Terechkov Evgenii <evg@altlinux.ru> 3.6_SVNr195-alt1
- SVNr195
- New patches from SuSE
- Spec cleanup

* Sun Jan 27 2008 Terechkov Evgenii <evg@altlinux.ru> 3.6_SVNr183-alt1
- Spec cleanups
- Patch{1,2,3} updated to move scripts

* Mon Sep 10 2007 Terechkov Evgenii <evg@altlinux.ru> 3.6_SVNr183-alt0
- Patch2 added
- 3.6_SVNr183

* Sun Sep  9 2007 Terechkov Evgenii <evg@altlinux.ru> 3.6_SVNr175-alt1
- Patch0 splitted to Patch0,1

* Tue Jun 19 2007 Terechkov Evgenii <evg@altlinux.ru> 3.6_SVNr175-alt0
- Spec cleanups (Of cource!)
- Initial build for ALT (Thanks to OpenSuSE to spec)
