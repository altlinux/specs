%set_verify_elf_method textrel=relaxed
Name: ocaml-type-conv
Version: 113.00.02
Release: alt2%ubt
Summary: OCaml base library for type conversion
License: LGPLv2+ with exceptions and BSD
Group: Development/ML
Url: http://forge.ocamlcore.org/projects/type-conv/
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.04
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-camlp4-devel
BuildRequires(pre): rpm-build-ubt

%description
The type-conv mini library factors out functionality needed by
different preprocessors that generate code from type specifications,
because this functionality cannot be duplicated without losing the
ability to use these preprocessors simultaneously.

%prep
%setup
ocaml setup.ml -configure --prefix %prefix \
      --libdir %_libdir \
      --libexecdir %_libexecdir \
      --exec-prefix %_exec_prefix \
      --bindir %_bindir \
      --sbindir %_sbindir \
      --mandir %_mandir \
      --datadir %_datadir \
      --localstatedir %_localstatedir \
      --sharedstatedir %_sharedstatedir \
      --destdir $RPM_BUILD_ROOT

%build
ocaml setup.ml -build

%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%ocamldir
mkdir -p $OCAMLFIND_DESTDIR
ocaml setup.ml -install

%files
%doc CHANGES.md README.md LICENSE.txt LICENSE-Tywith.txt COPYRIGHT.txt
%ocamldir/type_conv

%changelog
* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 113.00.02-alt2%ubt
- rebuild with ocaml 4.04.2

* Wed May 17 2017 Anton Farygin <rider@altlinux.ru> 113.00.02-alt1%ubt
- first build for ALT

