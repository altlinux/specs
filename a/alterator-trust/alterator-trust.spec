# vim: set ft=spec: -*- rpm-spec -*-

Name: alterator-trust
Version: 0.6.2.1
Release: alt1

Summary: alterator module for setting one-way trust relationships
Group: System/Configuration/Other
License: GPL

BuildArch: noarch

Source: %name-%version.tar

Requires: alterator >= 4.6-alt3
Requires: alterator-l10n >= 2.4-alt4
Requires: libshell >= 0.0.7
Conflicts: alterator-fbi < 5.7-alt4
Conflicts: alterator-root < 0.8

BuildPreReq: alterator >= 4.6-alt3

%description
alterator module for setting one-way trust relationships

%prep
%setup

%build
%make_build

%install
%makeinstall
mkdir -p %buildroot{%_datadir/alterator/design,%_localstatedir/%name}
ln -s "$(relative %_localstatedir/%name/id_dsa.pub %_datadir/alterator/design/trust-key.pub)" %buildroot%_datadir/alterator/design/trust-key.pub
touch %buildroot%_localstatedir/%name/{id_dsa{,.pub},known_hosts{,.old}}

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_datadir/alterator/design/trust-key.pub
%_datadir/alterator/design/images/trust
%_alterator_backend3dir/*
%_bindir/*
%dir %_localstatedir/%name
%attr(700,root,root) %dir %_libexecdir/alterator/hooks/trust.d
%attr(600,root,root) %ghost %verify(not md5 size mtime) %config(missingok,noreplace) %_localstatedir/%name/id_dsa
%ghost %verify(not md5 size mtime) %config(missingok,noreplace) %_localstatedir/%name/id_dsa.pub
%ghost %verify(not md5 size mtime) %config(missingok,noreplace) %_localstatedir/%name/known_hosts
%ghost %verify(not md5 size mtime) %config(missingok,noreplace) %_localstatedir/%name/known_hosts.old

%changelog
* Wed Aug 19 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6.2.1-alt1
- Fix class for text entry field

* Wed Jun 17 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6.2-alt1
- Updated message about master server key
- Updated deps on alterator-l10n

* Sun Jun 14 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6.1-alt1
- Fix master/slave redirect (closes: #20441)
- Redirect to slave interface only if server role is "slave"

* Wed Jun 10 2009 Alexey I. Froloff <raorn@altlinux.org> 0.6-alt1
- Fix link to trust interface on slave server
- Report dead available hosts
- Use new API for file download

* Fri Apr 10 2009 Sir Raorn <raorn@altlinux.org> 0.5-alt1
- trust.desktop: UI is html

* Thu Mar 26 2009 Sir Raorn <raorn@altlinux.ru> 0.5-alt0.1
- Major design improvements

* Tue Mar 17 2009 Sir Raorn <raorn@altlinux.ru> 0.2-alt1
- Add hook directory

* Thu Mar 12 2009 Sir Raorn <raorn@altlinux.ru> 0.1-alt1
- Initial build

