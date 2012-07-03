Name: openvz-etersoft
Version: 0.1
Release: alt1

Summary: Etersoft's collection of OpenVZ additional utilities

Group: System/Servers
License: GPLv3

Source: %name-%version.tar

BuildArch: noarch

%description
Etersoft's collection of OpenVZ additional utilities.
Contains:
 - vzclone
 - vzfirewall (see http://habrahabr.ru/blogs/sysadm/87764/)
 - vzmem (see http://habrahabr.ru/blogs/sysadm/125979/)
 - vzset
 - vzenter (see http://dklab.ru/lib/dklab_vzenter/)

Thanks http://dklab.ru/

%prep
%setup

%install
mkdir -p %buildroot%_sbindir/
install -m755 vzclone/vzclone %buildroot%_sbindir/
install -m755 vzfirewall/vzfirewall %buildroot%_sbindir/
install -m755 vzmem/vzmem %buildroot%_sbindir/
install -m755 vzset/vzset %buildroot%_sbindir/
install -m755 vzenter/vzenter %buildroot%_sbindir/
ln -s vzenter %buildroot%_sbindir/e

%files
#%doc vzclone/README
%_sbindir/vzclone
%_sbindir/vzfirewall
%_sbindir/vzmem
%_sbindir/vzset
%_sbindir/vzenter
%_sbindir/e

%changelog
* Wed Sep 28 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
