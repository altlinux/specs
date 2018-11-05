Name: openvz-etersoft
Version: 0.2
Release: alt2

Summary: Etersoft's collection of OpenVZ additional utilities

Group: System/Servers
License: GPLv3

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

ExclusiveArch: x86_64

%description
Etersoft's collection of OpenVZ additional utilities.
Contains:
 - vzclone
 - vzfirewall (see http://habrahabr.ru/blogs/sysadm/87764/)
 - vzmem (see http://habrahabr.ru/blogs/sysadm/125979/)
 - vzset
 - vzenter (see http://dklab.ru/lib/dklab_vzenter/)
 - vzfailcnt (see https://github.com/DmitryKoterov/vzfailcnt)

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
install -m755 vzfailcnt/vzfailcnt %buildroot%_sbindir/
ln -s vzenter %buildroot%_sbindir/e

cp vzfailcnt/README.txt README.vzfailcnt
cp vzset/README README.vzset
cp vzmem/README README.vzmem
cp vzfirewall/README README.vzfirewall
cp vzenter/README README.vzenter
mkdir -p %buildroot/etc/
install -m755 vzfailcnt/vzfailcnt.conf %buildroot/etc/

%files
%doc vzfailcnt/vzfailcntcron
%doc README.vzfailcnt README.vzset README.vzmem README.vzfirewall README.vzenter
/etc/vzfailcnt.conf
%_sbindir/vzclone
%_sbindir/vzfirewall
%_sbindir/vzfailcnt
%_sbindir/vzmem
%_sbindir/vzset
%_sbindir/vzenter
%_sbindir/e

%changelog
* Mon Nov 05 2018 Alexey Shabalin <shaba@altlinux.org> 0.2-alt2
- build for x86_64 only

* Sat Nov 21 2015 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- add vzfailcnt
- add READMEs

* Fri Nov 21 2014 Danil Mikhailov <danil@altlinux.org> 0.1-alt2
- fixed vzclone, added start old ve and private dir creation

* Wed Sep 28 2011 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
