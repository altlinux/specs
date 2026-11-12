%def_with check

Name: gitum
Version: 2.1.0
Release: alt1

Summary: Git Upstream Manager

License: GPL-2.0-or-later
Group: Development/Other
Url: https://wiki.etersoft.ru/GitUM

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-git: https://github.com/Etersoft/gitum.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-pyproject
BuildRequires: python3-module-setuptools

%if_with check
BuildRequires: git-core >= 2.45
BuildRequires: python3-module-pytest
%endif

BuildRequires: python3 >= 3.11

Requires: git-core >= 2.45

Provides: git-um = %EVR
Obsoletes: git-um < %EVR

%description
gitum helps to develop in parallel with an external upstream and to stay
in sync with it: stacks of layer branches moved onto a new upstream
release in one pass, every change classified (applied, resolved, already
upstream, backported, dropped), an append-only journal of states shared
without force pushes, change fates and series with merge requests,
upstream submission queue, wine-staging style series and RPM patch sets.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# all tests: unit, end-to-end cycles over several releases, crash recovery;
# they need only git and run offline (a fake forge listens on 127.0.0.1)
%pyproject_run_pytest

%files
%_bindir/%name
%python3_sitelibdir/gitum/
%python3_sitelibdir/%name-%version.dist-info/

%changelog
* Thu Nov 12 2026 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- series: merge request texts with images (gitum mr), bugs in named
  trackers with an index (gitum bugs) and a [hooks] series event
- gitum restore brings the stack back to an earlier journal state
- export --dep3 writes change fates as DEP-3 fields, import reads them;
  export --verify checks that the patches rebuild the layer
- a series standing on a newer upstream than the local ref is warned about
- gitum reads only public merge requests and uses no tokens
- command line: subcommands for every command group, export/import
  --format quilt|spec|staging, port --onto, report --format html,
  reject; usage mistakes exit with 1; meaningless options are refused
- fixes from an audit: START tags no longer revert on publish, non-ASCII
  file names in conflicts, recovery of post-command and accept, claims
  and locks, patch numbering of dependent series, fewer git processes

* Thu Nov 12 2026 Vitaly Lipatov <lav@altlinux.ru> 2.0.0-alt1
- gitum 2, rewritten in Python 3 without GitPython:
  + layers over upstreams; gitum sync moves the whole stack onto a new
    release in one pass in a private work tree, branches move in one
    atomic transaction
  + every change classified (picked, resolved by rerere, rules, agent or
    a person, dropped as upstream or backport, revert pairs, emptied)
  + journal of states (gitum/journal) and linear history branches
    (gitum/history/*) shared without force pushes
  + review candidates, publish/pull with commits of others put on top,
    hooks with JSON events and a stable environment
  + change identities and fates, check-upstream with verified content,
    forges (GitHub, GitLab, Forgejo)
  + series with dependencies, variants, upstream queues, prepare for
    upstream, backports, claims for parallel sessions
  + generated layers (wine-staging, command), spec/quilt/staging patch
    sets, HTML reports
  + recovery from a crash at any point (gitum continue)
- gitum 1 commands and repositories are no longer supported
- end-to-end and crash tests run in %%check

* Fri Jul 13 2018 Vitaly Lipatov <lav@altlinux.ru> 0.8.6-alt2
- cleanup spec, fix build

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
