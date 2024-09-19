%define webserver_cgibindir %_var/www/cgi-bin/
%define subscribers_dir /lib/resolvconf

Name: host2cat
Version: 1.01
Release: alt8

Summary: Custom DNS resolver
License: BSD
Group: System/Servers
Url: www.netpolice.ru

Source0: %name-%version.tar.gz
Source1: %name.init
Source2: %name.sysconfig
Source3: squid.conf
Source4: %name.openresolv
Source5: README.ALT.host2cat
Source6: %name.service
Patch0: host2cat-alt-fix-include-config.ph.patch

BuildRequires: libadns-devel libmemcache-devel

# for findreq 
BuildRequires: perl-DBI perl-Net-DNS perl-CGI

# for apache2 user
Requires(pre): apache2-common
# for cgi-bin dir
Requires: apache2
Requires: apache2-htpasswd
Requires: perl-DBD-SQLite memcached
Requires: netpolice-filter squid-conf-%name squid-server >= 3.0
Requires: openresolv-%name

%description
DNS resolver for web content filtering with web interface.

%package -n squid-conf-%name
Summary: adapted squid config
Group: System/Servers
Requires: squid-common squid-helpers libshell
Requires: squid-server >= 3.1.19-alt2

%description -n squid-conf-%name
This package contains squid config adapted for %name.

%package -n openresolv-%name
Summary: host2cat subscriber for openresolv
Group: System/Configuration/Networking
Requires: openresolv
Requires: %name

%description -n openresolv-%name
host2cat subscriber for openresolv

%prep
%setup -q
%patch0 -p2

%build
aclocal --force 
autoconf --force
autoheader --force
automake --add-missing --force-missing --foreign

%configure
%make_build

%install
mkdir -p %buildroot{%_cachedir/%name,%webserver_cgibindir,%_libexecdir/%name}

install -m0755 -D %name %buildroot%_sbindir/%name
install -m0755 -D %SOURCE1 %buildroot%_initdir/%name
install -m0644 -D %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
install -m0644 -D %SOURCE3 %buildroot%_sysconfdir/squid/squid.conf.host2cat
install -m0644 -D %SOURCE4 %buildroot%subscribers_dir/%name
install -m0644 -D %SOURCE5 %buildroot%_sysconfdir/squid/README.ALT.host2cat
install -m0644 -D %SOURCE6 %buildroot%_unitdir/%name.service

install -m0755 contrib/get_file.pl %buildroot%webserver_cgibindir/get_file.pl
install -m0644 scripts/config.ph %buildroot%webserver_cgibindir/config.ph
install -m0755 scripts/*.cgi %buildroot%webserver_cgibindir/
install -m0755 scripts/*.pl %buildroot%_libexecdir/%name/
install -m0644 scripts/*.schema %buildroot%_libexecdir/%name/
install -m0644 scripts/custom_roles scripts/generic_roles scripts/users %buildroot%_libexecdir/%name/

touch %buildroot%_cachedir/%name/filter.db

mkdir -p %buildroot%_sysconfdir/httpd2/conf/{extra-start.d,extra-available,mods-start.d}
cat << EOF > %buildroot%_sysconfdir/httpd2/conf/extra-start.d/030-host2cat.conf
host2cat=yes
EOF

cat << EOF > %buildroot%_sysconfdir/httpd2/conf/extra-available/host2cat.conf
<IfModule alias_module>
	ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"
</IfModule>
EOF

cat << EOF > %buildroot%_sysconfdir/httpd2/conf/mods-start.d/030-host2cat.conf
alias=yes
cgi=yes
EOF

%post
%post_service %name
/usr/sbin/a2chkconfig &> /dev/null ||:
/sbin/service httpd2 condreload ||:
INITDB=%_libexecdir/%name/init_filter_db.pl
[ -x $INITDB ] && $INITDB -d %_libexecdir/%name/ dbi:SQLite:dbname=%_cachedir/%name/filter.db ||:

%preun
%preun_service %name

%post -n squid-conf-%name
# Make Squid autostart
/sbin/chkconfig squid on
touch %_sysconfdir/squid/passwd
htpasswd2 -b %_sysconfdir/squid/passwd netpolice netpolice

%files
%_initdir/%name
%_unitdir/%name.service
%_sysconfdir/sysconfig/%name
%_sysconfdir/httpd2/conf/extra-start.d/030-host2cat.conf
%_sysconfdir/httpd2/conf/extra-available/host2cat.conf
%_sysconfdir/httpd2/conf/mods-start.d/030-host2cat.conf
%_sbindir/%name
%webserver_cgibindir/get_file.pl
%_libexecdir/%name
%config(noreplace) %webserver_cgibindir/config.ph
%webserver_cgibindir/*.cgi
%dir %attr(711,apache2,root) %_cachedir/%name
%attr(644,apache2,root) %_cachedir/%name/filter.db

%files -n squid-conf-%name
%config(noreplace) %_sysconfdir/squid/squid.conf.host2cat
%doc %_sysconfdir/squid/README.ALT.host2cat

%files -n openresolv-%name
%subscribers_dir/%name

%changelog
* Thu Sep 19 2024 Andrey Cherepanov <cas@altlinux.org> 1.01-alt8
- Fix include config.ph (ALT #41426).

* Tue Nov 16 2021 Andrey Cherepanov <cas@altlinux.org> 1.01-alt7
- Add host2cat.service
- Set default DNS server to 127.0.0.1

* Thu Apr 11 2013 Andrey Cherepanov <cas@altlinux.org> 1.01-alt6
- Remove post and preun scripts for change Squid configuration
- Add README.ALT.host2cat to squid-conf-host2cat to help change
  Squid configuration manually

* Wed Apr 10 2013 Andrey Cherepanov <cas@altlinux.org> 1.01-alt5
- Don't conflict with /etc/squid/squid.conf, just replace default config
  file by /etc/squid/squid.conf.host2cat

* Wed Nov 07 2012 Paul Wolneykien <manowar@altlinux.ru> 1.01-alt4
- Fix the post-install hook: require apache2-htpasswd.

* Mon May 21 2012 Andrey Cherepanov <cas@altlinux.org> 1.01-alt3
- Make hook for openresolv to fill configuration file
- Adapt configuration for Squid >= 3.1.0
- Make squid service as autostarted

* Thu Nov 11 2010 Anton Pischulin <letanton@altlinux.ru> 1.01-alt2.2
- Some changes to spec

* Wed Mar 10 2010 Anton Pischulin <letanton@altlinux.ru> 1.01-alt2.1
- Change version to 1.01

* Mon Sep 28 2009 Grigory Batalov <bga@altlinux.ru> 0.2-alt1
- Updated version.

* Fri Apr 17 2009 Grigory Batalov <bga@altlinux.ru> 0.1-alt1.M40.2
- Remove test sites from policies.

* Fri Apr 17 2009 Grigory Batalov <bga@altlinux.ru> 0.1-alt1.M40.1
- Remove test user andrew.
- Update reject policies.
- Fix memcache servers list scan.

* Fri Apr 10 2009 Grigory Batalov <bga@altlinux.ru> 0.1-alt0.M40.1
- Initial build for ALT Linux branch 4.0.
