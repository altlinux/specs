# vim: set ft=spec: -*- rpm-spec -*-
%define _unpackaged_files_terminate_build 1

%def_with check
%def_with bzr

Name: breezy
Version: 3.3.7
Release: alt1

Summary: Breezy is a fork of the Bazaar version control system
License: GPL-2.0-or-later
Group: Development/Other

Url: https://github.com/breezy-team/breezy.git
Packager: Anatoly Kitaykin <cetus@altlinux.ru>

Source0: %name-%version.tar
Source1: %name-cargo.tar

Patch0: %name-%version-alt.patch
Patch1: drop-distutils.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-six
BuildRequires: python3-module-Cython
BuildRequires: python3-module-configobj
BuildRequires: python3-module-packaging
BuildRequires: python3-module-wheel
BuildRequires: python3-module-setuptools-rust
BuildRequires: python3-module-tzlocal
BuilDrequires: python3-module-yaml
BuildRequires: rust rust-cargo
BuildRequires: python3(setuptools-gettext)

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

Requires: python3-module-tzlocal

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
%setup -a1
%patch0 -p1
%patch1 -p1

%build
%add_optflags -fno-strict-aliasing

mkdir -p .cargo
cat > .cargo/config << EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "cargo"

[profile.release]
strip = "none"
lto= "thin"
debug = "full"
EOF
%pyproject_build

%install
%__make man1/brz.1
%pyproject_install

%if_with bzr
ln -s brz %buildroot%_bindir/bzr
%endif

%define breezy_docdir %_docdir/%name-%version

install -dm0755 %buildroot%breezy_docdir
install -m0644 BRANCH.TODO CODE_OF_CONDUCT.md INSTALL NEWS README.rst SECURITY.md TODO %buildroot%breezy_docdir
cp -a doc contrib %buildroot%breezy_docdir
%find_lang %name
install -dm0755 %buildroot%_man1dir
install -m0644 man1/brz.1 %buildroot%_man1dir/

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
* Wed May 08 2024 L.A. Kostis <lakostis@altlinux.ru> 3.3.7-alt1
- NMU:
  + 3.3.7.
  + added rust BR.

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
