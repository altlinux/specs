%def_with check
Name: opam
Version: 2.5.1
Release: alt1
Summary: A source-based package manager for OCaml
Group: Development/ML
License: LGPL-2.1-only WITH OCaml-LGPL-linking-exception
Url: https://opam.ocaml.org
VCS: https://github.com/ocaml/opam
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires: ocaml
BuildRequires: dune
BuildRequires: ocaml-compiler-libs
BuildRequires: ocaml-base64-devel >= 3.1.0
BuildRequires: ocaml-cudf-devel >= 0.7
BuildRequires: ocaml-dose3-devel >= 6.1
BuildRequires: ocaml-jsonm-devel
BuildRequires: ocaml-mccs-devel >= 1.1+17
BuildRequires: ocaml-ocamlgraph-devel
BuildRequires: ocaml-opam-0install-cudf-devel >= 0.5.0
BuildRequires: ocaml-opam-file-format-devel >= 2.1.4
BuildRequires: ocaml-patch-devel >= 3.0.0
BuildRequires: ocaml-re-devel >= 1.10.0
BuildRequires: ocaml-sha-devel >= 1.13
BuildRequires: ocaml-spdx_licenses-devel >= 1.0.0
BuildRequires: ocaml-swhid_core-devel
BuildRequires: ocaml-uutf-devel
BuildRequires: libstdc++-devel

Requires: ocaml-opam-installer = %EVR

%if_with check
BuildRequires: rpm-build-vm
BuildRequires: git
BuildRequires: diffutils
BuildRequires: libssl-devel
%endif

%description
OPAM stands for OCaml PAckage Manager.
It aims to suit to a vast number of users and use cases,
and has unique features:

 * Powerful handling of dependencies:
   versions constraints, optional dependencies, conflicts, etc.
 * Multiple repositories backends: HTTP, rsync, git
 * Ease to create packages and repositories
 * Ability to switch between different compiler versions

Typically, OPAM will probably make your life easier if you recognize
yourself in at least one of these profiles:

 * You use multiple versions of the OCaml compiler, or you hack the
   compiler yourself and needs to frequently switch between compiler
   versions.
 * You use or develop software that needs a specific and/or modified
   version of the OCaml compiler to be installed.
 * You use or develop software that depends on a specific version of an
   OCaml library, or you just want to install a specific version of a
   package, not just the latest one.
 * You want to create your own packages yourself, put them on your own
   repository, with minimal effort.

%package -n ocaml-opam-client
Summary: Client library for opam
Group: Development/ML

%description -n ocaml-opam-client
Actions on the opam root, switches, installations, and front-end.

%package -n ocaml-opam-client-devel
Summary: Development files for ocaml-opam-client
Requires: ocaml-opam-client = %EVR
Group: Development/ML

%description -n ocaml-opam-client-devel
Development files for ocaml-opam-client.

%package -n ocaml-opam-core
Summary: Core library for opam
Group: Development/ML

%description -n ocaml-opam-core
Small standard library extensions, and generic system interaction
modules used by opam.

%package -n ocaml-opam-core-devel
Summary: Development files for ocaml-opam-core
Requires: ocaml-opam-core = %EVR
Group: Development/ML

%description -n ocaml-opam-core-devel
Development files for ocaml-opam-core.

%package -n ocaml-opam-devel
Summary: Bootstrapped development binary for opam
Group: Development/ML

%description -n ocaml-opam-devel
This package compiles (bootstraps) opam. For consistency and safety of
the installation, the binaries are not installed into the PATH, but into
lib/opam-devel, from where the user can manually install them
system-wide.

%package -n ocaml-opam-devel-devel
Summary: Development files for ocaml-opam-devel
Requires: ocaml-opam-devel = %EVR
Group: Development/ML

%description -n ocaml-opam-devel-devel
Development files for ocaml-opam-devel.

%package -n ocaml-opam-format
Summary: Format library for opam
Group: Development/ML

%description -n ocaml-opam-format
Definition of opam datastructures and its file interface.

%package -n ocaml-opam-format-devel
Summary: Development files for ocaml-opam-format
Requires: ocaml-opam-format = %EVR
Group: Development/ML

%description -n ocaml-opam-format-devel
Development files for ocaml-opam-format.

%package -n ocaml-opam-installer
Summary: Installation of files to a prefix, following opam conventions
Group: Development/ML

%description -n ocaml-opam-installer
opam-installer is a small tool that can read *.install files, as defined
by opam [1], and execute them to install or remove package files without
going through opam.

[1] http://opam.ocaml.org/doc/2.0/Manual.html#lt-pkgname-gt-install

%package -n ocaml-opam-installer-devel
Summary: Development files for ocaml-opam-installer
Requires: ocaml-opam-installer = %EVR
Group: Development/ML

%description -n ocaml-opam-installer-devel
Development files for ocaml-opam-installer.

%package -n ocaml-opam-repository
Summary: Repository library for opam
Group: Development/ML

%description -n ocaml-opam-repository
This library includes repository and remote sources handling, including
curl/wget, rsync, git, mercurial, darcs backends.

%package -n ocaml-opam-repository-devel
Summary: Development files for ocaml-opam-repository
Requires: ocaml-opam-repository = %EVR
Group: Development/ML

%description -n ocaml-opam-repository-devel
Development files for ocaml-opam-repository.

%package -n ocaml-opam-solver
Summary: Solver library for opam
Group: Development/ML

%description -n ocaml-opam-solver
Solver and Cudf interaction. This library is based on the Cudf and Dose
libraries, and handles calls to the external solver from opam.

%package -n ocaml-opam-solver-devel
Summary: Development files for ocaml-opam-solver
Requires: ocaml-opam-solver = %EVR
Group: Development/ML

%description -n ocaml-opam-solver-devel
Development files for ocaml-opam-solver.

%package -n ocaml-opam-state
Summary: State library for opam
Group: Development/ML

%description -n ocaml-opam-state
Handling of the ~/.opam hierarchy, repository and switch states.

%package -n ocaml-opam-state-devel
Summary: Development files for ocaml-opam-state
Requires: ocaml-opam-state = %EVR
Group: Development/ML

%description -n ocaml-opam-state-devel
Development files for ocaml-opam-state.

%prep
%setup
%patch0 -p1

%build
%dune_build -p opam-client,opam-core,opam-devel,opam-format,opam-installer,opam-repository,opam-solver,opam-state,opam

%install
%dune_install_multi opam-client opam-core opam-devel opam-format opam-installer opam-repository opam-solver opam-state opam
mv ocaml-files.runtime.opam ocaml-files.runtime.opam.lst
cat ocaml-files.devel.opam >> ocaml-files.runtime.opam.lst
rm -f ocaml-files.devel.opam

%check
cat <<__EOF__ >run-test-in-vm.sh
#!/bin/bash
sudo /sbin/sysctl kernel.userns_restrict=0
sudo /sbin/sysctl kernel.unprivileged_userns_clone=1
export export TESTN0REP0=0
export TESTALL=0
%dune_check -p opam-client,opam-core,opam-format,opam-installer,opam,opam-repository,opam-state,opam-solver
__EOF__
chmod a+x ./run-test-in-vm.sh
vm-run --user ./run-test-in-vm.sh


%files -f ocaml-files.runtime.opam.lst

%files -n ocaml-opam-client -f ocaml-files.runtime.opam-client

%files -n ocaml-opam-client-devel -f ocaml-files.devel.opam-client

%files -n ocaml-opam-core -f ocaml-files.runtime.opam-core

%files -n ocaml-opam-core-devel -f ocaml-files.devel.opam-core

%files -n ocaml-opam-devel -f ocaml-files.runtime.opam-devel

%files -n ocaml-opam-devel-devel -f ocaml-files.devel.opam-devel

%files -n ocaml-opam-format -f ocaml-files.runtime.opam-format

%files -n ocaml-opam-format-devel -f ocaml-files.devel.opam-format

%files -n ocaml-opam-installer -f ocaml-files.runtime.opam-installer

%files -n ocaml-opam-installer-devel -f ocaml-files.devel.opam-installer

%files -n ocaml-opam-repository -f ocaml-files.runtime.opam-repository

%files -n ocaml-opam-repository-devel -f ocaml-files.devel.opam-repository

%files -n ocaml-opam-solver -f ocaml-files.runtime.opam-solver

%files -n ocaml-opam-solver-devel -f ocaml-files.devel.opam-solver

%files -n ocaml-opam-state -f ocaml-files.runtime.opam-state

%files -n ocaml-opam-state-devel -f ocaml-files.devel.opam-state

%changelog
* Mon Apr 20 2026 Anton Farygin <rider@altlinux.org> 2.5.1-alt1
- 2.5.0 -> 2.5.1

* Tue Mar 17 2026 Anton Farygin <rider@altlinux.org> 2.5.0-alt2
- temporarily added a dependency on opam-installer to the opam package
  to simplify the OCaml bootstrapping process in the p11 branch

* Thu Dec 25 2025 Anton Farygin <rider@altlinux.org> 2.5.0-alt1
- 2.3.0 -> 2.5.0
- switch from make to dune build system
- build opam libraries for use as dependencies by other packages
- enable tests

* Fri Jan 24 2025 Anton Farygin <rider@altlinux.ru> 2.3.0-alt2
- changed BR to fix build with rpm-build-ocaml >= 1.7

* Tue Dec 24 2024 Anton Farygin <rider@altlinux.ru> 2.3.0-alt1
- 2.2.1 -> 2.3.0

* Thu Sep 17 2024 Anton Farygin <rider@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Thu Nov 02 2023 Anton Farygin <rider@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Wed Jan 25 2023 Anton Farygin <rider@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Fri Oct 07 2022 Anton Farygin <rider@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Fri Dec 31 2021 Anton Farygin <rider@altlinux.ru> 2.1.2-alt1
- 2.1.2
- built with posix ACL support

* Wed Nov 03 2021 Anton Farygin <rider@altlinux.ru> 2.1.1-alt1
- 2.1.1
- added a patch from debian to support dose3 > 6.0.1

* Tue Aug 03 2021 Anton Farygin <rider@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Thu Jul 29 2021 Anton Farygin <rider@altlinux.ru> 2.0.9-alt1
- 2.0.9

* Wed May 19 2021 Anton Farygin <rider@altlinux.ru> 2.0.8-alt2
- removed ocaml-odoc from BR

* Mon Apr 05 2021 Anton Farygin <rider@altlinux.org> 2.0.8-alt1
- 2.0.8

* Fri Apr 24 2020 Anton Farygin <rider@altlinux.ru> 2.0.7-alt1
- 2.0.7

* Wed Apr 15 2020 Anton Farygin <rider@altlinux.ru> 2.0.6-alt2
- applied upstream patch for build with dune 2.5

* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 2.0.6-alt1
- 2.0.6

* Sat Aug 10 2019 Anton Farygin <rider@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 2.0.4-alt2
- rebuilt with ocaml-4.08

* Sat Apr 06 2019 Anton Farygin <rider@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Wed Feb 13 2019 Anton Farygin <rider@altlinux.ru> 2.0.3-alt1
- 2.0.3

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Mon Oct 22 2018 Anton Farygin <rider@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Wed May 23 2018 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1.rc
- 2.0.0-rc

* Thu May 17 2018 Anton Farygin <rider@altlinux.ru> 1.3.1-alt2
- fixed stubs libraries location

* Thu Dec 21 2017 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- first build for ALT

