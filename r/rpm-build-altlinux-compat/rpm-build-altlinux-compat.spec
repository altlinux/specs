# NOTE: do not use clean_spec or rpmcs for this spec

Name: rpm-build-altlinux-compat
Version: 1.7.20
Release: alt1

Summary: ALT Linux compatibility and extensions in rpm build

License: GPL
Group: Development/Other
Url: http://wiki.sisyphus.ru/devel/RpmBuildAltlinuxCompat

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: ftp://updates.etersoft.ru/pub/Etersoft/Sisyphus/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

# Tune additional rpm macros file placement
%if %_vendor == "alt"
%define macrofilename macros
%ifndef _rpmmacrosdir
%define _rpmmacrosdir %_sysconfdir/rpm/macros.d
%endif
BuildPreReq: altlinux-release
%else
# FreeBSD
%if %_vendor == "portbld" || %_vendor == "any"
%define _rpmmacrosdir %_etcrpm
%define macrofilename macros
%else
# in Mandriva for example
%if %{expand:%%{?_sys_macros_dir:1}%%{!?_sys_macros_dir:0}}
%define _rpmmacrosdir %_sys_macros_dir
%define macrofilename 99-altlinux-compat.macros
%else
%define _rpmmacrosdir /etc/rpm
%define macrofilename macros
%endif
%endif

Requires: ed
# ALT has it in rpm, but regular rpm requires define it
BuildRoot: %{_tmppath}/%{name}-%{version}
%endif

Requires: rpm-build

%description
This package contains ALT Linux compatibility layer
and some extensions for rpm build
on various rpm running platforms.

%package -n rpm-build-intro
Summary: New macros for ALT Linux rpm build
Group: Development/Other
Requires: %_rpmmacrosdir
# we will use distr_vendor from it
# Requires: rpm-build-compat

%description -n rpm-build-intro
This package contains new macros introduced for
include in ALT Linux rpm build.

If you wish to use these macros, add rpm-build-intro
package to buildrequires.

%package -n rpm-build-compat
Summary: ALT Linux compatibility macros for backport purposes
Group: Development/Other
Requires: %_rpmmacrosdir

%description -n rpm-build-compat
This package contains ALT Linux compatibility layer
for ALT Linux rpm build.
It is useful for backporting packages to previous ALT Linux distros.
Add it to buildrequires when backporting packages.
Command rpmbph from etersoft-build-utils will do it automatically.

%prep
%setup

%install
./install.sh %buildroot %_bindir %_rpmmacrosdir %macrofilename

%if %_vendor == "alt"

%files -n rpm-build-intro
%doc AUTHORS TODO
%_rpmmacrosdir/etersoft-intro

%files -n rpm-build-compat
%doc AUTHORS
%_rpmmacrosdir/compat
%_bindir/distr_vendor

%else

%files
%doc AUTHORS TODO ChangeLog
%_rpmmacrosdir/%macrofilename
%_bindir/add_changelog
%_bindir/stamp_spec
%_bindir/subst
%_bindir/distr_vendor

%endif

%changelog
* Tue Jun 05 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.20-alt1
- use x86_64 version instead regular if it exists

* Tue May 22 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.19-alt1
- major improve distr_vendor:
 + add support without ROOTDIR translation names
 + add SunOS support
 + cleanup
 + add -V for printout version

* Sat May 05 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.18-alt1
- fix Ubuntu/12.04 multiarch dir placement
- add _libexecdir for deb systems

* Sat May 05 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.17-alt1
- add support for Ubuntu 12.04 multiarch
- macros.intro: use prefix instead /usr (FreeBSD/Solaris uses /usr/local)

* Tue Apr 17 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.16-alt1
- add intro.backport to compat

* Tue Apr 17 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.15-alt1
- fix compat macros for ALT Linux

* Thu Apr 12 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.14-alt1
- add missed _lib32dir on ALT backports

* Tue Apr 10 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.13-alt1
- distr_vendor: update for new systems
- install.sh: fix subst using

* Tue Apr 10 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.12-alt1
- set _initddir as /etc/rc.d for ArchLinux (eterbug #7863)

* Mon Apr 09 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.11-alt1
- macros.intro: add _lib32dir

* Tue Mar 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.10-alt1
- add .x86_64 support and add hack for deb based systems

* Fri Jan 06 2012 Vitaly Lipatov <lav@altlinux.ru> 1.7.9-alt1
- use _sys_macros_dir for macros dir if defined

* Mon Oct 03 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.8-alt1
- do not use pushd/popd in specs

* Wed Sep 28 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.7-alt1
- add macros from control

* Tue Aug 30 2011 Denis Baranov <baraka@altlinux.ru> 1.7.6-alt2
- spec: add openpkg from SunOS support for macros dir

* Mon Jul 25 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.6-alt1
- add rpm-build-tts

* Wed Jul 13 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- distr_vendor: fixes for ALT Linux
- spec: add FreeBSD support for macros dir

* Fri Jul 01 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- distr_vendor: use uname -r for FreeBSD

* Sat Apr 02 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.3-alt1
- add _target_libdir, _target_libdir_noarch (needed for python macros)

* Sat Feb 19 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt3
- fix version detection for Fedora

* Tue Feb 08 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt2
- use /etc/init.d for SUSE based distro (eterbug #6629)

* Fri Feb 04 2011 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- distr_vendor: get Mandriva version via lsb-release
- use rc.d/init.d for rpm based distro (eterbug #6629)

* Wed Oct 13 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt2
- define _initddir for all pkgtype

* Wed Oct 13 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- remove python env. var. (http://bugs.etersoft.ru/show_bug.cgi?id=4754#c25)
- use _initddir instead _initdir, add _initdir to ALT compat macros (see ALT #24290)
- remove dup macros

* Sat Oct 02 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- split in two package on ALT Linux: rpm-build-compat and rpm-build-intro
- disable start_service on ALT Linux (fix for ALT bug #24152)
- improve detecting ALT Linux 5.1 and 6.0

* Fri Oct 01 2010 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- update SUSE/Mandriva/PCLinux detections
- fix install pkgtype related macros

* Mon Jul 26 2010 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt1
- add python, perl macros

* Mon May 31 2010 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- rearrange source macros file
- update distr_vendor

* Sat Apr 10 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt1
- introduce %%_sysconfigdir (%%_sysconfdir/sysconfig)

* Sun Mar 07 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt2
- fix translation distro name
- fix Url to new place
- add support for -p option to subst

* Sat Mar 06 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt1
- add macros from rpm-build-perl
- move build to BuildFarm

* Wed Jan 13 2010 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt1
- small rearrange macros
- move _aclocaldir, _locksubsysdir, _rpmmacrosdir to already realized in ALT

* Thu Nov 19 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- update cmake macros from cmake 2.8.0-alt1, move it to compat

* Sat Sep 26 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- fix cmake for build in build subdir

* Wed Jul 01 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- distr_vendor: add -n option for printout distro name in _vendor macros format
- update distr_vendor to newest distro support

* Mon Mar 02 2009 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- fix cmake, fix_permissions macros
- introduce remove_repo_info macro
- sync python_ macros with rpm-build-python

* Tue Jan 13 2009 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt2
- add bindir to install script

* Thu Jan 08 2009 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- introduce cmake, fix_permissions, python_check macros

* Wed Dec 10 2008 Yuri Fil <yurifil@altlinux.org> 1.2-alt4
- add compat add_python_req_skip, license macros
- introduce _locksubsysdir macro

* Thu Nov 13 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt3
- fix font path for other system

* Thu Oct 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt2
- add modified macroses from rpm-build-fonts for other systems
- bin/distr_vendor: right use status of the last command in functions

* Mon Jun 09 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt2
- fix copy/paste error in add_optflags/remove_optflags

* Sat Jun 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- add distro specific macroses support
- set correct fonts path for various distro

* Thu May 08 2008 Vitaly Lipatov <lav@altlinux.ru> 1.00-alt3
- add add_optflags/remove_optflags

* Mon Mar 24 2008 Vitaly Lipatov <lav@altlinux.ru> 1.00-alt2
- disable empty rpmldflags
- ignore return status from groupadd/useradd

* Thu Mar 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.00-alt1
- fix useradd/groupadd realization again
- update rpm opt* flags

* Sun Mar 02 2008 Vitaly Lipatov <lav@altlinux.ru> 0.99-alt1
- fix useradd/groupadd realization for various distros

* Sun Feb 24 2008 Vitaly Lipatov <lav@altlinux.ru> 0.98-alt1
- add autoreconf macros
- add add_findprov_lib_path skipping
- do not override add_findprov_lib_path and set_verify_elf_method on ArchLinux

* Sat Jan 19 2008 Vitaly Lipatov <lav@altlinux.ru> 0.97-alt1
- do not check tty -s in start_service for other platforms
- check DURING_INSTALL in start_service

* Fri Jan 11 2008 Vitaly Lipatov <lav@altlinux.ru> 0.96-alt1
- add make_install_std, makeinstall_std, omfdir
- cleanup spec according to etersoft-build-utils 1.3.6

* Sat Dec 15 2007 Vitaly Lipatov <lav@altlinux.ru> 0.95-alt2
- add set_verify_elf_method stub for non ALT systems

* Wed Nov 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.95-alt1
- upgrade dist_vendor script to newest systems
- add check for too old mktemp to add_changelog
- add defaultdocdir definition
- add ChangeLog file
- fix start_service macros
- add initial ArchLinux support
- use lxp suffix for LinuxXP and mdv for Mandriva

* Fri Sep 07 2007 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt1
- update distr_vendor
- add macros start_service for conditional start service during install

* Mon Jul 02 2007 Vitaly Lipatov <lav@altlinux.ru> 0.93-alt1
- upgrade dist_vendor script to newest systems

* Fri Mar 23 2007 Vitaly Lipatov <lav@altlinux.ru> 0.92-alt1
- do not add old ALT distro compatibility macroses for all (fix bug #11183)

* Thu Mar 08 2007 Vitaly Lipatov <lav@altlinux.ru> 0.91-alt1
- rewrite distr_vendor (add detect for all supported system)
- enable make_build to multiprocess build

* Mon Feb 26 2007 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- define post_service macroses separately for rpm and deb

* Thu Feb 22 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt5
- fix distr_vendor script, fixes for dash using
- pack distr_vendor for ALT Linux

* Sun Jan 14 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt4
- remove _libexecdir

* Thu Nov 02 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt3
- fix _libexecdir

* Sat May 13 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt2
- add _docdir
- use nil for correct macro functions
- fix subst script

* Sat Apr 15 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- add dummy macroses for menu/desktopdb update
- add distr_vendor script for distro version detecting
- use : in stub macroses

* Tue Apr 11 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt3
- fix chkconfig params
- change initdir to /etc/init.d (for non ALT)
- rewrite preun/post scripts

* Sun Apr 09 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt2
- revert prev. changes, fix some macroses

* Sun Apr 09 2006 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- define ALT macroses only if not defined yet
- add __niconsdir

* Sat Mar 04 2006 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- fix stupid bug with postun script name
- fix mktemp in old systems

* Sat Feb 18 2006 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- some fixes

* Sun Feb 12 2006 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- merge rpm-build-altlinux-compat and rpm-build-compat projects

* Mon Feb 06 2006 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- fix __autoreconf macro name
- add _aclocaldir macro

* Sun Feb 05 2006 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- add rpmcflags macro

* Sun Jan 29 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- start ALT backports compatibility project

* Fri Dec 30 2005 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- new release, macros updated by Denis Smirnov

* Sat Oct 29 2005 Vitaly Lipatov <lav@altlinux.ru> 0.1-redhat1
- test pre release
