%define pkgname ocamlbuild
Name: ocaml-%pkgname
Version: 0.14.1
Release: alt1
Epoch: 1

Summary: The Objective Caml project compilation tool
License: Distributable
Group: Development/ML
Url: https://github.com/ocaml/ocamlbuild

Source: %name-%version.tar
Source1: ocaml-ocamlbuild.watch

BuildRequires: ocaml >= 4.07

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package provides ocamlbuild, a tool automating the compilation
of OCaml projects.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
This package contains development files for %name.

%prep
%setup

%build
%add_optflags -DUSE_NON_CONST -D_FILE_OFFSET_BITS=64

env OCAML_NATIVE=true make configure
make

%install
make install DESTDIR=%buildroot BINDIR=%_bindir LIBDIR=%_libdir/ocaml

# Remove the META file.  It will be replaced by ocaml-ocamlfind (findlib).
rm %buildroot%_libdir/ocaml/%pkgname/META

%files
%doc Changes Readme.md LICENSE
%_bindir/ocamlbuild
%_bindir/ocamlbuild.byte
%_bindir/ocamlbuild.native
%_mandir/man1/ocamlbuild.1*
%_libdir/ocaml/ocamlbuild
%exclude %_libdir/ocaml/ocamlbuild/*.a
%exclude %_libdir/ocaml/ocamlbuild/*.o
%exclude %_libdir/ocaml/ocamlbuild/*.cmx
%exclude %_libdir/ocaml/ocamlbuild/*.cmxa
%exclude %_libdir/ocaml/ocamlbuild/*.mli

%files devel
%doc LICENSE
%_libdir/ocaml/ocamlbuild/*.a
%_libdir/ocaml/ocamlbuild/*.o
%_libdir/ocaml/ocamlbuild/*.cmx
%_libdir/ocaml/ocamlbuild/*.cmxa
%_libdir/ocaml/ocamlbuild/*.mli

%changelog
* Fri Mar 25 2022 Anton Farygin <rider@altlinux.ru> 1:0.14.1-alt1
- 0.14.1

* Mon Jul 01 2019 Anton Farygin <rider@altlinux.ru> 1:0.14.0-alt1
- 0.14.0

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1:0.13.1-alt2
- rebuilt for ocaml-4.07.1

* Wed Oct 17 2018 Anton Farygin <rider@altlinux.ru> 1:0.13.1-alt1
- 0.13.1

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.12.0-alt3.qa1
- NMU: applied repocop patch

* Mon Aug 13 2018 Anton Farygin <rider@altlinux.ru> 1:0.12.0-alt3
- rebuilt for ocaml 4.07.0

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1:0.12.0-alt2
- rebuilt for ocaml 4.06.1

* Mon Dec 18 2017 Anton Farygin <rider@altlinux.ru> 1:0.12.0-alt1
- new version

* Mon Jul 10 2017 Anton Farygin <rider@altlinux.ru> 1:0.11.0-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1:0.11.0-alt2
- rebuild with ocaml 4.04.1

* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 1:0.11.0-alt1
- updated to 0.11.0
- split to runtime and devel packages

* Thu Feb 16 2017 Anton Farygin <rider@altlinux.ru> 1:0.10.1-alt1
- updated to 0.10.1

* Sun Jun 19 2016 Andrey Bergman <vkni@altlinux.org> 4.03.0_0.9.2-alt1
- Initial release for Sisyphus.
