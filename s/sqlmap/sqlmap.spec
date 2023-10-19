Name: sqlmap
Version: 1.5.3
Release: alt1.1

Summary: Automatic SQL injection and database takeover tool

Group: Monitoring
License: GPLv2
Url: http://sqlmap.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/sqlmapproject/sqlmap/archive/%version.tar.gz
Source: %name-%version.tar

# Remove dependency on distutils
Patch: 69900a6c6efac5c8b43fcee5d8d03dc2afb063b5.patch

BuildArch: noarch

BuildPreReq: rpm-build-intro

BuildRequires: perl-Net-RawIP perl-NetPacket
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-paste

%add_python3_lib_path %_datadir/%name
%add_python3_req_skip thirdparty.six.moves
%add_findprov_skiplist %_datadir/%name/extra/*
%add_findprov_skiplist %_datadir/%name/lib/*
%add_findprov_skiplist %_datadir/%name/plugins/*
%add_findprov_skiplist %_datadir/%name/tamper/*
%add_findprov_skiplist %_datadir/%name/thirdparty/*

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
%patch -p1
%remove_repo_info
find . -type f -and -name '*.py' -exec sed -i "s|#!%_bindir/env python2\?\$|#!%__python3|" {} \;
%__subst "s|#!/usr/bin/env python$|#!%__python3|" sqlmap.py sqlmapapi.py

# remove obsoleted bundled modules
%__subst "s|thirdparty.chardet|chardet|" lib/{core,request}/*.py
rm -rfv thirdparty/{xdot,chardet}

%install
install -d -m 755 %buildroot%_datadir/%name
install -m 755 sqlmap.py %buildroot%_datadir/%name
install -m 755 sqlmapapi.py %buildroot%_datadir/%name
cp -pr data %buildroot%_datadir/%name/
cp -pr extra %buildroot%_datadir/%name/
rm -rfv %buildroot%_datadir/%name/extra/runcmd/
rm -rfv %buildroot%_datadir/%name/extra/shutils/
cp -pr lib %buildroot%_datadir/%name/
cp -pr plugins %buildroot%_datadir/%name/
cp -pr tamper %buildroot%_datadir/%name/
cp -pr thirdparty %buildroot%_datadir/%name/

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
* Thu Oct 19 2023 Grigory Ustinov <grenka@altlinux.org> 1.5.3-alt1.1
- NMU: dropped dependency on distutils.

* Wed Mar 31 2021 Pavel Nakonechnyi <zorg@altlinux.org> 1.5.3-alt1
- new version (1.5.3) with rpmgs script
- do not pack runcmd
- skip finding provides in (some) sqlmap' scripts

* Mon Jul 27 2020 Pavel Nakonechnyi <zorg@altlinux.org> 1.4.7-alt1
- new version 1.4.7

* Fri Jan 31 2020 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- new version 1.4 (with rpmrb script)
- cleanup build, switch to python3

* Sun Oct 06 2019 Pavel Nakonechnyi <zorg@altlinux.org> 1.3.10-alt1
- new version 1.3.10

* Fri Aug 02 2019 Pavel Nakonechnyi <zorg@altlinux.org> 1.3.7-alt1
- new version 1.3.7

* Mon Apr 15 2019 Pavel Nakonechnyi <zorg@altlinux.org> 1.3.4-alt2
- fix shebang removal to support versioned python call

* Sun Apr 14 2019 Pavel Nakonechnyi <zorg@altlinux.org> 1.3.4-alt1
- new version 1.3.4

* Sat Feb 16 2019 Pavel Nakonechnyi <zorg@altlinux.org> 1.3.2-alt1
- new version 1.3.2

* Fri Dec 14 2018 Pavel Nakonechnyi <zorg@altlinux.org> 1.2.12-alt1
- new version 1.2.12

* Sat Sep 15 2018 Pavel Nakonechnyi <zorg@altlinux.org> 1.2.9-alt1
- new version 1.2.9

* Sat Jul 28 2018 Pavel Nakonechnyi <zorg@altlinux.org> 1.2.7-alt1
- new version 1.2.7

* Sat Jun 16 2018 Pavel Nakonechnyi <zorg@altlinux.org> 1.2.6-alt1
- new version 1.2.6

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

