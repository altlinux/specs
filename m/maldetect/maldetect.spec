# TODO: use special user
Name: maldetect
Version: 1.4.2
Release: alt1

Summary: inux Malware Detect (LMD) is a malware scanner for Linux 

License: GPLv2
Group: File tools
Url: http://www.rfxn.com/projects/linux-malware-detect/

BuildArch: noarch

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: http://www.rfxn.com/downloads/%name-%version.tar.gz
Source: %name-%version.tar

%define maldetdir /var/lib/%name

Provides: maldet = %version-%release

# manually removed: rpm-build-python3 ruby ruby-stdlibs
# Automatically added by buildreq on Sun Sep 22 2013 (-bi)
# optimized out: ed python-base python3 python3-base
BuildRequires: mailx

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
%__subst "s|/usr/local/maldetect|%maldetdir|g" files/{maldet,ignore_paths,inotify/tlog,conf.maldet,*.pl}
%__subst "s|/usr/local/maldetect/maldet|maldet|g" files/modsec.sh
%__subst "s|/usr/local/lmd_update|/tmp/lmd_update|g" files/maldet
# unsupported
%__subst "s|/scripts/suspendacct|$disabled_scripts_suspendacct|g" files/maldet

%install
mkdir -p %buildroot%_sbindir/
mkdir -p %buildroot%maldetdir/
cp -pR files/* %buildroot%maldetdir/
mv %buildroot%maldetdir/maldet %buildroot%_sbindir/
ln -s maldet %buildroot%_sbindir/lmd
rm -rf %buildroot%maldetdir/inotify/*inotify*

mkdir -p %buildroot/%_sysconfdir/%name/
mv %buildroot%maldetdir/conf.maldet %buildroot/%_sysconfdir/%name/
ln -s %_sysconfdir/%name/conf.maldet %buildroot%maldetdir/conf.maldet

#cp $inspath/inotify/libinotifytools.so.0 /usr/lib/

mkdir -p %buildroot/etc/cron.daily/
cat <<EOF >%buildroot/etc/cron.daily/maldet
#!/bin/sh

MALDIR=%maldetdir

# clear quarantine/session/tmp data every 14 days
/usr/sbin/tmpwatch 336 $MALDIR/tmp >> /dev/null 2>&1
/usr/sbin/tmpwatch 336 $MALDIR/sess >> /dev/null 2>&1
/usr/sbin/tmpwatch 336 $MALDIR/quarantine >> /dev/null 2>&1
/usr/sbin/tmpwatch 336 $MALDIR/pub/*/ >> /dev/null 2>&1

# check for new definition set
#%_sbindir/maldet -u >> /dev/null 2>&1

# scan the last 2 days of file changes
# note! use ? instead *
#%_sbindir/maldet -r /home/?/www 2 >> /dev/null 2>&1
EOF

%files
%doc CHANGELOG README
%config(noreplace) %attr (0755, root, root) %_sysconfdir/%name/conf.maldet
%config(noreplace) %attr (0755, root, root) %_sysconfdir/cron.daily/maldet
%_sbindir/maldet
%_sbindir/lmd
%maldetdir/

%changelog
* Tue Oct 08 2013 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- new version 1.4.2 (with rpmrb script)

* Sun Sep 22 2013 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- initial build for ALT Linux Sisyphus

