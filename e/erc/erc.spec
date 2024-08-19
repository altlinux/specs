Name: erc
Version: 1.1.3
Release: alt1

Summary: Universal Archive Tool

License: AGPLv3
Group: File tools
Url: https://github.com/Etersoft/erc

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: http://git.etersoft.ru/projects/korinf/erc.git
Source: ftp://updates.etersoft.ru/pub/Korinf/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

# who really does all our work
Requires: patool >= 1.1
# also we have alternative
#Requires: p7zip

%description
Etersoft Universal Archive Tool is the archive manager for any format.
It provides universal command line interface to any archive manager.
Patool is used for real work with archives.

See detailed russian description here: http://wiki.etersoft.ru/ERC

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
%doc README LICENSE TODO
%_bindir/erc
%_bindir/unerc
%_bindir/ercat
%_datadir/%name/
%_man1dir/*
#%_sysconfdir/bash_completion.d/erc

%changelog
* Thu Aug 15 2024 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- erc: add some comments
- replace 7z to tar in unpack (eterbug #17370)

* Mon Apr 08 2024 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- ercat: fix to allow filenames with spaces
- erc: add AppImage unpacking

* Fri Sep 22 2023 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- ercat: add --quiet support
- fixed 7z working with spaces in names
- added assume Yes on all queries for unpack with 7z

* Sat Jul 29 2023 Vitaly Lipatov <lav@altlinux.ru> 1.1.0-alt1
- erc-sh-archive: get_archive_type(): hide warning for missed file
- erc: add support for repack tgz->tar in 7z mode
- erc: use tar for tar creating
- erc-sh-functions: improve realpath workaround to support -s
- erc: don't expand symlink in a path to a archive
- erc: extract_archive(): add tgz unpacking

* Sat Apr 22 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0.3-alt1
- erc: fix info about help if run with no args
- erc-sh-archive: add diag message if backend is missed
- erc-sh-archive: add checking for 7zr and 7zz

* Wed Apr 19 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0.2-alt1
- erc-sh-archive: add ERC_BACKEND parsing

* Mon Apr 10 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0.1-alt1
- erc-sh-functions: sync which using
- ercat: use is_command instead of which
- erc-sh-functions: improve color functions (don't use tput directly)

* Fri Mar 31 2023 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- use 7z as backend if patool is missed
- erc: add --use-7z and --use-patool to force using patool or 7z

* Wed Sep 28 2022 Vitaly Lipatov <lav@altlinux.ru> 0.9.6-alt1
- erc: fix unerc support
- erc-archive: add .tar.xz and .tar.std

* Thu Nov 19 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- erc: improve print supported formats
- erc: add exe archives support (hack)

* Tue Mar 10 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.4-alt1
- ercat: add check for unpack binary and epm assure
- ercat: add .zst (.zstd) support

* Sun Oct 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.3-alt1
- add support for pack to zip if one dir arg was received

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- fix get extension: check for tar.* firstly
- allow get type of archive for nonexists files too

* Mon Jul 10 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- ercat: add lz4 support

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- skip repack for the same input and output file
- erc: add add command
- erc: add tgz format recognize
- pack unerc

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- erc: add -f (--force) for override target, improve test

* Tue Aug 04 2015 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- add zpaq and pax to supported formats
- erc: add options support and implement --quiet
- add unerc command

* Fri Feb 20 2015 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- improve is_target_format to check against supported target formats

* Tue Oct 15 2013 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- erc-archive: fix basename issues
- use bash for all scripts (welcome to debug with dash!)

* Tue Sep 03 2013 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- ercat: add support for plain text files too
- update README, add man pages

* Fri Jul 26 2013 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- small fixes
- erc: enable search and improve help

* Fri Jul 26 2013 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- erc: unpack archive by default
- erc: add support for target arch to create and repack
- introduce ercat: cat any archive to stdout (like bzcat)

* Thu Jul 25 2013 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
