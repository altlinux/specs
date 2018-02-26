# NOTE: do not use clean_spec or rpmcs for this spec

Name: etersoft-build-utils
Version: 2.0.12
Release: alt1

Summary: A set of build rpm utilities

License: Public domain
Group: Development/Other
Url: http://www.altlinux.org/Etersoft-build-utils

Packager: Vitaly Lipatov <lav@altlinux.ru>

# git-clone http://git.altlinux.org/people/lav/packages/etersoft-build-utils.git
Source: ftp://updates.etersoft.ru/pub/Etersoft/Sisyphus/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

%define altcompat_ver 1.7.19

# Buildreqs note: C compiler is required by rpm-build; we do not require C++ here
BuildRequires: rpm-build-compat >= %altcompat_ver

Requires: rpm-build
Requires: rpm-build-compat >= %altcompat_ver

%if %_vendor == "alt"
Requires: sisyphus_check rsync openssh-clients srpmcmp
%else
# ALT has it in RPM
BuildRoot: %{_tmppath}/%{name}-%{version}
%endif

%description
This package contains a set of helper utils for RPM building process.
See info in Russian
on %url.

RECOMMENDED packages: gcc-c++ perl-libwww ccache elinks mutt hasher curl

%prep
%setup

%build
%make

%install
# install to datadir and so on
%makeinstall
%find_lang %name

%files -f %name.lang
%doc AUTHORS README TODO NEWS QuickHelp*
%_bindir/*
%_datadir/eterbuild/
# for backward compatibility (will removed in 2.0)
%_sysconfdir/rpm/etersoft-build-functions
%attr(0755,root,root) %_sysconfdir/bashrc.d/*
%dir %_sysconfdir/eterbuild/
%dir %_sysconfdir/eterbuild/apt/
%dir %_sysconfdir/eterbuild/repos/
%config(noreplace) %_sysconfdir/eterbuild/apt/apt.conf.*
%config(noreplace) %_sysconfdir/eterbuild/apt/sources.list.*
%config(noreplace) %_sysconfdir/eterbuild/config
%config(noreplace) %_sysconfdir/eterbuild/repos/*

%changelog
* Sat Jun 02 2012 Vitaly Lipatov <lav@altlinux.ru> 2.0.12-alt1
- rpmlog: disable sort -u for changelog items
- gpull: get tags for gpull -c too
- add arg support to get_remote_repo_list
- gpull: use remote branch name if local name does not exists there
- introduce gremote
- rename gitcam to gamend
- fix docmd and use it instead duplicate showcmd
- small cleanup
- common: introduce usearg and use it
- remove obsoleted publish-compat
- rpmbs: use get_last_tag
- git: introduce get_last_tag func
- rpmbs: rewrite check_gear_and_tag with is_last_commit_tag
- introduce is_last_commit_tag and use it
- ginit: small cleanup
- rewrite get_root_git_dir with using $ git rev-parse --git-dir is_gear: fix get_root_dir_dir using
- gpush: push last tag also
- update some pkgrepls
- allow use any RPM dir defined as topdir in ~/.rpmmacros
- rpmqf: add missed tune env

* Wed May 23 2012 Vitaly Lipatov <lav@altlinux.ru> 2.0.11-alt3
- update QuickHelp
- fix rpm-build-altlinux-compat requires

* Wed May 23 2012 Vitaly Lipatov <lav@altlinux.ru> 2.0.11-alt2
- fix rpm-build-altlinux-compat requires
- update pkgrepls (centos, deb)

* Tue May 22 2012 Vitaly Lipatov <lav@altlinux.ru> 2.0.11-alt1
- big replacement rules rewrite (deb related)
- ginit: filter project name before use
- gitcam: add new command for git --amend -a commit
- use global vars DISTRNAME, DISTRVERSION, BUILDARCH, PKGFORMAT, PKGVENDOR, RPMVENDOR
- replace DEFAULTARCH with BUILDARCH
- rpmbph: add fix commands in the build section in a more universal way
- rpmbph: add hack for repack on x86_64 system packages contains ExclusiveArch in spec

* Fri Apr 27 2012 Vitaly Lipatov <lav@altlinux.ru> 2.0.10-alt1
- many repl rules fixes
- add support for Source0:, add check for empty source name detected
- fix ALT 4.0/4.1 detection
- improve binary repo desciptions
- loginhsh: add -d, -q -r params
- myhsh: do not install debuginfo packages in test hasher
- repl: add hack for replace lib with lib64 on Mandriva
- rpmbph: some hack for build wine on x86_64
- rpmbsh: don't replace pushd/popd on ALT
- rpmcs: fix /etc and init.d replacement
- rpmcs: small fixes, fix replacement rules also
- rpmgp: add support for optimized dirs (/a, /b, /c subdirs)
- rpmgp: call gear repo as gear
- rpmgp: rename origin to gear
- rpmlog: add toTAG support
- rpmpub: fix ETERDESTSRPM handle
- tarball: add conv for zip
- tarball: add rar support
- web: skip download if exists

* Tue Dec 06 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0.9-alt2
- fix override tag

* Tue Dec 06 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0.9-alt1
- fix replrules for Mandriva 2011
- rpmbs: fix gpush error comment
- rpmbs: hack for multiple specs
- rename apt conf files

* Tue Nov 08 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0.8-alt1
- full support for p? / t?, update tests for M60P M60T
- some pkgrepl fixes
- update repos/srpms
- update support for p? and t? alt systems, do name translation more correctly
- web: replace 20 with space after download

* Tue Oct 18 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0.7-alt1
- dmake: add -t option for test build servers
- dmake/jmake: use nice
- fix pkgrepls
- gpull: fix get branch
- rpmbb: add dmake support
- rpmcs: add -h, --help support
- rpmcs: do not replace changelog part
- rpm: disable specname warning
- rpmgp: skip gcc-c++ for install
- rpmgs: fix changelog message
- rpmgs: use bash

* Mon Aug 01 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0.6-alt1
- dmake: add support for pump mode by default
- small fixes

* Thu Jul 28 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0.5-alt1
- add dmake for distcc support
- dmake: add support 64 bit build and build i586 on x86_64
- add replaces for VoiceMan
- rpmgs: fix add log after import

* Wed Jul 13 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0.4-alt1
- clean up helps for all commands
- common: introduce docmd and showcmd funcs
- gpull: do fetch before pull
- loginhsh: add -x option for login with X support
- rpmbph: normalize Patch0 name

* Fri Jul 01 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0.3-alt1
- repl: skip x86_64 before usual versions
- rpmbph: drop obsoleted Fedora rules (conflicts with Mandriva/2010)
- rpmbs: disable MD5 updating
- rpmcs: fix replace Requires rpmcs: use last rules for repl

* Fri Jun 10 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0.2-alt1
- add p6 source list
- add support for any p? system, do name translation more correctly
- gpull: use current branch name by default
- rpmgp: use subdir in tmp

* Mon May 23 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0.1-alt1
- get_etersoft_srpm_path: allow Source0 also
- jmake: always use all CPUs
- rpmgp: rewrite git clone
- rpmgs: fix spec comment
- spec: add tarball url

* Tue Apr 26 2011 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- fix pkgrepls, remove bashism
- repl: sure our version we check firstly

* Mon Apr 04 2011 Vitaly Lipatov <lav@altlinux.ru> 1.9.9-alt2
- add rpm-build-compat requires (ALT bug #25356)

* Sat Apr 02 2011 Vitaly Lipatov <lav@altlinux.ru> 1.9.9-alt1
- build: disable _unpackaged_files_terminate_build
- gpull: always get tags
- pkgrepl: fix groups replacement
- repl: fix for use fedora.9, fedora.10 sort
- rpmbph: skip egg-info packing with python 2.4 on CentOS/5
- rpmgp: allow run without params
- tarball: add support for tgz unpack

* Thu Mar 03 2011 Vitaly Lipatov <lav@altlinux.ru> 1.9.8-alt1
- common: move function before used
- gpull: fix result output
- rpmbs: move srpm after extract tarball from it

* Sat Feb 19 2011 Vitaly Lipatov <lav@altlinux.ru> 1.9.7-alt1
- rpmbs/rpmbsh: move src.rpm to ETERDESTSRPM instead copying
- rpmqf: add deb support
- update src.rpm repos
- web: disable cert checking for wget

* Fri Jan 28 2011 Vitaly Lipatov <lav@altlinux.ru> 1.9.6-alt1
- drop release to alt1 if incrementing version
- fix cyclic group replacement again (ALT #24724)
- gpush: real check tag
- initial fix rules for new order
- introduce RELEASEPREFIX and use it
- remove all temp generated src.rpm, sources, specs
- rewrite replacement rule: check for each file from new version to old
- rpmbs: no error if no need to copy

* Tue Dec 28 2010 Vitaly Lipatov <lav@altlinux.ru> 1.9.5-alt1
- rpmgp: add support for clone via public url

* Thu Dec 23 2010 Vitaly Lipatov <lav@altlinux.ru> 1.9.4-alt1
- gpush: rewrite girar/branch detection part, refactoring
- gpush: use origin by default if exists
- rpmbs: use name from spec as target repo name

* Mon Dec 20 2010 Vitaly Lipatov <lav@altlinux.ru> 1.9.3-alt1
- gpush: full rewrite, use mygetopts
- rpmlog: strip sign (eterbug #6588)

* Tue Dec 14 2010 Vitaly Lipatov <lav@altlinux.ru> 1.9.2-alt1
- gpush: use remote alias, not direct path
- introduce grpmbs - send a group of packages to girar build introduce grpmbsh - build a group of packages in hasher
- remove Development Tools->Other (ALT #24724)
- rpmgs: add tar.xz support

* Fri Oct 22 2010 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- support rpm-build-intro (as rpm-build-compat)
- add script from create repo from package list
- check_display: do not run xset directly
- fix replace p5<->M50
- gpull: replace -n with -r/-m/-f options (do --ff-only by default)
- rpmbph: fix -n -u param handling
- rpmgs: add support for download and commit tarballs with more than one subdirs

* Thu Sep 16 2010 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- gpush: fix origin publish
- rpmbph: add -b REPONAME and -q (quiet) support
- rpmbs: add support for default remote, push branch too
- rpmcs: implement group replacing

* Fri Aug 20 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.9-alt1
- gpush: add some heuristic for default behavior
- show git diff only for interactive session

* Tue Jul 27 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.8-alt1
- gpull: do normal pull in additional to pull --rebase
- rpmbs/gpush: push only our tag, not all tags
- rpmbph: fix bug with positional -n param
- rpmbph: fix -n using again
- rpmbs: add support for -b (binary repo)
- rpmbs: add -t option (just set signed tag)
- rpmlog: add support for -v (increment version) introduce inc_release

* Mon Jun 28 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.7-alt1
- fix add_changelog (run with empty text)
- fix md5sum (correct overwrite hardlinked file)
- rpmlog: add check for package version/release

* Wed Jun 16 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.6-alt1
- all output from git pull to stdout
- improve aptU: skip glibc/stdc++ libs and lib versioning
- introduce echocon (print only if there is real console) and use it
- rewrite add_changelog_helper
- rpmlog: add test run mode, fix changelog format

* Thu Jun 10 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.5-alt1
- allow to set default target branch (via MENV in config)
- gpull: add -c option for check repo uptodate status
- gpush: add support for target origin
- introduce rpmlog command for autoupdate changelog from git log
- rpmbs: add pocket build support (-p option)

* Fri Jun 04 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.4-alt1
- rpmbph: fix rules using when build for target x86_64 from i586
- rpmbs: extract all tarballs from src.rpm to tarball dir
- add gpush origin support
- get spec path if spec is defined in gear rules
- introduce SYSARCH with real system arch, use it during work with spec and src.rpm packing
- fix replacements for gcc*, drop last spaces in list repl, add test for pkgrepl
- update pkgreplreqs

* Tue May 18 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.3-alt1
- improve some requires replacements
- use PROJECTNAME instead BASENAME
- add filter_gear_name for replace forbidden + with plus word
- hasher: fix arch replacement
- rpmbs: fix rsync upload for src.rpm

* Sat Apr 17 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.2-alt1
- rpmpub: add fatal error if target dir is not set
- fix get_root_git_dir against HOME
- rpmbs: create MD5SUM for packages
- do git reset after build with gear --commit
- add gacl: utility for acl control
- rpmpub: make cp -al for new releases from last link
- loginhsh: install dbus-tools-gui if package(s) requires dbus
- rpmbs: add git tag checking
- always set APTCONF and HASHERDIR
- add TOPDIR support

* Mon Mar 22 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- fix HASHERBASEDIR detecting
- rpmbs: chmod generated src.rpm
- skip AutoReq/AutoProv mingw32 for ALT before 4.1

* Fri Mar 12 2010 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- stable release 1.8.0
- aptU: initial realize for -l option
- fix rpmbsh -i mode and loginhsh
- rpmgs: fix downloading errors handling

* Mon Mar 08 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.9-alt1
- rpmbph: do undefine libtoolize for M50 too
- drop out ~/.ebconfig support, enable warning about ~/.eterbuild-config
- rpmbph: replace %release with the real value due using in Source: and Patch:
- rpmgp: only clone with -g, add new -gm option for remote clone and clone
- gpull: full rewrite for support -a (all branches) and various remote repo
- allow run rpmU under root user
- remove UPLOADDIR var using and drop out copying after rpmbs by default
- always clean hasher after build (by default). use rpmbsh -l if needed

* Mon Feb 22 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.8-alt1
- rpmgs: small bugfixes and update
- add aptU - update/install package(s) and update their requires

* Sun Feb 21 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.7-alt1
- rpmbph: forbid backport to Sisyphus
- rpmgs: fix spec path using, fix download tarball for src.rpm, improve download
- rpmbs: fix src.rpm run task
- enable support for use in gear without specname param
- rpmbs: disable default force create tag, add -f (force) param
- more bugfixes

* Fri Feb 05 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.6-alt1
- add bashrc.d aliases apti, apts, aptw, finds
- rpmgp: fix src.rpm import, allow to use several files
- rpmgs: add real source support (for Source-svn, Source-url commented lines)
- rpmbph: do not add rpm-build-compat buildreq to backported specs
- gpush: do ginit if no remote aliases

* Fri Jan 22 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.5-alt1
- rpmbs/rpmbsh: add -l option for lazy-cleanup after build
- rpmgp: add -m option for migrate spec to gear support
- rpmgp: fix -b option (install buildreqs packages) to work in distro independent manner
- rpmgp: fix get remote branches and main branch selecting

* Thu Jan 14 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.4-alt1
- rpmbph: support for branches like 5.1 if exists, instead M51
- rpmgp: clone all branches locally
- rpmbsh: fix remote src.rpm build from rpmbph
- gpush: push to all remote repos like git.*
- loginhsh: add -o option for run as root

* Wed Jan 13 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.3-alt1
- rpmgp: add acl list printing
- gpush: push without branch if --all
- rpmbph: do not insert fix for fuzzy patch in any case
- rpmgp: add -g option for remote and locally repo clone

* Fri Jan 08 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- rpmbph: realize gear repo backporting (eterbug #4766)
- myhsh: drop out backport related defines (it will be placed in the spec by rpmbph)
- gpush: push current branch definitely
- rpmbs: fix task build on various repos

* Fri Jan 08 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.1-alt1
- myhsh: error if there are unpackaged files in the build
- rpmgp: improve package checking (support non installed packages)
- use sources.list from /etc/eterbuild if apt.conf in /etc/eterbuld too

* Sun Jan 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.7.0-alt1
- check_publish.sh: add check for exist git repo, list acl for package if it in git
- config: add GEAR_USER
- rpmgp: add git checking
- clean_pkgreq: skip gcc/cpp general packages
- rpmgs: add rar archive support
- spec: fix url (fix alt bug #22476)

* Fri Nov 27 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.9-alt1
- fix GIRARHOST for subcommand
- drop rpm-build-compat requires

* Sat Nov 21 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.8-alt1
- rpmcs: fix %%__awker and so on replacement
- rpmurl -p: fix local missed package situation
- all utils: add support git.somename in the first param
- rpmbb: add -R option for buildreq -bi
- myhsh: write path to hasher in log
- add apt conf files for 5.1 repo
- rpmbph: add KORINFTARGETRELEASE support
- rpmbs: add hack to replace alt release to eter
- rpmbs: skip some sisyphus_check for local src.rpm build

* Tue Sep 22 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.7-alt2
- rpmbs: imprpove publish tarball function, add md5sum for tarball
- rpmbs: skip some sisyphus_check for local src.rpm build

* Sat Sep 19 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.7-alt1
- add ccache support and use it in rpmbb
- rpmbph: set vendor name part in release inherited from prev. release
- rpmbph: remove SOURCE and SPEC files after build src.rpm
- add new command jmake for run parallel make with ccache
- rpmgs: add tbz support
- rpmbs: add support for tarball target subdir

* Thu Aug 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.6-alt2
- set script version to 166

* Wed Jul 29 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.6-alt1
- require make and gcc in any way (as part of build env)
- fix mcbc build
- rpmbph: replace readlink with realpath on FreeBSD

* Fri Jul 24 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.5-alt1
- rpmunmets: fix direct hasher deps
- fix set_last_link
- rpmbb: run build_rpms_name in any way (due broken LOGFILE initializing)
- rpmbs: set project name to gpush

* Mon Jul 20 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.4-alt1
- add alternative .gear/rules support
- add support for ETERBUILD_APTREPO conf
- rpmbsh: make temporary commit before build with -t option (rpmbb like behaviour)
- fix set last link, fix rpmpub / target detecting

* Wed Jul 15 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.3-alt1
- rpmpub: replace version only in last or unstable component
- add gpull command as git pull --rebase
- fix rpmbb -r (buildreq)
- open sisyphus.ru with source rpm name
- update ginit/gpush
- rpmunmets: search for the same arch in old repo
- add handle ssh and local target to get_etersoft_srpm_path
- rpmpub improvements
- introduce COMPANYNAME and TARGETFTPBASE for company independence
- fix rpmbs packing after hasher build
- rpmgs: rewrote code with tar in source support (gear support)

* Thu Jul 09 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt1
- add universal make_release script
- check version if NEEDETERBUILD contains needed version
- rpmbph: remove -m64 from optflags on Ubuntu/Debian
- fix rpmbs from gear build after rpmrb/rpmbsh
- rpmpub: initial version of project publish script
- introduce COMPANYNAME and TARGETFTPBASE for company independence
- gpush: improve: push master by default, add -a|--all support

* Thu Jul 09 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt1
- rpmbs: add ssh target support for ETERDESTSRPM
- fix backports version (altbug#20431)
- rpmbs: fix add srpm to task, add verbose
- repl: add x86_64 support for replacement rules
- rpmbs: add -a option for add to shared task
- ginit: add remote alias origin, load config
- rpmbph: replace pushd/popd with cd
- build with gear --commit only via rpmbb

* Fri Jun 12 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt1
- rpmbs: switch to use git.alt build srpm command instead rsync to Incoming
- rpmbs: support git.alt for -u at gear repo
- rpmbph: use legacy compression for ALT 4.0/4.1 and not alt systems
- rpmgs: add gear import support
- support xdg-open instead BROWSER
- rpmcs: correct handle + (plus sign) in package names
- gpush: add -f/--force support
- rpmgs: add 7z archive support
- rpmbs: add save log entry for task build
- add undefine libtoolize for alt systems
- set correct vendor when repack src.rpm with rpmbph
- rpmunmets: add compare packages requires with their previous versions
- rpmbph: small fixes, replace Patch with Patch0
- pkgrepl.rpm: update rules
- fix build in empty RPM dir

* Fri Feb 13 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.6-alt1
- rpmbph: full rewrote repacking, add src.rpm and gear support
- mkpatch: check Makefile before Makefile.in

* Fri Jan 30 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt2
- rpmbph: fix readlink

* Thu Jan 15 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt1
- rpmbph: support non numerical releases
- loginhsh: enable /proc mount
- rpmqf: value link recursively
- rpmgs: add set version support (altbug #14397)
- update repl rules
- cleanup code

* Tue Jan 06 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.4-alt1
- introduce eterbuild/eterbuild script for public use
- cleanup code, remove obsoleted functions
- add support set version via rpmgs
- fix build result detecting

* Sun Jan 04 2009 Vitaly Lipatov <lav@altlinux.ru> 1.5.3-alt1
- add IGNOREGEAR env var support
- detect package arch from spec
- rpmgp: use getopt, add -d options for download package (list only by default)

* Sat Dec 13 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- really 1.5.2, cleanup code
- rewrite rpmgp: use getopt, add -d options for download package
- use gear via vars, do not require it

* Thu Dec 11 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt2
- add get_version, fix inc_release, inc_subrelease
- clean up code (thanks Slava Semushin for comments)
- fix rpmbb -r (buildreq) with git

* Sat Dec 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- APTCONF sets used apt.conf if defined
- add support for x86_64 build with generic i586 sources.list
- set git tag during rpmbs -s
- fix release checking in universal manner
- skip sisyphus_check if build from git
- update QuickHelp, remove unneeded comments
- fix __python_ and so on incorrect replacement
- disable __subst and libtoolize/autoconf and so on replacement
- fix _datadir/doc replacement (altbug #16604)
- use fonts-ttf-liberation from loginhsh

* Wed Oct 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.9-alt1
- add macroses from rpm-build-fonts
- support Mandriva 2009
- update pkgrepl rules
- bin/rpmrb: fix to use rpmrb without version
- bin/rpmgp: fix package download

* Sun Jul 20 2008 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- build from git, move install commands to makefile
- move /etc/rpm/etersoft-build-config to /etc/eterbuild/config
- move /etc/rpm/etersoft-build-functions to /usr/share/eterbuild/common
- update README, TODO

* Thu Jul 17 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.8-alt1
- bin/rpmgp: add support for get src.rpm from various rpm repos
- do not override CC/CXX, disable ccache detecting
- add support for M42
- update pkgrepl rules

* Thu Jul 03 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.7-alt1
- bin/rpmbs: add -z support (legacy compression)
- bin/rpmcs: disable change source tarball name by default
- bin/rpmbugs: use Sisyphus product for bugzilla
- bin/rpmbph: create rpms with legacy compression without spec line

* Fri Jun 27 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.6-alt1
- bin/rpmbph: use gzip method for backported src.rpm
- improve rpmqf to support links and files in the current dir
- update pkgrepl rules

* Fri Jun 13 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.5-alt1
- fix M41 build (fix bug #15969)
- add M41 support to rpmbph

* Thu May 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.4-alt1
- fix M40 upload to updates
- rpmurl: add -p option for open sisyphus.ru page for the package

* Sat May 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.3-alt1
- add M41 (backport/update) support
- fix missed defattr injecting in rpmbph
- run add_changelog separately for each spec (fix altbug #15495) in rpmgs
- disable attr removing, remove only defattr(-,root,root) in rpmcs
- fix defattr injecting (add missed |) in rpmbph (thanks to boris@)

* Mon Mar 24 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.2-alt1
- do not replace source ext in git repo case
- add more rules for removing %%_macroses
- fix Group replacement

* Sat Feb 23 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- fix Group replacement
- add python macroses support in rpmcs
- small fixes

* Sat Jan 19 2008 Vitaly Lipatov <lav@altlinux.ru> 1.4.0-alt1
- cleanup spec
- add rpm-build repl for SUSE
- use perl -pe for replacing, small fixes
- clean up rpmcs code
- fix bug #13974

* Fri Jan 11 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt3
- fix prepare_tarball function
- fix rpmbph for curret distro detect

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt2
- fix rpmcs hang
- fix rpmbph on ALT spec changelogs
- more correctly clean pkgreqs

* Thu Jan 10 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.5-alt1
- add -l key to rpmgp (lists buildreqs for the spec)
- big update of pkg replacement files (Xorg, NX, Postgres...)
- introduce rpmunmets script for unmets detect in fresh packages
- improve BuildReq handling in rpmbph
- fix replace package names only in *Req* and *Group* spec lines in rpmcs
- add -o key to rpmbs for nosrc.rpm generating

* Thu Dec 27 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt3
- fix replacements only in *Req* and Group* lines
- small fixes
- update replacemens for NX build

* Thu Dec 13 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt2
- remove empty tags (buildreq and so on)
- add perl-devel and python-devel replacements
- fix ALT Linux 3.0 replacements

* Thu Nov 08 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- write package release as in ALT
- fix rpmbph to support %%{_vendor}, %%_vendor, eter in release
- use bash for rpmbph, rpmbs
- major update replacement list (check by Wine build)
- add replacements for modularized XOrg packages
- rename mandriva tag release to mdv
- fix rpmbph for legacy mktemp using
- add gconf_schema_install replacement to rpmcs (fix bug #13614)

* Wed Nov 07 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.3-alt1
- add support to upload to incoming/Update (-U option)
- update replacement list (special Mandriva rules)
- add tbz2 tarball support
- fix build log greping
- update README

* Sun Oct 28 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.2-alt1
- small fixes in rpmbph scripts
- update replacement list
- add support for Incoming/Updates (-U key instead -u for upload)

* Tue Sep 25 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- fix rpmbph on ALT, add error handling in rpmcs
- add git support in mkpatch, use .orig firstly
- add some rules for Debian, Mandriva, common rules for rpm, deb

* Sat Sep 08 2007 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- improve rpmbph to support any target system
- use replacement lists in rpmbph and rpmcs
- add git support in mkpatch

* Mon Aug 06 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- fix rpmbb for use with gear (thanks to php-coder@)
- improve rpmcs
- fix pack_src_rpm()

* Mon Jul 10 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1.9-alt1
- alpha version, all systems support in rpmbph
- add all rpm based system initial support in rpmbph
- add parallel bzip (pbzip2) support
- add -r (remote) option to rpmrb

* Wed May 30 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1.8-alt1
- add support for ALT Linux 4.0 backports
- remove hasher from requires, add check for hsh
- set download timeouts against sf.net mirrors lags
- cleanup chroot after loginhsh using

* Fri Mar 16 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1.7-alt1
- rpmrb: remove minor version if only major used (fix bug #11103)
- detect sticky tag when recheckout from cvs
- use alt1 release as default for new release
- myhsh: use --mountpoints=/proc,/dev/pts by default

* Thu Jan 18 2007 Vitaly Lipatov <lav@altlinux.ru> 1.1.6-alt1
- small changes, remove hack for glibc-i686 requires
- fix check url in rpmurl

* Wed Dec 27 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.5-alt1
- add test with bzip -t for tarballs
- use bash for rpmbb (due dash problem on Ubuntu 6.10)
- fix some replacements in rpmbph
- disable ccache warning

* Sun Nov 19 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.4-alt1
- add initial support for gear/git
- add local mode for prepare_tarball (without cvs using)
- fix temp dir create, fix project directory name using
- fix nice using
- update library replacing to rpmbph
- fix mkpatch behaviour
- some hasher args fixes
- some bugfixes

* Tue May 23 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.3-alt1
- smallfix release (see NEWS)
- improve hasher using (disable buildtime, support for x86_64)
- improve mkpatch

* Sun Apr 09 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.2-alt1
- add mkpatch for make patch against one file in source tree
- remove -v from hsh args by default (fix bug #9387)
- some improvements (see NEWS)

* Wed Mar 08 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- bugfix release (see NEWS)

* Sun Mar 05 2006 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- some improvements (see NEWS), small bugfixes
- use apt.conf.SS/sources.list.SS by default now
- add check_spec.sh for compare rpmcs results with original specs
- remove elinks, perl-libwww, ccache requires (thanks mithraen@ for Uwaga)

* Tue Feb 21 2006 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- welcome to future improvement release (see NEWS)
- add functions for release small project (publish and rpmish)
- add nice to rpmbuild
- improve to more compatibility with other Linux distros

* Wed Feb 15 2006 Vitaly Lipatov <lav@altlinux.ru> 0.99.9-alt1
- some improvements (see NEWS)
- add fixes for ignore /etc/apt/sources.list.d/*
- add requires for rpm-build-*-compat
- test on various Linux distros (see README)
- fix Source URL
- temporarely disabled requires for rpm-build-compat

* Sat Jan 28 2006 Vitaly Lipatov <lav@altlinux.ru> 0.99.8-alt1
- some improvements (see NEWS)
- remove rpmlint from the package requires
- add console output in rpmbugs (f.i. use rpmbugs bug_number)
- add support for rpm-build-compact (for backports support)

* Wed Jan 04 2006 Vitaly Lipatov <lav@altlinux.ru> 0.99.7-alt1
- some improvements (see NEWS)
- remove cbuildreq

* Tue Dec 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.99.6-alt3
- fix small mistakes in scripts

* Mon Dec 26 2005 Vitaly Lipatov <lav@altlinux.ru> 0.99.6-alt2
- fix use loginhsh

* Mon Dec 26 2005 Vitaly Lipatov <lav@altlinux.ru> 0.99.6-alt1
- add M31 build support
- remove gcc-c/c++ dependencies
- rename bashbsh to loginhsh
- disable mail report (was broken feature)

* Sat Dec 24 2005 Vitaly Lipatov <lav@altlinux.ru> 0.99.5-alt1
- add requires for rpm-build-altlinux-compat for non ALT system
- change Incoming host from incoming to devel
- some improvement (see NEWS)

* Mon Dec 05 2005 Vitaly Lipatov <lav@altlinux.ru> 0.99.4-alt1
- change group to Development/Other
- minor fixes

* Sat Nov 26 2005 Vitaly Lipatov <lav@altlinux.ru> 0.99.3-alt1
- minor fixes (prepare for 1.0 release)

* Wed Nov 16 2005 Vitaly Lipatov <lav@altlinux.ru> 0.99.2-alt1
- minor fixes
- support for test install into hasher

* Fri Nov 04 2005 Vitaly Lipatov <lav@altlinux.ru> 0.99.1-alt1
- new version (major option parsing rewrite)
- ls-incoming added

* Sat Oct 15 2005 Vitaly Lipatov <lav@altlinux.ru> 0.99-alt1
- new version (bug fix release)
- upload-to-alt script restored

* Sun Sep 18 2005 Vitaly Lipatov <lav@altlinux.ru> 0.98-alt1
- new version (code rewrite, more smart options)
- remove upload-to-alt scripts (use -u option for rpmbs(h) instead)

* Sun Sep 11 2005 Vitaly Lipatov <lav@altlinux.ru> 0.97-alt1
- new version (more utilites, improve usability)

* Sat Sep 10 2005 Vitaly Lipatov <lav@altlinux.ru> 0.96-alt1
- new version

* Wed Sep 07 2005 Vitaly Lipatov <lav@altlinux.ru> 0.95-alt1
- new version (code rewrite)

* Tue Sep 06 2005 Vitaly Lipatov <lav@altlinux.ru> 0.94-alt1
- bugfix release (fix BUILDROOT, update translation)

* Mon Sep 05 2005 Vitaly Lipatov <lav@altlinux.ru> 0.93-alt1
- new version (code rewrite, more functionality, see README)

* Sat Sep 03 2005 Vitaly Lipatov <lav@altlinux.ru> 0.92-alt1
- new version (see NEWS)

* Wed Aug 24 2005 Vitaly Lipatov <lav@altlinux.ru> 0.91-alt1
- new version (small changes)

* Wed Aug 03 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt0.3
- fix unexpanded macros again

* Sat Jul 30 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt0.2
- fix bug #7491 (unexpanded macros)

* Sun Jun 05 2005 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt0.1
- add requires for C/C++ compilers
- add russian translation for script messages

* Fri Apr 15 2005 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- new release (other repository support)

* Sat Apr 09 2005 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- bugfix release
- fix missing rpm-build-functions

* Wed Mar 09 2005 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- new release

* Mon Feb 28 2005 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt0.1
- first build for ALT Linux Sisyphus
