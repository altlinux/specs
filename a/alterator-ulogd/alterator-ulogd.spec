Name: alterator-ulogd
Version: 2.0.0
Release: alt1

Summary: alterator module for network traffic statistics
License: GPL
Group: System/Configuration/Other
Url: http://wiki.sisyphus.ru/Alterator

Source: %name-%version.tar

BuildArch: noarch

Requires(post): sqlite3
Requires: alterator >= 3.5 gettext etcnet
Requires: ulogd-sqlite3 >= 2.0.2-alt1
Requires: alterator-net-iptables >= 4.3-alt1
Requires: libshell alterator-net-functions alterator-sh-functions
Requires: alterator-service-functions
Requires: alterator-l10n >= 2.5-alt14

BuildPreReq: alterator >= 3.5-alt2

# Automatically added by buildreq on Mon Jul 11 2005 (-bi)
BuildRequires: alterator

%define sqlite3db %_localstatedir/ulogd/alterator_sqlite3.db
%define ulogd_conf %_sysconfdir/ulogd.conf

%description
Iptables traffic statistics alterator module

%prep
%setup -q

%build
%make_build

%install
%makeinstall
install -D -m644 ulogd.scheme %buildroot/%_datadir/%name/ulogd.scheme

%post
if [ $1 -eq 1 ]; then
    /usr/bin/sqlite3 -batch %sqlite3db <%_datadir/%name/ulogd.scheme >/dev/null ||:
    chown ulogd:ulogd %sqlite3db ||:
    sed -i -r -e 's;^#(plugin=".+/ulogd_output_SQLITE3.so");\1;' \
	    -e 's;^#(plugin=".+/ulogd_inppkt_ULOG.so);\1;'  \
	    -e 's;^(stack=log1:NFLOG,.+,emu1:LOGEMU);#\1;'  \
		%ulogd_conf
    sed -i -r "/^\[ct1\]/i # stack for alterator-ulogd \\
stack=ulog1:ULOG,base1:BASE,ip2str1:IP2STR,alterator_sqlite3:SQLITE3 \\
    " %ulogd_conf
    cat >>%_sysconfdir/ulogd.conf <<EOF

[alterator_sqlite3]
table="ulog"
db="%sqlite3db"
buffer=200
EOF
/etc/init.d/ulogd condreload >/dev/null 2>&1 ||:
fi

%files
%_alterator_backend3dir/*
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_datadir/%name

%changelog
* Fri Aug 23 2013 Mikhail Efremov <sem@altlinux.org> 2.0.0-alt1
- Updated for ulogd-2.x.
- Use alterator-service-functions.

* Thu Sep 03 2009 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt2
- fix requires.

* Thu Sep 03 2009 Mikhail Efremov <sem@altlinux.org> 1.3.1-alt1
- 'In' -> 'Incoming traffic', 'Out' -> 'Outgoing traffic'.

* Mon Aug 31 2009 Mikhail Efremov <sem@altlinux.org> 1.3.0-alt1
- only one 'iptables_helper list' call.
- not show '-' if iface not has addr.
- handle 'database is locked' error.
- backend: rewrite data selecting.
- fix requires.

* Fri Aug 28 2009 Mikhail Efremov <sem@altlinux.org> 1.2.0-alt1
- rename 'Enable statistics collecting' -> 'Enable data collection'.
- ui update when iface changed.
- don't call update-services on init.
- remove 'Start date' label.
- use min and max date values from table for start and end dates.
- use write_bool_param() for 'Enable...' checkbox.

* Thu Aug 27 2009 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1
- added creation iptables rules.
- call update-services on init.
- 'Start date' label is added.
- 'Check IP' checkbox is removed.
- 'Enable statistics collecting' checkbox is added.
- removed unused function list_services().
- use set_locale for services list.
- commented debug output.

* Tue Aug 25 2009 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1
- rewritten backend on shell
- use workflow 'none'
- create tables in post script

* Wed Jan 28 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt5
- move help and translations to alterator-l10n

* Tue Dec 09 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt4
- update help

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt3
- fix desktop

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.5-alt2
- update help and po

* Wed Sep 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- remove constraints

* Fri Aug 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- resurrect stylesheet

* Thu Aug 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- update build system
- replace dateedit calendar with more compact dateedit picker
- remove template-*
- replace POST+redirect with GET

* Tue Aug 05 2008 Paul Wolneykien <manowar@altlinux.ru> 0.3-alt1
- Use shared calendar component (16210, 16211).

* Tue Jun 17 2008 Grigory Batalov <bga@altlinux.ru> 0.2-alt3
- Require alterator-services instead of alterator-chkconfig.

* Fri Jun 06 2008 Grigory Batalov <bga@altlinux.ru> 0.2-alt2
- Rebuild for Sisyphus.

* Fri May 30 2008 Grigory Batalov <bga@altlinux.ru> 0.2-alt1.M41.1
- Russian help page.
- Change help paths to the new style.
- Service restart link update.

* Tue Nov 27 2007 Grigory Batalov <bga@altlinux.ru> 0.2-alt1
- Aggregate daily counters.

* Thu Nov 15 2007 Grigory Batalov <bga@altlinux.ru> 0.1-alt1
- Initial release
