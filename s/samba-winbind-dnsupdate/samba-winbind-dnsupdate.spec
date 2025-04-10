%define script_name winbind-dnsupdate

Name: samba-winbind-dnsupdate
Version: 0.7.1
Release: alt1

Summary: Dynamic dns update for winbind backend
License: GPLv3
Group: System/Configuration/Networking

URL: https://github.com/altlinuxteam/samba-winbind-dnsupdate
VCS: https://github.com/altlinuxteam/samba-winbind-dnsupdate

Source: %name-%version.tar

# actually not anymore but e2k has a standalone girar
BuildArch: noarch
%ifnarch %e2k
BuildRequires: shellcheck
%endif

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
install -Dm 644 org.altlinux.winbind.dnsupdate.gschema.xml \
      %buildroot%_datadir/glib-2.0/schemas/org.altlinux.winbind.dnsupdate.gschema.xml

%check
%ifnarch %e2k
shellcheck %script_name
%endif

%files
%doc README.md
%_bindir/%script_name
%_unitdir/%script_name.timer
%_unitdir/%script_name.service
%_datadir/bash-completion/completions/%script_name
%_sysconfdir/sysconfig/%script_name
%_man1dir/winbind-dnsupdate.1.*
%_datadir/glib-2.0/schemas/org.altlinux.winbind.dnsupdate.gschema.xml

%changelog
* Thu Apr 10 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.7.1-alt1
- Fix incorrect description of options (ALT #52951)

* Wed Jan 22 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.7-alt1
- Remove ini file

* Thu Jan 16 2025 Evgenii Sozonov <arzdez@altlinux.org> 0.6-alt1
- Change the method of getting parameters from dconf to gsettings
- Change dconf path in winbind dnsupdate.ini
- Add gsettings schema file
- Fix typo in man file (ALT #51551)
- Changing the default behavior of working with dconf (ALT #51611)
- Fix typo (ALT #51552)

* Mon Sep 30 2024 Michael Shigorin <mike@altlinux.org> 0.5-alt2
- E2K: avoid shellcheck due to ghc still lacking

* Wed Sep 18 2024 Evgenii Sozonov <arzdez@altlinux.org> 0.5-alt1
- Change the site name retrieval method
- Move the server availability check cycle into a separate function
- Add getting reacheble dns servers on other sites
- Add "get_site_list" finction
- Add information about dconf to the man page and README file (thx Olga Kamaeva)

* Tue Sep 03 2024 Andrey Limachko <liannnix@altlinux.org> 0.4-alt1
- Add getting parammetrs from dconf (thx Evgenii Sozonov)
- Fix update PTR records (thx Evgenii Sozonov)
- Change the method for obtaining an available DNS server (thx Evgenii Sozonov)

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
