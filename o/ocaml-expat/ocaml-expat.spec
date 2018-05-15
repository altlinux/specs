%set_verify_elf_method textrel=relaxed
Name: ocaml-expat
Version: 1.1.0
Release: alt2%ubt
Summary: OCaml wrapper for the Expat XML parsing library
License: MIT
Group: Development/ML

Url: http://www.xs4all.nl/~mmzeeman/ocaml/
Source0: %name-%version.tar

BuildRequires(pre):rpm-build-ubt
BuildRequires: ocaml
BuildRequires: ocaml-findlib-devel, libexpat-devel, chrpath
BuildRequires: util-linux-ng, gawk

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
  allopt \
  OCAMLC="ocamlc.opt -g" \
  OCAMLOPT="ocamlopt.opt -g"

%install
export DESTDIR=$RPM_BUILD_ROOT
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install

# Remove rpath from stublibs .so file.
chrpath --delete $RPM_BUILD_ROOT%_libdir/ocaml/stublibs/*.so

%files
%doc LICENCE README changelog
%_libdir/ocaml/expat
%_libdir/ocaml/stublibs/*.so
%_libdir/ocaml/stublibs/*.so.owner
%exclude %_libdir/ocaml/expat/*.a
%exclude %_libdir/ocaml/expat/*.cmxa
%exclude %_libdir/ocaml/expat/*.mli

%files devel
%doc LICENCE README changelog
%_libdir/ocaml/expat/*.a
%_libdir/ocaml/expat/*.cmxa
%_libdir/ocaml/expat/*.mli

%changelog
* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 1.1.0-alt2%ubt
- rebuilt for ocaml-4.06.1

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1%ubt
- first build for ALT, based on RH spec

