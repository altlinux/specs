Name: needrestart
Version: 2.7
Release: alt2

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

%prep
%setup -n %name-%version
%patch0 -p1

%build

%install
%makeinstall_std
rm -f %buildroot%perl_vendor_privlib/NeedRestart/UI/Debconf.pm
install -pDm 644 man/%name.1 %buildroot%_man1dir/%name.1

%find_lang --all-name %name

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

%changelog
* Tue Mar  8 2016 Terechkov Evgenii <evg@altlinux.org> 2.7-alt2
- Fix mail/dbus notifications

* Mon Mar  7 2016 Terechkov Evgenii <evg@altlinux.org> 2.7-alt1
- Initial build for ALT Linux Sisyphus
