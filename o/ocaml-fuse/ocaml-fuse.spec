%define ocamlsitelib %_libdir/ocaml/
%define ocamlstublib %_libdir/ocaml/stublibs/
Name: ocaml-fuse
Version: 2.7.1
Release: alt3%ubt
Summary: Ocaml FUSE binding
Group: Development/ML
License: GPL-2.0
Url: https://forge.ocamlcore.org/projects/gdfuse/
Source: %name-%version.tar
BuildRequires: libfuse-devel
BuildRequires: ocaml ocaml-camlidl ocaml-camlidl-devel ocaml-findlib ocaml-ocamldoc
BuildRequires(pre):rpm-build-ubt

%description
This is a binding to fuse for the ocaml programming language, enabling
you to write multithreaded filesystems in the ocaml language. It has
been designed with simplicity as a goal, as you can see by looking at
example/fusexmp.ml. Efficiency has also been a separate goal. The
Bigarray library is used for read and writes, allowing the library to
do zero-copy in ocaml land.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
cd lib
make CFLAGS="-w -D_FILE_OFFSET_BITS=64 -fPIC" OCAMLMKLIB_FLAGS=%_libdir/ocaml/libcamlidl.a all 

%install
mkdir -p %buildroot/%ocamlsitelib/Fuse
mkdir -p %buildroot/%_libdir/ocaml/caml
mkdir -p %buildroot/%ocamlstublib
mkdir -p %buildroot/%_bindir

cd lib
export OCAMLFIND_LDCONF=ignore
make OCAMLLIB=%buildroot/%_libdir/ocaml\
     OCAMLFIND_INSTFLAGS="-destdir %buildroot/%_libdir/ocaml"\
     BINDIR=%buildroot/%_bindir \
     install

%files
%doc LICENSE
%_libdir/ocaml/Fuse
%_libdir/ocaml/stublibs/*
%exclude %_libdir/ocaml/Fuse/*.a
%exclude %_libdir/ocaml/Fuse/*.cmxa
%exclude %_libdir/ocaml/Fuse/*.mli

%files devel
%_libdir/ocaml/Fuse/*.a
%_libdir/ocaml/Fuse/*.cmxa
%_libdir/ocaml/Fuse/*.mli

%changelog
* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 2.7.1-alt3%ubt
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 2.7.1-alt2%ubt
- split to devel and runtime

* Mon Feb 13 2017 Anton Farygin <rider@altlinux.ru> 2.7.1-alt1%ubt
- first build for ALT, version 2.7.1.cvs4
