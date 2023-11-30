%def_with check
Name: ocaml-dose3
Version: 7.0.0
Release: alt2
Summary: Framework for managing distribution packages and dependencies
Group: Development/ML

%global libname %(echo %name | sed -e 's/^ocaml-//')

# Linking exception, see included COPYING file.
License: LGPLv3+ with OCaml-LGPL-linking-exception
Url: http://www.mancoosi.org/software/

Source0: %name-%version.tar

BuildRequires: ocaml
BuildRequires: dune
BuildRequires: ocaml-ocamlgraph-devel
BuildRequires: ocaml-extlib-devel
BuildRequires: ocaml-expat-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-cudf-devel
BuildRequires: ocaml-camlbz2-devel
BuildRequires: ocaml-base64-devel
BuildRequires: ocaml-parmap-devel
BuildRequires: ocaml-odoc
BuildRequires: ocaml-zip-devel
BuildRequires: ocaml-camlp-streams-devel
%if_with check
BuildRequires: ocaml-ounit-devel
BuildRequires: /usr/bin/dpkg 
BuildRequires: python3-module-yaml
%endif
BuildRequires: rpm-devel
BuildRequires: zlib-devel
BuildRequires: perl

# Depend on pod2man, pod2html.
BuildRequires: /usr/bin/pod2man
BuildRequires: /usr/bin/pod2html

%description
Dose3 is a framework made of several OCaml libraries for managing
distribution packages and their dependencies.

Though not tied to any particular distribution, dose3 constitutes a pool of
libraries which enable analyzing packages coming from various distributions.

Besides basic functionalities for querying and setting package properties,
dose3 also implements algorithms for solving more complex problems
(monitoring package evolutions, correct and complete dependency resolution,
repository-wide uninstallability checks).

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%package -n dose3-tools
Summary: Tools suite from the dose3 framework
Group: Development/ML

%description -n dose3-tools
Dose3 is a framework made of several OCaml libraries for managing
distribution packages and their dependencies.

This package contains the tools shipped with the dose3 framework
for manipulating packages of various formats.

%prep
%setup

%build
sed -i 's,oUnit,ounit2,' src/*/tests/dune
sed -i 's/stdlib-shims//' src/common/dune
%dune_build --release @install @doc
pushd doc/manpages
make man
popd

%install
%dune_install --release

mkdir -p %buildroot{%_man1dir,%_man8dir,%_man5dir}
install -m0644 doc/manpages/*.1 %buildroot%_man1dir/
install -m0644 doc/manpages/*.8 %buildroot%_man8dir/
install -m0644 doc/manpages/*.5 %buildroot%_man5dir/

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.architecture COPYING

%files devel -f ocaml-files.devel
%doc COPYING

%files -n dose3-tools
%doc COPYING
%doc doc/apt-cudf/
%_man1dir/*
%_man8dir/*
%_man5dir/*
%_bindir/apt-cudf
%_bindir/dose-challenged
%_bindir/dose-ceve
%_bindir/dose-distcheck
%_bindir/dose-deb-coinstall
%_bindir/dose-outdated
%_bindir/dose-builddebcheck

%changelog
* Fri Nov 10 2023 Anton Farygin <rider@altlinux.ru> 7.0.0-alt2
- fixed build with ocamlgraph 2.1.0 
- updated BuildRequires for ocaml-4.14 environment

* Thu Nov 04 2021 Anton Farygin <rider@altlinux.ru> 7.0.0-alt1
- 7.0.0

* Thu Mar 18 2021 Anton Farygin <rider@altlinux.org> 6.1-alt1
- 6.1

* Fri Dec 11 2020 Anton Farygin <rider@altlinux.ru> 5.0.2-alt8.5.2git2c1b8df
- built without ounit

* Wed Feb 19 2020 Anton Farygin <rider@altlinux.ru> 5.0.1-alt7.5.2git2c1b8df
- fixed build with ounit2

* Sat Mar 16 2019 Anton Farygin <rider@altlinux.ru> 5.0.1-alt6.5.2git2c1b8df
- build with curl, bz2 and xml-light support  

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 5.0.1-alt5.5.2git2c1b8df
- rebuild with ocaml-re

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 5.0.1-alt4.5.2git2c1b8df
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 5.0.1-alt3.5.2git2c1b8df
- up to 2c1b8df from git

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 5.0.1-alt2.5.2git09392e2
- rebuilt for ocaml-4.06.1

* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 5.0.1-alt1.5.2git09392e2
- cleanup  buildrequires

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 5.0.1-alt0.5.2git09392e2
- first build for ALT, based on RH spec

