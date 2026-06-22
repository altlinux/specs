Name: erc
Version: 1.1.10
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
%doc README.md LICENSE TODO
%_bindir/erc
%_bindir/unerc
%_bindir/ercat
%_datadir/%name/
%_man1dir/*
#%_sysconfdir/bash_completion.d/erc

%changelog
* Sun Jun 07 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1.10-alt1
- ercat: return error code on failed files like cat does
- erc: add extract_tar_stdin helper
- erc: reuse extract_tar_stdin in extract_command
- erc: add makeself (.run) archive extraction support
- erc: add makeself repack support via extract_makeself_tar
- erc-sh-archive: prefer 7zz (official 7-Zip) over deprecated p7zip
- erc: derive ercat path from script name for eepm compatibility
- erc: make --quiet suppress 7z output
- erc: fix symlink support in 7z create (-l -> -snl)
- erc: fix duplicate -y flag with 7zz
- man: rewrite erc.1 with all commands, options and extraction rules
- erc: fail on incomplete AppImage extraction via 7z, suggest squashfs-tools
- erc: always name extracted directory after archive basename
- erc: fix lost exit code from extract commands
- erc: add --here/--no-subdir to extract without creating subdirectory
- erc: add --flat/-j/--junk-paths to extract stripping directory structure
- erc: fix --help examples and add extraction rules
- erc: fix --flat for special archives (AppImage, squashfs, exe, run)
- erc: find squashfs offset by magic for cross-arch AppImage extraction
- erc: fix --flat with 7z for special archives (use absolute paths)
- erc: add ERC_USE_7Z_SQUASHFS to force 7z backend for squashfs
- erc: use -snld flag for 7z 25.01+ to preserve symlinks with ../
- erc: document system directory exception in --help
- erc: apply subdir logic for -C and special archives
- erc: add dotglob when counting items in move_from_tdir/move_to_target_dir
- erc: clean up temp dir in extract_special_archive on unsupported type
- erc: add -no-xattrs to unsquashfs to avoid exit code 2 on xattr failures
- erc: quote $(pwd) in mktemp to support paths with spaces
- erc: check for 7z backend availability before using it for unsupported types
- erc: fall back to 7z for tar.* when native (de)compressor is missing

* Thu Feb 19 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1.9-alt1
- ercat: use pigz when available for faster decompression
- ercat: use parallel decompressors (pigz, pbzip2, pixz) when available
- erc: refactor AppImage extraction with --appimage-offset support
- erc-sh-archive: add content detection via file(1) mime-type
- erc: get_archive_type uses file(1) with extension priority
- ercat: add stdin support, decomp/unpack_type refactor
- erc: add basename command
- erc: support repack for any format pair with 7z backend
- add new README.md with project description and usage examples
- erc: add -C/--directory/--extract-to/--destination/--outdir to extract to specified directory
- ercat: skip broken files instead of aborting when processing multiple files

* Fri Jan 09 2026 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt1
- erc fix: prevent code execution via AppImage and regex injection
- erc fix: quote shell variables to prevent word splitting
- erc fix: improve safety of mv, mktemp and glob operations
- erc: add snap extraction, refactor squashfs handling

* Tue Dec 23 2025 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt1
- erc: fix -b and other single-letter commands (ALT bug 57263)
- erc: fix empty args check
- erc: add missing -h flag for tar.bz2 extraction
- erc: fix wrong variable in repack loop
- erc: fail when target exists without -f flag
- erc-sh-archive: fix list_formats output for 7z backend

* Wed Dec 10 2025 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt1
- erc: add support for repack zip->tar with 7z
- erc: fix path to unpacked archives
- erc-sh-archive: add .7Z detection

* Thu May 22 2025 Vitaly Lipatov <lav@altlinux.ru> 1.1.5-alt1
- erc-sh-archive: Use 7za only if there is no 7z (eterbug #18296)
- erc: add squashfs support
- erc: unpack exe to subdir, add dll unpacking support

* Fri Mar 21 2025 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- erc: add missing quotes for $tdir
- unpack tar.bz2 archives using tar (eterbug #17830)

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
