Name: opam
Version: 2.0.2
Release: alt1
Summary: A source-based package manager for OCaml
License: LGPLv3
Group: Development/ML
Url: http://opam.ocamlpro.com/
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch
BuildRequires: ocaml
BuildRequires: ocaml-camlp4-devel
BuildRequires: ocaml-opam-file-format-devel
BuildRequires: hevea
BuildRequires: ocaml-cppo_ocamlbuild-devel
BuildRequires: ocaml-cppo
BuildRequires: ocaml-mccs-devel
BuildRequires: ocaml-odoc
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-cudf-devel
BuildRequires: ocaml-ocamlgraph-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-dose3-devel
BuildRequires: ocaml-extlib-devel
BuildRequires: ocaml-jsonm-devel
BuildRequires: ocaml-result-devel
BuildRequires: curl dune ocaml-omd gcc-c++

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

%package doc
Summary: Documentation files for %name
Group: Documentation
Requires: %name = %version-%release

%description doc
The %name-doc package contains documentation for using %name.

%prep
%setup -q
%patch0 -p1

%build
%configure

make all
make man

%install
%makeinstall_std LIBINSTALL_DIR=%buildroot%_libdir/ocaml

rm -rf %buildroot%prefix/doc

%files
%doc README.md LICENSE CHANGES
%doc AUTHORS CONTRIBUTING.md
%_bindir/%name
%_bindir/%name-installer
%_libdir/ocaml/opam-installer
%_mandir/man1/%name.1*
%_mandir/man1/%name-*.1*

%files doc
%doc doc/
%doc tests/
%doc shell/

%changelog
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

