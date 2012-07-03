%define _altdata_dir %_datadir/alterator

Name: alterator-mirror
Version: 0.4.1
Release: alt1

BuildArch: noarch

Source:%name-%version.tar

Summary: local mirrors setup and maintainance
License: GPL
Packager: Stanislav Ievlev <inger@altlinux.org>

Group: System/Configuration/Other

Requires: alterator >= 3.9-alt2 alterator-sh-functions >= 0.10-alt5 libshell sisyphus-mirror > 0.7.2-alt1
Requires: alterator-l10n >= 2.4-alt9

BuildPreReq: alterator >= 3.5-alt1

Conflicts: alterator-fbi < 5.17-alt4
Conflicts: apt-conf-sisyphus < 5.0-alt3
Conflicts: apt-conf-desktop < 5.0-alt2
Conflicts: apt-conf-branch < 5.0-alt2

%description
local mirrors setup and maintainance

%prep
%setup -q

%build
%make_build

%install
%makeinstall

install -d %buildroot%_logdir/%name
install -Dpm640 %name.logrotate %buildroot%_sysconfdir/logrotate.d/%name

%files
%config(noreplace) %_sysconfdir/logrotate.d/*
%config(noreplace) %_sysconfdir/alterator/mirror
%_sbindir/*
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*
%_alterator_backend3dir/*
%attr(700,root,adm) %_logdir/%name

%changelog
* Fri May 04 2012 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.1-alt1
- add support for new arepo

* Tue Aug 23 2011 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4-alt1
- add support for arepo and arm repositories

* Tue Aug 04 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- use workflow 'none'
- improve schedule setup (closes: #20370)

* Mon Jun 08 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt9
- create destdir if it doesn't exists (closes: #20369)

* Thu Apr 16 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt8
- fix work if /srv is a symlink

* Thu Apr 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt7
- menu file: move to "servers" group, update translations

* Fri Mar 27 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt6
- fix menu file

* Thu Mar 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt5
- relocate module data to /srv/public
- little interface improvements

* Mon Mar 23 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt4
- fix module name

* Fri Feb 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt3
- improve local mirrors publication

* Thu Feb 12 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- publish updates in avahi
- fix url re

* Wed Feb 11 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- redesign module to use as a server for automatic updates

* Tue Feb 03 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt4
- use external mirror and repository databases from apt-conf
- minor module update

* Tue Jan 27 2009 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt3
- move translations to alterator-l10n

* Fri Dec 05 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt2
- rebuild with new l10n

* Thu Nov 20 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build

