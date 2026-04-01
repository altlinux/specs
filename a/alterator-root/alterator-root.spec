Name: alterator-root
Version: 1.5
Release: alt1

Source:%name-%version.tar

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary: alterator module for edit system administrator properties
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Requires: alterator >= 4.6-alt3 alterator-sh-functions >= 0.13-alt2
Requires: shadow-utils passwdqc-utils
Requires: alterator-l10n >= 2.7-alt3
Conflicts: alterator-lookout < 2.2-alt1
Conflicts: alterator-fbi < 5.25-alt4
Conflicts: alterator-users < 8.1

BuildPreReq: alterator >= 4.6-alt3
BuildRequires: qt6-tools

%description
alterator module for edit system administrator properties

%prep
%setup -q

%build
%make_build

# QML translations for alterator-framework UI
lrelease-qt6 alterator-framework/ts/root_ru.ts

%install
%makeinstall

install -Dpm644 dbus-backends/root.backend %buildroot%_datadir/alterator/backends/root.backend
install -Dpm644 dbus-backends/org.altlinux.alterator.root.policy %buildroot%_datadir/polkit-1/actions/org.altlinux.alterator.root.policy
install -d %buildroot%_datadir/alterator-framework/modules/root
install -m 644 alterator-framework/manifest.json %buildroot%_datadir/alterator-framework/modules/root/
install -m 644 alterator-framework/main.qml %buildroot%_datadir/alterator-framework/modules/root/
install -d %buildroot%_datadir/alterator-framework/modules/root/ts
install -m 644 alterator-framework/ts/root_ru.qm %buildroot%_datadir/alterator-framework/modules/root/ts/

%files
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*
%attr(700,root,root) %dir %_libexecdir/alterator/hooks/root.d

%_datadir/alterator/backends/root.backend
%_datadir/polkit-1/actions/org.altlinux.alterator.root.policy

%dir %_datadir/alterator-framework
%dir %_datadir/alterator-framework/modules
%dir %_datadir/alterator-framework/modules/root
%_datadir/alterator-framework/modules/root/manifest.json
%_datadir/alterator-framework/modules/root/main.qml
%dir %_datadir/alterator-framework/modules/root/ts
%_datadir/alterator-framework/modules/root/ts/root_ru.qm

%changelog
* Mon Mar 23 2026 Maria Alexeeva <alxvmr@altlinux.org> 1.5-alt1
- add polkit action translations (thx Oleg Chagaev)

* Thu Feb 26 2026 Maria Alexeeva <alxvmr@altlinux.org> 1.4-alt1
- remove version from AlteratorFramework import (thx Oleg Chagaev)

* Fri Jan 16 2026 Maria Alexeeva <alxvmr@altlinux.org> 1.3-alt1
- add alterator-framework UI support (thx Oleg Chagaev)

* Thu Jul 1 2025 Alexey Romanyuta <r9odt@altlinux.org> 1.2-alt1
- backend3/root: add iscrypted parameter to allow pass crypted
  password to module

* Tue Oct 06 2015 Aleksey Avdeev <solo@altlinux.org> 1.1-alt3
- fix test (closes: #31317)

* Wed Nov 18 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt2
- add passwordbox API for code reuse in firsttime like interfaces

* Tue Nov 17 2009 Stanislav Ievlev <inger@altlinux.org> 1.1-alt1
- use alterator_export_proc

* Thu Sep 17 2009 Stanislav Ievlev <inger@altlinux.org> 1.0-alt1
- add message on successful password update (closes: #21317)

* Tue Aug 11 2009 Stanislav Ievlev <inger@altlinux.org> 0.9-alt2
- add support of $ALTERATOR_DESTDIR variable (stanv@)

* Tue Aug 04 2009 Stanislav Ievlev <inger@altlinux.org> 0.9-alt1
- html ui: use workflow 'none'
- qt ui: use modern form API

* Tue May 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.8-alt2
- fix temporary files removal

* Fri Mar 13 2009 Sir Raorn <raorn@altlinux.ru> 0.8-alt1
- do not show ssh keys owned by alterator-trust

* Thu Feb 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- add hooks to allow distribution specific behaviour

* Tue Feb 17 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- add authorized ssh keys management

* Mon Feb 02 2009 Mikhail Efremov <sem@altlinux.org> 0.5-alt2
- test is added

* Mon Jan 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- use help and translations directly from alterator-l10n

* Wed Jan 21 2009 Mikhail Efremov <sem@altlinux.org> 0.4-alt9
- move templates/* -> ui/

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt8
- rebuild with new l10n

* Tue Dec 02 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.4-alt7
- rebuild with new l10n (fixes by azol@)

* Mon Nov 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt6
- rebuild with new l10n (english help)

* Wed Nov 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt5
- minor module update

* Thu Sep 25 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt4
- fix tab order: setup focus after visibility setup

* Fri Aug 29 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- use empty redirect-url instead of name-attribute hack

* Thu Jul 31 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- first edit in focus now
- improve html ui

* Wed Jun 25 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- remove passwordbox widget support
- html ui: improve style

* Tue Jun 24 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- use effects instead of special widget
- remove po-files
- use module.mak

* Fri May 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- improve ui layout
- remove autoinstall backend usage
- remove po files

* Sun May 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt7
- join to common translation database

* Sun May 04 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- don't use obsolete attribute "invisible"
- use function small from common library
- remove html-messages
- improve ui

* Mon Apr 07 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- fix behaviour in installer

* Thu Apr 03 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- little ui improvements

* Wed Mar 19 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.2-alt3
- add conflicts: alterator-users < 8.1
- change focus and clear text fields when wron password entered

* Tue Mar 11 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- add /design/scripts/password.js
- use alterator-sh-functions

* Wed Mar 05 2008 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- remove template-*

* Mon Jan 28 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- more provides

* Wed Jan 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
