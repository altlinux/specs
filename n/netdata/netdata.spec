Name: netdata
Version: 1.2.0
Release: alt1

Summary: Real-time performance monitoring, done right!

License: GPLv3+
Group: File tools
Url: http://netdata.firehol.org/

# https://github.com/firehol/netdata/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

# manually removed: python-module-google python-module-mwlib python3-dev python3-module-yieldfrom python3-module-zope ruby ruby-stdlibs 
# Automatically added by buildreq on Fri Aug 05 2016
# optimized out: perl pkg-config python-base python-modules python3 python3-base
BuildRequires: libuuid-devel zlib-devel

%if_with nfacct
BuildRequires: libmnl-devel
BuildRequires: libnetfilter_acct-devel
%endif

%add_findreq_skiplist %_libexecdir/%name/plugins.d/*.plugin

%description
netdata is the fastest way to visualize metrics. It is a resource
efficient, highly optimized system for collecting and visualizing any
type of realtime timeseries data, from CPU usage, disk activity, SQL
queries, API calls, web site visitors, etc.

netdata tries to visualize the truth of now, in its greatest detail,
so that you can get insights of what is happening now and what just
happened, on your systems and applications.

%package -n csed
Summary: Color stream substitution filter
Group: Editors
Requires: lib%name = %version-%release

%description -n csed
Color stream substitution filter

%prep
%setup

%build
%autoreconf
%configure \
	--docdir=%_docdir/%name-%version \
	--with-zlib \
	--with-math \
	%{?with_nfacct:--enable-plugin-nfacct} \
	--with-user=netdata
%make_build

%install
%makeinstall_std

mkdir -p %buildroot%_sysconfdir/%name/
install -m 644 -p system/netdata.conf %buildroot%_sysconfdir/netdata.conf

find %buildroot -name .keep | xargs rm

install -d %buildroot%_unitdir/
install -m 644 -p system/netdata.service %buildroot%_unitdir/netdata.service

%pre
getent group netdata > /dev/null || groupadd -r netdata
getent passwd netdata > /dev/null || useradd -r -g netdata -c netdata -s /sbin/nologin -d / netdata

%files
%attr(-,netdata,netdata) %dir %_localstatedir/cache/%name
%attr(-,netdata,netdata) %dir %_localstatedir/log/%name
%config(noreplace) %_sysconfdir/netdata.conf
%dir %_sysconfdir/%name/
%config(noreplace) %verify(not md5 mtime size) %_sysconfdir/%name/*.conf
%_sbindir/%name
%_unitdir/netdata.service
%dir %_libexecdir/%name/
%_libexecdir/%name/charts.d/
%_libexecdir/%name/node.d/
%_libexecdir/%name/plugins.d/
%dir %_datadir/%name

# override defattr for web files
#defattr(644,root,netdata,755)
%_datadir/%name/web

%changelog
* Thu May 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- initial build for ALT Linux Sisyphus

* Mon May 16 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.2.0-1
- netdata is now 30%% faster.
- netdata now has a registry (my-netdata menu on the dashboard).
- netdata now monitors Linux containers.
- Several more improvements, new features and bugfixes.
* Wed Apr 20 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.1.0-1
- Several new features (IPv6, SYNPROXY, Users, Users Groups).
- A lot of bug fixes and optimizations.
* Tue Mar 22 2016 Costa Tsaousis <costa@tsaousis.gr> - 1.0.0-1
- First public release.
* Sun Nov 15 2015 Alon Bar-Lev <alonbl@redhat.com> - 0.0.0-1
- Initial add.
