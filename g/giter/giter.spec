Name: giter
Version: 1.2
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
