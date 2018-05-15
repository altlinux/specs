Name: jbuilder
Version: 1.0
Release: alt2.beta20
Summary: A composable build system for OCaml
Group: Development/ML
License: ASL 2.0
Url: https://github.com/janestreet/jbuilder/
Source0: %name-%version-%release.tar

BuildRequires: ocaml >= 4.06.1
BuildRequires: ocaml-findlib-devel

# Required by tests.
BuildRequires: ocaml-menhir

%description
Jbuilder is a build system designed for OCaml/Reason projects only. It focuses
on providing the user with a consistent experience and takes care of most of
the low-level details of OCaml compilation. All you have to do is provide a
description of your project and Jbuilder will do the rest.

The scheme it implements is inspired from the one used inside Jane Street and
adapted to the open source world. It has matured over a long time and is used
daily by hundred of developers, which means that it is highly tested and
productive.

%prep
%setup -n %name-%version-%release

%build
%make_build release VERSION=%version-%release

%install
# jbuilder's makefile has a "make install" target. Tragically, it uses opam-install(er)
# to install itself. Even more tragically, opam now requires jbuilder to build.
# Therefore as a workaround we can just manually install things ourselves--
# jbuilder is *mostly* just a binary, making this easy.
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir/ocaml/jbuilder/
mkdir -p %buildroot%_mandir/man1

# The files to install are stored in _build as symlinks; dereference them.
cp -aL _build/install/default/bin/jbuilder %buildroot%_bindir/
cp -aL _build/install/default/lib/jbuilder/* %buildroot%_libdir/ocaml/jbuilder/
cp -aL _build/install/default/man/man1/* %buildroot%_mandir/man1

%files
%doc README.md CHANGES.md
%_libdir/ocaml/%name
%_bindir/jbuilder
%_mandir/man1/jbuilder.1*
%_mandir/man1/jbuilder-build.1*
%_mandir/man1/jbuilder-clean.1*
%_mandir/man1/jbuilder-exec.1*
%_mandir/man1/jbuilder-external-lib-deps.1*
%_mandir/man1/jbuilder-install.1*
%_mandir/man1/jbuilder-installed-libraries.1*
%_mandir/man1/jbuilder-rules.1*
%_mandir/man1/jbuilder-runtest.1*
%_mandir/man1/jbuilder-subst.1*
%_mandir/man1/jbuilder-uninstall.1*
%_mandir/man1/jbuilder-utop.1*

%changelog
* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 1.0-alt2.beta20
- update to beta20

* Tue Dec 19 2017 Anton Farygin <rider@altlinux.ru> 1.0-alt1.git4570020
- first build for ALT, based on RH spec


