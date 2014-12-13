Name: giter
Version: 0.5
Release: alt1

Summary: Etersoft wrapper for git commands

License: AGPLv3
Group: Development/Other
Url: http://wiki.etersoft.ru/Giter

Packager: Vitaly Lipatov <lav@altlinux.ru>

# git-clone http://git.altlinux.org/people/lav/packages/giter.git
Source: ftp://updates.etersoft.ru/pub/Etersoft/Sisyphus/sources/tarball/%name-%version.tar

BuildArchitectures: noarch

Conflicts: etersoft-build-utils < 2.1

%description
This package contains a set of helper utils for git and gitum.
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
