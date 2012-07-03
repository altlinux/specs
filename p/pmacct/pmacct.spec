Name: pmacct
Version: 0.14.0
Release: alt3.rc3
License: GPLv2
Summary: pcap-based accounting tools
Group: System/Servers
Url: http://www.pmacct.net
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Source: http://www.pmacct.net/%name-%version.tar
Patch: %name-%version-%release.patch

PreReq: %name-storage = %version-%release 
Requires: %name-common = %version-%release

BuildRequires: zlib-devel libpcap-devel libMySQL-devel postgresql-devel libsqlite3-devel

%description
pcap-based accounting daemon; it gathers packets from an
interface it is bound to (enabling optionally Promiscuous
mode); statistics may be either pushed to stdout, stored
in a memory table or a PostgreSQL/MySQL/SQLite database.

%package common
Summary: Common files for %name, nfacct, sfacct
Group: System/Servers
BuildArch: noarch

%description common
Common files for %name, nfacct, sfacct

%package full
Summary: pcap-based accounting daemon for store data in PostgreSQL/MySQL/SQLite
Group: System/Servers
Provides: %name-storage = %version-%release

%description full
pcap-based accounting daemon; it gathers packets from an
interface it is bound to (enabling optionally Promiscuous
mode); statistics may be either pushed to stdout, stored
in a memory table or a PostgreSQL/MySQL/SQLite database.

%package mysql
Summary: pcap-based accounting daemon for store data in MySQL
Group: System/Servers
Provides: %name-storage = %version-%release

%description mysql
pcap-based accounting daemon; it gathers packets from an
interface it is bound to (enabling optionally Promiscuous
mode); statistics may be either pushed to stdout, stored
in a memory table or a MySQL database.

%package pgsql
Summary: pcap-based accounting daemon for store data in PostgreSQL
Group: System/Servers
Provides: %name-storage = %version-%release

%description pgsql
pcap-based accounting daemon; it gathers packets from an
interface it is bound to (enabling optionally Promiscuous
mode); statistics may be either pushed to stdout, stored
in a memory table or a PostgreSQL database.

%package sqlite3
Summary: pcap-based accounting daemon for store data in SQLit
Group: System/Servers
Provides: %name-storage = %version-%release

%description sqlite3
pcap-based accounting daemon; it gathers packets from an
interface it is bound to (enabling optionally Promiscuous
mode); statistics may be either pushed to stdout, stored
in a memory table or a SQLite database.

# nfacct
%package -n nfacct
Summary: NetFlow accounting tools
Group: System/Servers
BuildArch: noarch
PreReq: nfacct-storage = %version-%release
Requires: %name-common = %version-%release

%description -n nfacct
NetFlow accounting daemon; it listens for NetFlow packets
v1/v5/v7/v8/v9 on one or more interfaces (IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a PostgreSQL/MySQL/SQLite database.

%package -n nfacct-full
Summary: NetFlow accounting daemon for store data in PostgreSQL/MySQL/SQLite
Group: System/Servers
Provides: nfacct-storage = %version-%release

%description -n nfacct-full
NetFlow accounting daemon; it listens for NetFlow packets
v1/v5/v7/v8/v9 on one or more interfaces (IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a PostgreSQL/MySQL/SQLite database.

%package -n nfacct-mysql
Summary: NetFlow accounting daemon for store data in MySQL
Group: System/Servers
Provides: nfacct-storage = %version-%release

%description -n nfacct-mysql
NetFlow accounting daemon; it listens for NetFlow packets
v1/v5/v7/v8/v9 on one or more interfaces (IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a MySQL database.

%package -n nfacct-pgsql
Summary: NetFlow accounting daemon for store data in PostgreSQL
Group: System/Servers
Provides: nfacct-storage = %version-%release

%description -n nfacct-pgsql
NetFlow accounting daemon; it listens for NetFlow packets
v1/v5/v7/v8/v9 on one or more interfaces (IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a PostgreSQL database.

%package -n nfacct-sqlite3
Summary: NetFlow accounting daemon for store data in SQLite
Group: System/Servers
Provides: nfacct-storage = %version-%release

%description -n nfacct-sqlite3
NetFlow accounting daemon; it listens for NetFlow packets
v1/v5/v7/v8/v9 on one or more interfaces (IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a SQLite database.

# sfacct
%package -n sfacct
Summary: sFlow accounting tools
Group: System/Servers
BuildArch: noarch
PreReq: sfacct-storage = %version-%release
Requires: %name-common = %version-%release

%description -n sfacct
sFlow accounting daemon; it listens for sFlow packets v2,
and v5 on one or more interfaces (both IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a PostgreSQL/MySQL/SQLite database.

%package -n sfacct-full
Summary: sFlow accounting daemon for store data in PostgreSQL/MySQL/SQLite
Group: System/Servers
Provides: sfacct-storage = %version-%release

%description -n sfacct-full
sFlow accounting daemon; it listens for sFlow packets v2,
and v5 on one or more interfaces (both IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a PostgreSQL/MySQL/SQLite database.

%package -n sfacct-mysql
Summary: sFlow accounting daemon for store data in MySQL
Group: System/Servers
Provides: sfacct-storage = %version-%release

%description -n sfacct-mysql
sFlow accounting daemon; it listens for sFlow packets v2,
and v5 on one or more interfaces (both IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a MySQL database.

%package -n sfacct-pgsql
Summary: sFlow accounting daemon for store data in PostgreSQL
Group: System/Servers
Provides: sfacct-storage = %version-%release

%description -n sfacct-pgsql
sFlow accounting daemon; it listens for sFlow packets v2,
and v5 on one or more interfaces (both IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a PostgreSQL database.

%package -n sfacct-sqlite3
Summary: sFlow accounting daemon for store data in SQLite
Group: System/Servers
Provides: sfacct-storage = %version-%release

%description -n sfacct-sqlite3
sFlow accounting daemon; it listens for sFlow packets v2,
and v5 on one or more interfaces (both IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a SQLite database.


# uacct
%package -n uacct
Summary: ULOG accounting tools
Group: System/Servers
BuildArch: noarch
PreReq: uacct-storage = %version-%release
Requires: %name-common = %version-%release

%description -n uacct
ULOG accounting daemon; it listens for ULOG packets
on one or more interfaces (both IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a PostgreSQL/MySQL/SQLite database.

%package -n uacct-full
Summary: ULOG accounting daemon for store data in PostgreSQL/MySQL/SQLite
Group: System/Servers
Provides: uacct-storage = %version-%release

%description -n uacct-full
ULOG accounting daemon; it listens for ULOG packets,
on one or more interfaces (both IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a PostgreSQL/MySQL/SQLite database.

%package -n uacct-mysql
Summary: ULOG accounting daemon for store data in MySQL
Group: System/Servers
Provides: uacct-storage = %version-%release

%description -n uacct-mysql
ULOG accounting daemon; it listens for ULOG packets
on one or more interfaces (both IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a MySQL database.


%package -n uacct-pgsql
Summary: ULOG accounting daemon for store data in PostgreSQL
Group: System/Servers
Provides: uacct-storage = %version-%release

%description -n uacct-pgsql
ULOG accounting daemon; it listens for ULOG packets
on one or more interfaces (both IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a PostgreSQL database.

%package -n uacct-sqlite3
Summary: ULOG accounting daemon for store data in SQLite
Group: System/Servers
Provides: uacct-storage = %version-%release

%description -n uacct-sqlite3
ULOG accounting daemon; it listens for sFlow packets
on one or more interfaces (both IPv4 and IPv6);
statistics may be either pushed to stdout, stored in a
memory table or a SQLite database.

%prep
%setup -q -n %name-%version
%patch -p1

%build
#autoreconf
%define common_opts \\\
	--with-pgsql-includes=%_includedir/pgsql \\\
	--enable-64bit \\\
	--enable-threads \\\
	--enable-ulog

%configure \
	%common_opts \
	--enable-mysql \
	--disable-pgsql \
	--disable-sqlite3
%make

mv src/pmacct src/pmacct-mysql
mv src/pmacctd src/pmacctd-mysql
mv src/nfacctd src/nfacctd-mysql
mv src/sfacctd src/sfacctd-mysql
mv src/uacctd src/uacctd-mysql

%make clean
#autoreconf
%configure \
	%common_opts \
	--disable-mysql \
	--enable-pgsql \
	--disable-sqlite3
%make

mv src/pmacct src/pmacct-pgsql
mv src/pmacctd src/pmacctd-pgsql
mv src/nfacctd src/nfacctd-pgsql
mv src/sfacctd src/sfacctd-pgsql
mv src/uacctd src/uacctd-pgsql

%make clean
#autoreconf
%configure \
	%common_opts \
	--disable-mysql \
	--disable-pgsql \
	--enable-sqlite3
%make

mv src/pmacct src/pmacct-sqlite3
mv src/pmacctd src/pmacctd-sqlite3
mv src/nfacctd src/nfacctd-sqlite3
mv src/sfacctd src/sfacctd-sqlite3
mv src/uacctd src/uacctd-sqlite3

%make clean
#autoreconf
%configure \
	%common_opts \
	--enable-mysql \
	--enable-pgsql \
	--enable-sqlite3
%make

%install
%makeinstall
for suf in mysql pgsql sqlite3; do
%__install -p -m 755 src/pmacct-$suf  %buildroot%_bindir/pmacct-$suf
%__install -p -m 755 src/pmacctd-$suf  %buildroot%_sbindir/pmacctd-$suf
%__install -p -m 755 src/nfacctd-$suf  %buildroot%_sbindir/nfacctd-$suf
%__install -p -m 755 src/sfacctd-$suf  %buildroot%_sbindir/sfacctd-$suf
%__install -p -m 755 src/uacctd-$suf  %buildroot%_sbindir/uacctd-$suf
done

mv %buildroot%_bindir/pmacct %buildroot%_bindir/pmacct-full
mv %buildroot%_sbindir/pmacctd %buildroot%_sbindir/pmacctd-full
mv %buildroot%_sbindir/nfacctd %buildroot%_sbindir/nfacctd-full
mv %buildroot%_sbindir/sfacctd %buildroot%_sbindir/sfacctd-full
mv %buildroot%_sbindir/uacctd %buildroot%_sbindir/uacctd-full

%__mkdir_p %buildroot%_initrddir
%__mkdir_p %buildroot%_sysconfdir/%name
%__mkdir_p %buildroot%_datadir/%name/
%__mkdir_p %buildroot/var/lib/pmacct

%__install -p -m 640 examples/nfacctd-print.conf.example %buildroot%_sysconfdir/%name/nfacctd.conf
%__install -p -m 640 examples/nfacctd-print.conf.example %buildroot%_sysconfdir/%name/sfacctd.conf
%__install -p -m 640 pmacctd.conf %buildroot%_sysconfdir/%name/pmacctd.conf
%__install -p -m 640 pmacctd.conf %buildroot%_sysconfdir/%name/uacctd.conf
%__install -p -m 755 pmacctd  %buildroot%_initrddir/pmacctd
%__install -p -m 755 nfacctd  %buildroot%_initrddir/nfacctd
%__install -p -m 755 sfacctd  %buildroot%_initrddir/sfacctd
%__install -p -m 755 uacctd  %buildroot%_initrddir/uacctd
cp -a sql/* %buildroot%_datadir/%name/

%__mkdir_p %buildroot%_datadir/doc/pmacct-%version
%__mkdir_p %buildroot%_datadir/doc/nfacct-%version
%__mkdir_p %buildroot%_datadir/doc/sfacct-%version
%__mkdir_p %buildroot%_datadir/doc/uacct-%version

ln -sf %_datadir/%name %buildroot%_datadir/doc/pmacct-%version/sql
ln -sf %_datadir/%name %buildroot%_datadir/doc/nfacct-%version/sql
ln -sf %_datadir/%name %buildroot%_datadir/doc/sfacct-%version/sql
ln -sf %_datadir/%name %buildroot%_datadir/doc/uacct-%version/sql

ln -sf %_datadir/doc/%name-common-%version/examples %buildroot%_datadir/doc/pmacct-%version/examples
ln -sf %_datadir/doc/%name-common-%version/examples %buildroot%_datadir/doc/nfacct-%version/examples
ln -sf %_datadir/doc/%name-common-%version/examples %buildroot%_datadir/doc/sfacct-%version/examples
ln -sf %_datadir/doc/%name-common-%version/examples %buildroot%_datadir/doc/uacct-%version/examples

#Make alternatives
%__mkdir_p %buildroot%_altdir
cat > %buildroot%_altdir/%name-mysql <<__EOF__
/usr/sbin/pmacctd /usr/sbin/pmacctd-mysql	40
/usr/bin/pmacct /usr/bin/pmacct-mysql	40
__EOF__
cat > %buildroot%_altdir/%name-pgsql <<__EOF__
/usr/sbin/pmacctd /usr/sbin/pmacctd-pgsql	30
/usr/bin/pmacct /usr/bin/pmacct-pgsql	30
__EOF__
cat > %buildroot%_altdir/%name-sqlite3 <<__EOF__
/usr/sbin/pmacctd /usr/sbin/pmacctd-sqlite3	20
/usr/bin/pmacct /usr/bin/pmacct-sqlite3	20
__EOF__
cat > %buildroot%_altdir/%name-full <<__EOF__
/usr/sbin/pmacctd /usr/sbin/pmacctd-full	10
/usr/bin/pmacct /usr/bin/pmacct-full	10
__EOF__

cat > %buildroot%_altdir/nfacct-mysql <<__EOF__
/usr/sbin/nfacctd /usr/sbin/nfacctd-mysql	40
__EOF__
cat > %buildroot%_altdir/nfacct-pgsql <<__EOF__
/usr/sbin/nfacctd /usr/sbin/nfacctd-pgsql	30
__EOF__
cat > %buildroot%_altdir/nfacct-sqlite3 <<__EOF__
/usr/sbin/nfacctd /usr/sbin/nfacctd-sqlite3	20
__EOF__
cat > %buildroot%_altdir/nfacct-full <<__EOF__
/usr/sbin/nfacctd /usr/sbin/nfacctd-full	10
__EOF__

cat > %buildroot%_altdir/sfacct-mysql <<__EOF__
/usr/sbin/sfacctd /usr/sbin/sfacctd-mysql	40
__EOF__
cat > %buildroot%_altdir/sfacct-pgsql <<__EOF__
/usr/sbin/sfacctd /usr/sbin/sfacctd-pgsql	30
__EOF__
cat > %buildroot%_altdir/sfacct-sqlite3 <<__EOF__
/usr/sbin/sfacctd /usr/sbin/sfacctd-sqlite3	20
__EOF__
cat > %buildroot%_altdir/sfacct-full <<__EOF__
/usr/sbin/sfacctd /usr/sbin/sfacctd-full	10
__EOF__

cat > %buildroot%_altdir/uacct-mysql <<__EOF__
/usr/sbin/uacctd /usr/sbin/uacctd-mysql	40
__EOF__
cat > %buildroot%_altdir/uacct-pgsql <<__EOF__
/usr/sbin/uacctd /usr/sbin/uacctd-pgsql	30
__EOF__
cat > %buildroot%_altdir/uacct-sqlite3 <<__EOF__
/usr/sbin/uacctd /usr/sbin/uacctd-sqlite3	20
__EOF__
cat > %buildroot%_altdir/uacct-full <<__EOF__
/usr/sbin/uacctd /usr/sbin/uacctd-full	10
__EOF__


%post
%post_service pmacctd
%preun
%preun_service pmacctd

%post -n nfacct
%post_service nfacctd
%preun -n nfacct
%preun_service nfacctd

%post -n sfacct
%post_service sfacctd
%preun -n sfacct
%preun_service sfacctd

%post -n uacct
%post_service uacctd
%preun -n uacct
%preun_service uacctd

%files
%_datadir/doc/pmacct-%version
%config(noreplace) %attr(0640,root,root) %_sysconfdir/pmacct/pmacctd.conf
%_initdir/pmacctd

%files common
%doc AUTHORS CONFIG-KEYS COPYING ChangeLog EXAMPLES FAQS NEWS README TODO TOOLS UPGRADE
%doc docs/* examples
%dir %_sysconfdir/pmacct
%_datadir/%name
/var/lib/pmacct

%files full
%_bindir/pmacct-full
%_sbindir/pmacctd-full
%_altdir/%name-full

%files mysql
%_bindir/pmacct-mysql
%_bindir/pmmyplay
%_sbindir/pmacctd-mysql
%_altdir/%name-mysql

%files pgsql
%_bindir/pmacct-pgsql
%_bindir/pmpgplay
%_sbindir/pmacctd-pgsql
%_altdir/%name-pgsql

%files sqlite3
%_bindir/pmacct-sqlite3
%_sbindir/pmacctd-sqlite3
%_altdir/%name-sqlite3

%files -n nfacct
%_datadir/doc/nfacct-%version
%config(noreplace) %attr(0640,root,root) %_sysconfdir/pmacct/nfacctd.conf
%_initdir/nfacctd

%files -n nfacct-full
%_sbindir/nfacctd-full
%_altdir/nfacct-full

%files -n nfacct-mysql
%_sbindir/nfacctd-mysql
%_altdir/nfacct-mysql

%files -n nfacct-pgsql
%_sbindir/nfacctd-pgsql
%_altdir/nfacct-pgsql

%files -n nfacct-sqlite3
%_sbindir/nfacctd-sqlite3
%_altdir/nfacct-sqlite3

%files -n sfacct
%_datadir/doc/sfacct-%version
%config(noreplace) %attr(0640,root,root) %_sysconfdir/pmacct/sfacctd.conf
%_initdir/sfacctd

%files -n sfacct-full
%_sbindir/sfacctd-full
%_altdir/sfacct-full

%files -n sfacct-mysql
%_sbindir/sfacctd-mysql
%_altdir/sfacct-mysql

%files -n sfacct-pgsql
%_sbindir/sfacctd-pgsql
%_altdir/sfacct-pgsql

%files -n sfacct-sqlite3
%_sbindir/sfacctd-sqlite3
%_altdir/sfacct-sqlite3

%files -n uacct
%_datadir/doc/uacct-%version
%config(noreplace) %attr(0640,root,root) %_sysconfdir/pmacct/uacctd.conf
%_initdir/uacctd

%files -n uacct-full
%_sbindir/uacctd-full
%_altdir/uacct-full

%files -n uacct-mysql
%_sbindir/uacctd-mysql
%_altdir/uacct-mysql

%files -n uacct-pgsql
%_sbindir/uacctd-pgsql
%_altdir/uacct-pgsql

%files -n uacct-sqlite3
%_sbindir/uacctd-sqlite3
%_altdir/uacct-sqlite3

%changelog
* Thu Dec 15 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.14.0-alt3.rc3
- Add --enable-ulog (#26714)

* Wed Dec 14 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.14.0-alt2.rc3
- Set BuildArch: noarch for pmacct-common, nfacct, sfacct, uacct

* Wed Dec 14 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.14.0-alt1.rc3
- New release candidate

* Sat Sep 03 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.14.0-alt1.rc2
- New release candidate

* Tue Apr 05 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.5-alt1
- New release

* Sat Nov 27 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.4-alt1
- New release

* Thu Sep 02 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.3-alt1
- New release

* Wed Apr 14 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.1-alt1
- New release

* Wed Feb 17 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.0-alt3
- New release

* Tue Jan 12 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.0-alt2.rc4
- Fix init scripts

* Sun Jan 10 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.0-alt1.rc4
- New release

* Thu Oct 29 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.0-alt1.rc3
- New release (#22174)
- Add new subpackages uacct*
- Fix stop, restart in init scripts

* Wed Sep 09 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.0-alt1.rc2
- New release
- Add subpackage pmacct-common
- Move examples to pmacct-common

* Fri Aug 21 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 0.12.0-alt1.rc1
- build for ALT
