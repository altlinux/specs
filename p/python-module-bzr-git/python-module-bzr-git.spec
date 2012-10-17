# $Id: python-module-bzr-git.spec $
# -*- coding: utf-8 -*-
Name: python-module-bzr-git
Version: 0.6.9
Release: alt1

%setup_python_module bzr-git

Summary: A plugin for bzr to work with git trees.
License: %gpl2plus
Group: Development/Python

Url: https://launchpad.net/bzr-git
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: %modulename-%version.tar

BuildRequires(Pre): rpm-build-licenses

%description
A plugin for bzr to work with git trees.
All operations except for "push" are supported.

This also includes a remote helper for Git to work with bzr.

This module is built for python %_python_version

%package -n git-remote-bzr
Summary: Remote helper for git to work with bzr
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
* Wed Oct 17 2012 Anatoly Kitaykin <cetus@altlinux.org> 0.6.9-alt1
- initial build


