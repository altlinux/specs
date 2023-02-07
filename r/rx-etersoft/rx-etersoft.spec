%define oname freenx-server
%define hooksroot rx-etersoft

Name: rx-etersoft
Version: 1.5.2
Release: alt2

Summary: RX@Etersoft - NX based application/thin-client server

Group: Networking/Remote access
License: GPLv2
Url: http://wiki.etersoft.ru/RX

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: /var/ftp/pvt/Etersoft/RX@Etersoft/%version/source/tarball/%name-%version.tar
Source1: %name.init
Source2: %name.outformat
Source6: sudoers.conf
Source8: nx-terminate-suspend

Obsoletes: freenx
Provides: freenx = %version

Obsoletes: %oname
Provides: %oname = %version

%define NXVERSION 3.5.2
Requires: nx-libs >= 3.5.2
Requires: nxagent

Requires: setxkbmap
Requires: numlockx
Requires: sessreg
Requires: openssl openssh-server openssh-clients
Requires: netcat expect sudo xauth
Requires: zenity
Requires: iconv

Requires: cups cifs-utils

# See eterbug #12003
# Requires: foomatic-db foomatic-db-engine

# for %_libexecdir/cups/backend/smb
# Requires: samba-client

%if "%_vendor" == "alt"
Requires: dbus-tools-gui
%endif

# _sudoersdir, _cupslibdir
BuildPreReq: rpm-build-intro >= 1.7.25

BuildRequires: imake xorg-cf-files gccmakedep

BuildRequires: expect sudo

AutoReq: yes, nopython

%description
RX@Etersoft (formely freenx-server) is an application/thin-client server based on NX technology.
NoMachine NX is the X compression and roundtrip suppression scheme.
It can operate remote X11 sessions over 56k modem dialup links
or anything better. This package contains a free (GPL) implementation
of the nxserver component.

Recommended Requires: foomatic-db foomatic-db-engine

%prep
%setup
%__subst "s|\$NX_DIR/lib|%_libdir|g" nxloadconfig
# subst version info
%__subst 's|^NX_VERSION=.*|NX_VERSION="%NXVERSION %version-%release"|g' nxloadconfig
%__subst 's|^NX_BACKEND_VERSION=.*|NX_BACKEND_VERSION="%NXVERSION"|g' nxloadconfig

%build
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_var/lib/%name/home/
mkdir -p %buildroot%_var/lib/%name/db/
mkdir -p %buildroot%_sysconfdir/%name/node.conf.d/
mkdir -p %buildroot%_sysconfdir/%name/commands/
mkdir -p %buildroot%_sysconfdir/%name/acls/
mkdir -p %buildroot%_sysconfdir/cron.d/
mkdir -p %buildroot%_datadir/misc/


install -m755 xephyr-run %buildroot%_bindir/
install -m755 rxsetup %buildroot%_bindir/
install -m755 rxreport %buildroot%_bindir/
#install -Dp -m755 %SOURCE1 %buildroot%_initdir/%name
install -Dp -m755 data/fixkeyboard %buildroot%_sysconfdir/%name/fixkeyboard
install -Dp -m755 data/Xsession %buildroot%_sysconfdir/%name/Xsession
install -Dp -m644 data/Xkbmap %buildroot%_sysconfdir/%name/Xkbmap
install -Dp -m400 %SOURCE6 %buildroot%_sudoersdir/rxetersoft
install -Dp -m755 %SOURCE8 %buildroot%_sbindir/nx-terminate-suspend
install -Dp -m644 conf/node.conf %buildroot%_sysconfdir/%name/node.conf
install -m644 conf/conf.d/*.conf %buildroot%_sysconfdir/%name/node.conf.d/
install -m644 conf/acls/* %buildroot%_sysconfdir/%name/acls/
install -m755 commands/* %buildroot%_sysconfdir/%name/commands/

mkdir -p -m755 %buildroot%_sysconfdir/%hooksroot
cp -r hooks %buildroot%_sysconfdir/%hooksroot

mkdir -p -m755 %buildroot%_libdir/%hooksroot
cp -r hooks %buildroot%_libdir/%hooksroot

cat > %buildroot%_sysconfdir/%hooksroot/Xephyr.conf <<EOF
-extension GLX -fullscreen
EOF

%if "%_vendor" != "alt"
install -m755 %SOURCE2 %buildroot%_datadir/misc/
%endif

install -Dp -m644 data/logrotate %buildroot%_sysconfdir/logrotate.d/%name
#install -Dp -m644 nx-session-launcher/ConsoleKit-NX.conf %buildroot%_sysconfdir/dbus-1/system.d/ConsoleKit-NX.conf
mv nx-session-launcher/README nx-session-launcher/README.suid

rm -v %buildroot%_bindir/nx-session-launcher
rm -v %buildroot%_bindir/nx-session-launcher-suid

cat >> %buildroot%_sysconfdir/cron.d/%name << EOF
# Terminate suspend sessions if needed
#*/5 * * * *       root    %_sbindir/nx-terminate-suspend
EOF

%pre
%groupadd nx 2>/dev/null ||:
%useradd -g nx -G utmp -d /var/lib/%name/home -s %_bindir/nxserver \
        -c "NX System User" nx 2>/dev/null ||:

%files
%doc AUTHORS CONTRIB
#docnx-session-launcher/README.suid
%dir %_sysconfdir/%name/
%dir %_sysconfdir/%name/node.conf.d/
%dir %_sysconfdir/%name/acls/
%dir %_sysconfdir/%name/commands/
%config(noreplace) %_sysconfdir/%name/node.conf
%config(noreplace) %_sysconfdir/%name/node.conf.d/*
%config(noreplace) %_sysconfdir/%name/acls/*
%attr (0755,root,root) %config(noreplace) %_sysconfdir/%name/commands/*
%config(noreplace) %_sysconfdir/logrotate.d/%name
%attr(0400,root,root) %config(noreplace) %_sudoersdir/rxetersoft
#%config(noreplace) %_sysconfdir/dbus-1/system.d/ConsoleKit-NX.conf
%config(noreplace) %_sysconfdir/%name/Xkbmap
%config(noreplace) %_sysconfdir/%name/Xephyr.conf
%_sysconfdir/%name/fixkeyboard
%_sysconfdir/%name/Xsession
%dir %_sysconfdir/%hooksroot/hooks/
%_sysconfdir/%hooksroot/hooks/*
%dir %_libdir/%hooksroot/hooks/
%_libdir/%hooksroot/hooks/*
%attr(0400,root,root) %config(noreplace) %_sysconfdir/cron.d/%name
%_sbindir/nx-terminate-suspend
#%_initddir/%name
%if "%_vendor" != "alt"
%_datadir/misc/%name.outformat
%endif

#%_bindir/nx-session-launcher
#%attr(4711,nx,root) %_bindir/nx-session-launcher-suid
%_bindir/nxacl.app
%_bindir/nxacl.sample
%_bindir/nxcheckload
%_bindir/nxcups-gethost
%_bindir/nxdesktop_helper
%_bindir/nxdialog
%_bindir/nxkeygen
%_bindir/nxloadconfig
%_bindir/nxnode
%_bindir/nxnode-login
%_bindir/nxpasswd
%_bindir/nxprint
%_bindir/nxredir
%_bindir/cupsredir
%_bindir/nxserver
%_bindir/nxserver-helper
%_bindir/nxserver-suid
%_bindir/nxserver-usermode
%_bindir/nxsetup
%_bindir/nxviewer_helper
%_bindir/rxsetup
%_bindir/rxreport
%_bindir/xephyr-run
%dir %_libdir/%name/
%attr(755,root,root) %_libdir/%name/libnxredir.so.0
%attr(755,root,root) %_libdir/%name/libcupsredir.so.0
%_cupslibdir/backend/nx*
%dir %_var/lib/%name/
%attr(2750,nx,nx) %_var/lib/%name/home/
%attr(2750,root,nx) %_var/lib/%name/db/

%changelog
* Thu Nov 10 2022 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt2
- add default /etc/rx-etersoft/Xephyr.conf and use xephyr-run if Xephyr command is exists
- use xephyr-run as latest wrapper in the command line

* Wed Nov 09 2022 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- use xephyr-run wrapper if /etc/rx-etersoft/Xephyr.conf is exists

* Fri Jul 29 2022 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt2
- fix bare words in spec

* Fri Jul 08 2022 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- nxsetup: remove ssh-dss support
- nxsetup: temp. drop no-port-forwarding

* Thu Jul 07 2022 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-eter1
- new experimental CUPS and PCSCD tunneling (eterbug #15556)

* Tue Feb 22 2022 Konstantin Kondratyuk <kondratyuk@altlinux.org> 1.4.9-eter1
- disable ssh host key checking in nxnode-login

* Sun Feb 20 2022 Vitaly Lipatov <lav@altlinux.ru> 1.4.8-alt1
- spec: remove last slash from nx user work dir path
- drop rx-etersoft service (todo: use something from it in future)
- change nxssh prompt options for disable ssh host key checking

* Wed Feb 09 2022 Vitaly Lipatov <lav@altlinux.ru> 1.4.7-alt1
- nxserver: rewrite set_auth_mode detection
- use authorized_keys instead of authorized_keys2
- nxloadconfig: add check for DEFAULT_X_SESSION=/etc/X11/xinit/xinitrc
- nxserver: improve logs, cleanup
- replace nxclient/opennx with rxclient, remove obsoleted INSTALL

* Sun Sep 05 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4.6-alt1
- nxdialog: fix requote function
- don't pack nx-session-launcher*

* Tue Mar 16 2021 Vitaly Lipatov <lav@altlinux.ru> 1.4.5-alt1
- remove bashisms (eterbug #14996)
- use client.id_rsa.key instead of client.id_dsa.key for server forwarding
- use SSH_LOCAL_KEY conf variable instead of users.id_dsa
- small text cleanup

* Fri Jan 31 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt2
- skip nx-session-launcher* packing (obsoleted python2 script for ConsoleKit)

* Thu Nov 21 2019 Konstantin Kondratyuk <kondratyuk@altlinux.org> 1.4.4-alt1
- rewrite rxsetup to use epm
- rxsetup: run me under root user
- nxloadconfig: fix mate detection, add support for mate-terminal (eterbug #14314)

* Mon Nov 18 2019 Konstantin Kondratyuk <kondratyuk@altlinux.org> 1.4.3-alt1
- fix session_close (eterbug #13765)

* Thu Oct 24 2019 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- nxloadconfig: add startkde5 support
- rx-etersoft.init: fix RX Etersoft name
- disable SET_LD_LIBRARY_PATH by default

* Fri Dec 28 2018 Etersoft Builder <builder@etersoft.ru> 1.4.1-alt3
- (CI): disabled release build for p7

* Wed Dec 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt2
- remove license check from GPL code

* Fri Nov 30 2018 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- (rxreport): added .xsession-errors files
- added 'sess_id' variable processing in getparam_sessionid
- added CUPS_DEFAULT_SYSTEM_GROUP ("sys root") and user main group for SystemGroup for cupsd. (eterbug #13290)
- (config): added timeout for cupsd start
- added timestamp for logs (eterbug #13312)

* Mon Sep 24 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt18
- fixed type=smb printer processing for CUPS_DEFAULT_DRIVER
- (CI): monitor fixes in service name

* Sun Sep 23 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt17
- (CI): send message to telegram only for tagged commits

* Sat Sep 22 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt16
- (nxnode): added waiting for cupsd to start eterbug #12972
- (nxnode): refactoring: added 'wait_event' function

* Thu Sep 13 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt15
- rxreport minor fixes

* Mon Sep 03 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt14
- (rxsetup): added command logon/logoff

* Sat Sep 01 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt13
- added rxreport to package

* Sat Sep 01 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt12
- (CI): added event bot message
- (rxreport): Fixed bug in prefix for session directory ('S-' --> 'F-')

* Fri Aug 31 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt11
- added rxreport script

* Tue Aug 14 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt10
- (CI): disable test build for i586.32 and p7
- set the default driver for all user printers (eterbug #13062)

* Fri Aug 10 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt9
- (CI): use 'rx-daas-templates' project

* Thu Aug 02 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt8
- fix terminate error (eterbug #12933)
- (CI): added real remove old builds
- (gitlab-ci): added tests with docker

* Thu Jun 28 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt7
- (CI): minor fixes in pipeline

* Wed Jun 27 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt6
- fix "add printer" bug (eterbug #12972)
- (CI): added test build stage

* Fri Jun 22 2018 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt5
- fix session cleanup error (eterbug #12933)

* Thu May 03 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt4
- added require for nxagent (eterbug #12860)

* Fri Apr 27 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt3
- implement taking over control (eterbug #12849)

* Thu Apr 12 2018 Etersoft Builder <builder@etersoft.ru> 1.4.0-alt2
- added changelog

* Thu Apr 12 2018 Pavel Vainerman <pv@altlinux.ru> 1.4.0-alt1
- update requires
- rename "xxx/nxserver" --> "xxx/rx-etersoft" (eterbug #12785)
- fixed bug with set numlock (eterbug #9384) 

* Thu Apr 05 2018 Etersoft Builder <builder@etersoft.ru> 1.3.0-alt2
- release 1.3.0

* Thu Apr 05 2018 Pavel Vainerman <pv@altlinux.ru> 1.3.0-alt1
- release 

* Wed Apr 04 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.0-alt11
- up version (test build)

* Wed Apr 04 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.0-alt10
- nxserver: move up server_get_params
- new build 1.1.4-alt1 (with rpmlog script)
- add LXDE/MATE support
- add rsa and ed25519 keys
- fix -pi using: -i not for pipe
- fix license message
- new build 1.1.4-alt2 (with rpmlog script)
- nxprint: skip hangup on empty list, fix linked dirs
- nxdialog: fix spaces strings comparing
- nxdialog: drop NXCLIENT
- 1.1.4-alt3
- spec: pack missed /var/lib/nxserver
- 1.1.4-alt4
- turn off no-agent-forwarding option
- new release (1.2.0)
- fixed bug in NXVERSION for nxloadconfig
- remove require for nxssh
- add auth_mode support
- implement smartcard authorization command for rx-etersoft (eterbug #12027)
- add $AUTH_MODE into nxnode-login command line
- add pause for non-slave mode
- fix NUMLOCKX_STATUS setting
- set numlock status 'client' as default
- add restriction parameters for user's resources
- implement ENABLE_PRINTING restriction
- implement ENABLE_SHARING restriction
- added .gitlab-ci.yml
- 1.2.0-alt4
- (gitlab-ci): enable for master branch - (gitlab-ci): move "build for p7" to main build task - fix NUMLOCKX_STATUS setting - set numlock status 'client' as default - add restriction parameters for user's resources - implement ENABLE_PRINTING restriction - implement ENABLE_SHARING restriction - implement ENABLE_SMARTCARD restriction - added .gitlab-ci.yml - SET VERSION 3.5.2 (sync with nx) - added support hooks for plugins
- 1.2.0-alt9
- NX_HOOKS_DIR --> NX_HOOKS_DIRS (use /usr/lib/.../hooks, /etc/nxserver/hooks/)
- added 'export2session' function (for modules)

* Mon Mar 26 2018 Etersoft Builder <builder@etersoft.ru> 1.2.0-alt9
- (gitlab-ci): enable for master branch - (gitlab-ci): move "build for p7" to main build task - fix NUMLOCKX_STATUS setting - set numlock status 'client' as default - add restriction parameters for user's resources - implement ENABLE_PRINTING restriction - implement ENABLE_SHARING restriction - implement ENABLE_SMARTCARD restriction - added .gitlab-ci.yml - SET VERSION 3.5.2 (sync with nx) - added support hooks for plugins

* Mon Mar 19 2018 Etersoft Builder <builder@etersoft.ru> 1.2.0-alt8
- (usbip): added support options 'usbip','usbipdev', attach/detach usbip devices
- (gitlab-ci): move "build for p7" to main build task

* Fri Mar 16 2018 Etersoft Builder <builder@etersoft.ru> 1.2.0-alt7
- SET VERSION 3.5.2
- (pcsc): excluded parasitic dependence on the script 'nx-pcsc-helper.sh'

* Tue Mar 13 2018 Etersoft Builder <builder@etersoft.ru> 1.2.0-alt6
- (pcsc): added check directory for socket and script

* Tue Mar 13 2018 Etersoft Builder <builder@etersoft.ru> 1.2.0-alt5
- fix NUMLOCKX_STATUS setting
- set numlock status 'client' as default
- add restriction parameters for user's resources
- implement ENABLE_PRINTING restriction
- implement ENABLE_SHARING restriction
- implement ENABLE_SMARTCARD restriction
- added .gitlab-ci.yml
- 1.2.0-alt4
- added support for pcscd forwarding
- (gitlab-ci): enable for master branch

* Thu Feb 08 2018 Pavel Vainerman <pv@altlinux.ru> 1.2.0-alt4
- implement smartcard authorization command for rx-etersoft (eterbug #12027)
- add $AUTH_MODE into nxnode-login command line
- add pause for non-slave mode
- fix NUMLOCKX_STATUS setting
- set numlock status 'client' as default
- add restriction parameters for user's resources
- implement ENABLE_PRINTING restriction
- implement ENABLE_SHARING restriction
- implement ENABLE_SMARTCARD restriction
- added .gitlab-ci.yml

* Mon Nov 13 2017 Pavel Vainerman <pv@altlinux.ru> 1.2.0-alt3
- remove require for nxssh

* Thu Nov 09 2017 Pavel Vainerman <pv@altlinux.ru> 1.2.0-alt2
- fixed NXVERSION for nxloadconfig

* Wed Nov 08 2017 Pavel Vainerman <pv@altlinux.ru> 1.2.0-alt1
- new release (nx + nxssh)

* Mon Oct 16 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt4
- drop foomatic requires (eterbug #12003), still recommended
- pack missed /var/lib/nxserver

* Mon Dec 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt3
- nxprint: skip hangup on empty list, fix linked dirs
- nxdialog: fix spaces strings comparing
- nxdialog: drop NXCLIENT

* Mon Dec 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt2
- add LXDE/MATE support
- add rsa and ed25519 keys
- fix -pi using: -i not for pipe

* Sat Dec 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- add environment variable PCSCLITE_CSOCK_NAME
- nxserver: move up server_get_params
- add pcscd sharing functionality

* Fri Nov 29 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt8
- changed the way cupsd is launched (eterbug #9555)
- nxnode: fix check cups-files.conf presence

* Thu Oct 03 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt7
- remove PidFile for CUPS (eterbug #9490)

* Tue Oct 01 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt6
- workaround for uid/gid issues with broken mount.cifs (eter bug #9542)

* Mon Aug 05 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt5
- nxredir: fix preloading
- nxnode: do not exit if license if missed (eterbug #9262)

* Wed Jul 31 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt4
- add logic for numlockx status "client"
- edit message about license, drop exit if no license (eterbug #9262)
- nx-terminate-suspend now executes in /bin/bash

* Fri Apr 26 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt3
- nx-terminate-suspend: now use config variables from conf.d/07-misc.conf

* Tue Apr 23 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt2
- nxnode: fix license message (eterbug #9262)

* Tue Apr 23 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- change place of kill wineserver
- add initial license checking (eterbug #9262)

* Mon Feb 18 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt17
- use introduced macro from rpm-build-intro 1.7.25
- rename freenx-server to rx-etersoft dir

* Mon Feb 18 2013 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt16
- use _libexecdir instead _prefix/lib

* Wed Jan 23 2013 Denis Baranov <baraka@altlinux.ru> 1.1.2-alt15
- add parametr ENABLE_CUPS_DIALOG for disable

* Tue Dec 25 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt14
- nx-terminate-suspend: fix for remove obsoleted sessions
- nx-terminate-suspend: fix for handle empty files
- nxnode: fix title

* Sat Dec 15 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt13
- nxnode: add fixme for xdmcp
- commands: remove wine reqs

* Sat Dec 15 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt12
- fix run scripts, add scripts for 1c80, 1c81
- add rx-missed-command and use it

* Thu Dec 13 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt11
- add support for run commands from /etc/nxagent/commands
- add run1c77, run1c82 scripts for example
- add detect for terminal Terminal
- possible add support for XFCE item in opennx
- add cron entry for nx-terminate-supend
- move SESSION_TTL param to conf.d/07-misc.conf

* Thu Dec 13 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt10
- rename service name to rx-etersoft
- rxsetup: more print to the screen, add print items, check cupsd server only if exists

* Fri Dec 07 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt9
- update buildreqs
- spec: really fix set version from package version
- replace FreeNX with RX@Etersoft
- remove redirect to commercial nomachine server support
- rxsetup: add nxsetup --test run
- nxloadconfig: test KDE_PRINTRC only under user, and disable ENABLE_KDE_CUPS by default

* Thu Dec 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt8
- rxsetup: run restorecon if possible (eterbug #7462)
- rxsetup: add docmd for illustrate commands
- set actual versions for RX and NX backend

* Thu Dec 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt7
- cleanup spec, update and fix requires, remove fonts dir linking code (eterbug #7265)
- move /etc/init.d/freenx-server.outformat to /usr/share/misc (eterbug #8381)
- nxsmb: run nxredir instead duplicated code, use nxloadconfig for get PATH_LIB
- rename /etc/sysconfig/freenx-server to /etc/sysconfig/rx-etersoft
- rename _libdir/freenx-server to _libdir/rx-etersoft

* Wed Dec 05 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt6
- move terminate-suspend-nx.sh to /usr/sbin/nx-terminate-suspend
- remove obsoleted files (from /usr/share/freenx-server too)
- install nxcheckload.sample as nxcheckload

* Tue Dec 04 2012 Denis Baranov <baraka@altlinux.ru> 1.1.2-alt5
- kill wineserver on terminate from session

* Tue Nov 20 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt4
- add autodetect CUPS_ETC and remove 99-altlinux.conf
- drop using ENABLE_AUTORECONNECT_BEFORE_140, ENABLE_1_5_0_BACKEND
- remove SAMBA_MOUNT_SHARE_PROTOCOL, COMMAND_SMBMOUNT/COMMAND_SMBUMOUNT using
- node: always use //127.0.0.1 for remote share (eterbug #8841)
- use autodetect for DEFAULT_X_SESSION
- move autodetect to nxloadconfig, remove unneeded params from config

* Mon Nov 19 2012 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt3
- remove detect NX_BACKEND_VERSION - drop using strings command and drop binutils requires
- sudoers.conf: use NXUSERS var instead USERS
- add detect for COMMAND_SMBUMOUNT_CIFS, fix checking
- remove COMMAND_SMBMOUNT/SMBUMOUNT
- rewrite sudomount_enable checking
- move passwd arg to the end of the cmdline
- remove KDE4_ENABLE and COMMAND_START_KDE4 support
- add detect for COMMAND_START_GNOME
- set startxfce4 as default for all COMMAND_START
- add requires setxkbmap

* Fri Jun 01 2012 Denis Baranov <baraka@altlinux.ru> 1.1.2-alt2
- fix spec

* Fri Jun 01 2012 Denis Baranov <baraka@altlinux.ru> 1.1.2-alt1
- add clean old know_host
- add requires setxkbmap
- change syscups printername to
- cosmetology code formating
- eNABLE_CUPS_SERVER_MODE for ipp + download ppds
- fix CUPS_SERVER export
- fixes ps output format errors
- fix remount printers
- more logs when printer mount
- revert "Add message..." - ideology epicfail
- reverting fast kill of suspend
- some stderr to /dev/null

* Fri Oct 21 2011 Denis Baranov <baraka@altlinux.ru> 1.1.1-alt13
- add nx-3.5.0 version in check function (eterbug #7728)

* Thu Sep 01 2011 Denis Baranov <baraka@altlinux.ru> 1.1.1-alt12
- fix requires

* Thu Aug 04 2011 Denis Baranov <baraka@altlinux.ru> 1.1.1-alt11
- add start kill suspend script every 10 min
- move sudo settings to sudoers.d folder

* Fri Jan 14 2011 Denis Baranov <baraka@etersoft.ru> 1.1.1-alt10
- Fix error with zenity
- Add message when folder not mount

* Thu Jan 06 2011 Denis Baranov <baraka@etersoft.ru> 1.1.1-alt9
- rxsetup: add check for expect
- fix error on mount folder with empty password
- fix rxsetup log path
- nxnode: logging is a little faster
- fix endless cycle in node_start_applications()
- new algorithm of share mounting (--smbmount)
- chg start-modes of share/printer adding
- norm_param(): check for iconv, logging switch off
- fix Makefile: add nxacl.app to
- smile acl syntax fix
- upd config to acls check
- add code&configs to acls check

* Thu Dec 16 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt8
- cleanup spec
- change SMB_MOUNT_OPTIONS again, change links to unixforum.org
- converting smb/cifs resurce-names
- fix check_remote_printer()
- fix for kde4 (merge with git.alt)
- fix node_umount_smb()
- new code to ENABLE_SHARE_MULTIMOUNT=1 or
- nxlog tunning
- rxsetup: disable direct dependency to /etc/init.d (missed on ALT)
- rxsetup write output into log
- update sudoers.conf

* Tue Oct 12 2010 Denis Baranov <baraka@etersoft.ru> 1.1.1-alt7
- load config files from node.conf.d/ only *.conf

* Mon Oct 11 2010 Denis Baranov <baraka@etersoft.ru> 1.1.1-alt6
- add autodetect KDE4 by default in conf
- clean node.conf, all values must be override from /etc/nxserver/node.conf.d/*.conf

* Thu Oct 07 2010 Denis Baranov <baraka@etersoft.ru> 1.1.1-alt5
- change COMMAND_MD5SUM on md5sum
- add in config default DPI=96 (eterbug#6112)

* Thu Oct 07 2010 Denis Baranov <baraka@etersoft.ru> 1.1.1-alt4
- fix build requeries

* Fri Oct 01 2010 Denis Baranov <baraka@etersoft.ru> 1.1.1-alt3
- fix requeries

* Fri Jul 30 2010 Denis Baranov <baraka@etersoft.ru> 1.1.1-alt2
- add support zenity for dialog interface
- add requires zenity

* Mon Jul 26 2010 Denis Baranov <baraka@etersoft.ru> 1.1.1-alt1
- release RX@Etersoft 1.1.1

* Sun Jul 25 2010 Boris Savelev <boris@altlinux.org> 0.7.4-alt24
- fix printer forwarding (thx to dimbor and unixforum)
- nxlog now always return '0'

* Mon Jul 12 2010 Boris Savelev <boris@altlinux.org> 0.7.4-alt23
- fix double slashes in nxsmb and nxredir (thx to dimbor)

* Sun Jul 11 2010 Boris Savelev <boris@altlinux.org> 0.7.4-alt22
- Added rxsetup script
- Fixed config replacement
- fix restore session after suspend (eterbug #5704)
- do not source /etc/X11/profile.d/* in freenx Xsession

* Sun Feb 14 2010 Boris Savelev <boris@altlinux.org> 0.7.4-alt21
- move default config set to %_datadir/nxserver/node.conf.d.
  All values must be override from /etc/nxserver/node.conf
  and /etc/nxserver/node.conf.d

* Sun Jan 31 2010 Boris Savelev <boris@altlinux.org> 0.7.4-alt20.1
- fix defaults for all
- add 100-altlinux.conf with ALTLinux defaults

* Sun Jan 31 2010 Boris Savelev <boris@altlinux.org> 0.7.4-alt20
- move all config values form node.conf to %_sysconfdir/nxserver/node.conf.d/*.conf

* Sun Jan 03 2010 Boris Savelev <boris@altlinux.org> 0.7.4-alt19.7
- fix permission on /tmp/.X11-unix after creating (fix eter#4653)

* Sun Jan 03 2010 Boris Savelev <boris@altlinux.org> 0.7.4-alt19.6
- fix NETCAT_COMMAND running (fix eter#3818)
- add additional config for profile including during node startup ('on' by default)

* Tue Dec 29 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt19.5
- fix COMMAND_START_GNOME for ALTLinux (fix eter#4725)
- don't start numlockx during session startup by default. Add additional config for numlockx

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt19.4.1
- Rebuilt with python 2.6

* Fri Nov 20 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt19.4
- disable terminate-suspend-nx.sh cron task by default

* Thu Nov 12 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt19.3
- add Requires schedutils for ALT-system (fix eter#4421)
- add cron-script for terminate suspended sessions (fix eter#4436)

* Wed Oct 07 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt19.2
- fix perm on nxserver sudo config (closes: #21860)

* Tue Oct 06 2009 Vitaly Lipatov <lav@altlinux.ru> 0.7.4-alt19.1
- fix mount-additional.conf packing

* Wed Sep 30 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt19
- add patch for Server mode CUPS
  and SMB per-user share mount (from dimbor)

* Tue Sep 22 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18.12
- fix CUPSLogLevel config parser

* Thu Jul 30 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18.11
- fix restoring suspended sessions

* Wed Jul 29 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18.10
- fix new bash regexp syntax

* Wed Jul 29 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18.9
- fix new bash regexp syntax

* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18.8
- add patch from Mario Becroft (increase nxserver work speed)

* Mon Jul 27 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18.7
- increase timeout for hangup session

* Tue Jul 21 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18.6
- fix typo in nxnode

* Tue Jul 21 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18.5
- fix typo in nxnode. Affected non-ALT systems

* Tue Jul 14 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18.4
- add additional conf for mount share and CUPS

* Sat Jun 13 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18.3
- xrdb merge /etc/X11/Xresources on startup

* Tue Jun 09 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18.2
- use %_bindir/xvt if possible for ALT (ALT#20381)

* Sat Jun 06 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18.1
- add requires Xdialog (ALT#20325)

* Sat Apr 11 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt18
- include patch from Jeffrey J. Kosowsky for CUPS

* Thu Apr 09 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt17
- 2 small fixes
- move fixkeyboard and etc to /etc/nxserver

* Tue Mar 10 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt16.1
- fix COMMAND_SMBMOUNT redifines

* Tue Mar 10 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt16
- build with for new nx

* Sat Mar 07 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt15
- force umount
- merge with teambzr upstream

* Fri Feb 27 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt14
- fix export CUPS_SERVER with Win-client

* Thu Feb 26 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt13
- don't use Xsession for start desktop

* Wed Feb 25 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt12
- move libnxredir to %%_libdir/%name
- check for first run in init-script

* Wed Feb 25 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt11
- add bungle for fixkeyboard
- fix perm on libnxredir (hack, will be fixed soon)

* Sun Feb 22 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt10
- logrotate rule.
- add LSB header.
- patches from Ubuntu.
- implementation of guest login.
- nx-session-launcher:
    + add DBUS rules
    + fix permission on nx-session-launcher-suid
    + add README for nx-session-launcher

* Fri Feb 20 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt9
- fix nxloadconfig for Etersoft SHARE_FAST_MOUNT

* Thu Feb 19 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt8
- fix eterbug #3226 (patch from horch)
- add sleeping wait for valid display (fixkeyboard fails)

* Thu Jan 08 2009 Boris Savelev <boris@altlinux.org> 0.7.4-alt7
- fix path to cups backends on x86_64 (alt bug #18462)
- fix path to LOCKDIR on Debian (eter bug #3094)

* Tue Dec 16 2008 Boris Savelev <boris@altlinux.org> 0.7.4-alt6
- fix path to cups
- run "numlockx on" on session start

* Sun Nov 23 2008 Boris Savelev <boris@altlinux.org> 0.7.4-alt5
- fix permission on nx homedir

* Sat Nov 22 2008 Boris Savelev <boris@altlinux.org> 0.7.4-alt4
- add support nx 3.3

* Tue Nov 11 2008 Boris Savelev <boris@altlinux.org> 0.7.4-alt3
- add /var/lib/nxserver

* Fri Sep 05 2008 Boris Savelev <boris@altlinux.org> 0.7.4-alt2
- Fixed non-encrypted session mode. You might need to set EXTERNAL_PROXY_IP in node.conf.

* Thu Aug 28 2008 Boris Savelev <boris@altlinux.org> 0.7.4-alt1
- Opened the 0.7.4 development.
- Fixed missing export of NX_ETC_DIR in Makefile, so node.conf.sample is installed correctly.
- Fixed broken round-robin load balance algorithm.
- Fixed --terminate|--suspend|--force-terminate for load balancing case.
- Fixed --terminate|--suspend|--force-terminate for usermode case.

* Sat Aug 23 2008 Boris Savelev <boris@altlinux.org> 0.7.3-alt3
- Changed type for external agents to windows-helper or vnc-helper so that those sessions can be mirrored / shadowed as well.
- Added nxshadowacl.sample component to be able to shadow foreign sessions.
- Prepared shadowing foreign users for VNC-shadowing.
- Added shadow support to --listsession command.
- Added shadow mode as nxagent target.
- Fixed shadow mode and made it usable.

* Mon Aug 18 2008 Boris Savelev <boris@altlinux.org> 0.7.3-alt2
- Build from git
- Finally checked for all service ports. (cups, media, samba) and also checked it on the host where the load balancing actually leads to.
- Fixed broken fallback logic if SSH_CLIENT variables cannot be read correctly.
- Overhauled the usermode:
- There are now two modes of operation.
- One statically setting the ENABLE_USERMODE_AUTHENTICATION key in node.conf. (old behavior)
- Or using nxserver-usermode as startup binary, which directly goes into the 103 stage.
- Fixed using commandline parameters like --cleanup for static usermode.
- Enabled the root commandline parameters in usermode.
- Fixed usage of "nx" user as normal user in usermode.
- Disabled slave mode and load balancing for usermode.
- Fixed creation of the logfile directory.
- Fixed nxnode usage of SSH_CLIENT using fallback mechanism.
- Added disabled nxserver-suid wrapper with help from Google. To enable it uncomment the suid_install target in Makefile.
- Automatically disabled slave mode, when load balancing is activated.
- Made ENABLE_SLAVE_MODE="1" the new default as its faster and more reliable. If you encounter any problems with it, disable it in node.conf.

* Mon Aug 11 2008 Boris Savelev <boris@altlinux.org> 0.7.3-alt1
- svn update to r565
- fix x86_64 build

* Tue Jul 15 2008 Boris Savelev <boris@altlinux.org> 0.7.2-alt2
- svn update to r546

* Fri Jun 13 2008 Boris Savelev <boris@altlinux.org> 0.7.2-alt1
- new version
- fix altbug #16049
- new init-script

* Mon Jan 14 2008 Igor Zubkov <icesik@altlinux.org> 0.7.2-alt5.r430
- fix path for libXrender

* Sun Jan 06 2008 Igor Zubkov <icesik@altlinux.org> 0.7.2-alt4.r430
- fix font path (#13830)

* Thu Jan 03 2008 Igor Zubkov <icesik@altlinux.org> 0.7.2-alt3.r430
- update from svn

* Fri Dec 28 2007 Igor Zubkov <icesik@altlinux.org> 0.7.2-alt2.r427
- mark %_sysconfdir/nxserver/node.conf a config(noreplace)
- own %_sysconfdir/nxserver dir
- add requires nx

* Mon Dec 24 2007 Igor Zubkov <icesik@altlinux.org> 0.7.2-alt1.r427
- build for Sisyphus

