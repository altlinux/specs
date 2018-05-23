Name: opam
Version: 2.0.0
Release: alt1%ubt.rc
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
BuildRequires: ocaml-cppo
BuildRequires: ocaml-findlib
BuildRequires: ocaml-cudf-devel
BuildRequires: ocaml-ocamlgraph-devel
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-dose3-devel
BuildRequires: ocaml-extlib-devel
BuildRequires: ocaml-jsonm-devel
BuildRequires: ocaml-result-devel
BuildRequires: curl jbuilder
BuildRequires(pre): rpm-build-ubt

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
pushd doc/dev-manual/
  make html
  make clean
popd

%install
%makeinstall_std

%files
%doc README.md LICENSE CHANGES
%doc AUTHORS CONTRIBUTING.md
%_bindir/%name
%_bindir/%name-installer
%_mandir/man1/%name.1*
%_mandir/man1/%name-*.1*

%files doc
%doc doc/
%doc tests/
%doc shell/

%changelog
* Wed May 23 2018 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1%ubt.rc
- 2.0.0-rc

* Thu May 17 2018 Anton Farygin <rider@altlinux.ru> 1.3.1-alt2%ubt
- fixed stubs libraries location

* Thu Dec 21 2017 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1%ubt
- first build for ALT

