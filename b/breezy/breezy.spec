# vim: set ft=spec: -*- rpm-spec -*-
%define _unpackaged_files_terminate_build 1

%def_with check
%def_with bzr

Name: breezy
Version: 3.2.2
Release: alt1.2

Summary: Breezy is a fork of the Bazaar version control system
License: GPL-2.0-or-later
Group: Development/Other

Url: https://github.com/breezy-team/breezy.git
Packager: Anatoly Kitaykin <cetus@altlinux.ru>

Source: %name-%version.tar

Patch0: %name-%version-alt.patch
Patch1: drop-distutils.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-six
BuildRequires: python3-module-Cython
BuildRequires: python3-module-configobj
BuildRequires: python3-module-packaging

%if_with check

BuildRequires: python3-module-docutils
BuildRequires: python3-module-paramiko
BuildRequires: python3-module-testtools
BuildRequires: python3-module-subunit
BuildRequires: python3-module-dulwich
BuildRequires: python3-module-subunit

%endif

%add_python3_req_skip lazr
# this module is provided by breezy.bzr.__init__ namespace
%add_python3_req_skip breezy.bzr.errors

Conflicts: %name-doc < %version-%release
Conflicts: bzr-git-remote

%description
Breezy (or brz) is a fork of the Bazaar version control system.
Breezy is a distributed version control system that is powerful, friendly, and scalable.
By default, Breezy provides support for both the Bazaar and Git file formats.

%package -n python3-module-breezy-tests
Summary: Tools for testing Breezy
Group: Development/Other
#BuildArch: noarch

Requires: %name = %version-%release
Provides: brz-selftest = %version-%release

%description -n python3-module-breezy-tests
Breezy is a fork of the Bazaar version control system.
This package contain tools and test suites for testing Breezy.

%package doc
Summary: %name documentation and examples
Group: Development/Other
BuildArch: noarch

Conflicts: %name < %version

%description doc
Breezy is a fork of the Bazaar version control system.
This package contains documentation and examples for using Breezy.

%if_with bzr
%package bzr
Summary: 'bzr' alias for Breezy
Group: Development/Other
BuildArch: noarch
Requires: %name
Provides: bzr = %EVR
Obsoletes: bzr

%description bzr
Breezy is a fork of the Bazaar version control system.
This package contains 'bzr' alias for breezy 'brz' command.
%endif

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%add_optflags -fno-strict-aliasing

%python3_build

%install

%python3_install --install-data=%_datadir

%if_with bzr
ln -s brz %buildroot%_bindir/bzr
%endif

%define breezy_docdir %_docdir/%name-%version

install -dm0755 %buildroot%breezy_docdir
install -m0644 BRANCH.TODO CODE_OF_CONDUCT.md INSTALL NEWS README.rst SECURITY.md TODO %buildroot%breezy_docdir
cp -a doc contrib %buildroot%breezy_docdir
# Hack! Need a subst in setup.py
cp -a breezy/locale %buildroot%_datadir
%find_lang %name

%check
%python3_build check

%files -f %name.lang
%_bindir/*
%exclude %_bindir/bzr
%_man1dir/*

%python3_sitelibdir/*
%exclude %python3_sitelibdir/breezy/tests
%exclude %python3_sitelibdir/breezy/bzr/tests
%exclude %python3_sitelibdir/breezy/git/tests
%exclude %python3_sitelibdir/breezy/util/tests
%exclude %python3_sitelibdir/breezy/plugins/*/tests

%breezy_docdir
%exclude %breezy_docdir/doc
%exclude %breezy_docdir/contrib

%files -n python3-module-breezy-tests
%python3_sitelibdir/breezy/tests
%python3_sitelibdir/breezy/bzr/tests
%python3_sitelibdir/breezy/git/tests
%python3_sitelibdir/breezy/util/tests
%python3_sitelibdir/breezy/plugins/*/tests

%files doc
%dir %breezy_docdir
%breezy_docdir/doc
%breezy_docdir/contrib

%if_with bzr
%files bzr
%_bindir/bzr
%endif

%changelog
* Fri Oct 27 2023 Anton Vyatkin <toni@altlinux.org> 3.2.2-alt1.2
- NMU: Dropped dependency on distutils.

* Wed Aug 16 2023 Daniel Zagaynov <kotopesutility@altlinux.org> 3.2.2-alt1.1
- NMU: ignored unmet dep breezy.bzr.errors

* Wed Apr 13 2022 Anatoly Kitaykin <cetus@altlinux.org> 3.2.2-alt1
- Release 3.2.2

* Wed Jan 26 2022 Grigory Ustinov <grenka@altlinux.org> 3.2.1-alt3
- Fixed build with python3.10

* Fri Sep 10 2021 Anatoly Kitaykin <cetus@altlinux.org> 3.2.1-alt2
- Fixed binary version

* Thu Sep 09 2021 Anatoly Kitaykin <cetus@altlinux.org> 3.2.1-alt1
- Release 3.2.1
- Symlink 'bzr' separated to breezy-bzr subpackage

* Mon Aug 23 2021 Anatoly Kitaykin <cetus@altlinux.org> 3.2.0-alt3
- Fixed package dependencies

* Mon Aug 23 2021 Anatoly Kitaykin <cetus@altlinux.org> 3.2.0-alt2
- Replaces bzr (closes #40738)

* Wed May 05 2021 Anatoly Kitaikin <cetus@altlinux.org> 3.2.0-alt1
- Release 3.2.0

* Tue Feb 02 2021 Anatoly Kitaykin <cetus@altlinux.org> 3.1.0.8-alt1
- Release 3.1.0-8 (debian)

* Fri Jul 10 2020 Anatoly Kitaikin <cetus@altlinux.org> 3.1.0-alt1
- Release 3.1.0

* Mon Jan 13 2020 Anatoly Kitaykin <cetus@altlinux.org> 3.0.2-alt1
- Release 3.0.2
- Check enabled

* Mon Aug 12 2019 Anatoly Kitaikin <cetus@altlinux.org> 3.0.1-alt3
- Git plugin path fix

* Tue Jul 09 2019 Anatoly Kitaikin <cetus@altlinux.org> 3.0.1-alt2
- Rebuilt with python3

* Wed Jun 19 2019 Anatoly Kitaykin <cetus@altlinux.org> 3.0.1-alt1
- Release 3.0.1

* Fri Apr 26 2019 Anatoly Kitaykin <cetus@altlinux.org> 3.0.0-alt1
- Initial build
