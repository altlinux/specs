Name: alterator-firsttime
Version: 0.4
Release: alt2

Packager: Stanislav Ievlev <inger@altlinux.org>

BuildArch: noarch

Source:%name-%version.tar

Requires: alterator >= 4.7-alt3 alterator-sh-functions
Requires: alterator-l10n >= 2.5-alt11
Conflicts: alterator-lookout < 1.6-alt6
Conflicts: alterator-fbi < 5.21-alt1

%add_findreq_skiplist %_datadir/install2/postinstall.d/*

Summary: first time system setup
License: GPL
Group: System/Configuration/Other

BuildPreReq: alterator >= 4.7-alt3

%description
first time system setup

%prep
%setup -q

%build
%make_build

%install
%makeinstall

install -Dpm644 ahttpd-firsttime.conf %buildroot%_sysconfdir/ahttpd/ahttpd-firsttime.conf
install -Dpm755 ahttpd-firsttime.init %buildroot/%_initrddir/ahttpd-firsttime

%post
%post_service ahttpd-firsttime

%preun
%preun_service ahttpd-firsttime

%files
%_sysconfdir/ahttpd/*.conf
%_initrddir/ahttpd-firsttime
%_datadir/alterator/ui/firsttime/*
%_datadir/alterator/interfaces/guile/workflow/*
%_alterator_backend3dir/*
%_libexecdir/alterator/hooks/firsttime.d

%changelog
* Mon Nov 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- use ui-corner-all class

* Wed Oct 07 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- update for latest alterator-fbi

* Tue Sep 01 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- use form_replace_if_ready

* Fri Aug 28 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- improve CSS rules

* Fri Aug 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- update design

* Fri Jun 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt6
- update styles

* Thu May 28 2009 Dmitry V. Levin <ldv@altlinux.org> 0.1-alt5
- Removed postinstall.d/99-firsttime.sh.
- backend3/firsttime: Removed manual ahttpd restart.

* Thu Apr 30 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- add firsttime.d hook
- notify about browsers without javascript support (closes: #19818)

* Fri Apr 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- remove unused "use-module (alterator ahttpd woo)"

* Thu Feb 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- move locale setup out from framework
- include jquery.cookie

* Thu Feb 19 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
