%define username _mysqlproxy

Name: mysql-proxy
Version: 0.8.2
Release: alt1.1

Summary: MySQL Proxy
License: GPLv2
Group: Databases

Url: http://forge.mysql.com/wiki/MySQL_Proxy
Source0: http://mysql.infocom.ua/Downloads/MySQL-Proxy/mysql-proxy-%version.tar.gz
Source1: mysql-proxy.init
Source2: mysql-proxy.sysconfig
Source3: mysql-proxy.conf
Source4: admin-1.lua

Patch1: mysql-proxy-installexamples.patch
Patch2: mysql-proxy-0.8.2-alt-DSO.patch

# Automatically added by buildreq on Wed Jun 15 2011
BuildRequires: MySQL-client flex glib2-devel libevent-devel liblua5-devel libmysqlclient-devel

%description
MySQL Proxy is a simple program that sits between your client and MySQL
server(s) that can monitor, analyze or transform their communication. Its
flexibility allows for unlimited uses; common ones include: load balancing;
failover; query analysis; query filtering and modification; and many more.

%prep
%setup
%patch1 -p1
%patch2 -p2

%build
# Upstream does not care about 64-bit library path, so fix it:
subst 's/g_build_filename(base_dir, "lib"/g_build_filename(base_dir, "%_lib"/g' src/chassis-frontend.c
subst 's/g_build_filename(srv->base_dir, "lib"/g_build_filename(srv->base_dir, "%_lib"/g' src/chassis-frontend.c

%autoreconf
%configure
%make_build

%install
%makeinstall_std

install -pD -m755 %SOURCE1 %buildroot%_initdir/mysql-proxy
install -pD -m644 %SOURCE2 %buildroot/etc/sysconfig/mysql-proxy

install -d %buildroot/var/log/mysql-proxy
install -d %buildroot%_datadir/mysql-proxy

install -d %buildroot%_sysconfdir/%name
cp -a %SOURCE3 %buildroot%_sysconfdir/%name/%name.conf

# upstream, please install daemons to %_sbindir!
install -d %buildroot%_sbindir
mv %buildroot{%_bindir,%_sbindir}/mysql-proxy

# move noarch data to %_datadir
install -d %buildroot%_datadir/%name/lua
mv %buildroot{%_libdir,%_datadir}/%name/lua/proxy
mv %buildroot{%_libdir,%_datadir}/%name/lua/examples
mv %buildroot{%_libdir,%_datadir}/%name/lua/admin.lua

cp -a %SOURCE4 %buildroot%_datadir/%name/lua/proxy

# -devel is not really needed, kill
rm -rf %buildroot%_includedir
rm -rf %buildroot%_libdir/libmysql-*.{la,so}
rm -rf %buildroot%_pkgconfigdir

%pre
%_sbindir/groupadd -r -f %username &>/dev/null
%_sbindir/useradd -r -g %username -d %_libdir/mysql-proxy -s /dev/null \
        -c "MySQL Proxy pseudouser" -M -n %username &>/dev/null ||:

%post
%post_service mysql-proxy

%preun
%preun_service mysql-proxy

%files
%_initdir/mysql-proxy
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/mysql-proxy
%config(noreplace) %attr(640,root,root) %verify(not md5 mtime size) /etc/mysql-proxy/mysql-proxy.conf
%_sbindir/mysql-proxy
%_bindir/*
%_libdir/libmysql-*
%_libdir/mysql-proxy
%exclude %_libdir/mysql-proxy/lua/*.la
%exclude %_libdir/mysql-proxy/plugins/*.la
%_datadir/mysql-proxy
%attr(750,root,%username) %dir /var/log/mysql-proxy

%changelog
* Thu Jul 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.2-alt1.1
- Fixed build

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 0.8.2-alt1
- 0.8.2

* Wed Jun 15 2011 Victor Forsiuk <force@altlinux.org> 0.7.2-alt2
- Rebuild with libevent2.

* Wed Nov 25 2009 Victor Forsyuk <force@altlinux.org> 0.7.2-alt1
- 0.7.2
- Refresh build requirements.
- Create subdir in /var/run when init-script run to handle situation
  of "gone" subdir (such as /var/run on temporarily filesystem).

* Tue Mar 18 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.6.1-alt1
- Initial build for ALT Linux based on PLD specfile.
