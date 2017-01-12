Name: bind-dyndb-ldap
Version: 10.1
Release: alt2

Summary: LDAP back-end plug-in for BIND
License: %gpl2plus
Group: System/Servers

URL: https://fedorahosted.org/bind-dyndb-ldap
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: bind-devel
BuildRequires: libldap-devel
BuildRequires: libkrb5-devel
BuildRequires: libuuid-devel
BuildRequires: libsasl2-devel

Requires: bind

%define _unpackaged_files_terminate_build 1

%description
This package provides an LDAP back-end plug-in for BIND. It features
support for dynamic updates and internal caching, to lift the load
off of your LDAP server.

%prep
%setup
%patch -p1

%build
#autoreconf
%configure
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_localstatedir/bind/zone/dyndb-ldap/

%files
%_defaultdocdir/%name
%_libdir/bind/ldap.so
%dir %attr(770, root, named) %_localstatedir/bind/zone/dyndb-ldap/

%exclude %_libdir/bind/*.la

%changelog
* Wed Dec 28 2016 Mikhail Efremov <sem@altlinux.org> 10.1-alt2
- Fix spec.
- packaging typos fixed (by Sergey Bolshakov).

* Mon Nov 14 2016 Mikhail Efremov <sem@altlinux.org> 10.1-alt1
- Initial build.

