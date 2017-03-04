# Do not require optional packages needed by restart hooks:
%add_findreq_skiplist %_sysconfdir/%name/restart.d/*

Name: needrestart
Version: 2.11
Release: alt1

Summary: Restart daemons after library updates
License: GPLv2
Group: System/Servers

URL: https://github.com/liske/needrestart
Source: %name-%version.tar
Patch0: %name-%version-alt.patch

Packager: %packager
BuildArch: noarch

BuildRequires: perl-devel perl-Module-Find perl-Proc-ProcessTable perl-Sort-Naturally perl-Term-ReadKey perl-libintl perl-Module-ScanDeps

%description
needrestart checks which daemons need to be restarted after library
upgrades. It is inspired by checkrestart from the debian-goodies
package.

%package list
Summary: Automaticaly list daemons needs restart after apt run
Group: System/Servers
Requires: %name = %version-%release

%description list
List daemons needs to be restarted after apt run

%prep
%setup -n %name-%version
%patch0 -p1

%build

%install
%makeinstall_std
rm -f %buildroot%perl_vendor_privlib/NeedRestart/UI/Debconf.pm
install -pDm 644 man/%name.1 %buildroot%_man1dir/%name.1

%find_lang --all-name %name

# %name-list subpackage:
mkdir -p %buildroot%_sysconfdir/apt/apt.conf.d
cat > %buildroot%_sysconfdir/apt/apt.conf.d/%name.conf << EOF
RPM::Post-Invoke      { "if [ -x /usr/sbin/needrestart ]; then /usr/sbin/needrestart -q -l -r l; fi"; };
EOF

%files -f %name.lang
%_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/%name.conf
%config(noreplace) %_sysconfdir/%name/notify.conf

%_sbindir/%name
%_libexecdir/%name
%perl_vendor_privlib/NeedRestart*
%_datadir/polkit-1/actions/net.fiasko-nw.needrestart.policy
%_man1dir/%name.1.*
%doc AUTHORS README* NEWS INSTALL* ChangeLog

%files list
%config(noreplace) %_sysconfdir/apt/apt.conf.d/%name.conf

%changelog
* Sat Mar  4 2017 Terechkov Evgenii <evg@altlinux.org> 2.11-alt1
- v2.11-3-g9423e6e

* Sun Nov 20 2016 Terechkov Evgenii <evg@altlinux.org> 2.10-alt4
- v2.10-4-g3a5c39c

* Fri Nov 11 2016 Terechkov Evgenii <evg@altlinux.org> 2.10-alt3
- Fix kernel version detection/reporting

* Fri Nov 11 2016 Terechkov Evgenii <evg@altlinux.org> 2.10-alt2
- Add subpackage with apt hook: %name-list

* Fri Nov 11 2016 Terechkov Evgenii <evg@altlinux.org> 2.10-alt1
- v2.10-1-gf28e5d4

* Fri Oct 14 2016 Terechkov Evgenii <evg@altlinux.org> 2.9-alt1
- 2.9

* Sat Jun 11 2016 Terechkov Evgenii <evg@altlinux.org> 2.8-alt2
- v2.8-4-ge9c29f4

* Fri May 20 2016 Terechkov Evgenii <evg@altlinux.org> 2.8-alt1
- 2.8

* Tue Apr 26 2016 Terechkov Evgenii <evg@altlinux.org> 2.7-alt3
- v2.7-7-g65c981d

* Tue Mar  8 2016 Terechkov Evgenii <evg@altlinux.org> 2.7-alt2
- Fix mail/dbus notifications

* Mon Mar  7 2016 Terechkov Evgenii <evg@altlinux.org> 2.7-alt1
- Initial build for ALT Linux Sisyphus
