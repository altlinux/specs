%define script_name winbind-dnsupdate

Name: samba-winbind-dnsupdate
Version: 0.3
Release: alt1

Summary: Dynamic dns update for winbind backend
License: GPLv3
URL: https://github.com/altlinuxteam/samba-winbind-dnsupdate
VCS: https://github.com/altlinuxteam/samba-winbind-dnsupdate

BuildArch: noarch
Group: System/Configuration/Networking
Source: %name-%version.tar

BuildRequires: shellcheck

Requires: samba-winbind

%description
A program that implements dynamic update of addresses
on a DNS server when used as a winbind backend

%prep
%setup

%build
# Change version
sed -i 's/^VERSION=.*/VERSION=%version/' %script_name

%install

install -Dm 755 %script_name %buildroot/%_bindir/%script_name
install -Dm 644 %script_name.bash-completion \
     %buildroot%_datadir/bash-completion/completions/%script_name
install -Dm 644 %script_name.timer %buildroot%_unitdir/%script_name.timer
install -Dm 644 %script_name.service %buildroot%_unitdir/%script_name.service
install -Dm 644 %script_name.sysconfig %buildroot%_sysconfdir/sysconfig/%script_name
install -Dm 644 doc/winbind-dnsupdate.1 %buildroot/%_man1dir/winbind-dnsupdate.1

%check
shellcheck %script_name

%files
%doc README.md
%_bindir/%script_name
%_unitdir/%script_name.timer
%_unitdir/%script_name.service
%_datadir/bash-completion/completions/%script_name
%_sysconfdir/sysconfig/%script_name
%_man1dir/winbind-dnsupdate.1.*

%changelog
* Fri Aug 23 2024 Andrey Limachko <liannnix@altlinux.org> 0.3-alt1
- Add explicit selection of DNS server for update. Change getting
  host addres method (thx Evgenii Sozonov)
- Edit incorrect log message (thx Evgenii Sozonov)
- Add explicit krb5 temp cache file deletion (thx Evgenii Sozonov)

* Tue Aug 13 2024 Andrey Limachko <liannnix@altlinux.org> 0.2-alt1
- Add man page (thx Olga Kamaeva)
- Add README file (thx Olga Kamaeva)

* Wed Jul 31 2024 Andrey Limachko <liannnix@altlinux.org> 0.1-alt2
- Build for sisyphus.

* Mon Jul 29 2024 Evgenii Sozonov  <arzdez@altlinux.org> 0.1-alt1
- Initial release.
