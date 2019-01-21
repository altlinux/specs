%set_verify_elf_method textrel=relaxed
Name: js_of_ocaml
Version: 3.3.0
Release: alt1
Summary: A compiler of OCaml byte-code to Javascript
License: LGPLv2 with exceptions
Group: Development/ML
Url: http://ocsigen.org/js_of_ocaml/
Source0: %name-%version.tar
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml-camlp4-devel
BuildRequires: ocaml
BuildRequires: ocaml-cppo
BuildRequires: ocaml-graphics
BuildRequires: ocaml-findlib
BuildRequires: ocaml-lwt-devel >= 2.4.4
BuildRequires: ocaml-menhir
BuildRequires: ocaml-tyxml-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-reactiveData-devel
BuildRequires: ocaml-migrate-parsetree-devel
BuildRequires: ocaml-yojson-devel
BuildRequires: ocaml-ppx_tools-devel
BuildRequires: ocaml-ppx_deriving-devel
BuildRequires: dune opam
BuildRequires: ocaml-ocamldoc
Requires: ocaml-%name = %version-%release
Requires: ocaml-lwt

%description
js_of_ocaml is a compiler of OCaml byte-code to Javascript.  It makes it
possible to run OCaml programs in a Web browser.
Its key features are the following:
* the whole language, and most of the standard library are
supported;
* the generated code can be used with any web server and browser;
* you can use a standard installation of OCaml to compile your
programs. In particular, you do not have to recompile a library to
use it with Js_of_ocaml. You just have to link your program with a
specific library to interface with the browser APIs.

%package -n     ocaml-%name
Summary: Runtime files for %name
Group: Development/ML
Requires: ocaml-ppx_deriving
Requires: ocaml-lwt

%description -n ocaml-%name
The ocaml-%name package contains the bytecode libraries for running
applications that use %name.

%package -n     ocaml-%name-devel
Summary: Development files for %name
Group: Development/ML
Requires: ocaml-%name = %version-%release
Requires: ocaml-ppx_deriving-devel
Requires: ocaml-lwt-devel

%description -n ocaml-%name-devel
The ocaml-%name-devel package contains the signature
files for developing applications that use %name.

%prep
%setup

%build
make

%install
for instfile in *.install;do \
   opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml --mandir=%buildroot%_mandir $instfile; \
done

%files
%_bindir/js_of_ocaml
%_bindir/jsoo_minify
%_bindir/jsoo_mkcmis
%_bindir/jsoo_mktop
%_bindir/jsoo_link
%_bindir/jsoo_listunits
%_man1dir/*.1*

%files -n ocaml-%name
%doc LICENSE README.md
%dir %_libdir/ocaml/%name
%dir %_libdir/ocaml/%name/deriving
%_libdir/ocaml/%{name}*/*.dune
%_libdir/ocaml/%{name}*/opam
%_libdir/ocaml/%{name}*/META
%_libdir/ocaml/%{name}*/*.cma
%_libdir/ocaml/%{name}*/*.cmi
%_libdir/ocaml/%{name}*/*.cmxs
%_libdir/ocaml/%{name}*/*/*.dune
%_libdir/ocaml/%{name}*/*/*.cma
%_libdir/ocaml/%{name}*/*/*.cmi
%_libdir/ocaml/%{name}*/*/*.cmxs
%_libdir/ocaml/%{name}*/*.js
%_libdir/ocaml/stublibs/*.so*

%files -n ocaml-%name-devel
%doc examples
%doc LICENSE README.md examples doc/api doc/manual
%_libdir/ocaml/%{name}*/*.ml
%_libdir/ocaml/%{name}*/*.mli
%_libdir/ocaml/%{name}*/*.a
%_libdir/ocaml/%{name}*/*.cmxa
%_libdir/ocaml/%{name}*/*.cmt*
%_libdir/ocaml/%{name}*/*.cmx
%_libdir/ocaml/%{name}*/*/*.ml
%_libdir/ocaml/%{name}*/*/*.mli
%_libdir/ocaml/%{name}*/*/*.a
%_libdir/ocaml/%{name}*/*/*.cmxa
%_libdir/ocaml/%{name}*/*/*.cmt*
%_libdir/ocaml/%{name}*/*/*.cmx

%changelog
* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Fri Oct 26 2018 Anton Farygin <rider@altlinux.ru> 3.2.1-alt1
- first build for ALT

