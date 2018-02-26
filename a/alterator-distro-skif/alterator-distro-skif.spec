Name: alterator-distro-skif
Version: 0.7
Release: alt1

BuildArch: noarch

Source: %name-%version.tar

Summary: HPC specific tunings
License: GPL
Group: System/Configuration/Other

Provides: alterator-hpc-client = %version-%release alterator-hpc-server = %version-%release alterator-hpc = %version-%release
Obsoletes: alterator-hpc-client alterator-hpc-server alterator-hpc

BuildRequires: alterator

%description
HPC specific tunings

%prep
%setup

%build
%make_build

%install
%makeinstall HTMLROOT=%buildroot%_var/www/
%find_lang alterator-hpc

%files -f alterator-hpc.lang
%_alterator_backend3dir/*
%_datadir/alterator/ui/*/
%_datadir/alterator/help/*/*
%_datadir/alterator-hpc

%changelog
* Mon Oct 19 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.7-alt1
- renamed to alterator-distro-skif

* Wed Oct 15 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt4
- add help

* Tue Oct 14 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt3
- update module

* Wed Jun 25 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt2
- remove ldap setup

* Tue Feb 26 2008 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- add syslog tuning to installer, rename syslog-ng backend to hpc-syslog
- rename /hpc/storage to /hpc/node (General Node settings)
- remove server/client subpackages
- improve hpc-ldap backend (remove init action, more libshell)

* Tue Feb 19 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- use libshell
- start ldap on IPADDR_ANY
- add auto-skip to /hpc/mpi and /hpc/ldap

* Thu Jan 31 2008 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- add mpi selection support
- remove unused hpc/finish

* Wed Jan 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt4
- update to new alterator-users (require alterator-root now)

* Mon Jan 21 2008 Stanislav Ievlev <inger@altlinux.org> 0.4-alt3
- hpc-storage: start nfslock service before mount

* Tue Oct 09 2007 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- rename hpc/user to hpc/ldap

* Fri Sep 28 2007 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- add backend for simplest syslog-ng setup

* Mon Sep 24 2007 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- split to client and server subpackages to reduce deps
- add finish step ui
- add translation

* Mon Sep 17 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt2
- add backend for torque setup

* Mon Sep 10 2007 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- improve ldap admin password dialog

* Mon Sep 03 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
