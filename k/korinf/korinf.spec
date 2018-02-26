Name: korinf
Version: 1.9.6
Release: alt1

Summary: Korinf multidistro build system

License: AGPLv3
Group: Development/Other
Url: http://freesource.info/wiki/korinf

Packager: Vitaly Lipatov <lav@altlinux.ru>

# git-clone http://git.altlinux.org/people/lav/packages/korinf.git
# git-clone http://git.etersoft.ru/people/lav/packages/korinf.git
Source: %name-%version.tar

BuildArchitectures: noarch

Requires: etersoft-build-utils >= 2.0.11
Requires: alien

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
%_bindir/korlogin
%dir %_sysconfdir/eterbuild/lists/
%config(noreplace) %_sysconfdir/eterbuild/lists/*
%config(noreplace) %_sysconfdir/eterbuild/rpmopt/*
%config(noreplace) %_sysconfdir/eterbuild/korinf
%config(noreplace) %_sysconfdir/eterbuild/linked
%_datadir/eterbuild/korinf/

%changelog
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

