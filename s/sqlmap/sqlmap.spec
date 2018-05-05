Name: sqlmap
Version: 1.2.5
Release: alt1

Summary: Automatic SQL injection and database takeover tool

Group: Monitoring
License: GPL
Url: http://sqlmap.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/sqlmapproject/sqlmap/archive/%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildPreReq: rpm-build-intro

%add_findreq_skiplist %_datadir/%name/udf/mysql/linux/*/*.so
%add_findreq_skiplist %_datadir/%name/udf/postgresql/linux/*/*/*.so
%add_verify_elf_skiplist %_datadir/%name/udf/postgresql/linux/*/*/*.so
%add_verify_elf_skiplist %_datadir/%name/udf/mysql/linux/*/*.so

# Automatically added by buildreq on Sat Jan 21 2012 (-bi)
# optimized out: python-base python-module-peak python-modules-compiler
BuildRequires: perl-Net-RawIP perl-NetPacket python-module-paste

%description
sqlmap is an open source penetration testing tool that automates the process of
detecting and exploiting SQL injection flaws and taking over of database
servers. It comes with a powerful detection engine, many niche features for the
ultimate penetration tester and a broad range of switches lasting from database
fingerprinting, over data fetching from the database, to accessing the
underlying file system and executing commands on the operating system via
out-of-band connections.

%prep
%setup
%remove_repo_info
# Drop shebang from non-executable python files
find . -type f -and -name '*.py' -and ! -executable -exec  sed -i "sa#!%_bindir/env pythonaa" {} \;

%install
install -d -m 755 %buildroot%_datadir/%name
install -m 755 sqlmap.py %buildroot%_datadir/%name
install -m 755 sqlmapapi.py %buildroot%_datadir/%name
cp -pr extra %buildroot%_datadir/%name/
cp -pr lib %buildroot%_datadir/%name/
cp -pr plugins %buildroot%_datadir/%name/
cp -pr procs %buildroot%_datadir/%name/
cp -pr shell %buildroot%_datadir/%name/
cp -pr tamper %buildroot%_datadir/%name/
cp -pr thirdparty %buildroot%_datadir/%name/
cp -pr txt %buildroot%_datadir/%name/
cp -pr udf %buildroot%_datadir/%name/
cp -pr waf %buildroot%_datadir/%name/
cp -pr xml %buildroot%_datadir/%name/

install -d -m 755 %buildroot%_bindir
for app in sqlmap sqlmapapi; do
cat > %buildroot%_bindir/$app <<EOF
#!/bin/sh
cd %_datadir/%name
exec ./$app.py \$@
EOF
chmod +x %buildroot%_bindir/$app
done

install -d -m 755 %buildroot%_sysconfdir
install -m 644 sqlmap.conf %buildroot%_sysconfdir
pushd %buildroot%_datadir/%name
ln -s ../../..%_sysconfdir/sqlmap.conf .
popd

%files
%doc doc/*
%_datadir/%name
%_bindir/%name
%_bindir/%{name}api
%config(noreplace) %_sysconfdir/%name.conf

%changelog
* Sat May 05 2018 Pavel Nakonechnyi <zorg@altlinux.org> 1.2.5-alt1
- new version 1.2.5

* Sun Apr 08 2018 Pavel Nakonechnyi <zorg@altlinux.org> 1.2.4-alt1
- new version 1.2.4

* Sun Oct 29 2017 Pavel Nakonechnyi <zorg@altlinux.org> 1.1.10-alt1
- new version 1.1.10

* Sat Sep 02 2017 Pavel Nakonechnyi <zorg@altlinux.org> 1.1.9-alt1
- new version 1.1.9

* Mon Jun 05 2017 Pavel Nakonechnyi <zorg@altlinux.org> 1.1.6-alt1
- new version 1.1.6

* Sun May 14 2017 Pavel Nakonechnyi <zorg@altlinux.org> 1.1.5-alt1
- new version 1.1.5

* Sat Apr 08 2017 Pavel Nakonechnyi <zorg@altlinux.org> 1.1.4-alt1
- new version 1.1.4

* Sat Apr 01 2017 Pavel Nakonechnyi <zorg@altlinux.org> 1.1.3-alt1
- new version 1.1.3
- return "non-Linux stuff" as it is executed on target system
- include sqlmapapi

* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- new version 1.0 (with rpmrb script)

* Fri Jan 20 2012 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva!)

* Tue Dec 27 2011 Denis Silakov <dsilakov@mandriva.org> 0.9-2
+ Revision: 745518
- drop non-linux files, fix launcher

* Thu Jul 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-1
+ Revision: 689092
- import sqlmap

