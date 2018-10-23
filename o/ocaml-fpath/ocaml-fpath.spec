%set_verify_elf_method textrel=relaxed
%define libname fpath
Name:           ocaml-%libname
Version:        0.7.2
Release:        alt1
Summary:        File system paths for OCaml
License:        ISC
Group:          Development/ML
Url:            http://erratique.ch/software/fpath
# https://github.com/dbuenzli/fpath
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.07.1 opam
BuildRequires: ocaml-astring

%package devel
Summary: Development files for programs which will use the %name
Group: Development/ML
Requires: %name = %version-%release

%description
Fpath is an OCaml module for handling file system paths with POSIX or Windows conventions.
Fpath processes paths without accessing the file system and is independent from any system library.

%description devel
This package includes development files necessary for developing 
programs which use %name

%prep
%setup -q

%build
sed -i 's,%%%%VERSION_NUM%%%%,%version,g' pkg/META
ocaml pkg/pkg.ml build

%install
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

%files
%doc LICENSE.md CHANGES.md README.md
%_libdir/ocaml/%libname
%exclude %_libdir/ocaml/%libname/*.a
%exclude %_libdir/ocaml/%libname/*.cmxa
%exclude %_libdir/ocaml/%libname/*.cmx
%exclude %_libdir/ocaml/%libname/*.mli

%files devel
%_libdir/ocaml/%libname/*.a
%_libdir/ocaml/%libname/*.cmxa
%_libdir/ocaml/%libname/*.cmx
%_libdir/ocaml/%libname/*.mli

%changelog
* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 0.7.2-alt1
- first build for ALT

