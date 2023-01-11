%filter_from_requires /^\/usr\/bin\/view/d
%filter_from_requires /^\/usr\/bin\/scan/d

# TODO: use special user
Name: maldetect
Version: 1.6.4
Release: alt1

Summary: Linux Malware Detect (LMD) is a malware scanner for Linux

License: GPLv2
Group: File tools
Url: http://www.rfxn.com/projects/linux-malware-detect/

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

#Source-url: http://www.rfxn.com/downloads/%name-%version.tar.gz
# Source-url: http://www.rfxn.com/downloads/%name-current.tar.gz
Source: %name-%version.tar

%define maldetdir /var/lib/%name

Provides: maldet = %version-%release
Obsoletes: maldet < %EVR

# Automatically added by buildreq on Sun Sep 22 2013 (-bi)
# optimized out: ed python-base python3 python3-base
BuildRequires: mailx rpm-build-intro

AutoReq: no
Requires: stmpclean crontabs bash coreutils grep gzip sed util-linux

%description
Linux Malware Detect (LMD) is a malware scanner for Linux released under the GNU GPLv2 license,
that is designed around the threats faced in shared hosted environments.
It uses threat data from network edge intrusion detection systems
to extract malware that is actively being used in attacks
and generates signatures for detection.
In addition, threat data is also derived from user submissions
with the LMD checkout feature and from malware community resources.
The signatures that LMD uses are MD5 file hashes and HEX pattern matches,
they are also easily exported to any number of detection tools such as ClamAV.

See also http://habrahabr.ru/post/194346/

%prep
%setup
%__subst "s|/usr/local/maldetect|%maldetdir|g" files/{maldet,hookscan.sh,ignore_paths,internals/tlog,conf.maldet,internals/*.pl,internals/*.conf,service/maldet.sysconfig}
%__subst "s|/usr/local/maldetect/maldet|maldet|g" files/modsec.sh
%__subst "s|/usr/local/sbin/maldet|%_sbindir/maldet|g" files/internals/scan.etpl files/ignore_paths
%__subst "s|/usr/local/lmd_update|/tmp/lmd_update|g" files/maldet
# unsupported
%__subst "s|/scripts/suspendacct|$disabled_scripts_suspendacct|g" files/maldet files/internals/functions

%install
mkdir -p %buildroot%_sbindir/
mkdir -p %buildroot%_man1dir/
mkdir -p %buildroot%maldetdir/
cp -pR files/* %buildroot%maldetdir/
mv %buildroot%maldetdir/maldet %buildroot%_sbindir/
mv %buildroot%maldetdir/maldet.1 %buildroot%_man1dir/
ln -s maldet %buildroot%_sbindir/lmd
rm -f %buildroot%maldetdir/uninstall.sh

# TODO: restore service and inotify?
rm -rf %buildroot%maldetdir/service/
rm -rf %buildroot%maldetdir/inotify/*inotify*

mkdir -p %buildroot/%_sysconfdir/%name/
mv %buildroot%maldetdir/conf.maldet %buildroot/%_sysconfdir/%name/
ln -s %_sysconfdir/%name/conf.maldet %buildroot%maldetdir/conf.maldet

install -m644 -D files/service/maldet.sysconfig %buildroot%_sysconfigdir/maldet


mkdir -p %buildroot/etc/cron.daily/
cat <<EOF >%buildroot/etc/cron.daily/maldet
#!/bin/sh

MALDIR=%maldetdir

# clear quarantine/session/tmp data every 14 days
/usr/sbin/tmpwatch 336 \$MALDIR/tmp >> /dev/null 2>&1
/usr/sbin/tmpwatch 336 \$MALDIR/sess >> /dev/null 2>&1
/usr/sbin/tmpwatch 336 \$MALDIR/quarantine >> /dev/null 2>&1
/usr/sbin/tmpwatch 336 \$MALDIR/pub/*/ >> /dev/null 2>&1

# check for new definition set
#%_sbindir/maldet -u >> /dev/null 2>&1

# scan the last 2 days of file changes
# note! use ? instead *
#%_sbindir/maldet -r /home/?/www 2 >> /dev/null 2>&1
EOF
chmod 0755 %buildroot/etc/cron.daily/maldet

%files
%doc CHANGELOG README
%dir %_sysconfdir/%name/
%config(noreplace) %_sysconfdir/%name/conf.maldet
%config(noreplace) %_sysconfdir/cron.daily/maldet
%config(noreplace) %_sysconfigdir/maldet
%_sbindir/maldet
%_sbindir/lmd
%_man1dir/*
%maldetdir/

%changelog
* Thu Aug 11 2022 Vitaly Lipatov <lav@altlinux.ru> 1.6.4-alt1
- new version 1.6.4 (with rpmrb script)
- update spec
- disable autoreq due many extra requires

* Thu Dec 10 2015 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- new version 1.5 (with rpmrb script)

* Fri Aug 14 2015 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt3
- update to real 1.4.2 version
- detection and alerting of openssl heartbleed vulnerability
- update signatures

* Thu Oct 10 2013 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt2
- fix tmpwatch dir

* Tue Oct 08 2013 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version 1.4.2 (with rpmrb script)

* Sun Sep 22 2013 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- initial build for ALT Linux Sisyphus

