Name: alterator-bacula
Version: 0.8
Release: alt1

Source:%name-%version.tar

%add_findreq_skiplist %_libexecdir/alterator/backend3/bacula-restore

%define backupadmin_group backupadmin

Summary: module for Bacula backup system
License: GPL
Group: System/Configuration/Other
Requires(pre): shadow-utils
Requires: bacula-storage bacula-storage bacula-client bacula-dir
# require console timeout feature
Requires: bacula-console >= 3.0.2-alt6
Requires: ntfs-3g
Requires: alterator >= 4.10-alt5
Requires: alterator-l10n >= 2.7-alt19
Requires: alterator-bacula-functions
Requires: alterator-sh-functions alterator-net-functions alterator-hw-functions >= 0.6-alt1
Conflicts: alterator-lookout < 2.1-alt1
Conflicts: alterator-fbi < 5.20-alt1

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

%files
%config(noreplace) %_sysconfdir/alterator/bacula
%_datadir/alterator/ui/*
%_alterator_backend3dir/*
%_datadir/alterator/applications/*
%_datadir/alterator/steps/*
%_datadir/alterator/type/*

%changelog
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
- add UI for backup server

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
