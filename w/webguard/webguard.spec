%define auditwriter audit-writer
%define _with_audit_writer 0
%set_verify_elf_method none

Name:       webguard
Version:    1.9
Release:    alt1

Summary:    Web-guard system core
License:    non-exclusive
Group:      Security/Networking

Packager:   Lenar Shakirov <snejok@altlinux.org>

BuildRequires:  libpq, libmemcached, libjson-glib, libmemcached-devel, libfcgi, glib2-devel
Requires:       libpq, memcached, libmemcached, glib2, libjson-glib, glibc-core, glibc-pthread, libfcgi

Source0:        %name-%version.tar.gz
Source1:        acl_loader_agentd.init

%if %_with_audit_writer
Source2:        %auditwriter-%version.tar.gz
Source3:        audit_writer_agentd.init
%endif

Conflicts:      webguard-debug

ExclusiveArch:  x86_64 %ix86

%ifarch x86_64
%define dir_arch 64bit
%endif
%ifarch %ix86
%define dir_arch 32bit
%endif

%description
The product is a software data protection designed to protect against unauthorized access to the Web-server queuing system. The product is responsible for the authentication and authorization of users, and makes registration of user activity in the system (audit), filtering HTTP-user requests.
Web-guard system is designed for external differentiation of user rights in the application due to:
* restricting access the WEB resources for WEB-applications.


%package devel
Summary:    WebGard development header files
Group:      Security/Networking
Requires:   webguard == 1.9

%description devel
The webguard-devel package contains the header files needed to compile applications which will directly interact with a WebGard system. You need to install this package if you want to develop applications which will interact with a WebGard system.


%prep
%setup

%install
install -d %buildroot%_bindir
cp -r %dir_arch%_bindir/* %buildroot%_bindir

install -d %buildroot%_libdir
cp -r %dir_arch%_libdir/* %buildroot%_libdir

install -d %buildroot%_sysconfdir/%name
cp -r conf/* %buildroot%_sysconfdir/%name

install -pD -m755 %SOURCE1 %buildroot%_initdir/acl_loader_agentd

%if %_with_audit_writer
tar xvzf %SOURCE2
install -p -d -m755 %buildroot%_datadir/%name/%auditwriter
cp -r %auditwriter-%version/%dir_arch/* %buildroot%_datadir/%name/%auditwriter

install -pD -m755 %SOURCE3 %buildroot%_initdir/audit_writer_agentd
%endif


install -d %buildroot%_includedir
cp -r %dir_arch%_includedir/* %buildroot%_includedir

%post
%post_service acl_loader_agentd
%if %_with_audit_writer
%post_service audit_writer_agentd
%endif

echo "NOTE: before using webguard please make sure service memcached is running. If it is not, start it with the following command:"
echo "service memcached start"
echo "NOTE: before using WebGard please start acl_loader with the following command:"
echo "service acl_loader_agentd start"
%if %_with_audit_writer
echo "and " %auditwriter ":"
echo "service audit_writer_agentd start"
%endif

%preun
%preun_service acl_loader_agentd
%if %_with_audit_writer
%preun_service audit_writer_agentd
%endif

%files
#%doc LICENSE CHANGES README DOC
%_initrddir/acl_loader_agentd
%_bindir/acl_loader
%_bindir/wgstats
%_libdir/%name/
%config(noreplace) %_sysconfdir/%name/
# audit-writer
%if %_with_audit_writer
%_initrddir/audit_writer_agentd
%attr(2755,root,root) %_datadir/%name/%auditwriter/bin/auditWriter
%ifarch x86_64
%attr(2755,root,root) %_datadir/%name/%auditwriter/bin/wrapper-linux-x86-64
%endif
%ifarch %ix86
%attr(2755,root,root) %_datadir/%name/%auditwriter/bin/wrapper-linux-x86-32
%endif
%_datadir/%name/
%endif

%files devel
%_includedir/acl_loader/
%_includedir/libwebguard-audit/
%_includedir/libwebguard-cachewriter/
%_includedir/libwebguard-urlauth/
%_includedir/libwebguard-logger/
%_includedir/libwebguard-fcgisrv/
%_includedir/libwebguard-utils/

%_pkgconfigdir/%name.pc

%changelog
* Fri Oct 17 2014 Lenar Shakirov <snejok@altlinux.org> 1.9-alt1
- added webguard.pc file
- removed filtering SQL-queries.
- added acl_loader and audit-writer services.
- added devel-package.
* Thu Dec 12 2013 Lenar Shakirov <snejok@altlinux.org> 1.3-alt1
- initial build for ALT Linux Sisyphus
