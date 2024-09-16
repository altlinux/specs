%set_verify_elf_method textrel=relaxed
Name: cinaps
Version: 0.15.1
Release: alt2
Summary: Trivial metaprogramming tool.
License: Apache-2.0
Group: Development/ML
Url: https://github.com/ocaml-ppx/cinaps
Source0: %name-%version.tar
BuildRequires: dune ocaml-re-devel

%description
Cinaps is a trivial Metaprogramming tool using the OCaml toplevel. It is based
on the same idea as expectation tests. The user write some OCaml code inside
special comments and cinaps make sure that what follows is what is printed by
the OCaml code.

%prep
%setup

%build
%dune_build -p %name

%install
%dune_install

%check
# TODO: build ppx_jane
#dune_check

%files
%doc README.org
%dir %_libdir/ocaml/%name
%_bindir/cinaps
%_libdir/ocaml/%name/META
%_libdir/ocaml/%name/dune-package
%_libdir/ocaml/%name/opam
%_libdir/ocaml/%name/runtime

%changelog
* Wed Sep 04 2024 Anton Farygin <rider@altlinux.ru> 0.15.1-alt2
- cleanup buildrequires

* Thu Mar 18 2021 Anton Farygin <rider@altlinux.org> 0.15.1-alt1
- 0.15.1

* Fri Jan 22 2021 Anton Farygin <rider@altlinux.org> 0.15.0-alt1
- 0.15.0

* Wed Dec 30 2020 Anton Farygin <rider@altlinux.ru> 0.14.0-alt1
- 0.14.0

* Wed Jan 29 2020 Anton Farygin <rider@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Mon Jul 01 2019 Anton Farygin <rider@altlinux.ru> 0.12.0-alt1
- 0.12.0

* Tue Nov 06 2018 Anton Farygin <rider@altlinux.ru> 0.11.0-alt1
- first build for ALT
