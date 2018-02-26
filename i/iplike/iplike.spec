Name: iplike
Version: 2.0.2
Release: alt1
License: GPL
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
Group: Databases
Summary: PostgreSQL complex IP Address text field query
Source: %name-%version.tar.gz
URL: http://www.opennms.org

# Automatically added by buildreq on Thu Jun 21 2007
BuildRequires: gcc-c++ postgresql-devel

%description
PostgreSQL function for doing complex IP address queries
on a text field.

%package -n lib%name
Summary: PostgreSQL complex IP Address text field query
Group: Databases
Provides: %name = %version-%release
Requires: postgresql-server

%description -n lib%name
PostgreSQL function for doing complex IP address queries
on a text field.

%prep
%setup -n %name-%version

%build
%autoreconf
%configure --libdir=%_libdir/pgsql --libexecdir=%_libdir/pgsql
%__make libdir=%_libdir/pgsql libexecdir=%_libdir/pgsql

%install
%__make DESTDIR=%buildroot libdir=%_libdir/pgsql libexecdir=%_libdir/pgsql install


%files -n lib%name
%_libdir/pgsql/iplike*so*
#_sbindir/install_iplike.sh

%changelog
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
