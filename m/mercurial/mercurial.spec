# tests are too slow
%def_without check

Name: mercurial
Version: 6.3.1
Release: alt1

Summary: Mercurial source code management system

Group: Development/Other
License: GPLv2+
Url: https://mercurial-scm.org

Source: %name-%version.tar

Packager: Yury Yurevich <anarresti@altlinux.org>

BuildPreReq: rpm-build-python3
BuildRequires: asciidoc xmlto python3-module-docutils
BuildRequires: python3-modules-sqlite3 libzstd-devel

%if_with check
BuildRequires: unzip
%endif

Provides: hg = %version-%release

%add_findreq_skiplist %python3_sitelibdir/hgext/*
%add_findreq_skiplist %python3_sitelibdir/mercurial/win*
%add_findreq_skiplist %python3_sitelibdir/mercurial/scmwin*
%add_findreq_skiplist %python3_sitelibdir/mercurial/httpclient/tests/*
%add_findreq_skiplist %python3_sitelibdir/mercurial/py3kcompat.py

%description
Mercurial is a fast fast, lightweight
Source Control Management system designed for
efficient handling of very large distributed projects

%package -n bash-completion-%name
Summary: Bash completion for mercurial
Group: Development/Other
BuildArch: noarch

%description -n bash-completion-%name
Bash completion for mercurial

%package -n %name-hgext
Summary: Mercurial bundled extensions
Group: Development/Other
Requires: %name = %version-%release, tk, python3-module-Pygments

%description -n %name-hgext
Bundled extensions for Mercurial SCM. See
http://mercurial.selenic.com/wiki/UsingExtensions for details.
This extensions are included in package:

- acl -- Manage commit access to parts of a repo using control list
- alias -- User-defined command aliases
- bisect -- Quickly find revision that introduces a bug or feature
- bookmarks -- Markers on commits that move on commit
- bugzilla -- Update Bugzilla entries from commit messages
- children -- Display children revisions
- churn -- Show change statistics per author
- convert -- Convert repositories from other SCMs into Mercurial
- color -- Color output for the diff, status and qseries commands
- extdiff -- Compare changes using external programs
- fetch -- Conveniently pull, merge and update in one step
- gpg -- Sign changesets and check signatures using GnuPG
- graphlog -- Show revision history alongside an ASCII revision graph
- hgcia -- Send notifications to http://cia.navi.cx
- highlight -- Highlight syntax in the file revision view of hgweb
- imerge --Perform interactive, interruptible merges
- interhg -- Change changelog and summary text in InterWiki way
- keyword -- Use CVS-like keyword expandsion in tracked files
- mq -- Mercurail Patch Queues - manage changes as series of patches
- notify -- Send email to subscribed emails to notify repository changes
- pager -- Allows you to use pager
- parentrevspec -- Use git-like foo^ to refer to the parent of revision foo
- patchbomb -- Send a collection of changesets as a series of patch emails
- progress -- Show progress bars for some actions
- purge -- Purge all files and dirs that are not being tracked
- rebase -- Move revisions from one point to another
- record -- Comit changes per-hunk, like darcs record or git interactive commit
- relink -- Recreates hardlinks between repository clones
- schemes -- Add shortcuts to urls as url schemes
- share -- Share repository history between multiply repos
- transplant -- Cherry-picking, rebasing and changeset rewriting
- zeroconf -- Announce and browse repositories via zeroconf/bonjour

%prep
%setup

%build
%python3_build

%make PYTHON=%__python3 -C doc clean
%make PYTHON=%__python3 -C doc all

%install
%python3_install
install -D doc/hg.1 %buildroot%_man1dir/hg.1
install -D doc/hgrc.5 %buildroot%_man5dir/hgrc.5
install -D doc/hgignore.5 %buildroot%_man5dir/hgignore.5
install -D contrib/bash_completion %buildroot%_sysconfdir/bash_completion.d/%name
install -D contrib/hgk  %buildroot%_bindir/hgk
install contrib/hg-ssh %buildroot%_bindir/

mkdir -p %buildroot%_sysconfdir/%name/hgrc.d

%check
%make PYTHON=%__python3 check

%files
%doc CONTRIBUTORS README.rst contrib doc/*html
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/hgrc.d
%_bindir/hg
%_bindir/hg-ssh
%python3_sitelibdir/mercurial
%python3_sitelibdir/hgdemandimport
%python3_sitelibdir/%name-*py%_python3_version.egg-info
%_man1dir/hg.*
%_man5dir/hgrc.*
%_man5dir/hgignore.*

%exclude %python3_sitelibdir/hgext/*

%files -n bash-completion-%name
%dir %_sysconfdir/bash_completion.d
%_sysconfdir/bash_completion.d/%name
%dir %_datadir/bash-completion
%dir %_datadir/bash-completion/completions
%_datadir/bash-completion/completions/hg
%dir %_datadir/zsh
%dir %_datadir/zsh/site-functions
%_datadir/zsh/site-functions/_hg

%files -n %name-hgext
%_bindir/hgk
%python3_sitelibdir/hgext
%python3_sitelibdir/hgext3rd

%changelog
* Tue Nov 29 2022 Grigory Ustinov <grenka@altlinux.org> 6.3.1-alt1
- 6.3.1.

* Mon Jul 25 2022 Grigory Ustinov <grenka@altlinux.org> 6.2-alt1
- 6.2.

* Tue Jan 11 2022 Grigory Ustinov <grenka@altlinux.org> 6.0.1-alt1
- 6.0.1.

* Mon Sep 13 2021 Grigory Ustinov <grenka@altlinux.org> 5.9.1-alt1
- 5.9.1.

* Tue May 25 2021 Grigory Ustinov <grenka@altlinux.org> 5.8-alt1
- 5.8.

* Fri Mar 19 2021 Grigory Ustinov <grenka@altlinux.org> 5.7.1-alt1
- 5.7.1.

* Tue Nov 10 2020 Grigory Ustinov <grenka@altlinux.org> 5.6-alt1
- 5.6.

* Thu Oct 29 2020 Grigory Ustinov <grenka@altlinux.org> 5.5.2-alt1
- 5.5.2. (Closes: #39138)
- Use bundled libzstd (details in revert commit).

* Thu Oct 01 2020 Grigory Ustinov <grenka@altlinux.org> 5.5.1-alt1
- 5.5.1.
- Transfer on python3.
- Use system libzstd.

* Tue Jun 30 2020 Grigory Ustinov <grenka@altlinux.org> 5.4.1-alt1
- 5.4.1 (Closes: #38654).
- spec: Set explicitly PYTHON=%%__python to make the docs. (thx arei@)
- Set python version explicitly in the shebang of hg-ssh. (thx arei@)

* Thu Aug 08 2019 Grigory Ustinov <grenka@altlinux.org> 5.1-alt1
- 5.1

* Mon May 20 2019 Grigory Ustinov <grenka@altlinux.org> 5.0-alt1
- 5.0

* Wed Mar 06 2019 Grigory Ustinov <grenka@altlinux.org> 4.9-alt1
- 4.9

* Thu Oct 18 2018 Alexey Shabalin <shaba@altlinux.org> 4.7.2-alt1
- 4.7.2

* Thu Jul 07 2016 Alexey Shabalin <shaba@altlinux.ru> 3.8.4-alt1
- 3.8.4

* Tue Aug 18 2015 Alexey Shabalin <shaba@altlinux.ru> 3.5-alt1
- 3.5

* Thu Jul 02 2015 Alexey Shabalin <shaba@altlinux.ru> 3.4.2-alt1
- 3.4.2

* Mon Dec 22 2014 Alexey Shabalin <shaba@altlinux.ru> 3.2.3-alt1
- 3.2.3

* Fri Oct 03 2014 Alexey Shabalin <shaba@altlinux.ru> 3.1.2-alt1
- 3.1.2

* Fri Sep 12 2014 Alexey Shabalin <shaba@altlinux.ru> 3.1.1-alt1
- 3.1.1

* Tue May 13 2014 Alexey Shabalin <shaba@altlinux.ru> 3.0-alt1
- 3.0

* Fri Mar 14 2014 Alexey Shabalin <shaba@altlinux.ru> 2.9.1-alt1
- 2.9.1

* Tue Jan 14 2014 Alexey Shabalin <shaba@altlinux.ru> 2.8.2-alt1
- 2.8.2

* Mon Sep 09 2013 Alexey Shabalin <shaba@altlinux.ru> 2.7.1-alt1
- 2.7.1

* Tue Jan 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1
- Version 2.4.2 (ALT #27599)

* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Wed Nov 30 2011 Alexey Shabalin <shaba@altlinux.ru> 2.0-alt1
- 2.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.5-alt2.1.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt2.1
- Rebuilt for debuginfo

* Sat Mar  6 2010 Yury Yurevich <anarresti@altlinux.org> 1.5-alt2
- Fix gear inheritance by merging with 1.4-alt1.1

* Sat Mar  6 2010 Yury Yurevich <anarresti@altlinux.org> 1.5-alt1
- Update upstream to 1.5
- Move bundled extensions to separate package

* Wed Feb 24 2010 Alexey Shabalin <shaba@altlinux.ru> 1.4.3-alt1
- Update upstream to 1.4.3
- Update license to GPLv2+
- Add provides hg
- Move bash-completion to subpackage
- Add mercurial-hgk subpackage
- Add system wide config dir %_sysconfdir/%name/hgrc.d
- Add hg-ssh, mercurial-convert-repo utils

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4-alt1.1
- Rebuilt with python 2.6

* Mon Nov 23 2009 Yury Yurevich <anarresti@altlinux.org> 1.4-alt1
- Update upstream to 1.4

* Fri Jul 24 2009 Yury Yurevich <anarresti@altlinux.org> 1.3.1-alt1
- Update upstream to 1.3.1

* Sun Jul 12 2009 Yury Yurevich <anarresti@altlinux.org> 1.3-alt1
- Update upstream to 1.3

* Fri Apr 10 2009 Yury Yurevich <anarresti@altlinux.org> 1.2.1-alt1
- Update upstream to 1.2.1
- Push sources to gear

* Wed Dec 03 2008 Igor Zubkov <icesik@altlinux.org> 1.1-alt1
- 1.0.1 -> 1.1

* Tue Jul 15 2008 Igor Zubkov <icesik@altlinux.org> 1.0.1-alt1
- 1.0 -> 1.0.1
- CVE-2008-2942
  + insufficient input validation (patch from upstream)

* Mon May 12 2008 Igor Zubkov <icesik@altlinux.org> 1.0-alt3
- build without test

* Thu Apr 10 2008 Igor Zubkov <icesik@altlinux.org> 1.0-alt2
- fix build on x86_64

* Thu Apr 03 2008 Igor Zubkov <icesik@altlinux.org> 1.0-alt1
- 0.9.5 -> 1.0
- buildreq

* Fri Feb 15 2008 Grigory Batalov <bga@altlinux.ru> 0.9.5-alt1.1
- Rebuilt with python-2.5.

* Tue Oct 23 2007 Igor Zubkov <icesik@altlinux.org> 0.9.5-alt1
- 0.9.4 -> 0.9.5
- build with tests
- buildreq

* Wed Jul 18 2007 Igor Zubkov <icesik@altlinux.org> 0.9.4-alt1
- 0.9.3 -> 0.9.4
- buildreq

* Sat Feb 03 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.9.3-alt1
- New version

* Sun Sep 10 2006 Igor Zubkov <icesik@altlinux.org> 0.9.1-alt2
- remove python2.4(win32api) from requires
- buildreq

* Wed Aug 23 2006 Igor Zubkov <icesik@altlinux.org> 0.9.1-alt1
- 0.8 -> 0.9.1

* Sat Mar 25 2006 Igor Zubkov <icesik@altlinux.ru> 0.8-alt1
- 0.8

* Wed Nov 16 2005 Igor Zubkov <icesik@altlinux.ru> 0.7-alt1
- Initial build for Sisyphus
