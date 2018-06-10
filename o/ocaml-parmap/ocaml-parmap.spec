%set_verify_elf_method textrel=relaxed
Name: ocaml-parmap
Version: 1.0
Release: alt1.rc9
Summary: small OCaml library allowing to exploit multicore architectures
Group: Development/ML
License: LGPLv2+ with exceptions

Url: http://rdicosmo.github.io/parmap/
Source0: %name-%version.tar

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-ocamldoc
BuildRequires(pre): rpm-build-ocaml

%description
Parmap is a minimalistic library allowing to exploit multicore
architectures for OCaml programs with minimal modifications.

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
%configure --libdir=%_libdir --with-findlib
%__subst 's:lib/ocaml:%_libdir/ocaml:' Makefile
%__subst 's:/man/man3:%_man3dir:' Makefile
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc Changelog README.md
%doc LICENSE
%_libdir/ocaml/parmap/META
%_libdir/ocaml/parmap/*.cmi
%_libdir/ocaml/parmap/*.cma
%_libdir/ocaml/parmap/*.cmxs
%_libdir/ocaml/stublibs/dllparmap_stubs.so*

%files devel
%doc LICENSE
%_libdir/ocaml/parmap/*.a
%_libdir/ocaml/parmap/*.cmxa
%_libdir/ocaml/parmap/*.cmx
%_libdir/ocaml/parmap/*.mli
%_man3dir/*.3o*

%changelog
* Sun Jun 10 2018 Vitaly Chikunov <vt@altlinux.ru> 1.0-alt1.rc9
- First build of ocaml-parmap for ALT.

