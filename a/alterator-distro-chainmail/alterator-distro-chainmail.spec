Name: alterator-distro-chainmail
Version: 3.0.0
Release: alt1

Source: %name-%version.tar

Summary: special alterator modules for IVK Chainmail
License: GPL
Group: System/Configuration/Other

BuildArch: noarch

Requires: alterator >= 4.12-alt1 alterator-sh-functions
Requires: alterator-net-iptables
Requires: alterator-net-domain >= 0.1-alt2
Requires: alterator-root >= 1.1-alt1
Requires: alterator-l10n >= 2.4-alt2

Conflicts: alterator-net-eth < 4.3-alt5
Conflicts: alterator-fbi < 5.25-alt6

# We setup MySQL by our own hook
Conflicts: installed-db-office-server

BuildPreReq: alterator >= 4.12-alt1

%description
special alterator modules for IVK Chainmail:
- alterator's workflow
- hooks for administrator password

%package -n installer-step-chainmail-domain
Summary: Installer step for creating domain
Group: System/Configuration/Other

Requires: alterator-net-domain
Requires: alterator-net-iptables

Conflicts: installer-feature-network-shares-stage3 < 0.5-alt1

%description -n installer-step-chainmail-domain
Create domain and set external interfaces
during installation.

%prep
%setup

%build
%make_build

%install
%makeinstall
%find_lang %name

%files
%config(noreplace) %_sysconfdir/alterator/logs/.order
%dir %_datadir/alterator/ui/chainmail/
%_datadir/alterator/ui/chainmail/framework/
%_libexecdir/alterator/hooks/*.d/*
%_datadir/alterator/interfaces/guile/workflow/*

%files -n installer-step-chainmail-domain
%_datadir/alterator/ui/chainmail/domain/
%_datadir/install2/steps/*.desktop

%changelog
* Fri Jan 30 2015 Mikhail Efremov <sem@altlinux.org> 3.0.0-alt1
- Update Chainmail's workflow.
- Drop /chainmail/login interface.
- Always use 'testdomain.ru' as default domain name.

* Tue Oct 14 2014 Mikhail Efremov <sem@altlinux.org> 2.99.0-alt1
- Add 'Domain' installer step.

* Wed Aug 20 2014 Mikhail Efremov <sem@altlinux.org> 2.97.0-alt1
- Add hook for setup MySQL password.

* Fri Jun 20 2014 Mikhail Efremov <sem@altlinux.org> 2.96.0-alt1
- Drop hook and helper for setting MySQL password.
- Update description.
- Drop firsttime.

* Wed Nov 03 2010 Mikhail Efremov <sem@altlinux.org> 2.1-alt2
- drop setting MySQL passwords for moodle and wikidb.
- resurrect utility for mysql.

* Wed Nov 18 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt1
- update to newest versions of alterator-fbi and alterator-root
- use standard logout-button instead of own logout page

* Mon Nov 02 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt12
- use ui-corner-all class

* Wed Oct 07 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt11
- fix style (no div with width 100%%)
- update to latest alterator-fbi: new help engine, drop links to unexistent js files

* Fri Oct 02 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt10
- be sure domain is not null (closes: #21810)

* Wed Sep 30 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt9
- commit-iptables: use special "firsttime" action

* Wed Sep 30 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt8
- commit-iptables: use standard port list from alterator-net-iptables package

* Fri Sep 25 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt7
- optimize menu generation

* Thu Sep 24 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt6
- update framework for latest alterator-fbi

* Fri Aug 28 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt5
- improve CSS rule

* Thu Aug 27 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt4
- made package noarch, remove unused utility for mysql.
- commit: made commit-domain a last operation (this operation buggy and takes a lot of time)

* Mon Aug 24 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt3
- use special help page for control center

* Fri Aug 21 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt2
- update design

* Wed Aug 19 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt1
- Initial build
