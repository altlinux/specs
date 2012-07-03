Name: sqlmap
Version: 0.9
Release: alt1

Summary: Automatic SQL injection and database takeover tool

Group: Monitoring
License: GPL
Url: http://sqlmap.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sourceforge.net/sqlmap/sqlmap-%version.tar

BuildArch: noarch

BuildPreReq: rpm-build-intro

%add_findreq_skiplist %_datadir/%name/udf/mysql/linux/*/*.so
%add_findreq_skiplist %_datadir/%name/udf/postgresql/linux/*/*/*.so
%add_verify_elf_skiplist %_datadir/%name/udf/postgresql/linux/*/*/*.so
%add_verify_elf_skiplist %_datadir/%name/udf/mysql/linux/*/*.so
%add_verify_elf_skiplist %_datadir/%name/lib/contrib/upx/linux/upx

# Automatically added by buildreq on Sat Jan 21 2012 (-bi)
# optimized out: python-base python-module-peak python-modules-compiler
BuildRequires: MySQL-client perl-Net-RawIP perl-NetPacket python-module-mwlib python-module-paste

%description
sqlmap is an open source penetration testing tool that automates the process of
detecting and exploiting SQL injection flaws and taking over of database
servers. It comes with a powerful detection engine, many niche features for the
ultimate penetration tester and a broad range of switches lasting from database
fingerprinting, over data fetching from the database, to accessing the
underlying file system and executing commands on the operating system via
out-of-band connections.

%prep
%setup -n sqlmap
%remove_repo_info
# Drop shebang from non-executable python files
find . -type f -and -name '*.py' -and ! -executable -exec  sed -i "sa#!%_bindir/env pythonaa" {} \;
# Dro non-Linux stuff
rm -rf lib/contrib/upx/macosx
rm -rf lib/contrib/upx/windows
rm -rf udf/mysql/windows
rm -rf udf/postgresql/windows

%install
install -d -m 755 %buildroot%_datadir/%name
install -m 755 sqlmap.py %buildroot%_datadir/%name
cp -pr extra %buildroot%_datadir/%name
cp -pr lib %buildroot%_datadir/%name
cp -pr plugins %buildroot%_datadir/%name
cp -pr shell %buildroot%_datadir/%name
cp -pr txt %buildroot%_datadir/%name
cp -pr udf %buildroot%_datadir/%name
cp -pr xml %buildroot%_datadir/%name

install -d -m 755 %buildroot%_bindir
cat > %buildroot%_bindir/sqlmap <<EOF
#!/bin/sh
cd %_datadir/%name
exec ./sqlmap.py \$@
EOF
chmod +x %buildroot%_bindir/sqlmap

install -d -m 755 %buildroot%_sysconfdir
install -m 644 sqlmap.conf %buildroot%_sysconfdir
pushd %buildroot%_datadir/%name
ln -s ../../..%_sysconfdir/sqlmap.conf .
popd

%files
%doc doc/*
%_datadir/%name
%_bindir/%name
%config(noreplace) %_sysconfdir/%name.conf

%changelog
* Fri Jan 20 2012 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- initial build for ALT Linux Sisyphus (thanks, Mandriva!)

* Tue Dec 27 2011 Denis Silakov <dsilakov@mandriva.org> 0.9-2
+ Revision: 745518
- drop non-linux files, fix launcher

* Thu Jul 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-1
+ Revision: 689092
- import sqlmap

