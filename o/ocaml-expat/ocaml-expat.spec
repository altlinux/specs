%global pkgname expat
%define ocamlsitelib %_libdir/ocaml
%define pkgsitelib %ocamlsitelib/%pkgname
%define ocamlstublib %_libdir/ocaml/stublibs
Name: ocaml-%pkgname
Version: 1.3.0
Release: alt2
Summary: OCaml wrapper for the Expat XML parsing library
License: MIT
Group: Development/ML

Url: https://mmzeeman.home.xs4all.nl/ocaml/
VCS: https://github.com/whitequark/ocaml-expat
Source0: %name-%version.tar

BuildRequires: ocaml
BuildRequires: ocaml-findlib-devel, libexpat-devel
BuildRequires: chrpath
BuildRequires: rpm-build-ocaml >= 1.6

%description
An ocaml wrapper for the Expat XML parsing library. It allows you to
write XML-Parsers using the SAX method. An XML document is parsed on
the fly without needing to load the entire XML-Tree into memory.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
make depend
make all \
%ifarch %ocaml_native_arch
  allopt \
  OCAMLC="ocamlc.opt -g" \
  OCAMLOPT="ocamlopt.opt -g"
%endif

%install
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
%makeinstall_std
chrpath -d %buildroot%ocamlstublib/*.so

%ocaml_find_files

%files -f ocaml-files.runtime
%doc LICENCE README changelog
%ocamlstublib/*.so.owner

%files devel -f ocaml-files.devel

%changelog
* Thu Nov 16 2023 Anton Farygin <rider@altlinux.ru> 1.3.0-alt2
- added support for bytecode-only version of the ocaml package

* Mon Nov 06 2023 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Wed Jul 31 2019 Anton Farygin <rider@altlinux.ru> 1.1.0-alt5
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.1.0-alt4
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 1.1.0-alt3
- rebuilt with ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 1.1.0-alt2
- rebuilt for ocaml-4.06.1

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- first build for ALT, based on RH spec

