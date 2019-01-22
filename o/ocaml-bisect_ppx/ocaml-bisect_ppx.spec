%set_verify_elf_method textrel=relaxed
%define libname bisect_ppx
Name: ocaml-%libname
Version: 1.4.0
Release: alt1
Summary: Code coverage for OCaml
Group: Development/ML
License: MPL2
Url: https://github.com/aantron/bisect_ppx
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.07.1
BuildRequires: ocaml-findlib-devel
BuildRequires: opam dune
BuildRequires: ocaml-ppx_tools_versioned-devel
BuildRequires: ocaml-migrate-parsetree-devel
BuildRequires: ocaml-result-devel

%description
Bisect_ppx helps you test thoroughly. It is a small preprocessor that inserts
instrumentation at places in your code, such as if-then-else and match
expressions. After you run tests, Bisect_ppx gives a nice HTML report
showing which places were visited and which were missed.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%make_build

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml --mandir=%buildroot/%_mandir --docdir=%buildroot/%_docdir bisect_ppx.install

%files
%doc README.md LICENSE
%_bindir/bisect-ppx-report
%dir %_libdir/ocaml/%libname
%_libdir/ocaml/%libname/META
%_libdir/ocaml/%libname/opam
%_libdir/ocaml/%libname/*.dune
%_libdir/ocaml/%libname/*.cmi
%_libdir/ocaml/%libname/*.cma
%dir %_libdir/ocaml/%libname/runtime
%_libdir/ocaml/%libname/runtime/*.dune
%_libdir/ocaml/%libname/runtime/*.cmi
%_libdir/ocaml/%libname/runtime/*.cma


%files devel
%_libdir/ocaml/%libname/*.ml*
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.cmt*
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmxs
%_libdir/ocaml/%libname/runtime/*.ml*
%_libdir/ocaml/%libname/runtime/*.a
%_libdir/ocaml/%libname/runtime/*.cmxa
%_libdir/ocaml/%libname/runtime/*.cmx
%_libdir/ocaml/%libname/runtime/*.cmt*
%_libdir/ocaml/%libname/runtime/*.cmxs

%changelog
* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- first build for ALT


