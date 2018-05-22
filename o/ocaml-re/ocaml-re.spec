%set_verify_elf_method textrel=relaxed
Name: ocaml-re
Version: 1.7.1
Release: alt2%ubt
Summary: A regular expression library for OCaml

License: LGPLv2 with exceptions
Url: https://github.com/ocaml/ocaml-re
Source0: ocaml-re-%version.tar
Group: Development/ML
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-ocamlbuild
BuildRequires(pre): rpm-build-ubt

%description
A pure OCaml regular expression library. Supports Perl-style regular
expressions, Posix extended regular expressions, Emacs-style regular
expressions, and shell-style file globbing.  It is also possible to
build regular expressions by combining simpler regular expressions.
There is also a subset of the PCRE interface available in the Re.pcre
library.

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
./configure --prefix %prefix --disable-docs
make 
make doc

%install
export OCAMLFIND_DESTDIR=$RPM_BUILD_ROOT%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install DESTDIR=%buildroot

# We want to manually get the documentation anyway especially
# since documentation gets put in _docdir/re by buildsystem.
rm -rf %buildroot%_docdir/re/

%files
%doc CHANGES README.md
%_libdir/ocaml/re
%exclude %_libdir/ocaml/re/*.a
%exclude %_libdir/ocaml/re/*.cmxa
%exclude %_libdir/ocaml/re/*.cmx
%exclude %_libdir/ocaml/re/*.mli

%files devel
%_libdir/ocaml/re/*.a
%_libdir/ocaml/re/*.cmx
%_libdir/ocaml/re/*.cmxa
%_libdir/ocaml/re/*.mli

%changelog
* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 1.7.1-alt2%ubt
- rebuilt for ocaml 4.06.1

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.7.1-alt1%ubt
- first build for ALT, based on RH spec

