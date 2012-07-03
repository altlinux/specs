Name: asterisk-base
Summary: User and groups for asterisk-related packages
Version: 0.60
Release: alt1
License: GPL
Group: System/Servers
BuildArch: noarch
%add_findreq_skiplist %_initdir/asterisk
Url: http://sisyphus.ru/srpm/Sisyphus/asterisk-base
Source: %name-%version.tar.gz
Packager: Denis Smirnov <mithraen@altlinux.ru>
Conflicts: asterisk1.4 < 1.4.21.2
Conflicts: asterisk1.6 < 1.6.0-alt6.beta9
Conflicts: asterisk-sounds-en <= 1.4.12-alt1
Conflicts: asterisk-sounds-extra-en <= 1.4.5-alt3
Conflicts: asterisk-sounds-es <= 1.4.6-alt2
Conflicts: asterisk-sounds-fr <= 1.4.6-alt1
Conflicts: astmanproxy <= 1.22-alt2.pre.20061015
Requires: pbx-music-base
Requires(pre): asterisk-user

%package configs
Summary: Some essential Asterisk config files
Group: System/Servers
BuildArch: noarch
Requires(pre): asterisk-base

%description configs
Some essential Asterisk config files

%package -n asterisk-files-all
Summary: some data files for Asterisk
Group: System/Servers
Requires: asterisk-images
Requires: asterisk-keys
Requires: asterisk-firmware

%description -n asterisk-files-all
some data files for Asterisk

%package -n asterisk-firmware
Summary: images for Asterisk interface
Group: System/Servers
Requires: asterisk-base

%description -n asterisk-firmware
images for Asterisk interface

%package -n asterisk-images
Summary: images for Asterisk interface
Group: System/Servers
Requires: asterisk-base

%description -n asterisk-images
images for Asterisk interface

%package -n asterisk-initscript
Summary: Initscript for Asterisk
Group: System/Servers
BuildArch: noarch
Requires: monit-base
Requires(pre): asterisk-user

%description -n asterisk-initscript
Initscript for Asterisk

%package -n asterisk-keys
Summary: images for Asterisk interface
Group: System/Servers
Requires: asterisk-base

%description -n asterisk-keys
images for Asterisk interface

%package -n asterisk-user
Summary: User and groups for asterisk-related packages
Group: System/Servers
BuildArch: noarch
Requires(pre): shadow-utils
Requires(pre): pbx-base-user

%description -n asterisk-user
User and groups for asterisk-related packages

%package -n dahdi-udev
Summary: udev rules for Zaptel & DAHDI
Group: System/Servers
BuildArch: noarch
Conflicts: zaptel < 20071228:1.4.12.1-alt12
Requires(pre): asterisk-user

%description -n dahdi-udev
udev rules for Zaptel & DAHDI

%description
User and groups for asterisk-related packages


%prep
%setup

%install
mkdir -p \
	%buildroot%_sysconfdir/asterisk \
	%buildroot/%_datadir/asterisk/sounds
pushd asterisk-base-configs
for s in *.conf; do
    install -D -m 750 "$s" %buildroot%_sysconfdir/asterisk
done
cd udev
for s in *.rules; do
    install -D -m 644 "$s" %buildroot%_sysconfdir/udev/rules.d/$s
done
popd
mkdir -p %buildroot/usr/lib/asterisk/agi-bin
mkdir -p %buildroot/var/spool/asterisk/dictate
mkdir -p %buildroot/var/spool/asterisk/monitor
mkdir -p %buildroot/var/spool/asterisk/outgoing
mkdir -p %buildroot/var/spool/asterisk/system
mkdir -p %buildroot/var/spool/asterisk/tmp
mkdir -p %buildroot/var/log/asterisk
mkdir -p %buildroot/var/log/asterisk/cdr-csv
mkdir -p %buildroot/var/log/asterisk/cdr-custom
mkdir -p %buildroot/var/spool/asterisk
mkdir -p %buildroot/var/run/asterisk
mkdir -p %buildroot/usr/share/asterisk/firmware
mkdir -p %buildroot/usr/share/asterisk/images
mkdir -p %buildroot/usr/share/asterisk/keys
mkdir -p %buildroot/var/lib/asterisk/documentation
mkdir -p %buildroot/usr/share/asterisk/documentation
mkdir -p %buildroot/var/lib/asterisk/licenses
for s in asterisk-images/*; do
    install -m644 -D "$s" %buildroot%_datadir/asterisk/images/$s
done
for s in asterisk-keys/*; do
    install -m644 -D "$s" %buildroot%_datadir/asterisk/keys/$s
done
install -m644 -D asterisk-firmware/iaxy.bin %buildroot%_datadir/asterisk/firmware/iax/iaxy.bin
install -D -m755 asterisk-initscript/asterisk-init      %buildroot%_initdir/asterisk
install -D -m644 asterisk-initscript/asterisk-monit     %buildroot%_sysconfdir/monitrc.d/asterisk
install -D -m644 asterisk-initscript/asterisk-logrotate %buildroot%_sysconfdir/logrotate.d/asterisk
install -D -m664 asterisk-initscript/sysconfig			%buildroot%_sysconfdir/sysconfig/asterisk
install -D -m775 asterisk.filetrigger %buildroot/usr/lib/rpm/asterisk.filetrigger
install -D -m775 asterisk-base/select-asterisk %buildroot/usr/sbin/select-asterisk
mkdir -p %buildroot%_sysconfdir/modprobe.d
echo "options wct4xxp t1e1override=0xff" > %buildroot%_sysconfdir/modprobe.d/dahdi

%post -n asterisk-user
%_sbindir/groupadd -r -f _asterisk
%_sbindir/useradd -r -g _asterisk -r -c "Asterisk IP PBX" -s /dev/null -d /dev/null -n _asterisk > /dev/null 2>&1 ||:

%files
%dir %attr(0750,root,_asterisk) /usr/lib/asterisk/agi-bin
%dir %attr(2770,_asterisk,pbxadmin) %_sysconfdir/asterisk
%dir %attr(3755,root,_asterisk) %_datadir/asterisk/sounds
%dir %attr(3770,_asterisk,pbxadmin) /var/lib/asterisk
%dir %attr(3770,_asterisk,pbxadmin) /var/lib/asterisk/licenses
%dir %_datadir/asterisk
%dir %_libexecdir/asterisk
%dir %attr(3770,_asterisk,pbxadmin) /var/spool/asterisk/dictate
%dir %attr(3770,_asterisk,pbxadmin) /var/spool/asterisk/monitor
%dir %attr(3770,_asterisk,pbxadmin) /var/spool/asterisk/outgoing
%dir %attr(3770,_asterisk,pbxadmin) /var/spool/asterisk/system
%dir %attr(3770,_asterisk,pbxadmin) /var/spool/asterisk/tmp
%dir %attr(3770,_asterisk,pbxadmin) /var/log/asterisk
%dir %attr(3770,_asterisk,pbxadmin) /var/log/asterisk/cdr-csv
%dir %attr(3770,_asterisk,pbxadmin) /var/log/asterisk/cdr-custom
%dir %attr(3770,_asterisk,pbxadmin) /var/spool/asterisk
%dir %attr(3770,_asterisk,pbxadmin) /var/run/asterisk
%dir %attr(0750,_asterisk,pbxadmin) %_datadir/asterisk/firmware
%dir %attr(0750,_asterisk,pbxadmin) %_datadir/asterisk/images
%dir %attr(0750,_asterisk,pbxadmin) %_datadir/asterisk/keys
%dir %attr(0755,root,root) /var/lib/asterisk/documentation
%dir %attr(0755,root,root) /usr/share/asterisk/documentation
%attr(0755,root,root) /usr/lib/rpm/asterisk.filetrigger
%_sbindir/select-asterisk

%files configs
%config(noreplace) %attr(0664,_asterisk,pbxadmin) %_sysconfdir/asterisk/*.conf

%files -n asterisk-files-all

%files -n asterisk-firmware
%dir %_datadir/asterisk/firmware/iax
%_datadir/asterisk/firmware/iax/iaxy.bin*

%files -n asterisk-images
%_datadir/asterisk/images/*

%files -n asterisk-initscript
%_initdir/asterisk
%_sysconfdir/monitrc.d/asterisk
%_sysconfdir/logrotate.d/asterisk
%attr(0664,root,pbxadmin) %_sysconfdir/sysconfig/asterisk

%files -n asterisk-keys
%_datadir/asterisk/keys/*

%files -n asterisk-user

%files -n dahdi-udev
%_sysconfdir/udev/rules.d/00-dahdi.rules
%_sysconfdir/modprobe.d/dahdi

%changelog
* Fri Dec 23 2011 Denis Smirnov <mithraen@altlinux.ru> 0.60-alt1
- select-asterisk: run alternatives-update after select

* Tue Sep 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.59-alt1
- add /etc/modprobe.d/dahdi

* Fri Jul 22 2011 Denis Smirnov <mithraen@altlinux.ru> 0.58-alt1
- add /usr/share/asterisk/documentation

* Sun Feb 13 2011 Denis Smirnov <mithraen@altlinux.ru> 0.57-alt1
- add select-asterisk utility
- fix pbxadmin group name in initscript

* Sun Dec 26 2010 Denis Smirnov <mithraen@altlinux.ru> 0.56-alt1
- add default encoding to cdr_pgsql

* Wed Nov 17 2010 Denis Smirnov <mithraen@altlinux.ru> 0.55-alt1
- add agi-bin to asterisk-base

* Tue Nov 16 2010 Denis Smirnov <mithraen@altlinux.ru> 0.54-alt1
- asterisk-initscript: add requires to asterisk-user

* Tue Sep 14 2010 Denis Smirnov <mithraen@altlinux.ru> 0.53-alt1
- asterisk-initscript -> use bash instead of /bin/sh (for ulimit)

* Wed May 26 2010 Denis Smirnov <mithraen@altlinux.ru> 0.52-alt1
- internal_timing=yes by default

* Mon May 03 2010 Denis Smirnov <mithraen@altlinux.ru> 0.51-alt1
- add /var/lib/asterisk/licenses

* Thu Mar 25 2010 Denis Smirnov <mithraen@altlinux.ru> 0.50-alt1
- noload cdr_sqlite and cdr_radius by default

* Mon Nov 16 2009 Denis Smirnov <mithraen@altlinux.ru> 0.49-alt1
- fix dahdi requires in initscript

* Wed Nov 11 2009 Denis Smirnov <mithraen@altlinux.ru> 0.48-alt1
- enable busydetect by default

* Fri Oct 23 2009 Denis Smirnov <mithraen@altlinux.ru> 0.47-alt1
- asterisk console access for users in pbxadmin group

* Fri Oct 23 2009 Denis Smirnov <mithraen@altlinux.ru> 0.46-alt1
- fix dahdi-udev requires

* Tue Oct 13 2009 Denis Smirnov <mithraen@altlinux.ru> 0.45-alt1
- fix typo

* Mon Oct 12 2009 Denis Smirnov <mithraen@altlinux.ru> 0.44-alt1
- add rpm filetrigger

* Sun Oct 11 2009 Denis Smirnov <mithraen@altlinux.ru> 0.43-alt1
- add /etc/sysconfig/asterisk

* Sun Oct 11 2009 Denis Smirnov <mithraen@altlinux.ru> 0.42-alt1
- import asterisk-files

* Sun Oct 11 2009 Denis Smirnov <mithraen@altlinux.ru> 0.41-alt1
- import asterisk-initscript package

* Fri Oct 09 2009 Denis Smirnov <mithraen@altlinux.ru> 0.21-alt1
- move moh directory to pbx-music-base

* Wed Oct 07 2009 Denis Smirnov <mithraen@altlinux.ru> 0.20-alt1
- add /var/lib/asterisk/documentation

* Fri Sep 25 2009 Denis Smirnov <mithraen@altlinux.ru> 0.19-alt1
- change /var/lib/asterisk owner to _asterisk

* Tue Sep 22 2009 Denis Smirnov <mithraen@altlinux.ru> 0.18-alt1
- fix access to Asterisk configs

* Mon Sep 21 2009 Denis Smirnov <mithraen@altlinux.ru> 0.17-alt1
- use /var/lib/pbx/music for music on hold

* Mon Sep 21 2009 Denis Smirnov <mithraen@altlinux.ru> 0.16-alt1
- move pbxadmin group to pbx-base

* Fri Sep 18 2009 Denis Smirnov <mithraen@altlinux.ru> 0.15-alt1
- some more security changes

* Fri Sep 18 2009 Denis Smirnov <mithraen@altlinux.ru> 0.14-alt1
- include config generated by dahdi_genconf
- some security changes
- cleanup udev rules
- update Asterisk configs

* Sun Sep 13 2009 Denis Smirnov <mithraen@altlinux.ru> 0.13-alt1
- move _asterisk user creation to separate package

* Tue Sep 08 2009 Denis Smirnov <mithraen@altlinux.ru> 0.12-alt1
- not load chan_ss7.so by default

* Tue Aug 04 2009 Denis Smirnov <mithraen@altlinux.ru> 0.11-alt1
- fix build

* Tue Aug 04 2009 Denis Smirnov <mithraen@altlinux.ru> 0.10-alt1
- move more dirs from asterisk* to asterisk-base

* Thu Jul 23 2009 Denis Smirnov <mithraen@altlinux.ru> 0.9-alt1
- create dahdi-udev subpackage

* Sat Jul 04 2009 Denis Smirnov <mithraen@altlinux.ru> 0.8-alt1
- build asterisk-base and asterisk-base-configs from one srpm
- add /var/lib/asterisk and /usr/share/asterisk

* Sun Apr 26 2009 Denis Smirnov <mithraen@altlinux.ru> 0.7-alt4
- Add Url (for repocop)

* Wed Dec 10 2008 Denis Smirnov <mithraen@altlinux.ru> 0.7-alt3
- conflict to old versions asterisk1.6 (with file conflicts)

* Wed Dec 03 2008 Denis Smirnov <mithraen@altlinux.ru> 0.7-alt2
- add Packager

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.7-alt1
- cleanup specfile

* Fri Jul 25 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt1
- package %_datadir/asterisk/sounds

* Sun Apr 29 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5-alt1
- package /var/lib/asterisk/mohmp3 directory

* Tue Aug 29 2006 Denis Smirnov <mithraen@altlinux.ru> 0.4-alt1
- add SGID to %_sysconfdir/asterisk

* Wed Aug 23 2006 Denis Smirnov <mithraen@altlinux.ru> 0.3-alt1
- added %_sysconfdir/asterisk

* Fri Aug 18 2006 Denis Smirnov <mithraen@altlinux.ru> 0.2-alt1
- spec cleanup

* Sun Aug 13 2006 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- first build for Sisyphus

