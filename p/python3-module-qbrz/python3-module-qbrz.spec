# -*- coding: utf-8 -*-
%define _unpackaged_files_terminate_build 1

Name: python3-module-qbrz
Version: 0.23.2
Release: alt2.bzr20200724

Summary: A simple Qt cross-platform frontend for some of Bazaar commands
License: GPLv2+
Group: Development/Python

Url: https://launchpad.net/qbrz
Packager: Anatoly Kitaikin <cetus@altlinux.org>

Source: qbrz-%version.tar

Patch0: %name-%version-%release.patch

Provides: qbrz

BuildRequires(pre): rpm-build-python3

%description
The purpose of this plugin is to provide a graphical user
interface for those Breezy commands where it can simplify the usage.
Highlighting of differences between files, "browsable" log view, commit
only some files without listing them all on the command line, etc.

QBrz provides a GUI frontend for many core brz commands and several
universal dialogs and helper commands.  The qbrz equivalents for core
brz commands have the same names as the CLI commands but with a 'q'
prefix.  See home page for more details.

Breezy is a fork of Bazaar version control system

This module is built for python %__python_version

%package tests
Summary: Qbrz plugin tests
Group: Development/Other

Requires: %name = %version-%release

%description tests
This package contains tools and test suites for testing qbrz plugin.

%prep
%setup -n qbrz-%version
%patch0 -p1

%build
%python3_build

%install
%python3_install --install-lib %python3_sitelibdir

%files
%python3_sitelibdir/breezy/plugins/qbrz
%exclude %python3_sitelibdir/breezy/plugins/qbrz/*.txt
%exclude %python3_sitelibdir/breezy/plugins/qbrz/lib/tests
%python3_sitelibdir/*.egg-info
%doc AUTHORS.txt NEWS.txt README.txt TODO.txt

%files tests
%dir %python3_sitelibdir/breezy/plugins/qbrz/lib
%python3_sitelibdir/breezy/plugins/qbrz/lib/tests

%changelog
* Wed Aug 05 2020 Anatoly Kitaikin <cetus@altlinux.org> 0.23.2-alt2.bzr20200724
- current snapshot

* Sun Feb 16 2020 Anatoly Kitaikin <cetus@altlinux.org> 0.23.2-alt1.bzr20191027
- Qt frontend for breezy

* Fri Dec 01 2017 Anatoly Kitaykin <cetus@altlinux.org> 0.23.2-alt1
- release 0.23.2

* Wed Oct 02 2013 Anatoly Kitaykin <cetus@altlinux.org> 0.23.1-alt1
- release 0.23.1
- separate package for qbzr tests

* Sun Oct 07 2012 Anatoly Kitaikin <cetus@altlinux.org> 0.23.0-alt1
- release 0.23.0

* Thu Apr 19 2012 Anatoly Kitaikin <cetus@altlinux.org> 0.22.2-alt1
- Qt frontend for bazaar 

