%define auditwriter audit-writer

Name:		webguard
Version:	1.3
Release:	alt1

Summary:	Web-guard system core
License:	non-exclusive
Group:		Security/Networking

Packager: Lenar Shakirov <snejok@altlinux.org>

BuildRequires: libpq, libmemcached, libjson-glib, libmemcached-devel
Requires: libpq, memcached, libmemcached, glib2, libjson-glib

Source0:	%name-%version.tar.gz

ExclusiveArch: x86_64 %ix86

%ifarch x86_64
%define dir_arch 64bit
%endif
%ifarch %ix86
%define dir_arch 32bit
%endif

%description
The product is a software data protection designed to protect against unauthorized access to the Web-server queuing system. The product is responsible for the authentication and authorization of users, and makes registration of user activity in the system (audit), filtering HTPP-, SQL- user requests.
Web-guard system is designed for external differentiation of user rights in the application due to:
* restricting access the WEB resources for WEB-applications;
* restricting access the database using SQL-queries;
* restricting access when calling stored procedures in the database.

%prep
%setup

%install

cd %dir_arch

install -d %buildroot%_bindir
cp usr/bin/acl_loader %buildroot%_bindir/acl_loader

install -d %buildroot%_includedir
cp -r usr/include/* %buildroot%_includedir

cd -

install -d %buildroot%_libdir
cp -r %dir_arch%_libdir/* %buildroot%_libdir

install -d %buildroot%_sysconfdir/%name
cp conf/aclloader.conf %buildroot%_sysconfdir/%name/aclloader.conf
cp conf/url.conf %buildroot%_sysconfdir/%name/url.conf
cp conf/sql.conf %buildroot%_sysconfdir/%name/sql.conf
install -p -d -m 0755 %buildroot%_datadir/%name/%auditwriter
cp -r %auditwriter %buildroot%_datadir/%name

%post
echo "NOTE: before using webguard please make sure service memcached is running. If it is not, start it with the following command:"
echo "service memcached start"
echo "NOTE:" %auditwriter "is located in" %buildroot%_datadir/%name

%files
#%doc LICENSE CHANGES README DOC
%_bindir/acl_loader
%_includedir/acl_loader/acl_loader_plugin.h
%_includedir/libaudit/audit.h
%_includedir/libcachewriter/cachewriter.h
%exclude %_includedir/libchecksign/checksign.h
%_includedir/libpostgresplugin/postgres_plugin.h
%_includedir/libsqlauth/sqlaudit.h
%_includedir/libsqlauth/sqlauth.h
%_includedir/libsqlauth/sqlauth_types.h
%_includedir/liburlauth/urlauth.h
%_includedir/liburlauth/urlauthdata.h
%_includedir/liburlauth/urlauthstr.h
%_includedir/logger/logger.h
%_libdir/libaudit.so
%_libdir/libcachewriter.so
#%_libdir/libchecksign.so
%_libdir/libpostgresplugin.so
%_libdir/libsqlauth.so
%_libdir/liburlauth.so
%config(noreplace) %_sysconfdir/%name/aclloader.conf
%config(noreplace) %_sysconfdir/%name/url.conf
%config(noreplace) %_sysconfdir/%name/sql.conf
%_datadir/%name/%auditwriter/*


%changelog
* Thu Dec 12 2013 Lenar Shakirov <snejok@altlinux.org> 1.3-alt1
- initial build for ALT Linux Sisyphus
