%define module result
Name: ocaml-%module
Version: 1.2
Release: alt1%ubt
Summary: Compat result type

License: BSD
Url: https://github.com/janestreet/result/
Source0: %name-%version.tar
Group: Development/ML

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires(pre): rpm-build-ubt

%description
Projects that want to use the new result type defined in
OCaml >= 4.03 while staying compatible with older versions
of OCaml should use the Result module defined in this library.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature
files for developing applications that use %name.

%prep
%setup

%build
%make_build byte
%make_build native

%install
# Currently result installs itself with ocamlfind.
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot/%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make install

%files
%doc README.md
%_libdir/ocaml/%module
%exclude %_libdir/ocaml/%module/*.a
%exclude %_libdir/ocaml/%module/*.cmxa
%exclude %_libdir/ocaml/%module/*.cmx
%exclude %_libdir/ocaml/%module/*.ml

%files devel
%_libdir/ocaml/%module/*.a
%_libdir/ocaml/%module/*.cmxa
%_libdir/ocaml/%module/*.cmx
%_libdir/ocaml/%module/*.ml

%changelog
* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.2-alt1%ubt
- first build for ALT, based on RH spec

