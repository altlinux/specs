%define _altdata_dir %_datadir/alterator

Name:     alterator-mass-management
Version:  0.1.6
Release:  alt1

Source:   %name-%version.tar

Packager: Andrey Cherepanov <cas@altlinux.ru>

Summary: Alterator module for configuration mass management
License: GPLv3+
Group:   System/Configuration/Other

BuildArch: noarch

BuildPreReq: alterator >= 4.10-alt5
Requires: alterator >= 4.10-alt5 alterator-sh-functions >= 0.12-alt1
Requires: alterator-net-eth alterator-dhcp
Requires: ansible >= 1.9.2
Requires: git-core

%define amm_pull_user _alterator_mass_management_pull

%description
Alterator module for configuration management.

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%pre
getent passwd %amm_pull_user > /dev/null || \
%_sbindir/useradd -M -r -U -c 'Alterator-mass-management user for ansible-pull access' \
     -d /var/lib/alterator-mass-management/tasks %amm_pull_user 2> /dev/null ||:

%files
%config %_localstatedir/alterator-mass-management/ansible.cfg
%_datadir/alterator/applications/*
%_datadir/alterator/ui/*/
%_datadir/%name/common-ansible-tasks/
%_alterator_backend3dir/*
%_libexecdir/%name/scripts/worker
%_libexecdir/%name/scripts/worker-actions/
%_libexecdir/%name/scripts/amm-pull-cronjob
%dir %_logdir/%name
%dir %_localstatedir/alterator-mass-management/tasks
%attr(701, root, root) %dir %_localstatedir/alterator-mass-management/keys


%changelog
* Thu Oct 08 2015 Andrey Cherepanov <cas@altlinux.org> 0.1.6-alt1
- Remove \r from imported files

* Mon Sep 28 2015 Andrey Cherepanov <cas@altlinux.org> 0.1.5-alt1
- Completely support of pull mode

* Thu Sep 17 2015 Andrey Cherepanov <cas@altlinux.org> 0.1.4-alt1
- Fill and apply profile
- Initial support of pull mode
- Split main stript to sibtask-based scripts

* Fri Aug 21 2015 Andrey Cherepanov <cas@altlinux.org> 0.1.3-alt1
- Implement profile apply (sem@)
- Extract backend actions from worker script (sem@)
- Support role (for master, slave and slave with pull mode) (cas@)
- Support remote server for logging in worker script for pull-mode (cas@)

* Fri Jul 10 2015 Andrey Cherepanov <cas@altlinux.org> 0.1.2-alt1
- Log date on client too
- Fix tymesync arguments handling

* Wed Jul 08 2015 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1
- Key management and task restart support

* Fri Jun 26 2015 Andrey Cherepanov <cas@altlinux.org> 0.1.0-alt1
- Initial build in Sisyphus

