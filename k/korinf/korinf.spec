Name: korinf
Version: 2.1.9
Release: alt1

Summary: Korinf multidistro single source build system

License: AGPLv3
Group: Development/Other
Url: http://freesource.info/wiki/korinf

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/vitlav/korinf
Source: %name-%version.tar

BuildArchitectures: noarch

Requires: eepm >= 2.1.1
Requires: etersoft-build-utils >= 2.5.2
Requires: alien >= 8.86-alt3
Requires: lsof

%description
This package contains Korinf multidistro build system.

%prep
%setup

%build
%make

%install
%makeinstall

%files
%doc README TODO NEWS AUTHORS COPYING
%_bindir/korinf
%_bindir/korexec
%_bindir/korlogin
%dir %_sysconfdir/eterbuild/lists/
%dir %_sysconfdir/eterbuild/rpmopt/
%config(noreplace) %_sysconfdir/eterbuild/lists/*
%config(noreplace) %_sysconfdir/eterbuild/rpmopt/*
%config(noreplace) %_sysconfdir/eterbuild/korinf
%config(noreplace) %_sysconfdir/eterbuild/linked
%config(noreplace) %_sysconfdir/eterbuild/remote
%_datadir/eterbuild/korinf/

%changelog
* Fri Dec 15 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.9-alt1
- install: fix --show-command-only issue when there are no args
- korinf: print source src.rpm name
- check_reqs: do not check requires for debug packages

* Wed Oct 18 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.8-alt1
- add install initial buildreqs without internal eepm (bootstrap)
- update repo for publish
- update system list
- update x86_64 linked for Debian/9 and Ubuntu 17.10
- lists: update systems

* Sun Jul 23 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.7-alt1
- update nfound script
- fix su missed: set PATH for chrooted
- build: do not remove broken package files
- lists: add missed RHEL
- add ALT c7, c8
- install: add build-essential for deb
- build_for_new_system.sh: run install buildreqs firstly

* Wed Apr 05 2017 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- add bin-rx scripts, fix path to RX@Etersoft
- add source filename checking
- copying: fix debug subpackages moving to extra
- add build script for PG9.6
- funcs/build: refactoring and any package checking
- add eepm to WINE@Etersoft downloading
- fix build on latest ArchLinux

* Wed Dec 21 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.5-alt1
- add check_distr_vendor.sh (moved from rpm-build-altlinux-compat)
- last_rpm: use correct rpmquery command
- run eepm with /dev/null input
- move RX@Etersoft to pvt

* Mon Dec 12 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- checked with rpm-4.13
- fix typo in INITIALBOOTSTRAP (fix rpm-build-altlinux-compat bootstrap)
- fix epm checking
- update lists, add Fedora 25 and Ubuntu 16.10
- add x86_64/GosLinux
- fix last_rpm against broken rpmquery -p for src.rpm
- add SRPMGPGCHECKING for enable rpmsign --checksig (disabled since now by default)

* Thu Jul 21 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.3-alt1
- use epm print binpkgfilelist instead obsoleted internal func get_binpkg_list
- skip libx11-private requires in dh_shlibdeps (eterbug #11025) drop setarch
- replace rpmvercmp with rpmevrcmp if possible
- fix src.rpm compatible packing
- update systems list, add x86_64/AstraLinux
- improve build-strap for eepm and rpm-build-altlinux-compat
- copying: fix dir checking, do not create MD5SUM

* Thu Apr 14 2016 Vitaly Lipatov <lav@altlinux.ru> 2.1.2-alt1
- converts/deb: do not replace depends
- write dependences only when ALTLinux/Sisyphus, do not fatal
- update lists
- windows: support .gear/mingwbuild.sh for windows build
- use rpmbp instead rpmbh -n
- robot: skip check_dist when run for license only task
- jump to 2016 year
- drop local alien convert code
- list: strict grep for versions
- add ALT Linux p8 support
- rename Debian/?.0 to Debian/? (eterbug #11093)

* Sat Nov 07 2015 Vitaly Lipatov <lav@altlinux.ru> 2.1.1-alt1
- windows: add korinf/mingwbuild.sh
- fix bug with 2 file created
- korinf: print help when --help in the last position
- switch to convert deb packages via target system alien (eterbug #8345)
- install: add hack to install alien, fakeroot and debhelper requires for deb

* Mon Aug 24 2015 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- korinf: full rewrite, fix args handling
- fix korinf command using

* Sun Aug 23 2015 Vitaly Lipatov <lav@altlinux.ru> 2.0.12-alt1
- remove unsupported ALT Linux 4.0/4.1
- last_rpm: use more correct rpmevrcmp
- remove suddenly printer package name
- add Fedora/22

* Tue Jun 16 2015 Vitaly Lipatov <lav@altlinux.ru> 2.0.11-alt1
- fix linked systems list, update system list
- mount: try to umount twice
- mainbuild: never override links
- converts/archlinux: use number part of version

* Fri Feb 06 2015 Vitaly Lipatov <lav@altlinux.ru> 2.0.10-alt1
- get_target_list: fix TARGETPATH assert
- set_rebuildlist: remove TARGETPATH assert

* Sat Oct 04 2014 Vitaly Lipatov <lav@altlinux.ru> 2.0.9-alt1
- korlogin: comment out local checking
- install: use quotes for epm install (due parenteses in a packages names)
- update system lists
- selta: use Postgre link as needed PG package dir
- parse link to get real PG path
- windows: set correct status after copying

* Mon Jun 09 2014 Vitaly Lipatov <lav@altlinux.ru> 2.0.8-alt1
- update lists, add FreeBSD/8.4
- rewrite windows build script
- cleanup install script
- major fixes for fix FreeBSD build

* Sat Mar 29 2014 Vitaly Lipatov <lav@altlinux.ru> 2.0.7-alt1
- update system lists

* Tue Mar 11 2014 Vitaly Lipatov <lav@altlinux.ru> 2.0.6-alt1
- many fixes
- simply experiment's with build for Windows in Korinf
- alfa-release code of build TBZ2 for Gentoo with debug functions
- korlogin: update hasher support (pass arch, root mode, initialize only if first time)
- message: do not cut .failed file if called second time (eterbug #9553)

* Tue Oct 22 2013 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- korinf/mount: improve: make /tmp from tmpfs, fix devpts mount
- korinf: fix options parsing (do options really unpositional)

* Sat Oct 12 2013 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- korexec, korlogin - add small support for ALT Linux
- replace get_rpm_sources with get_sources_dir (rewrite), drop check_and_refresh_package_wine
- add korexec install, fix korlogin install

* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- separate write alt deps to separate file
- tools/publish: do not republish packages with the same name (see eterbug #8890)
- robot/products/wine-etersoft: do not follow links if it changed arch
- introduce korexec - tool for run any command in distros
- rearrange lists, add CUR version for ArchLinux and Gentoo
- distro: add check and install build requires before build
- rewrite korexec
- rewrite korlogin with common mount functions

* Thu Feb 21 2013 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- filelist: will output one big package for FreeBSD, ArchLinux, Gentoo, Solaris, Windows
- big update etc/lists
- introduce new convert_archlinux, which makes nice pkgs with depends: can build wine
- need etersoft-build-utils 2.0.23 version
- log: use 22 instead 2 status code
- replace nxclient with opennx

* Thu Feb 07 2013 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- convert: drop non lib requires only for wine on Ubuntu
- update lists: add Ubuntu 12.10, Debian 7, Fedora 18
- run force build when try build again
- convert: add freebsd support
- add build support for p7 and cert6
- move assert_var to etersoft-build-utils 2.0.18
- improve run_in_chroot, add initial remote build
- message: introduce exit_now and use it in fatal, warning, error
- intro /etc/remote for remote systems configuration, add to run_in_chroot remote support
- build/rpm: rewrite with run_in_chroot using, run script via pipe
- run_in_chroot: add --user USER support
- install: use epm install --auto
- check_reqs: use rpmreqs from repo if possible

* Fri Aug 17 2012 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- release 2.0
- fast add epm support to run-script.sh
- install: use one-line args
- install: add packages from minimal build environment
- introduce -I for force install, -i now installs only for failed builds
- rewrite run_in_chroot: simpled and correct return state
- install: use direct install only for eepm and only if preinstalled epm is failed
- introduce -B (force build and install), change -b: now do things only if build needed
- cleanup and fix ArchLinux build
- install: use epm install instead internal case
- update/add install wine/gecko-mono script
- cront/build: always use -f

* Wed Aug 01 2012 Vitaly Lipatov <lav@altlinux.ru> 1.9.8-alt1
- check_reqs: use epm --skip-installed simulate instead filter_out_internal_packages
- fix run from logit before log initialization
- fix x86_64 linked
- introduce set_destlogdir and use it
- install_req: use epm --skip-installed install instead internal code
- check_reqs: drop try_install_by_list (use epm simulate)
- check_integrity: use epm integrity
- check-reqs: use epm instead run-script
- separate run in chroot in standalone func

* Sat Jul 21 2012 Vitaly Lipatov <lav@altlinux.ru> 1.9.7-alt1
- makeiso-selta: actualize script
- add wine-mono script
- add some hacks for package reqs (Ubuntu/12.04 and mandriva)
- use new rpmreqs for dependence generation
- improve tests
- install_req: use parse_dist_name inside
- use mount_linux with distr name as first arg
- introduce assert_var function and use it
- fix external get_distro_list using
- korinf: fix build_package return status
- checkreqs: add rules for Mandriva and SUSE
- improve get_bin_package: do not use MAILFILESLIST var
- install: do not ask for install from apt
- add build-any-package.sh, add prevcommit support
- remove debug packages from install list if already install it in /extra
- message: introduce error message function and use it
- make license file for RX@Etersoft
- fixed #8487 for Gentoo ebuild generation
- korinf: use -v for set version

* Tue May 22 2012 Vitaly Lipatov <lav@altlinux.ru> 1.9.6-alt1
- major rewrite
- add autobuild script for wine private
- add check-x86_64-wine.sh (eterbug #4550)
- add initial script for install wine on vanilla
- add status module with build status related functions and use it
- introduce check_reqs for test dependencies (deb only)
- rewrite copying
- do build output more pretty looks
- do not define BUILDROOT if not needed
- fixed bug #8410. Tested for Gentoo/2009
- fix run-script to allow any user, add scripts for remove packages, fix update/install
- fix Windows version, add x86_64/Windows
- improve rpm -> deb dependecies conversion (eterbug #8345)
- install: do apt-get -f install after dpkg -i
- install: install only not installed packages
- install: mark as failed if afterbuild install is failed
- install_req: convert reqs to target directly, without package conversion
- korinf: add -r/-R option for check install requires
- list: add support for include files from korinf/lists dir
- mainbuild: do not build twice linked systems
- mainbuild: do not just pass up-to-date packages
- mount: mount /dev/shm if possible
- move rpm-to-target part in separate convert file
- move to use DISTRNAME, DISTRVERSION, BUILDARCH, PKGVENDOR..
- rpm: add --without debug for nonrpm builds
- wine-etersoft: autorebuild fonts-ttf-ms

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.9.5-alt1.1
- Rebuild with Python-2.7

* Wed Jul 13 2011 Vitaly Lipatov <lav@altlinux.ru> 1.9.5-alt1
- add links for LinuxWizard, NauLinux
- build_for_new_system: rewrite for support separate build
- fix build FreeBSD 8.2

* Fri Jul 01 2011 Vitaly Lipatov <lav@altlinux.ru> 1.9.4-alt1
- add CentOS/6
- copying sources ever if build is broken
- add initial script for build all packages for new system
- mount: run su with -, skip login part
- robot: disable checking target dir existing
- update arobot-retouch.sh
- use PG 9.0 for SELTA since 1.1.0

* Mon May 23 2011 Vitaly Lipatov <lav@altlinux.ru> 1.9.3-alt1
- add cleancache for cleanup repos from obsoleted packages
- add grep for not found libs
- fix run-script (use newest functions)
- korlogin: fix system list, arch issues,
- new check product and change in list for SUSE
- run-script: add search and update
- script for postgre-etersoft9.0 added
- set emails/jabber in config
- some changes in freebsd script, and new script for postgres8.4 added
- update list_all_nfound script
- update systems list

* Mon Apr 04 2011 Vitaly Lipatov <lav@altlinux.ru> 1.9.2-alt1
- add test_ld - for test LD bugs
- add update_eterwine script
- build/rpm: define='_unpackaged_files_terminate_build 0'
- common: more strict check src.rpm
- main: fix ssh key checking (only for local key)
- worker: do interrupted if orphaned run is found

* Sat Feb 19 2011 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- add Debian 6.0
- build/hasher: build src.rpm in hasher, not installed spec
- check_integrity: skip ebuild, exe
- deprecate debug packages and source copying for proprietary packages
- do not use relative path to distr.list dir
- dropout BUILTSRPM, use TARGETSRPM (contains full path now)
- fix TARGET/TARGETPKGDISTRO/BUILDROOT/BUILDERHOME situation
- korinf: add support for -F (force rebuild all). -f now rebuild only failed
- korlogin: run bash by default, fix param using
- main: fix private key permissions
- prepare_copying was renamed to clean_copying_destination
- remove debug packages if not permitted
- remove src.rpm if do not need copy it
- restructurization and remove obsoleted code
- update system list
- use latest package instead first one

* Mon Dec 20 2010 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- add build/windows script
- add Fedora/14, add Windows branch, add x86_64/SUSE/11.3
- build_funcs: do reset hard if push is failed (see eterbug #6560)
- copying: copy source if allowed, run genbase for ALT distro
- get_bin_package: disable hack for use *buildname if buildname does not exist
- move lists/x86_64-* to lists/x86_64 subdir
- remove all CentOS 5.X (see eterbug #6292)
- rename common distro lists files to the same name as the system

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.9-alt1
- add drop_failed_status.sh script for remove all .build.failed files
- add FreeBSD/8.1, PCLinux/2010.07, SUSE/11.3, Ubuntu/10.10
- add quotation marks for SRC_URI (for multiple URIs); RT #15490
- check built package existense before removing
- copy each file instead of copying whole list
- copying: fix first package checking result
- fix missing EXPRPMEXTRAFILES for non-rpm builds
- fix using on ALT with LSB support
- remove ALT Linux 5.0 support (use p5 instead)

* Mon Jul 26 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.8-alt1
- add rx-etersoft build support since RX 1.1.1
- again fix build in hasher with host arch != target arch (real major change in etersoft-build-utils 184)
- cron build: add checking for last tag (do not create changelog if tag already at HEAD)
- do rpmbph arch related
- fix build in hasher with host arch != target arch
- global rearrange and update distro list
- hasher: disable ~/.config/eterbuild creating (run with HASHER_NOCHECK directly)
- introduce serapate sign (FIL) for failed builds
- use correct package name
- use list files (MAINFILES, EXTFILES) for get built packages names

* Tue May 18 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.7-alt1
- make md5sum after copying
- no build if STOP file is exists
- rewrite makeiso scripts
- upgrade generate_sig to uft8 version
- add reconnect to sshfs
- check every package for integrity during work on task
- add zip support
- fix hasher cleaning after build error (add missed MENVARG)
- rewrite build process in a new manner
- add TOPDIR support for run from any dir
- add install script for install pkg in systema
- fix install_wine on Ubuntu
- fix config to ~/.config/eterbuild
- recode to UTF-8
- introduce support of commands dir and realize last_rpm in the new way, with test
- korlogin: disable broken log
- add messages/fio module, add get_dear_from_fio func and update fio test

* Tue Mar 09 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.6-alt1
- many fixes and rewrites with many improvements
- korinf: rewrite script, fix args handling and build list
- initial support for Linked system, autocreate links
- add initial rpmopt support (options for rpm build in etc/rpmopt/system file
- do not build repo index due rpm-dir using instead
- check_products: add -b key support (for build)

* Sat Nov 21 2009 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt1
- common: incorporate in get_distr_list filter_distr_list for support SKIPBUILDLIST
- now 'all' builds only for target distro. For build for all distros, use ALL keyword.
- check_built: set MIS in the status column
- queuewatcher: add flag to run now
- fixes for ebuilds
- replace Gentoo hack with more clean one
- install_wine: add initial install support
- config: export global variable, always include system wide config from /etc/eterbuild/korinf
- introduce PUBLICURL and FTPDIR and use it for DESTURL
- rpm: fix alien using in 32-bit environment for 64-bit target
- add wrapper used in dpkg-architecture
- korlogin: use system name instead chroot
- korinf: fix target dir detecting from spec
- robot build: get project version from SOURCEPATH
- distro: additional TARGET check

* Wed Aug 05 2009 Vitaly Lipatov <lav@altlinux.ru> 1.8.4-alt1
- build Gentoo and ArchLinux in generic way, fix TARGET vars setting
- add new scripts for run task in all OSes
- rewrite build freebsd scripts
- korinf: add -b param (buildstrap build enable)
- add korlogin script to log in the chroot system
- small improvements

* Fri Jul 24 2009 Vitaly Lipatov <lav@altlinux.ru> 1.8.3-alt1
- korinf: do not use subdir by default
- skip Windows build
- copying: add apt repo generating after build
- Author: Vitaly Lipatov <lav@etersoft.ru>

* Mon Jul 20 2009 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- bin/korinf: add support for build from spec (use rpmpub), add optional target support
- common: add support for installed korinf and installed etersoft-build-utils
- fix FreeBSD build
- small improvements

* Tue Jul 14 2009 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- add need for versioned etersoft-build-utils
- rewrite freebsd build related scripts
- get_rpm_sources: add TARGET/Windows support
- rpm: write config log separately
- correct set BUILDARCH (parse dist)
- use bin/korinf with standart build_package function
- do not need etersoft-build-utils anymore in target system

* Fri Jun 12 2009 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- improve and cleanup code, use etersoft-build-utils >= 1.6.0
- convert src.rpm in host system now

* Sat Mar 07 2009 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- improve code, fix to use etersoft-build-utils 1.5.6

* Wed Jan 14 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- update version

* Tue Jan 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- update to lastest source, big restructure
- change License to GPLv3

* Sun Jul 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- initial build for ALT Linux Sisyphus

