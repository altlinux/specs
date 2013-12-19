Name: alterator-bacula
Version: 1.1
Release: alt1

Source:%name-%version.tar

%add_findreq_skiplist %_libexecdir/alterator/backend3/bacula-restore

%define backupadmin_group backupadmin

Summary: module for Bacula backup system
License: GPL
Group: System/Configuration/Other
Requires(pre): shadow-utils
Requires: bacula-storage bacula-client bacula-dir
# require console timeout feature
Requires: bacula-console >= 3.0.2-alt6
Requires: ntfs-3g
Requires: alterator >= 4.10-alt5
Requires: alterator-l10n >= 2.7-alt19
Requires: alterator-sh-functions alterator-net-functions alterator-hw-functions >= 0.6-alt1
Requires: passwdqc-utils
Requires: bacula-director-mysql
Requires: MySQL-server-control
Requires: mysql-server
Requires: mysql-client
Conflicts: alterator-lookout < 2.1-alt1
Conflicts: alterator-fbi < 5.20-alt1

Provides:  alterator-bacula-functions = %version-%release
Obsoletes: alterator-bacula-functions < %version-%release
Provides:  alterator-backup-server = %version-%release
Obsoletes: alterator-backup-server < %version-%release
Provides:  alterator-distro-backup-server = %version-%release
Obsoletes: alterator-distro-backup-server < %version-%release
Provides:  alterator-bacula-server = %version-%release
Obsoletes: alterator-bacula-server < %version-%release

BuildArch: noarch

BuildPreReq: alterator >= 4.10-alt5

%description
module for Bacula backup system

%pre
/usr/sbin/groupadd -r -f %backupadmin_group

%prep
%setup -q

%build
%make_build

%install
%makeinstall
%define altdir %_datadir/alterator
mkdir -p %buildroot/%altdir/{applications,desktop-directories}
install -m644 desktop-directories/*.directory %buildroot/%altdir/desktop-directories/

for n in archive settings clients schedule; do
  sed 's/X-Backup-Server/X-Alterator-Backup/' \
     applications/bacula-server-$n.desktop \
     > %buildroot/%altdir/applications/bacula-$n.desktop
done

%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 postinstall.d/*.sh %buildroot%hookdir/

%post
mkdir -m 0750 /srv/backup
chown -R bacula:bacula /srv/backup
/etc/init.d/alteratord restart
alterator-cmdline /bacula-director action init

%files
%config(noreplace) %_sysconfdir/alterator/bacula
%_datadir/alterator/ui/*
%_datadir/alterator/ui/bacula/local-backup/
%_alterator_backend3dir/*
%_alterator_backend3dir/bacula-local-backup
%_datadir/alterator/applications/*
%_datadir/alterator/applications/bacula-local-backup.desktop
%_datadir/alterator/steps/*
%_datadir/alterator/type/*
%_bindir/*
%_sbindir/*
%hookdir/*
%altdir/desktop-directories/*

%changelog
* Thu Dec 19 2013 Andrey Kolotov <qwest@altlinux.org> 1.1-alt1
- Recovered local backup.

* Wed Dec 18 2013 Andrey Kolotov <qwest@altlinux.org> 1.0-alt2
- Added script from package alterator-distro-backup-server:
  * in sbin/bacula-reset-settings.

* Mon Dec 16 2013 Andrey Kolotov <qwest@altlinux.org> 1.0-alt1
- Remove options with mysql database bacula
- Create mysql database after install package

* Fri Dec 06 2013 Andrey Cherepanov <cas@altlinux.org> 0.9-alt2
- Replace Conflicts by Provides/Obsoletes pairs

* Sat Jun 29 2013 Andrey Kolotov <qwest@altlinux.org> 0.9-alt1
- unification with package alterator-bacula-functions:
  * moved bin files;
  * changed Makefile.
- unification with alterator-bacula-server:
  * add postinstall.d/50-reset-bacula.sh;
  * add desktop-directories/backup.directory.
- add desktop files from alterator-backup-server
- add functions in backend3/bacula-director:
    - daemon_status()
    - daemon_on()
    - daemon_off()
- add functions in bin/bacula-sh-functions:
    - mysql_create_database_bacula()
    - mysql_update_database_bacula()
    - mysql_remove_database_bacula()
    - bacula_storage_set_password()
    - bacula_director_set_password()
    - bacula_storage_get_password()
    - bacula_director_get_password()
- ui director html:
  * new option with mysql database bacula:
    - create, update and remove database;
    - auto add new user 'bacula' in mysql;
    - add generate password to bacula.
  * add change password for director
  * add change password fo storage
  * add director server on/off
  * add storage server on/off
- new require passwdqc-utils for generate password

* Sun Apr 21 2013 Michael Shigorin <mike@altlinux.org> 0.8-alt2
- drop reportedly broken local-backup UI and desktop file (closes: #28854)

* Tue Apr 19 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.8-alt1
- chroot after restore added (if alteratord & alterator-grub are found)

* Wed Mar 9 2011 Alexandra Panyukova <mex3@altlinux.ru> 0.7-alt14
- alterator-bacula-functions separation

* Fri Feb 18 2011 Alexandra Panyukova <mex3@altlinux.ru> 0.7-alt13
- storage address field added

* Wed Dec 22 2010 Lenar Shakirov <snejok@altlinux.ru> 0.7-alt12
- restore paths with spaces fixed

* Wed Oct 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt11
- add storage and director status infromation to "archive" screen
- new bacula-status backend
- add interface for bacula director administration (closes: #21800)

* Mon Oct 12 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt10
- use color rows
- improve schedule table

* Thu Oct 08 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt9
- use bconsole timeout feature.
- bacula-client-backup backend: clear temporary files.
- list active jobs only in tables (closes: #21246)
- automatically update job tables in background (closes: #21257)
- little interface improvements (scrolling, remove with:100%% from div styles, add padding etc.)

* Fri Oct 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt8
- get client's fd config from template (closes: #21794)
- redesign template infrastructure

* Thu Oct 01 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7-alt7
- remove unused bacula_backupcatalog_set_catalog_password

* Thu Sep 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt6
- client-backup/client ui:
   * improve confirmation dialog;
   * show message on successful update;
   * use accordion widget, move fileset edition into this dialog from separate page.

* Fri Sep 04 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt5
- fix time calculation

* Fri Aug 28 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt4
- add backupadmin group

* Wed Aug 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt3
- add bacula-select installer's step

* Mon Aug 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt2
- bacula/local-backup html ui: show restore status
- fix i18n in enumerations (closes: #21076)
- bacula_restore_all: explicitly specify client and fileset

* Thu Aug 13 2009 Stanislav Ievlev <inger@altlinux.org> 0.7-alt1
- ui: always use workflow 'none'
- new feature: download client's config file
- always cancel local jobs by name

* Wed Jul 08 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt8
- add templates for client (win/linux)

* Mon Jun 29 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt7
- restore something to different client/path feature

* Fri Jun 26 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6-alt6
- remove strict bacula-director-sqlite3 dependency
- add function to set Catalog password (for MySQL database)

* Thu Jun 25 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt5
- fix filelist listing
- fileset ui: print client's name
- fix bacula_pool_clear(), bacula_pool_del(): read volume names from database for purge, read volume names from filesystem

* Tue Jun 23 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt4
- use message class from branding

* Thu Jun 18 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt3
- minimize number of daemon reloading
- cancel client's jobs on cleanup and delete actions
- use 'Enabled' parameter to turn off schedulling
- more beautiful restore progress

* Mon Jun 15 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt2
- client-backup UI improvements:
  * show restore progress
  * client, schedule, archive: hide main page if no clients found.
  * add parameter constraints
- add functions:
    - bacula_console_query_cmd() - common entry point for all console requests
    - bacula_file_get_progress()
    - bacula_console_set_director()
    - bacula_storage_set_director()
    - bacula_file_set_director()
    - bacula_director_get_name()
    - bacula_director_set_name()
- optimize functions (use single sql query instead of sed and grep):
    -  bacula_local_backup_list() 
    - optimize bacula_local_backup_date_list()
    - optimize bacula_job_status()
    - optimize bacula_job_list_active()
- fix functions:
    - bacula_config_*() - support section boundaries with comments, move section range generation into separate function
    - __parse_jobid(): copy output to stderr for debug
    - add simple check that restore job was started

* Tue Jun 09 2009 Stanislav Ievlev <inger@altlinux.org> 0.6-alt1
- finish redesign of local backup functions to support multiple clients
- add UIfunctions: for backup server

* Tue Jun 02 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt5
- restore: add ability to select backup date
- bacula-sh-functions: redesign API to support multiple clients

* Mon Jun 01 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt4
- allow to go to the next step on error
- remove restore_type support (don't need it, because we have removed 'backup user data' switch)
- redesign fileset support

* Fri May 29 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt3
- bacula_set_path: change file owner too

* Thu May 28 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt2
- redesign "advanced settings" dialog: edit exclude-list, cancel jobs
- restore: fix fstab creation
- update translations

* Tue May 26 2009 Stanislav Ievlev <inger@altlinux.org> 0.5-alt1
- automatically create default configuration for bacula at the first start
- change config file format, add support for "exclude list"
- little ui improvements:
   * enable/disable controls
   * show backup path for "system disk"
- improve restore process:
       * always chmod/chown backup directory
       * improve messages

* Fri May 22 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt2
- add step file

* Thu May 21 2009 Stanislav Ievlev <inger@altlinux.org> 0.4-alt1
- add qt ui
- add additional disk selection

* Tue May 19 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt2
- improve restore process (create devices, fix fstab)

* Fri May 15 2009 Stanislav Ievlev <inger@altlinux.org> 0.3-alt1
- add restore mode for installer

* Fri May 08 2009 Stanislav Ievlev <inger@altlinux.org> 0.2-alt1
- bugfixes
- improve ui (closes: #19857)

* Wed Apr 29 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt4
- add script to restore sqlite3 catalog from backupdir

* Wed Apr 15 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt3
- fix work if /srv is a symlink (readlink -e /srv)

* Tue Mar 31 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- fix menu file

* Tue Mar 24 2009 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
