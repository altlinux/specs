Summary: Maui Scheduler
Name: maui
Version: 3.3
Release: alt1

License: Maui Scheduler General Public License
Group: System/Servers

Packager: Denis Pynkin <dans@altlinux.org>

URL: http://www.supercluster.org/maui/

Source: %name-%version.tar

Source100: maui.init

%define mauihome %_spooldir/%name
%define mauiuser _maui

#Source2:	setup_maui
#Source3:	maui.cfg
#Source4:	maui-joborga

# Automatically added by buildreq on Thu Aug 09 2007
BuildRequires: libnet1-devel libtorque-devel openldap-clients

%description
Maui is an advanced job scheduler for use on clusters and supercomputers.
It is a highly configurable tool capable of supporting a large array of
fairness policies, dynamic priorities, extensive reservations, and fairshare.
It is currently in use at many of the leading government and academic labs
throughtout the US and around the world.  It is running on machines ranging
from clusters of a few processors to multi-teraflop supercomputers.

"This product includes software developed for The University of New
Mexico High Performance Computing Education and Research Center for use 
in the Maui Scheduler software.  Maui Scheduler is a trademark of 
Science & Technology Corporation @ UNM"

%package -n lib%name-devel
Summary: Development package with static libs and headers
Group: Development/C
Requires: %name = %version-%release

%description -n lib%name-devel
Static libraries and header files required for compiling maui plugins.

%prep
%setup -q

#hasher/gear specific hack
%__install -d lib
%__install -d bin

%build
%configure --with-spooldir=%mauihome
%make_build

%install
%make BUILDROOT=$RPM_BUILD_ROOT install
[ "%prefix/lib" = "%_libdir" ] || mv %buildroot/%prefix/lib %buildroot/%_libdir

sed -r 's/^ADMIN1[[:space:]].*/ADMIN1 %mauiuser, root/' -i %buildroot/%mauihome/*.cfg
sed -r 's/^SERVERHOST[[:space:]].*/SERVERHOST 127.0.0.1/' -i %buildroot/%mauihome/*.cfg
sed -r 's/RMCFG\[.*/RMCFG[127.0.0.1] TYPE=PBS/' -i %buildroot/%mauihome/*.cfg

%__install -Dpm755 %SOURCE100 %buildroot%_initdir/%name


%post
%post_service %name
echo
echo 'This product includes software developed for The University of New Mexico
High Performance Computing Education and Research Center for use in the Maui
Scheduler software.  Maui Scheduler is a trademark of Science & Technology
Corporation @ UNM'
echo

%preun
%preun_service %name

%pre
/usr/sbin/groupadd -r -f %mauiuser
/usr/sbin/useradd -r -g %mauiuser -d /dev/null -s /dev/null -n %mauiuser >/dev/null 2>&1 ||:


%files
%doc docs/* LICENSE.mcompat
%_initdir/%name
%_sbindir/*
%_bindir/*
%attr(755,%mauiuser,%mauiuser) %dir %mauihome
%attr(755,%mauiuser,%mauiuser) %mauihome/spool
%attr(755,%mauiuser,%mauiuser) %mauihome/stats
%attr(755,%mauiuser,%mauiuser) %mauihome/log
%attr(755,%mauiuser,%mauiuser) %mauihome/traces
%attr(755,%mauiuser,%mauiuser) %mauihome/tools
%attr(644,%mauiuser,%mauiuser) %config(noreplace) %mauihome/*.cfg

%files -n lib%name-devel
%_libdir/*.a
%_includedir/*.h

%changelog
* Sat Feb 20 2010 Denis Pynkin <dans@altlinux.ru> 3.3-alt1
- New version

* Mon Aug 24 2009 Denis Pynkin <dans@altlinux.ru> 3.2.6p21-alt2
- fixed possible overflows
- changed packager name

* Mon Jul 20 2009 Denis Pynkin <dans@altlinux.ru> 3.2.6p21-alt1
- Version 3.2.6p21

* Thu Apr 17 2008 Denis Pynkin <dans@altlinux.ru> 3.2.6p19-alt2
- unmet: libtorque soname

* Fri Aug 10 2007 Stanislav Ievlev <inger@altlinux.org> 3.2.6p19-alt1
- 3.2.6p19

* Thu Aug 09 2007 Stanislav Ievlev <inger@altlinux.org> 3.2.6p13-alt1
- Initial release
