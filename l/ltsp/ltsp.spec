%def_with jetpipe
%def_with ldminfod

%define rev 847

%define Codename ALTLinux

%define Name ALTSP
Name: ltsp
Version: 5.1.21
Release: alt0.12.4
Summary: %Name is ALT Linux blend of LTSP5 and LTSP4.2
License: %gpl2only
Group: Networking/Remote access
URL: http://www.altlinux.org/LTSP
%ifdef rev
# bzr branch http://bazaar.launchpad.net/~ltsp-upstream/ltsp/ltsp-trunk ltsp
# bzr update ltsp
Source0: %name-r%rev.tar
%else
Source0: %name-%version.tar
%endif
Source13: %name-rdp.sh
Source14: %name-rdpx.sh
Source15: lts-parameters.alt
Source21: ltsconf.tcl
Source22: conffile.tcl
#Patch0: %name-5.1.21-alt.patch
#Patch1: ltsp-5.1.21-alt-initscripts.patch
#Patch2: ltsp-5.1.21-alt-kserial.patch
#Patch3: ltsp-5.1.21-alt-typo.patch
#Patch4: ltsp-5.1.21-alt-compcache.patch
#Patch5: ltsp-5.1.21-alt-HOSTNAME.patch
#Patch6: ltsp-5.1.21-alt-fastboot.patch
#Patch7: ltsp-5.1.21-alt-tmpfs-options.patch
#Patch8: ltsp-5.1.21-alt-lbc.patch
#ExclusiveArch: %ix86 %arm
#ExclusiveOS: linux
Provides: %{name}5 = %version-%release
Obsoletes: %{name}5

# Automatically added by buildreq on Fri Mar 14 2008
BuildRequires: flex libX11-devel libpopt-devel

BuildRequires: gettext-tools
BuildRequires: rpm-build-licenses

%description
%url

%package server
Summary: %Name server
Group: Networking/Remote access
BuildArch: noarch
AutoReq: yes, noshell
Conflicts: %name-client %{name}5-client
Requires: /usr/bin/rpmvercmp
Requires: gettext
Requires: xmessage
Requires: setarch
Provides: %{name}5-server = %version-%release
Obsoletes: %{name}5-server

%description server
%Name server (to be installer onto the host system)


%package client
Summary: %Name client
Group: Networking/Remote access
Requires: service
Requires: mkinitrd-initramfs >= 3.0.4
Requires: e2fsprogs
Requires: mkinitrd
Provides: %_sysconfdir/%{name}_chroot
AutoReq: yes, noshell
Conflicts: %name-server %{name}5-server
Conflicts: alterator-backend-x11 < 0.13.1
Provides: %{name}5-client = %version-%release
Obsoletes: %{name}5-client


%description client
%Name client (to be installed into LTSP chroot)


%if_with jetpipe
%package -n jetpipe
Summary: Minimal print-server
Group: System/Servers
BuildArch: noarch

%description -n jetpipe
jetpipe will bind a printer device to a given portnumber so the printer
can be accessed through the JetDirect protocol from a remote client.
%endif


%if_with ldminfod
%package -n ldminfod
Summary: Service for output login sessions and available locales
Group: System/Servers
BuildArch: noarch

%description -n ldminfod
ldminfod is a service for output login sessions and available locales.
ldminfod will output the login sessions and locales available. It is
usually run from an inetd or xinetd instance. it is used by ldm to
remotely determine available login and locale settings.
%endif


%prep
%ifdef rev
%setup -n %name-r%rev
%else
%setup -n %name-%version
%endif
#patch0 -p1
#patch1 -p1
#patch2 -p1
#patch3 -p1
#patch4 -p1
#patch5 -p1
#patch6 -p1
#patch7 -p1
#patch8 -p1
iconv -f cp1251 -t utf-8 %SOURCE15 > client/lts-parameters.alt
%define make_alsa_conf [ -f %_datadir/alsa/alsa.conf ] && \
for n in null pulse xaudio; do \
    [ -f %_sysconfdir/%name/asound-$n.conf ] && \
    sed -e 's|"/etc/asound\.conf"|"%_sysconfdir/%name/asound-'$n'.conf"|g' \\\
	-e '/asoundrc/d' %_datadir/alsa/alsa.conf > %_datadir/%name/alsa-$n.conf ||: \
done ||:

%build
%{!?autoreconf:%define autoreconf autoreconf -fisv}
%define _optlevel s
%make_build -C client/getltscfg CFLAGS="%optflags"
%make_build -C po
pushd client/xrexecd
%autoreconf
%configure
%make_build
popd
for l in ru uk; do
    msgfmt -c -o server/configs/ALTLinux/po/ltsp-login.$l.{gm,p}o
done

sed -e 's|@LIBDIR@|%_libdir|g' \
    server/configs/%Codename/ltsp-profile.sh.in \
    > server/configs/%Codename/ltsp-profile.sh
sed -e 's/@ARCH@/%_target_cpu/g' server/configs/%Codename/dhcpd.conf.in \
    > server/configs/%Codename/dhcpd.conf
sed -e 's/@ARCH@/%_target_cpu/g' \
    server/configs/%Codename/%name-build-client.conf.in \
    > server/configs/%Codename/%name-build-client.conf
sed -e 's|@XORGEXTDIR@|%_libdir/X11/modules/extensions|g' client/initscripts/%Codename/ltsp-client.init.in > \
    client/initscripts/%Codename/ltsp-client.init


%install
# common
install -d -m 0755 %buildroot{%_sbindir,%_sysconfdir/{%name,sysconfig},%_x11sysconfdir,%_datadir/%name,%_man8dir}
install -m 0644 {client/initscripts/%Codename/%name-vendor,%name-common}-functions %buildroot%_datadir/%name/

# Server
install -d -m 0755 %buildroot{%_sysconfdir/{net,profile.d,xinetd.d},%_x11sysconfdir/profile.d,%_datadir/%name/{plugins/%name-build-client/{%Codename,common},scripts},%_localstatedir/{%name-client-setup,tftpboot/%name}}
for n in pulse null; do
    install -m 0644 /dev/null %buildroot%_datadir/%name/alsa-$n.conf
done
install -m 0755 server/configs/%Codename/%name-profile.sh %buildroot%_x11sysconfdir/profile.d/%name.sh
install -m 0644 server/configs/%Codename/dhcpd.conf %buildroot%_sysconfdir/%name/
install -m 0644 server/configs/%Codename/nbd-server.config %buildroot%_sysconfdir/%name/
install -m 0755 server/scripts/%Codename/mkswapfile %buildroot%_datadir/%name/scripts/
install -m 0755 server/%name-keys %buildroot%_sysconfdir/net/
install -m 0755 server/scripts/%Codename/%name-mkbootiso %buildroot%_sbindir/
install -m 0755 server/{%name-{keys,update-*},nbd*} %buildroot%_sbindir/
install -m 0644 server/xinetd.d/* %buildroot%_sysconfdir/xinetd.d/
install -m 0644 server/doc/{%name-,nbd}*.8 %buildroot%_man8dir/
install -m 0644 server/configs/%Codename/%name-update-kernels.conf %buildroot%_sysconfdir/%name/
install -m 0755 server/configs/%Codename/%name-login.sh %buildroot%_x11sysconfdir/profile.d/
echo "VENDORDEF=%Codename" > %buildroot%_sysconfdir/sysconfig/%{name}dist
for l in ru uk; do
    install -D -m 0644 server/configs/%Codename/po/%name-login.$l.gmo \
	%buildroot%_datadir/locale/$l/LC_MESSAGES/%name-login.mo
done
install -m 0644 server/configs/%Codename/asound-*.conf %buildroot%_sysconfdir/%name/
%make_install -C po DESTDIR=%buildroot install
install -m 0755 server/%name-build-client %buildroot%_sbindir/
install -m 0644 server/plugins/functions %buildroot%_datadir/%name/plugins/
install -m 0644 server/plugins/%name-build-client/common/* %buildroot%_datadir/%name/plugins/%name-build-client/common/
install -m 0644 server/plugins/%name-build-client/%Codename/* %buildroot%_datadir/%name/plugins/%name-build-client/%Codename/
install -m 0644 server/configs/%Codename/%name-build-client.conf %buildroot%_sysconfdir/%name/

%find_lang %name
%find_lang --append --output=%name.lang %name-login

# Client
%make_install -C client/xrexecd DESTDIR=%buildroot install
install -d -m 0755 %buildroot{%_bindir,%_initdir,%_datadir/%name/screen.d,%_man1dir,%_sysconfdir/{default,rc.d/scripts},%_var/cache/%{name}conf}
install -m 0755 client/{screen_session,update-kernels} %buildroot%_datadir/%name/
install -m 0644 client/screen-x-common %buildroot%_datadir/%name/
install -m 0755 client/initscripts/%Codename/start_* %buildroot%_datadir/%name/
install -m 0755 client/screen.d/{shell,xdmcp,telnet} %buildroot%_datadir/%name/screen.d/
ln -sf xdmcp %buildroot%_datadir/%name/screen.d/startx
install -m 0755 %SOURCE13 %buildroot%_datadir/%name/screen.d/rdp
install -m 0755 %SOURCE14 %buildroot%_datadir/%name/screen.d/rdpx
install -m 0644 client/%{name}_config %buildroot%_datadir/%name/
install -m 0644 client/initscripts/%Codename/%name-client-eth-modules.list %buildroot%_sysconfdir/%name/
install -m 0644 client/initscripts/%Codename/sysconfig-installkernel %buildroot%_sysconfdir/sysconfig/installkernel1
install -m 0755 client/getltscfg/getltscfg %buildroot%_bindir/
install -m 0644 client/getltscfg/getltscfg.1 %buildroot%_man1dir/
#install -m 0755 client/initramfs/init-bottom/unionfs_cow %buildroot%_datadir/%name/
install -m 0644 client/initscripts/%Codename/%name-client-setup.default %buildroot%_sysconfdir/default/%name-client-setup
install -m 0755 client/initscripts/%Codename/%name-client-bind-mounts.init %buildroot%_sysconfdir/rc.d/scripts/%name-client-bind-mounts
install -m 0755 client/initscripts/%Codename/%name-client.init %buildroot%_initdir/%name-client
install -m 0755 client/initscripts/%Codename/%name-client-setup.init %buildroot%_initdir/%name-client-setup
install -m 0755 client/initscripts/%Codename/%name-client-swap.init %buildroot%_initdir/%name-client-swap
install -m 0644 client/initscripts/%Codename/lts.conf.default %buildroot%_sysconfdir/lts.conf
install -m 0644 client/initscripts/%Codename/update-kernels.conf %buildroot%_sysconfdir/%name/
install -m 0644 client/initscripts/%Codename/%name.pa %buildroot%_sysconfdir/%name/
install -m 0755 %SOURCE21 %buildroot%_sbindir/ltsconf
install -m 0644 %SOURCE22 %buildroot%_datadir/%name/conffile.tcl
install -m 0755 client/initscripts/%Codename/%name-client-mkinitrd %buildroot%_datadir/%name/

# jetpipe
%if_with jetpipe
install -m 0755 client/jetpipe/jetpipe %buildroot%_sbindir/
install -m 0644 client/jetpipe/jetpipe.8 %buildroot%_man8dir/
%endif


# ldminfod
%if_with ldminfod
install -m 0755 server/ldminfod %buildroot%_sbindir/
install -m 0644 server/doc/ldminfod.8 %buildroot%_man8dir/
%endif


%post server
%make_alsa_conf


%post client
%post_service %name-client-setup
%post_service %name-client-swap
%post_service %name-client


%preun client
%preun_service %name-client
%preun_service %name-client-swap
%preun_service %name-client-setup


%triggerin server -- libalsa
%make_alsa_conf


%files server -f %name.lang
%doc server/doc/{examples,FAQ,plugins,workstation}
%doc server/doc/lts-parameters.* client/getltscfg/lts.conf
%_sbindir/%name-*
%_sbindir/nbd*
%_man8dir/%name-*
%_man8dir/nbd*
%dir %_datadir/%name
%_datadir/%name/plugins
%_datadir/%name/scripts
# the following file required for client and server
%_datadir/%name/%name-*-functions
%exclude %_datadir/%name/alsa-*.conf
%ghost %_datadir/%name/alsa-*.conf
%config(noreplace) %_sysconfdir/%name/dhcpd.conf
%config(noreplace) %_sysconfdir/%name/%name-update-kernels.conf
%config(noreplace) %_sysconfdir/%name/update-kernels.conf
%config(noreplace) %_sysconfdir/%name/%name-build-client.conf
%config(noreplace) %_sysconfdir/xinetd.d/*
%_sysconfdir/%name/asound-*.conf
%_sysconfdir/%name/nbd-server.config
%_sysconfdir/net/%name-keys
%_sysconfdir/sysconfig/%{name}dist
%dir %_localstatedir/tftpboot/%name
%_x11sysconfdir/profile.d/*


%files client
%_bindir/*
%_man1dir/*
%dir %_datadir/%name
%dir %_datadir/%name/screen.d
%_datadir/%name/screen.d/*
# the following file required for client and server
%_datadir/%name/%name-*-functions
%_datadir/%name/screen-x-common
%_datadir/%name/screen_session
%_datadir/%name/start_*
%_datadir/%name/%{name}_config
%_datadir/%name/update-kernels
%_datadir/%name/%name-client-mkinitrd
%_datadir/%name/conffile.tcl
%config(noreplace) %_sysconfdir/default/*
%config(noreplace) %_sysconfdir/lts.conf
%_initdir/%name-client*
%_sysconfdir/rc.d/scripts/*
%_sysconfdir/sysconfig/installkernel1
%dir %_var/cache/%{name}conf
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.pa
%config(noreplace) %_sysconfdir/%name/%name-client-eth-modules.list
%_sbindir/ltsconf
%dir %_localstatedir/%name-client-setup


%if_with jetpipe
%files -n jetpipe
%_sbindir/jetpipe
%_man8dir/jetpipe.*
%endif


%if_with ldminfod
%files -n ldminfod
%_sbindir/ldminfod
%_man8dir/ldminfod.*
%endif


%changelog
* Thu Mar 08 2012 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.12.4
- updated links and descriptions a bit

* Mon Jan 23 2012 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.12.3
- if there's ramzswap, NBD gets used as a backing swap, not directly

* Fri Jan 20 2012 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.12.2
- fixed the following client-server arch combos:
  + i586-i586
  + x86_64-x86_64
  at the expense of i586-x86_64 being still unsupported

* Tue Dec 20 2011 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.12.1
- s/tmc-tc/ltsp-client/

* Sun Dec 18 2011 Michael A. Kangin <prividen@altlinux.org> 5.1.21-alt0.12
- git version
- fix client chroot build

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 5.1.21-alt0.11.1
- Rebuild with Python-2.7

* Thu Sep 30 2010 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.11
- updated default ltsp-build-client regarding kernel flavour
  (led-tc was superseded by tmc-tc); thanks K. A. Bylym

* Sat Jul 24 2010 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.10
- finally applied tmpfs options patch by solo@ (closes: #23608)

* Thu Mar 11 2010 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.9
- dropped /etc/HOSTNAME tmpfs mount (should be a /proc symlink)
- added "diskless fastboot" kernel options

* Sun Dec 27 2009 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.8
- fixed compcache support:
  + module name and params differ by now
  + lts.conf lacked COMPCACHE=auto

* Thu Dec 10 2009 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.7
- fixed overlooked typo in ltsp-login.sh

* Wed Sep 09 2009 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.6
- applied a forgotten local hatch to cope with kernel-image packages
  with Serial:/Epoch: (closes: #21498)

* Wed Sep 09 2009 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.5
- replaced rpm-utils dependency with /usr/bin/rpmvercmp one
  (closes: #21479)

* Sat Jun 13 2009 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.4
- NMU: added temporary initscripts update patch (needs merging)
  + NBD swap setup fixed
  + pulseaudio startup fixed

* Fri Mar 06 2009 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.3
- NMU: hacked patch to provide working
  /var/lib/tftpboot/ltsp/i586/pxelinux.cfg/default

* Thu Mar 05 2009 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.2
- NMU: added e2fsprogs to ltsp-client dependencies (/sbin/fsck)

* Tue Mar 03 2009 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.1.2
- NMU: removed ExclusiveArch: per led@'s advice
- require setarch unconditionally (otherwise noarch reqs get volatile)

* Mon Feb 23 2009 Michael Shigorin <mike@altlinux.org> 5.1.21-alt0.1.1
- NMU: fixed ltsp-server %%post scriptlet to be more robust

* Thu Aug 28 2008 Led <led@altlinux.ru> 5.1.21-alt0.1
- 5.1.21
- updated:
  + ltsp-client-eth-modules.list
  + ltsp-client-setup.init
  + dhcpd.conf.in
  + ???-apt-get-update plugin

* Fri Jun 20 2008 Led <led@altlinux.ru> 5.1.9-alt0.1
- 5.1.9:
- added support for custom X modes (thanx mike@ for patch)

* Fri Jun 20 2008 Led <led@altlinux.ru> 5.1.7-alt0.4
- fixed ltsconf (#16098)

* Sat Jun 07 2008 Led <led@altlinux.ru> 5.1.7-alt0.3
- fixed client's initrd generating

* Mon May 12 2008 Led <led@altlinux.ru> 5.1.7-alt0.2
- added support / on NBD device

* Wed May 07 2008 Led <led@altlinux.ru> 5.1.7-alt0.1
- 5.1.7
- updated %name-5.1.7-alt.patch

* Wed Apr 23 2008 Led <led@altlinux.ru> 5.1.3-alt0.4
- added %_datadir/%name/%name-*-functions to %name-server package

* Thu Apr 17 2008 Led <led@altlinux.ru> 5.1.3-alt0.3
- updated ltsp-r696-alt.patch
- added local scanner support
- replaced %_x11sysconfdir/profile.d/ltsp-sound.sh with
  %_x11sysconfdir/profile.d/ltsp.sh

* Mon Apr 14 2008 Led <led@altlinux.ru> 5.1.3-alt0.2
- fixed ltsp-vendor-functions
- cleaned up default lts.conf
- updated lts-parameters.alt

* Mon Apr 14 2008 Led <led@altlinux.ru> 5.1.3-alt0.1
- 5.1.3
- updated ltsp-r696-alt.patch
- added support PULSE_OPTS in lts.conf for %_initdir/%name-client

* Tue Apr 08 2008 Led <led@altlinux.ru> 5.1.2-alt0.3
- added support for xaudio

* Tue Apr 08 2008 Led <led@altlinux.ru> 5.1.2-alt0.2
- fixed:
  + ltsp-update-kernels (server)
  + update-kernels (client)

* Mon Apr 07 2008 Led <led@altlinux.ru> 5.1.2-alt0.1
- 5.1.2
- updated %name-r682-alt.patch:
  + added asound-xaudio.conf
  + cleaned up asound-null.conf
  + updated ???-exports plugin

* Mon Mar 31 2008 Led <led@altlinux.ru> 5.1.1-alt0.3
- fixed %_x11sysconfdir/profile.d/ltsp-sound.sh

* Mon Mar 31 2008 Led <led@altlinux.ru> 5.1.1-alt0.2
- renamed ltsp5 -> ltsp
- cleaned up %_initdir/ltsp-client-setup

* Fri Mar 28 2008 Led <led@altlinux.ru> 5.1.1-alt0.1
- 5.1.1 (revision 683)

* Thu Mar 27 2008 Led <led@altlinux.ru> 5.1.0-alt0.6
- fixed %_sysconfdir/sysconfig/installkernel again (#15084)

* Wed Mar 26 2008 Led <led@altlinux.ru> 5.1.0-alt0.5
- added start_printer script
- fixed and moved %_sysconfdir/profile.d/ltsp.sh to
  %_x11sysconfdir/profile.d/ltsp-sound.sh

* Wed Mar 26 2008 Led <led@altlinux.ru> 5.1.0-alt0.4
- cleaned up:
  + %_sysconfdir/default/ltsp-client-setup
  + %_sysconfdir/sysconfig/installkernel
- added %_sysconfdir/sysconfig/ltspdist
- fixed %_sysconfdir/sysconfig/installkernel (#15084)

* Tue Mar 25 2008 Led <led@altlinux.ru> 5.1.0-alt0.3
- added %_datadir/ltsp/plugins/ltsp-build-client/functions-altlinux
- cleaned up:
  + ltsp-r576-alt.patch
  + ???-gen-ltsp-base plugin
- fixed %_initdir/ltsp-client-swap

* Fri Mar 21 2008 Led <led@altlinux.ru> 5.1.0-alt0.2
- moved ldminfod into subpackage

* Thu Mar 20 2008 Led <led@altlinux.ru> 5.1.0-alt0.1
- revision 576
- updated:
  + %_initdir/ltsp-client-setup
  + %_initdir/ltsp-client
  + %_initdir/ltsp-client-swap
  + ltsp-r576-alt.patch
  + ldminfod-r576-alt.patch
- removed:
  + ltsp5-start_telnet.patch
  + ltsp5-startx.patch
  + ltsp5-start_printer.patch
- support clients with RAM>=16M

* Wed Mar 12 2008 Led <led@altlinux.ru> 5.0-alt0.75
- fixed:
  + %_x11sysconfdir/profile.d/ltsp-login.sh
  + %_sysconfdir/profile.d/ltsp.sh

* Tue Mar 11 2008 Led <led@altlinux.ru> 5.0-alt0.74
- updated %_x11sysconfdir/profile.d/ltsp-login.sh for support
  Tk (wish), gxmessage

* Tue Mar 11 2008 Led <led@altlinux.ru> 5.0-alt0.73
- updated %_x11sysconfdir/profile.d/ltsp-login.sh for support
  kdialog, zenity, Xdialog without GTK+, xmessage

* Fri Mar 07 2008 Led <led@altlinux.ru> 5.0-alt0.72
- added:
  + %_sysconfdir/ltsp/asound-pulse.conf
  + %_sysconfdir/ltsp/asound-null.conf
  + %_x11sysconfdir/profile.d/ltsp-login.sh
  + compcache support to %_initdir/ltsp-client-swap
- removed:
  + %_sysconfdir/ltsp/asound.conf
  + removed alterator-backend-x11 workaround
- Conflicts: alterator-backend-x11 < 0.13.1
- updated %%make_alsa_conf
- updated spec
- without jetpipe
- without ldm

* Wed Feb 06 2008 Led <led@altlinux.ru> 5.0-alt0.71
- set SOUND_VOL=80 in ltsp-client's default %_sysconfdir/lts.conf

* Tue Feb 05 2008 Led <led@altlinux.ru> 5.0-alt0.70
- fixed %%files

* Tue Feb 05 2008 Led <led@altlinux.ru> 5.0-alt0.69
- updated:
  + %_initdir/ltsp-client (unmute ALSA's Master)
  + %_sysconfdir/ltsp/ltsp-build-client.conf
  + %_sysconfdir/ltsp/ltsp-client-eth-modules.list

* Mon Feb 04 2008 Led <led@altlinux.ru> 5.0-alt0.68
- fixed ltsp5-client's Requires
- updated:
  + %_initdir/ltsp-client-setup
  + %_sysconfdir/ltsp/dhcpd.conf
  + %_sysconfdir/ltsp/ltsp-build-client.conf
  + %_sysconfdir/ltsp/ltsp-client-eth-modules.list
- fixed %%changelog
- fixed and cleaned up spec
- removed conflicts grub and lilo from ltsp5-client

* Thu Dec 27 2007 Led <led@altlinux.ru> 5.0-alt0.67
- fixed %_sysconfdir/ltsp/dhcpd.conf
- updated ???-kernel-modules plugin
- fixed License
- added %_localstatedir/ltsp-client-setup directory to ltsp-client

* Sun Dec 23 2007 Led <led@altlinux.ru> 5.0-alt0.66
- exluded subpackage jetpipe from ltsp5-client
- cleaned up spec
- updated ???-gen-base, ???-basic-configuration plugins
- removed gen-ltsp-root script
- added %_initdir/ltsp-client-swap
- cleaned up %_initdir/ltsp-client-setup

* Fri Dec 14 2007 Led <led@altlinux.ru> 5.0-alt0.65
- updated %_initdir/ltsp-client-setup: added support X_DISPLAY_SIZE
  parameter
- updated lts-parameters.alt
- added ???-make-dirs plugin
- fixed %_initdir/ltsp-client.init

* Thu Dec 13 2007 Led <led@altlinux.ru> 5.0-alt0.64
- added ???-etc-inittab plugin
- fixed %_libexecdir/ltsp/screen.d/rdp (#13560)
  (thanx to Michael A. Kangin)
- updated %_initdir/ltsp-client-setup

* Wed Dec 12 2007 Led <led@altlinux.ru> 5.0-alt0.63
- updated %_sysconfdir/profile.d/ltsp.sh
- use pulseaudio by default

* Tue Dec 11 2007 Led <led@altlinux.ru> 5.0-alt0.62
- updated:
  + %_datadir/ltsp/scripts/mkswapfile
  + %_initdir/ltsp-client-setup: added support swap over NFS
  + ltsp5-20070817-alt.patch
  + lts-parameters.alt
  + moved lts-parameters.* to ltsp5-server package

* Sun Nov 11 2007 Led <led@altlinux.ru> 5.0-alt0.61
- updated:
  + %_initdir/ltsp-client-setup
  + %_sysconfdir/profile.d/ltsp.sh

* Thu Nov 01 2007 Led <led@altlinux.ru> 5.0-alt0.60
- updated:
  + %_sysconfdir/ltsp/ltsp-client-eth-modules.list
  + %_sbindir/ltsconf
  + %_sysconfdir/sysconfig/installkernel
  + %_sysconfdir/ltsp/ltsp-build-client.conf
- added %_sysconfdir/ltsp/clients.conf

* Wed Oct 24 2007 Led <led@altlinux.ru> 5.0-alt0.59
- fixed ltsp-client-mkinitrd

* Wed Oct 24 2007 Led <led@altlinux.ru> 5.0-alt0.58
- updated ltsp5-20070817-alt.patch: set RAM limit for X server

* Mon Oct 22 2007 Led <led@altlinux.ru> 5.0-alt0.57
- added %_libexecdir/ltsp/ltsp-client-mkinitrd
- updated %_sysconfdir/sysconfig/installkernel
- cleaned up ltsp5-20070817-alt.patch
- added ???-sysctl plugin

* Mon Oct 22 2007 Led <led@altlinux.ru> 5.0-alt0.56
- updated %_sysconfdir/{default/ltsp-client-setup,sysconfig/installkernel},
  %_initdir/ltsp-client{,-setup}
- added ???-ssh-keys plugin
- updated ltsp-client-eth-modules.list

* Sat Oct 20 2007 Led <led@altlinux.ru> 5.0-alt0.55
- fixed ltsp-client-setup.init
- updated ???-dev plugin: don't remove /dev/urandom (need for passwd)

* Wed Oct 17 2007 Led <led@altlinux.ru> 5.0-alt0.54
- set size of client's tmpfs
- updated ???-gen-ltsp-base plugin and gen-ltsp-root script:
  added resolving for FTP|HTTP|SSH|RSH sources
- updated ???-manage-mirror plugin: added support "copy:/" sources
- updated ltsp-client-setup.init

* Mon Oct 15 2007 Led <led@altlinux.ru> 5.0-alt0.53
- added ???-udev plugin

* Mon Oct 15 2007 Led <led@altlinux.ru> 5.0-alt0.52
- added missed %_sysconfdir/ltsp/nbd-server.config
- updated ltsp-client-setup.init:
  + create only 2 nbd devices
  + use /dev/nbd1 for swap

* Mon Oct 15 2007 Led <led@altlinux.ru> 5.0-alt0.51
- updated ltsp-client-setup.init
- added {mk,rm}swapfile scripts
- added %_sysconfdir/ltsp/nbd-server.config

* Wed Oct 10 2007 Led <led@altlinux.ru> 5.0-alt0.50
- updated ltsp-client-eth-modules.list: added b44 and tg3 modules

* Wed Oct 10 2007 Led <led@altlinux.ru> 5.0-alt0.49
- updated ltsp5-20070817-alt.patch for ability X-session without xfs
- updated ???-manage-mirror (without awk)

* Tue Oct 09 2007 Led <led@altlinux.ru> 5.0-alt0.48
- fixed plugin ???-manage-mirror
- cleaned up spec

* Mon Oct 08 2007 Led <led@altlinux.ru> 5.0-alt0.47
- fixed plugin ???-manage-mirror
- cleaned up spec

* Fri Oct 05 2007 Led <led@altlinux.ru> 5.0-alt0.46
- fixed ltsp-build-client plugin ???-dev: create /dev/{null,cobsole}
  devices

* Fri Oct 05 2007 Led <led@altlinux.ru> 5.0-alt0.45
- fixed ???-manage-mirror plugin
- added support for "cdrom:" and verbatim ("rpm <URL> <arch> <comp>")
  sources in MIRROR
- build client's chroot without spt
- fixed #12982

* Tue Sep 04 2007 Led <led@altlinux.ru> 5.0-alt0.44
- updated ltsp5-20070817-alt.patch:
  + fixed ltsp-update-kernels
- fixed ???-make-dirs-file plugin

* Tue Sep 04 2007 Led <led@altlinux.ru> 5.0-alt0.43
- changed vendor to ALTLinux
- cleaned up ltsp5-client requires
- updated %_sysconfdir/default/ltsp-client-setup

* Mon Sep 03 2007 Led <led@altlinux.ru> 5.0-alt0.42
- fixed ltsp5-client requires

* Sun Aug 19 2007 Led <led@altlinux.ru> 5.0-alt0.41
- updated ltsp-mkbootiso
- updated ltsp-client.init
- fixed ldm Requires

* Sun Aug 19 2007 Led <led@altlinux.ru> 5.0-alt0.40
- added ldminfod-20070817-alt.patch
- updated ltsp5-20070817-alt.patch
- fixed Requires
- added ltsp5-start_printer.patch

* Sat Aug 18 2007 Led <led@altlinux.ru> 5.0-alt0.39
- new snapshot (2007-08-17)
- updated ltsp5-20070817-alt.patch
- updated/fixed ltsp-dhcpd.conf
- cleaned up %%files

* Mon Aug 06 2007 Led <led@altlinux.ru> 5.0-alt0.38
- updated ltsp-client.init:
  + added sound volume setting
- fixed %_sysconfdir/profile.d/ltsp.sh

* Mon Aug 06 2007 Led <led@altlinux.ru> 5.0-alt0.37
- fixed #12464
- removed ltsp-client-sound.sh
- added %_sysconfdir/profile.d/ltsp.sh
- cleaned up ltsp5-alt.patch

* Thu Aug 02 2007 Led <led@altlinux.ru> 5.0-alt0.36
- updated ltsp-dhcpd.conf
- added %_sbindir/ltsconf

* Wed Aug 01 2007 Led <led@altlinux.ru> 5.0-alt0.35
- added ???-restore-saved script

* Sat Jul 28 2007 Led <led@altlinux.ru> 5.0-alt0.34
- fixed Sisyphus/???-make-dirs-files script
- updated ltsp5-alt.patch:
  + gtk.py -> ldm_gtk.py
  + fixed ltsp-update-kernels
  + fixed update-kernels
- replaced %_sysconfdir/{profile,bashrc}.d/ltsp-mkinitrd.sh with
  %_sysconfdir/sysconfig/installkernel
- cleaned up requires of ltsp5-client
- added %_localstatedir/pulse to rw_dirs in ltsp-client-setup.default

* Thu Jul 26 2007 Led <led@altlinux.ru> 5.0-alt0.33
- updated ltsp5-alt.patch:
  + used separate dhcpd.conf
  + support mkelfImage in update-kernels script

* Thu Jul 19 2007 Led <led@altlinux.ru> 5.0-alt0.32
- updated ltsp5-alt.patch:
  + dhcpd.conf
  + fixed tftpboot path in ltsp-update-kernels

* Thu Jul 12 2007 Led <led@altlinux.ru> 5.0-alt0.31
- added pulseaudio support via ALSA pulse plugin

* Wed Jul 11 2007 Led <led@altlinux.ru> 5.0-alt0.30
- added pulseaudio support

* Mon Jul 09 2007 Led <led@altlinux.ru> 5.0-alt0.29
- fixed ltsp-client-setup.init (local swaps)

* Mon Jul 09 2007 Led <led@altlinux.ru> 5.0-alt0.28
- added ltsp5-server <=> ltsp5-client Conflicts
- added ltsp-mkbootiso to ltsp5-server

* Mon Jul 09 2007 Led <led@altlinux.ru> 5.0-alt0.27
- updated ltsp-client-bind-mounts.init for bind %_var/cache/ltspconf
- updated ltsp-client-setup.init for usability x11_autosetup
- added %_var/cache/ltspconf dir to ltsp5-client
- added %_x11sysconfdir/xorg.conf.auto -> %_var/cache/ltspconf/xorg.conf
  softlink for usability x11_autosetup

* Fri Jul 06 2007 Led <led@altlinux.ru> 5.0-alt0.26
- updated %_sysconfdir/default/ltsp-client-setup,
  %_initdir/ltsp-client-setup and ltsp5-client requires for
  available proprietary nvidia X-Window driver

* Thu Jul 05 2007 Led <led@altlinux.ru> 5.0-alt0.25
- added forcedeth to ltsp-client-eth-modules.list

* Tue Jul 03 2007 Led <led@altlinux.ru> 5.0-alt0.24
- fixed gen-ltsp-image (broken sources.list if EXTRA_MIRROR not set)

* Mon Jul 02 2007 Led <led@altlinux.ru> 5.0-alt0.23
- fixed gen-ltsp-image and Sisyphus/???-gen-ltsp-base

* Tue Jun 26 2007 Led <led@altlinux.ru> 5.0-alt0.22
- fixed ltsp-client.init for TC reboot/poweroff ability
  (via ltspinfo)

* Mon Jun 25 2007 Led <led@altlinux.ru> 5.0-alt0.21
- fixed ltsp5-alt.patch:
  + dhcpd.conf

* Sat Jun 16 2007 Led <led@altlinux.ru> 5.0-alt0.20
- updated lts-parameters.alt: added RDP parameters

* Fri Jun 08 2007 Led <led@altlinux.ru> 5.0-alt0.19
- added lts-parameters.alt

* Fri Jun 01 2007 Led <led@altlinux.ru> 5.0-alt0.18
- ltsp5-client requires mkinitrd-initramfs >= 3.0.4
- cleaned up 000-basic-configuration

* Fri Jun 01 2007 Led <led@altlinux.ru> 5.0-alt0.17
- updated ltsp5-alt.patch:
  + dhcpd.conf
  + %_localstatedir/tftpboot/ltsp/* permissions

* Sat May 26 2007 Led <led@altlinux.ru> 5.0-alt0.16
- fixed ltsp-client.init (start_sound)

* Fri May 25 2007 Led <led@altlinux.ru> 5.0-alt0.15
- updated ltsp-client.init (start_sound):
  + use ALSA for EsounD
  + default NAS for OSS and EsounD for ALSA

* Thu May 24 2007 Led <led@altlinux.ru> 5.0-alt0.14
- fixed ltsp-client-setup.init:
  + configure_fstab
  + configure_resolver

* Wed May 23 2007 Led <led@altlinux.ru> 5.0-alt0.13
- added screen session for RDP (rdesktop)
- updated ltsp5-alt.patch: moved loop from screen_session to startx
  screen session
- updated ltsp-client-setup.init

* Mon May 21 2007 Led <led@altlinux.ru> 5.0-alt0.12
- updated lts.conf.default
- added %_x11sysconfdir/xinit.d/ltsp-client-sound
- updated ltsp-client.init: audio
- updated 005-nbdswapd: default swap dir is %_var/spool/swaps

* Fri May 18 2007 Led <led@altlinux.ru> 5.0-alt0.11
- fixed %%files for ltsp5-client: noreplace configs
- fixed ltsp-client.init: audio

* Fri May 18 2007 Led <led@altlinux.ru> 5.0-alt0.10
- updated ltsp-client-setup.init: support POWER_BUTTON conf parameter
- updated ltsp-client.init: load ALSA's OSS-compat module if needed

* Thu May 17 2007 Led <led@altlinux.ru> 5.0-alt0.9
- updated ltsp5-alt.patch:
  + cleaned up
  + loop in screen_session
- fixed ltsp-client-setup.init and ltsp-client-setup.default for
  customizing keyboard

* Wed May 16 2007 Led <led@altlinux.ru> 5.0-alt0.8
- updated ltsp-client-mkinitrd.sh: support --noload minitrd's key

* Wed May 16 2007 Led <led@altlinux.ru> 5.0-alt0.7
- changed default ltsp-build-client.conf
- fixed 000-init-whitelist
- updated ltsp5-alt.patch:
  + remove runlevel in kernel parameters
- fixed 000-basic-configuration
- fixed %_sysconfdir/ltsp/dhcpd.conf

* Fri May 11 2007 Led <led@altlinux.ru> 5.0-alt0.6
- fixed esd support in ltsp-client.init
- updated ltsp5-alt.patch:
  + default runlevel 2
- fixed Sisyphus/000-init-whitelist

* Thu May 10 2007 Led <led@altlinux.ru> 5.0-alt0.5
- fixed Sisyphus/095-exports
- fixed Requires for ltsp5-server
- cleaned up ltsp5-server %%files
- default UDP protocol for NFSROOT
- updated ltsp5-alt.patch
- updated %_sysconfdir/ltsp/update-kernels.conf

* Mon May 07 2007 Led <led@altlinux.ru> 5.0-alt0.4
- cleaned up ltsp-client-setup.init

* Thu Apr 26 2007 Led <led@altlinux.ru> 5.0-alt0.3
- updated ltsp5-alt.patch
- updated ltsp-client-setup.init
- updated ltsp-client.init
- set ltsp5-client Conflicts

* Mon Apr 23 2007 Led <led@altlinux.ru> 5.0-alt0.2
- fixed ltsp-client-setup.init and lts.conf.default for support local
  client devices

* Mon Apr 16 2007 Led <led@altlinux.ru> 5.0-alt0.1
- initial build
