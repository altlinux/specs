Name: alterator-distro-chainmail
Version: 2.1
Release: alt1

Source:%name-%version.tar

Packager: Stanislav Ievlev <inger@altlinux.org>

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

BuildPreReq: alterator >= 4.12-alt1

%description
special alterator modules for IVK Chainmail:
- firsttime settings
- hooks for administrator password

%prep
%setup -q

%build
%make_build

%install
%makeinstall
%find_lang %name

%files
%config(noreplace) %_sysconfdir/alterator/logs/.order
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_libexecdir/alterator/hooks/*.d/*
%_datadir/alterator/interfaces/guile/workflow/*

%changelog
* Wed Nov 18 2009 Stanislav Ievlev <inger@altlinux.org> 2.1-alt1
- update to newest versions of alterator-fbi and alterator-root
- use standard logout-button instead of own logout page

* Mon Nov 02 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt12
- use ui-corner-all class

* Wed Oct 07 2009 Stanislav Ievlev <inger@altlinux.org> 2.0-alt11
- fix style (no div with width 100%)
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
