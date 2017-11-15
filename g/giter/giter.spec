Name: giter
Version: 1.14
Release: alt1

Summary: Etersoft wrapper for git commands

License: AGPLv3
Group: Development/Other
Url: http://wiki.etersoft.ru/Giter

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git http://git.altlinux.org/people/lav/packages/giter.git
Source: ftp://updates.etersoft.ru/pub/Etersoft/Sisyphus/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

Conflicts: etersoft-build-utils < 2.1

Requires: eepm >= 1.5.13

%description
This package contains a set of helper utils for git, gitum and etersoft-build-utils.
See info in Russian on %url.

RECOMMENDED packages: git-core gitum

%prep
%setup

#build
#make

%install
# install to datadir and so on
%makeinstall
%find_lang %name

%files -f %name.lang
%doc AUTHORS README.md
%_bindir/*

%changelog
* Wed Nov 15 2017 Vitaly Lipatov <lav@altlinux.ru> 1.14-alt1
- grebase: add commit ID support

* Sat Mar 25 2017 Vitaly Lipatov <lav@altlinux.ru> 1.13-alt1
- gpush: use -a to push all branches and -r to push to all remotes
- gpull: add -A to pull all remove branches

* Wed Nov 30 2016 Vitaly Lipatov <lav@altlinux.ru> 1.12-alt1
- gpush: use origin by default if alone

* Fri Aug 26 2016 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- fix error when .ssh/config is missed
- gremote: add missed .git support when print out public url

* Tue Apr 19 2016 Vitaly Lipatov <lav@altlinux.ru> 1.10-alt1
- giter: fix print girar user, same small fix
- gpick: add --autoskip option

* Sun Dec 13 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9-alt1
- gremote: process all git@ aliases like urls when -p
- giter: fix number clean

* Sun Nov 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.8-alt1
- giter: fix for empty run
- gpull: print note if fast forward failed
- gremote: add github support in -p option
- gamend: add git add before amend
- gamend: don't reset author by default

* Sun Oct 11 2015 Vitaly Lipatov <lav@altlinux.ru> 1.7-alt1
- gpush: make options unpositional
- small cleanup comments

* Fri Oct 09 2015 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt1
- gclone: small fix
- gpush: fix options handling

* Wed Aug 26 2015 Vitaly Lipatov <lav@altlinux.ru> 1.5-alt1
- gremote: create git.* alias for our repos on git.*
- introduce gclone: git clone with git alias rewriting
- gremote: add -p option for convert paths to public
- giter: add print git url command

* Mon Aug 24 2015 Vitaly Lipatov <lav@altlinux.ru> 1.4-alt1
- ginit: use full path to people packages
- ginit: hack for git.eter
- gpull: add hack for use sisyphus branch for /gear repos
- gpull: use sisyphus only for empty run with many remote branch

* Wed Aug 19 2015 Vitaly Lipatov <lav@altlinux.ru> 1.3-alt1
- grebase: error if there is no unpublished commits
- estrlist: fix when empty list
- fix gpush behaviour

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- set 'merge.ff only' only for repos pushed to git.*:/projects
- add glog command
- grebase: rewrite to use real commit id, not number in a list
- grebase: allow only unpublished commit by default

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.1-alt1
- gpush: fix add list
- check for merge.ff only at a popular operations

* Tue Aug 11 2015 Vitaly Lipatov <lav@altlinux.ru> 1.0-alt1
- gpush: push to pub.*, git.* by default
- fix get_gear_name (when run outside git repo)
- gpush: fix args -b -a
- gremote: rewrite -u

* Tue Aug 04 2015 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- gpush: fix options handling

* Tue Aug 04 2015 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- gpush: force use first arg
- giter: fix command checking

* Tue Aug 04 2015 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- use GITHOST/GEARHOST instead GIRARHOST
- gpick: add patch support, but it is better to use git am directly
- giter: add list packages

* Tue Jul 21 2015 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- add gpick - git cherry pick all commits from git log file
- use fixed epm assure

* Sat Dec 13 2014 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- fix remote detecting
- rewrite to support various length commands
- add check girar access

* Mon Dec 08 2014 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- ginit: add support for direct set project name or path to the project dir
- ginit: create alias only if use current repo info
- add get_repo_name func (copied from etersoft-build-utils) and use it
- add initial giter script
- improve get_remote_repo_name (use repo dir name, use only girar remotes)

* Wed Feb 26 2014 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- gpush: add support for -a (push to all repos)
- fix girar host detection

* Fri Feb 14 2014 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- new version

* Fri Jan 31 2014 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
