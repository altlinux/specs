%define user _proxysql

Summary: A high-performance MySQL proxy
Name: proxysql
Version: 1.4.11
Release: alt1%ubt
License: GPLv3+
Group: Databases
Url: http://www.proxysql.com

Source: %name-%version.tar
Source1: proxysql.init
Source2: proxysql.service
Source3: proxysql.tmpfiles
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires: gcc-c++ cmake flex patch
BuildRequires: libpcre-devel libpcrecpp-devel
BuildRequires: libjemalloc-devel
BuildRequires: libuuid-devel
BuildRequires: libssl-devel
BuildRequires: libstdc++-devel
BuildRequires: zlib-devel liblzma-devel liblz4-devel
BuildRequires: libsqlite3-devel
BuildRequires: libconfig-devel libconfig-c++-devel
BuildRequires: libdaemon-devel
BuildRequires: libcurl-devel

%description
%summary

%prep
%setup
%patch -p1
rm -rf deps/{libconfig,libdaemon,sqlite3,curl,libjemalloc,pcre}

%build
#sed -i -e 's/c++11/c++0x/' lib/Makefile
#sed -i -e 's/c++11/c++0x/' src/Makefile
#export CFLAGS="-I%_includedir/jemalloc -I%_includedir/pcre"
export CXXFLAGS=$CFLAGS
export CPPFLAGS=$CXXFLAGS
%make_build

%install
mkdir -p %buildroot{%_bindir,%_sbindir,%_sysconfdir,%_initdir,%_unitdir,%_tmpfilesdir}
mkdir -p %buildroot{%_localstatedir,%_runtimedir,%_logdir}/%name
install -m 0755 src/proxysql %buildroot%_sbindir
install -m 0640 etc/proxysql.cnf %buildroot%_sysconfdir
install -m 0755 %SOURCE1 %buildroot%_initdir/%name
install -m 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -m 0644 %SOURCE3 %buildroot%_tmpfilesdir/%name.conf

%pre
/usr/sbin/groupadd -r -f %user
/usr/sbin/useradd -r -g %user -d %_localstatedir/%name -s /dev/null -c "ProxySQL" -n %user >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc doc LICENSE README.md FAQ.md RUNNING.md
%attr(0640,root,%user) %config(noreplace) %_sysconfdir/%name.cnf
%_sbindir/proxysql
%_initdir/%name
%_unitdir/%name.service
%_tmpfilesdir/%name.conf
%attr(3770,root,%user) %dir %_localstatedir/%name
%attr(0775,root,%user) %dir %_runtimedir/%name
#%attr(3770,root,%user) %dir %_logdir/%name

%changelog
* Thu Sep 13 2018 Alexey Shabalin <shaba@altlinux.org> 1.4.11-alt1%ubt
- 1.4.11
- build with system libconfig, libdaemon, sqlite3, curl, jemalloc, pcre

* Mon Sep 11 2017 Alexey Shabalin <shaba@altlinux.ru> 1.4.2-alt1%ubt
- 1.4.2
- delete files from percona proxysql-admin-tool project

* Fri Jul 28 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.8-alt1%ubt
- 1.3.8

* Fri May 12 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.6-alt1%ubt
- 1.3.6

* Fri Apr 21 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.5-alt1
- 1.3.5

* Thu Mar 02 2017 Alexey Shabalin <shaba@altlinux.ru> 1.3.4-alt1
- Initial build
