%ifarch %ix86 armh
%def_without check
%else
%def_with check
%endif
Name: js_of_ocaml
Version: 3.11.0
Release: alt3
Summary: A compiler of OCaml byte-code to Javascript
License: LGPLv2 with exceptions
Group: Development/ML
Url: http://ocsigen.org/js_of_ocaml/
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: rpm-build-ocaml >= 1.4
BuildRequires: ocaml-cmdliner-devel
BuildRequires: ocaml
BuildRequires: ocaml-cppo
BuildRequires: ocaml-graphics
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-lwt-devel >= 2.4.4
BuildRequires: ocaml-menhir
BuildRequires: ocaml-tyxml-devel
BuildRequires: ocaml-reactiveData-devel
BuildRequires: ocaml-yojson-devel
BuildRequires: ocaml-ppxlib-devel
BuildRequires: ocaml-fieldslib-devel
BuildRequires: dune
BuildRequires: nodejs
BuildRequires: libX11-devel
BuildRequires: ocaml-ocamldoc
%if_with check
BuildRequires: ocaml-num-devel
BuildRequires: ocaml-ppx_here-devel
BuildRequires: ocaml-ppx_hash-devel
BuildRequires: ocaml-ppx_inline_test-devel
BuildRequires: ocaml-ppx_compare-devel
BuildRequires: ocaml-time_now-devel 
BuildRequires: ocaml-ppx_sexp_conv-devel 
BuildRequires: ocaml-ppx_expect-devel 
BuildRequires: ocaml-ppx_enumerate-devel
%endif
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
Requires: ocaml-lwt

%description -n ocaml-%name
The ocaml-%name package contains the bytecode libraries for running
applications that use %name.

%package -n     ocaml-%name-devel
Summary: Development files for %name
Group: Development/ML
Requires: ocaml-%name = %version-%release
Requires: ocaml-lwt-devel

%description -n ocaml-%name-devel
The ocaml-%name-devel package contains the signature
files for developing applications that use %name.

%prep
%setup
%patch0 -p1
# remove vendored version of the ppx_expect
rm -rf vendor

%build
%dune_build --release @install

%install
%dune_install

%check
%dune_check

%files
%_bindir/js_of_ocaml
%_bindir/jsoo_fs
%_bindir/jsoo_minify
%_bindir/jsoo_mkcmis
%_bindir/jsoo_mktop
%_bindir/jsoo_link
%_bindir/jsoo_listunits
%_man1dir/*.1*

%files -n ocaml-%name -f ocaml-files.runtime
%doc LICENSE README.md

%files -n ocaml-%name-devel -f ocaml-files.devel
%doc examples
%_libdir/ocaml/js_of_ocaml-ppx/ppx_js

%changelog
* Wed Jan 05 2022 Anton Farygin <rider@altlinux.ru> 3.11.0-alt3
- added commit 8698bab from upstream to fix incompatability with new menhir

* Tue Jan 04 2022 Anton Farygin <rider@altlinux.ru> 3.11.0-alt2
- fix test for changes in exception format

* Thu Nov 04 2021 Anton Farygin <rider@altlinux.ru> 3.11.0-alt1
- 3.11.0

* Mon Sep 06 2021 Anton Farygin <rider@altlinux.ru> 3.10.0-alt1
- 3.10.0

* Sun Apr 04 2021 Anton Farygin <rider@altlinux.org> 3.9.1-alt2
- disabled check for ocaml-4.12 task

* Sun Mar 28 2021 Anton Farygin <rider@altlinux.org> 3.9.1-alt1
- 3.9.1

* Fri Dec 11 2020 Anton Farygin <rider@altlinux.ru> 3.8.0-alt1
- 3.8.0

* Sat Sep 19 2020 Anton Farygin <rider@altlinux.ru> 3.7.0-alt2
- optimized build dependencies

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 3.7.0-alt1
- 3.7.0

* Wed Jul 01 2020 Anton Farygin <rider@altlinux.ru> 3.6.0-alt1
- 3.6.0

* Wed Mar 11 2020 Anton Farygin <rider@altlinux.ru> 3.5.2-alt2
- cleaned up build requires

* Fri Jan 31 2020 Anton Farygin <rider@altlinux.ru> 3.5.2-alt1
- 3.5.2

* Sat Aug 03 2019 Anton Farygin <rider@altlinux.ru> 3.4.0-alt3
- rebuilt with ocaml 4.08

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 3.4.0-alt2
- added ocambuild to BuildRequires

* Sat May 11 2019 Anton Farygin <rider@altlinux.ru> 3.4.0-alt1
- 3.4.0

* Thu Mar 14 2019 Anton Farygin <rider@altlinux.ru> 3.3.0-alt3
- rebuilt with ocaml-yojson-1.7.0

* Wed Mar 13 2019 Anton Farygin <rider@altlinux.ru> 3.3.0-alt2
- rebuilt with dune-1.8

* Mon Jan 21 2019 Anton Farygin <rider@altlinux.ru> 3.3.0-alt1
- 3.3.0

* Fri Oct 26 2018 Anton Farygin <rider@altlinux.ru> 3.2.1-alt1
- first build for ALT

