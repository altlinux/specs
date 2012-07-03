%define oname apache-couchdb
Name: couchdb
Version: 1.0.2
Release: alt1
Packager: Mikhail Pokidko <pma@altlinux.org>
Url: http://couchdb.apache.org/
License: Apache
Group: Databases
Summary: A peer based distributed database system

Source: %name-%version-%release.tar
Source1: couch.init

BuildRequires: erlang erlang-devel erlang-otp-devel libicu-devel libcurl-devel help2man libjs-devel

Requires: libicu-devel erlang erlang-otp

%description
CouchDB is a peer based distributed database system. Any number of CouchDB hosts
(servers and offline-clients) can have independent "replica copies" of the same database,
where applications have full database interactivity (query, add, edit, delete). 
When back online or on a schedule, database changes are replicated bi-directionally. 

CouchDB has built-in conflict detection and management and the replication process is
incremental and fast, copying only documents and individual fields changed since the 
previous replication. Most applications require no special planning to take advantage 
of distributed updates and replication. 

Unlike cumbersome attempts to bolt distributed features on top of the same legacy models 
and databases, it is the result of careful ground-up design, engineering and integration. 
The document, view, security and replication models, the special purpose query language, 
the efficient and robust disk layout are all carefully integrated for a reliable and 
efficient system.

%prep
%setup -q

%build
./bootstrap
%configure --with-js-include=%_includedir/js --localstatedir=/var --libdir=%_libexecdir 
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_sbindir
mv %buildroot%_bindir/%name %buildroot%_sbindir/
mv %buildroot%_prefix/lib/%name/erlang %buildroot%_libexecdir

install -p -m755 -D %SOURCE1 %buildroot%_initdir/%name
mkdir -p %buildroot%_sysconfdir/sysconfig
mv %buildroot%_sysconfdir/default/%name %buildroot%_sysconfdir/sysconfig/

mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name

# fix paths
sed -i s@lib/lib@lib@g %buildroot%_sbindir/%name
sed -i s@%name/erlang@erlang@g %buildroot%_sbindir/%name
sed -i s#HEART_COMMAND=\"/usr/bin#HEART_COMMAND=\"/usr/sbin#g %buildroot%_sbindir/%name
sed -i s#/usr/lib/couchdb#/usr/lib# %buildroot%_sysconfdir/%name/default.ini

%pre
%_sbindir/groupadd -r -f _couchdb &>/dev/null ||:
%_sbindir/useradd -r -g _couchdb -d %_localstatedir/%name -s /dev/null \
	-c "couchdb pseudouser" -M -n _couchdb &>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name


%files
%dir %_sysconfdir/%name/
%config(noreplace) %attr(0660,root, _couchdb) %_sysconfdir/%name/local.ini
%_sysconfdir/%name/default.ini
%attr(0770,root, _couchdb) %_sysconfdir/%name/default.d/
%attr(0770,root, _couchdb) %_sysconfdir/%name/local.d/
%_sysconfdir/logrotate.d/couchdb
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%_libexecdir/erlang/lib/*
%_bindir/*
%_sbindir/*
%_datadir/%name
%_libexecdir/%name
%attr(0770,root, _couchdb) %_localstatedir/%name
%attr(0770,root, _couchdb) %_logdir/%name
%doc %_defaultdocdir/%name
%_man1dir/*



%changelog
* Wed Jan 19 2011 Mikhail Pokidko <pma@altlinux.org> 1.0.2-alt1
- Version 1.0.2

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt2.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Fri Dec 03 2010 Mikhail Pokidko <pma@altlinux.org> 1.0.1-alt2
- pre 1.0.2

* Tue Aug 17 2010 Mikhail Pokidko <pma@altlinux.org> 1.0.1-alt1
- v1.0.1 : Fixed data-loss bug

* Fri Jul 16 2010 Mikhail Pokidko <pma@altlinux.org> 1.0.0-alt1
- new shiny v1.0.0

* Thu Apr 01 2010 Mikhail Pokidko <pma@altlinux.org> 0.11-alt1
- Version 0.11. 

* Tue Mar 16 2010 Mikhail Pokidko <pma@altlinux.org> 0.10.1-alt2
- Rebuild with icu 4.4

* Fri Jan 15 2010 Mikhail Pokidko <pma@altlinux.org> 0.10.1-alt1
- a few commits later since 0.10.1

* Wed Nov 11 2009 Mikhail Pokidko <pma@altlinux.org> 0.10-alt1
- Version 0.10. commit 44fbd416a4b093c00eaf6124b03f92d0bba921f2

* Fri Jul 31 2009 Mikhail Pokidko <pma@altlinux.org> 0.9.0-alt1
- Version 0.9.0.

* Sun Jan 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.8.1-alt1
- new version 0.8.1, update buildreqs

* Sat Dec 08 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.7.2-alt1
- Initial build for ALT Linux
