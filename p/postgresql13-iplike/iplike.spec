%define pg_ver 13
%define prog_name iplike

Name: postgresql%pg_ver-%prog_name
Version: 2.3.0
Release: alt1
License: GPL
Group: Databases
Summary: PostgreSQL complex IP Address text field query
Source: %prog_name-%version.tar.gz
URL: http://www.opennms.org

# Automatically added by buildreq on Thu Jun 21 2007
#BuildRequires: gcc-c++ postgresql%pg_ver-server-devel
BuildRequires: postgresql%pg_ver-server-devel

Requires: postgresql%pg_ver-server

%description
PostgreSQL function for doing complex IP address queries
on a text field.

%prep
%setup -n %prog_name-%version

%build
%autoreconf
%configure --with-pgsql=%_bindir/pg_server_config
%make

%install
%makeinstall_std

%post
echo "Execute the following psql command inside any database that you want to install or update:"
echo "CREATE OR REPLACE FUNCTION iplike(i_ipaddress text,i_rule text) RETURNS bool AS '$$libdir/iplike.so' LANGUAGE 'c' RETURNS NULL ON NULL INPUT;"
%files
%_libdir/pgsql/*.so

%changelog
* Wed Nov 23 2022 Alexei Takaseev <taf@altlinux.org> 2.3.0-alt1
- Version 2.3.0
- Use server depended pg_server_config for build

* Mon Sep 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.6-alt1
- Version 2.0.6

* Fri May 13 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.2-alt1
- 2.0.2

* Mon Feb 28 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.0-alt1
- 2.0.0

* Wed Jul 21 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.9-alt1
- 1.0.9
- Remove packages-info-i18n-common from BuildRequires

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.8-alt3
- Remmove depricated ldconfig call in post

* Wed Oct 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.8-alt2
- Change to Pg 8.3

* Sun Aug 03 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.8-alt1
- 1.0.8

* Sat Mar 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.7-alt1
- 1.0.7

* Thu Jun 21 2007 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.5-alt1
- Update for Sisyphus
