Name: ocaml-xml-light
Version: 2.2
Release: alt1.1
Summary: Minimal XML parser and printer for OCaml

Group: Development/ML
License: LGPLv2+
Url: http://tech.motion-twin.com/xmllight.html
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Thu Nov 12 2009
BuildRequires: ocamldoc

BuildRequires: findlib
%description
Xml-Light is a minimal XML parser & printer for OCaml. It provides
functions to parse an XML document into an OCaml data structure, work
with it, and print it back to an XML document. It support also DTD
parsing and checking, and is entirely written in OCaml, hence it does
not require additional C library.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
make all doc
make opt
sed -e 's/@VERSION@/%version/' < META.in > META

%install
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml/site-lib
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
rm -f test.*
ocamlfind install xml-light META *.mli *.cmi *.cma *.a *.cmxa *.cmx

%files
%doc README
%_libdir/ocaml/site-lib/xml-light
%exclude %_libdir/ocaml/site-lib/xml-light/*.a
%exclude %_libdir/ocaml/site-lib/xml-light/*.cmxa
%exclude %_libdir/ocaml/site-lib/xml-light/*.cmx
%exclude %_libdir/ocaml/site-lib/xml-light/*.mli

%files devel
%doc README doc/*
%_libdir/ocaml/site-lib/xml-light/*.a
%_libdir/ocaml/site-lib/xml-light/*.cmxa
%_libdir/ocaml/site-lib/xml-light/*.cmx
%_libdir/ocaml/site-lib/xml-light/*.mli

%changelog
* Tue Dec 27 2011 Alexey Shabalin <shaba@altlinux.ru> 2.2-alt1.1
- rebuild with new ocaml

* Thu Nov 12 2009 Anton Farygin <rider@altlinux.ru> 2.2-alt1
- first build for Sisyphus, based on Fedora specfile
