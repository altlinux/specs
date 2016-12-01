# $Id: python-module-bzr-git.spec $
# -*- coding: utf-8 -*-
Name: python-module-bzr-git
Version: 0.6.12
Release: alt2

%setup_python_module bzr-git

Summary: A GIT branch and repository format implementation for bzr
License: %gpl2plus
Group: Development/Python

Url: https://launchpad.net/bzr-git
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %modulename-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(Pre): rpm-build-licenses
Provides: bzr-git

%description
Using Bazaar with Git.

The bzr-git plugin provides support for using Bazaar with local and remote
Git repositories, as just another format. You can clone, pull from and
push to git repositories as you would with any native Bazaar branch.

The bzr-git plugin also adds three new bzr subcommands:

 * bzr git-objects: Extracts Git objects out of a Bazaar repository
 * bzr git-refs: Display Git refs from a Bazaar branch or repository
 * bzr git-import: Imports a local or remote Git repository to a set of Bazaar
                   branches

The 'git:' revision specifier can be used to find revisions by short or long
GIT SHA1.

This module is built for python %_python_version

%package -n git-remote-bzr
Summary: Remote helper for git to work with bzr repositories
Group: Development/Other
Requires: %name = %version-%release

%description -n git-remote-bzr
This command provides support for using bzr repositories as Git
remotes, through the bzr-git plugin. At the moment it supports cloning
from, fetching from and pushing into Bazaar repositories. Fetch support
is still experimental, and may be slow.

%package -n python-module-bzr-git-tests
Summary: bzr-git plugin tests
Group: Development/Other
Requires: %name = %version-%release
Requires: python%_python_version(bzrlib.tests)
Requires: python%_python_version(pysqlite2)
Requires: python%_python_version(dulwich.tests)
Requires: python%_python_version(tdb)

%description -n python-module-bzr-git-tests
This package contain tools and test suites for testing bzr-git.

%prep
%setup -n %modulename-%version
%patch0 -p1

%build
%python_build

%install
%python_install --install-lib %python_sitelibdir
%find_lang %name
install -dm0755 %buildroot%_man1dir
install -m0644 git-remote-bzr.1 %buildroot%_man1dir

%files
%python_sitelibdir/bzrlib/plugins/git
%exclude %python_sitelibdir/bzrlib/plugins/git/tests
%python_sitelibdir/*.egg-info
%doc HACKING INSTALL NEWS README TODO notes/*

%files -n git-remote-bzr
%_bindir/*
%_man1dir/*

%files -n python-module-bzr-git-tests
%dir %python_sitelibdir/bzrlib/plugins/git
%python_sitelibdir/bzrlib/plugins/git/tests

%changelog
* Thu Dec 01 2016 Anatoly Kitaykin <cetus@altlinux.org> 0.6.12-alt2
- Update to current repository version

* Wed Oct 02 2013 Anatoly Kitaykin <cetus@altlinux.org> 0.6.12-alt1
- Release 0.6.12

* Wed Oct 17 2012 Anatoly Kitaykin <cetus@altlinux.org> 0.6.9-alt1
- initial build


