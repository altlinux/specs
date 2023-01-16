Name: deploy
Version: 0.3.9
Release: alt1

Summary: Script and set of ansible roles to deploy system services
License: GPL-3.0+
Group: System/Configuration/Other
Url: https://altlinux.org/Deploy

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Source: %name-%version.tar

Requires: python3
Requires: ansible

%description
deploy is script using predefined ansible playbooks to deploy some
system services like PostgreSQL or Moodle.

%prep
%setup

%install
%makeinstall_std

%files
%_bindir/%name
%_datadir/%name

%changelog
* Mon Jan 16 2023 Andrey Cherepanov <cas@altlinux.org> 0.3.9-alt1
- postgresql: use any available postgresql-server without version.

* Wed Aug 31 2022 Andrey Cherepanov <cas@altlinux.org> 0.3.8-alt1
- apache: disable module mod_php7.

* Tue Aug 23 2022 Andrey Cherepanov <cas@altlinux.org> 0.3.7-alt1
- Use PHP 8.0.

* Mon Nov 15 2021 Andrey Cherepanov <cas@altlinux.org> 0.3.6-alt1
- mariadb: fix service run at boot because ansible does not support service aliases.

* Thu Oct 28 2021 Andrey Cherepanov <cas@altlinux.org> 0.3.5-alt1
- nextcloud: add hostname to main configuration file.

* Wed Oct 27 2021 Andrey Cherepanov <cas@altlinux.org> 0.3.4-alt1
- nextcloud: backup config file with .new extension.

* Tue Oct 26 2021 Andrey Cherepanov <cas@altlinux.org> 0.3.3-alt1
- nextcloud: ignore deploy error (see https://github.com/nextcloud/server/issues/22590).
- nextcloud/password: use ncadmin username, fix memory warning.

* Mon Oct 25 2021 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- nextcloud: use ncadmin for admin user, show database name and database username.

* Sat Jul 17 2021 Andrey Cherepanov <cas@altlinux.org> 0.3.1-alt1
- Adapt for latest version of Mediawiki and Nextcloud.
- mediawiki: fix password generation program.

* Fri Jul 16 2021 Andrey Cherepanov <cas@altlinux.org> 0.3-alt1
- Add rule for: apache, mariadb, mediawiki, nextcloud, moodle. 

* Thu Jun 04 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.2.1-alt1
- Add option to show available parameters

* Fri May 29 2020 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Fix check return code of playbook run.
- Check for modules dir and superuser privileges.
- Pass variables from command-line paramenters.

* Thu May 21 2020 Andrey Cherepanov <cas@altlinux.org> 0.1.1-alt1
- postgresql: check /var/lib/pgsql/data/global for initialized database.

* Wed May 20 2020 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- Initial build in Sisyphus.
