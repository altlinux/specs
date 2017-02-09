Name: gitum
Version: 0.8.6
Release: alt1

Summary: Git Upstream Manager
License: GPLv2
Group: Development/Other

# git clone git://git.altlinux.org/people/piastry/packages/gitum.git

Url: http://wiki.etersoft.ru/GitUM
Packager: Konstantin Artyushkin <akv@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools-tests
BuildRequires: python-module-GitPython >= 0.3.0
BuildRequires: git-core >= 1.7

Requires: git-core >= 1.7
Requires: python-module-GitPython >= 0.3.0

Provides: gitum

Obsoletes: git-um

%description
Git Upstream Manager is the development tool that maintains your current
working git repository: pull upstream changes in the appropriate order
into your current working branch and keep all your patches up-to-date
and ready for a submission in the same time.

%prep
%setup -q

%build
%python_build

%install
%python_install

%check
%__python setup.py test

%files
%python_sitelibdir/*
%_bindir/%name

%changelog
* Tue Feb 07 2017 Konstantin Artyushkin <akv@altlinux.org> 0.8.6-alt1
- fix dosformat files bug with --keep-cr
- revert author wrong enocding utf-8
- added a git diff check in a gitum status command

* Fri Oct 07 2016 Konstantin Artyushkin <akv@altlinux.org> 0.8.5-alt1
- added stdout_as_string=False to git.show()
- log patch name when rebasing

* Fri Mar 04 2016 Konstantin Artyushkin <akv@altlinux.org> 0.8.4-alt2
- made --remote arg positional for push and pull commands

* Mon Oct 05 2015 Konstantin Artyushkin <akv@altlinux.org> 0.8.3-alt4
- fix for 0xE0 bug in hex of files by git.diff()

* Mon Feb 16 2015 Pavel Shilovsky <piastry@altlinux.org> 0.8.3-alt3
- Fix url

* Fri Jan 23 2015 Pavel Shilovsky <piastry@altlinux.org> 0.8.3-alt2
- Fix packager and urls in spec
- Fix setuptools buildrequires

* Thu Jan 22 2015 Pavel Shilovsky <piastry@altlinux.org> 0.8.3-alt1
- Continue removing branches if one does not exist
- Check current mainline HEAD for changes
- Fix update message when there is nothing to update

* Thu Jun 27 2013 Pavel Shilovsky <piastry@altlinux.org> 0.8.2-alt1
- Fix unicode commit messages support

* Sun Mar 31 2013 Pavel Shilovsky <piastry@altlinux.org> 0.8.1-alt1
- Use a default directory name for clone if missed
- Minor logging changes for pull and merge
- Fetch a new data from a remote before the existence check

* Fri Jan 18 2013 Pavel Shilovsky <piastry@altlinux.org> 0.8.0-alt1
- Improve logging
- Add status command

* Wed Nov 14 2012 Pavel Shilovsky <piastry@altlinux.org> 0.7.0-alt1
- Let setup.py run tests
- Improve restore command
- Move tests to unittest
- Rename current directory to upstream if the latter doesn't exist
- Improve branch processing during create
- Add capability for update to cherry-pick new commits
- Start patches branch from an empty state
- Make gitum commands work from non-root directory

* Thu Sep 20 2012 Pavel Shilovsky <piastry@altlinux.org> 0.6.4-alt1
- Use random temporary directory rather hardcoded one
- Fix python-module-GitPython dependence

* Mon Jun 18 2012 Pavel Shilovsky <piastry@altlinux.org> 0.6.3-alt1
- Fix creating config branch
- Fix missing merge branch

* Mon Jun 04 2012 Pavel Shilovsky <piastry@altlinux.org> 0.6.2-alt1
- Fix binary files problem
- Fix clone with a remote repo

* Fri May 11 2012 Pavel Shilovsky <piastry@altlinux.org> 0.6.1-alt1
- Fix bug in pull
- Fix bug in merge
- Change version in setup.py

* Sat May 05 2012 Pavel Shilovsky <piastry@altlinux.org> 0.6.0-alt1
- Add --track option for merge to save branch to defaults
- Save merge branch locally
- Add --track option for pull/push to save remote to defaults
- Fix pull without a saved remote
- Add support for several gitum remotes
- Add relative path support for clone

* Fri Mar 16 2012 Pavel Shilovsky <piastry@altlinux.org> 0.5.1-alt1
- Fix push config branch bug

* Wed Mar 14 2012 Pavel Shilovsky <piastry@altlinux.org> 0.5.0-alt1
- Fix push command
- Fix clone command in the no config branch case
- Reorder parameters in create call
- Change default name for current branch to mainline
- Let gitum work with default branches if a config is missed
- Eliminate editpatch command
- Change restore command
- Save config file in an empty branch
- Use specified message of update command in patches branch
- Simplify update command
- Allow optional restore for rebased branch only
- Work in rebased branch rather than current
- Make rebased branch local only
- Fix bugs in pull
- Minor code style fixes

* Wed Feb 15 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4.2-alt1
- Fix the argument parsing bug

* Fri Feb 03 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4.1-alt1
- Push rebased branch with --force option
- Add --remote option for pull

* Fri Feb 03 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4-alt1
- Add restore command
- Rename pull to merge
- Add clone/pull/push commands for a remote work
- Add --repo command line option to specify the repo path
- Bugfixes

* Wed Dec 14 2011 Pavel Shilovsky <piastry@altlinux.org> 0.3-alt1
- Make update command interface smarter
- Add editpatch command
- Fix a possible error during saving a state
- Improve logging

* Wed Nov 30 2011 Pavel Shilovsky <piastry@altlinux.org> 0.2-alt2
- Change a version in setup

* Wed Nov 30 2011 Pavel Shilovsky <piastry@altlinux.org> 0.2-alt1
- Improve create command
- Add remove command
- Simplify output messages
- Add branch argument to pull command
- Move config files to .git
- Use original authors for commits

* Mon Oct 31 2011 Pavel Shilovsky <piastry@altlinux.org> 0.1-alt1
- Initial build
