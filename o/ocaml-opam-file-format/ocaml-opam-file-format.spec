Name: ocaml-opam-file-format
Version: 2.0.0
Release: alt3
Summary: Parser and printer for the opam file syntax
Group: Development/ML

%global libname %(echo %name | sed -e 's/^ocaml-//')

# This is apparently a standard "OCaml exception" and is detailed
# in the license file. That wasn't included in the repo, but I filed
# a ticket (https://github.com/ocaml/opam-file-format/issues/5)
# and now it is, so I've added the commit that added license as a patch.
License: LGPLv2 with exceptions
Url: https://github.com/ocaml/opam-file-format/
Source0: %name-%version.tar
BuildRequires: ocaml

%description
Parser and printer for the opam file syntax.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature
files for developing applications that use %name.

%prep
%setup

%build
make byte
make native

%install
make install LIBDIR=%_libdir/ocaml DESTDIR=%buildroot

# The mli files don't seem to get installed by the makefile.
# This is suboptimal.
cp -a src/*.mli %buildroot%_libdir/ocaml/%libname/

%files
# There is no documentation.
%doc LICENSE
%_libdir/ocaml/%libname
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.mli

%files devel
%doc LICENSE
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/*/*.mli

%changelog
* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 2.0.0-alt3
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 2.0.0-alt2
- up to 2.0.0 release

* Wed May 23 2018 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1.rc2
- first build for ALT, based on RH spec

