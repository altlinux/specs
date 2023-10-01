Name: debmirror
Version: 2.38
Release: alt1

Summary: Debian partial mirror script, with ftp and package pool support

License: GPL
Group: Networking/Other
Url: http://packages.debian.org/sid/debmirror

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ftp.de.debian.org/debian/pool/main/d/debmirror/debmirror_%version.tar

Epoch: 1

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 17 2014 (-bi)
# optimized out: perl-Compress-Raw-Zlib perl-Encode perl-HTTP-Date perl-HTTP-Message perl-IO-Compress perl-IO-Socket-IP perl-Log-Agent perl-Pod-Escapes perl-Pod-Simple perl-Pod-Usage perl-Socket6 perl-URI perl-libnet python-base python3 python3-base
BuildRequires: perl-Digest-SHA perl-IO-Socket-INET6 perl-LockFile-Simple perl-Net-INET6Glue perl-libwww perl-podlators

%description
This program downloads and maintains a partial local Debian mirror. It can
mirror any combination of architectures, distributions and sections. Files
are transferred by ftp, http, hftp or rsync, and package pools are fully
supported. It also does locking and updates trace files.

%prep
%setup
# fix some typo in version 2.4.6
#subst 's|// ""||g' debmirror

dist=xenial
echo <<EOF > README.ALT
Download example for $dist distro:
#!/bin/sh -x
debmirror --nosource -m --passive --host=mirror.yandex.ru \
       --root=ubuntu --method=http --progress \
       --dist=$dist,$dist-security,$dist-updates,$dist-backports,$dist-proposed \
       --ignore-release-gpg --section=main,restricted,multiverse,universe \
       --arch=i386,amd64 ./download-dir

Also you can set this params in /etc/debmirror.conf (see %_sysconfdir/debmirror.conf.example)
See details here: https://help.ubuntu.com/community/Debmirror
EOF

%install
install -D -m 0755 debmirror %buildroot%_bindir/debmirror
mkdir -p %buildroot%_man1dir/
pod2man debmirror > %buildroot%_man1dir/debmirror.1
install -D -m 0644 examples/debmirror.conf %buildroot%_sysconfdir/debmirror.conf.example

%files
%doc doc/design.txt debian/changelog README.ALT
%_bindir/%name
%_sysconfdir/%name.conf.example
%_man1dir/*

%changelog
* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1:2.38-alt1
- new version 2.38 (with rpmrb script)

* Sat May 06 2023 Vitaly Lipatov <lav@altlinux.ru> 1:2.37-alt1
- new version 2.37 (with rpmrb script)

* Sat Nov 03 2018 Vitaly Lipatov <lav@altlinux.ru> 1:2.30-alt1
- new version 2.30 (with rpmrb script)

* Mon May 21 2018 Vitaly Lipatov <lav@altlinux.ru> 1:2.29-alt1
- new version 2.29 (with rpmrb script)

* Mon Apr 10 2017 Vitaly Lipatov <lav@altlinux.ru> 1:2.26-alt1
- new version 2.26 (with rpmrb script)

* Mon Feb 17 2014 Vitaly Lipatov <lav@altlinux.ru> 1:2.16-alt1
- new version 2.16 (with rpmrb script)

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 1:2.15-alt1
- new version 2.15 (with rpmrb script)

* Fri Jun 01 2012 Vitaly Lipatov <lav@altlinux.ru> 1:2.12-alt1
- new version 2.12 (with rpmrb script) (ALT bug #23693)

* Sat Oct 02 2010 Vitaly Lipatov <lav@altlinux.ru> 1:2.4.6-alt1
- new version 2.4.6 (with rpmrb script)

* Tue Jun 29 2010 Vitaly Lipatov <lav@altlinux.ru> 1:2.4.4-alt1
- new version (2.4.4) import in git (bug #23693)

* Sun May 24 2009 Vitaly Lipatov <lav@altlinux.ru> 20070123-alt1
- initial build for ALT Linux Sisyphus
