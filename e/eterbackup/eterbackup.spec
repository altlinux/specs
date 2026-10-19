Name: eterbackup
Version: 1.13
Release: alt1

Summary: Etersoft backup tools for journaling backup

License: AGPLv3
Group: System/Configuration/Packaging
Url: https://github.com/vitlav/eterbackup

Packager: Vitaly Lipatov <lav@altlinux.ru>

# git-clone http://git.etersoft.ru/projects/korinf/eterbackup.git
Source: ftp://updates.etersoft.ru/pub/Etersoft/Sisyphus/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

Requires: zpaq >= 715

%description
Etersoft Backup Tools intended for resolve typical backup tasks.
- eterpack is a tool for condensing files from a directory tree to one archive file.
- etertimemachine is a tool for backup and/or rotate file tree every time.

See detailed russian description here: http://wiki.etersoft.ru/Eterbackup

%prep
%setup

%install
# install to datadir and so on
%makeinstall version=%version-%release

#mkdir -p %buildroot%_sysconfdir/bash_completion.d/
#install -m 0644 bash_completion/erc %buildroot%_sysconfdir/bash_completion.d/erc

# shebang.req.files
#chmod a+x %buildroot%_datadir/%name/{erc-}*

%files
%doc README.md LICENSE TODO
%_bindir/eterpack
%_bindir/eterremove
%_bindir/etertimemachine
%_bindir/eterattrstore
#%_datadir/%name/
%_man1dir/*
#%_sysconfdir/bash_completion.d/erc

%changelog
* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 1.13-alt1
- eterpack, eterremove: remove obsolete TODO comments
- check_code.sh: drop unneeded SC2154 and SC2002 exclusions
- TODO: remove done items
- etertimemachine: sync symlinks pointing outside the tree (do not use rsync --safe-links)
- tests: etertimemachine syncs symlinks pointing outside the tree
- eterpack: do not keep parts without changes (zpaq adds a 104 bytes part on every run)
- tests: updates without changes add no parts
- eterpack: add compact command to remove empty parts
- tests: eterpack compact
- README, CLAUDE.md, TODO: describe empty parts, compact and --rollback N
- eterpack: stop when the index is missing or a part would follow a gap (do not move valid parts to .broken)
- tests: update with a missing index or missing parts
- TODO: merge the compact and zpaq rotation items
- eterpack, eterattrstore: remove CHECKME notes (eterattrstore does not use rhas)
- eterpack: skip dirs below an excluded path in dirs.list
- eterpack, eterattrstore: do not save special files in excluded dirs
- eterpack, eterattrstore: compare owner/group, mode and special files with the saved metadata
- eterpack: test checks that every dir from dirs.list has its archive
- eterpack: add --exclude-from option
- eterpack: add info command (archives with their versions and sizes)
- etertimemachine: set the rotate status only while rotating (rotate --force left it set)
- etertimemachine: lock the target dir and continue interrupted rotate, sync and delete
- etertimemachine: add --thinner lastN (keep N last dated dirs)
- eterremove: rename remove_short_paths to keep_deepest_paths
- tests: compare of attributes and special files, special files in excluded dirs
- tests: eterpack --exclude-from, info, check of dirs.list
- tests: etertimemachine interrupted runs, lock and --thinner lastN
- tests: run the POSIX sh scripts with dash (TEST_SH=dash)
- README, CLAUDE.md: describe compare of attributes, info, --exclude-from and etertimemachine recovery
- TODO: remove done and obsolete items

* Sun Oct 18 2026 Vitaly Lipatov <lav@altlinux.ru> 1.12-alt1
- eterpack: do not write metafiles to the source tree, save attrs inside followed links
- tests: read-only source, reserved metafile names, old backups, --followlinks attributes
- README, CLAUDE.md: describe metafiles location and drop fixed limitations

* Sat Oct 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- etertimemachine: do not sync with --inplace (it changed files of the previous snapshot)
- etertimemachine: fix --method number
- eterremove: --size removes the oldest files, not the newest
- eterremove: never remove the working dir and its parents
- eterpack: fix source path with spaces (only root files were packed)
- eterpack: fix --password with spaces
- eterpack: make compare work and exit with 1 if there are differences
- eterpack: fail extract on zpaq errors and on dirs without archives
- eterpack: fix --singlearchive with --depth 2 and more
- eterpack: store --followlinks dirs under the link names
- eterpack: support names started with '-'
- eterpack: keep empty dirs above the packing depth
- eterpack: mark removed files and dirs as removed in the backup
- eterpack: do not run two updates of the same backup at once
- eterattrstore: save special files in sv4cpio format (no ustar name limits)
- rewrite tests on bats, run them in a container (make check)
- README: describe what is used and the limitations

* Sat Oct 17 2026 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt1
- eterpack: allow repeatable --exclude option (closes: #32816)
- eterpack: fix packing root files with spaces and special chars in names

* Mon Feb 18 2019 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt1
- eterpack: add --rollback option
- eterpack: improve and fix status support (add .last-updated)
- eterpack: add check for dir with source backup

* Mon Feb 26 2018 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- eterpack: autoremove broken files

* Mon Feb 12 2018 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- eterpack: add --password support
- eterpack: rewrite options parsing

* Fri Feb 02 2018 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- eterpack: add --singlearchive support

* Wed Jan 31 2018 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- etertimemachine: fix help
- add shellcheck script, do small fixes
- eterpack: add --followlinks support

* Mon Aug 07 2017 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- eterpack: add checking if archive is found
- eterpack: create target dir when create one file archive
- eterpack: fix script name (eterpack, not eterbackup)
- eterpack: add zpaq version checking
- eterpack: user MAXDEPTH/MINDEPTH
- eterpack: rename list_files to list_rootfiles
- eterpack: pack extra empty dirs also
- eterpack: use -index option from zpaq 7.10
- eterpack: comment out incorrect reldir checking
- eterpack: use root name for root zpaq archive
- eterpack: use var for version and need zpaq version
- implement eterpack status
- update TODO

* Tue Apr 19 2016 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- require zpaq 710
- eterremove: add test for file modified order, fix error (eterbug #10728)
- eterpack: add warning about only only --exclude is supported

* Fri Apr 01 2016 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- pack missed eterattrstore
- eterpack: add echo command
- eterremove: add shift arg

* Wed Aug 26 2015 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- eterattrstore: do not pack sockets
- eterremove: check only files during by size removing

* Tue Aug 18 2015 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- pack eterremove command
- add eterattrstore: separate command for save&restore special files and file attrs
- eterpack: use external eterattrstore
- update eterpack man page, add backup/restore sinonyms addition to update/extract

* Wed Aug 12 2015 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- eterpack: rewrite exclude working (use dir name or path)
- extend and improve exclude tests

* Wed Aug 12 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- eterpack: fix exclude issues
- eterpack: fix compare for single archive

* Wed Aug 12 2015 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- add eterremove man and fix help
- eterremove: add --size N (in Gb) support for limit total file size
- etertimemachine: add initial --link support, improve help
- etertimemachine: add --inplace --safe-links --hard-links to rsync

* Tue Aug 11 2015 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- overall fixes
- etertimemachine: add delete with log2 algorithm using
- add eterremove for remove obsoleted dirs/files

* Sun Jul 19 2015 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- bugfix release
- eterpack: fix find special files
- eterpack: support for --depth 0 (create one archive per all directory tree)

* Sun Jul 19 2015 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- eterpack: add compare command (compare archive with directory without unpacking)
- eterpack: fix packing root files in depth 2 or more archives
- eterpack: add --checksum option for force check file contains
- etertimemachine: fix first time copying
- eterpack: add save attributes and special files via metastore and pax
- improve tests

* Sun Jul 19 2015 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- eterpack: add --execute option
- eterpack: backup root files too
- eterpack: fix DESTDIR heuristic
- eterpack: write dirs.list and files.list

* Sat Jul 18 2015 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- initial build for ALT Linux Sisyphus
