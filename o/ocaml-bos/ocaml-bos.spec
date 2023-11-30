%define libname bos
Name:           ocaml-%libname
Version:        0.2.1
Release:        alt2
Summary:        Basic OS interaction for OCaml
License:        ISC
Group:          Development/ML
Url:            https://erratique.ch/software/bos
VCS: https://github.com/dbuenzli/bos
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.07.1 opam
BuildRequires: ocaml-astring ocaml-rresult ocaml-fpath ocaml-fmt ocaml-logs-devel
BuildRequires(pre): rpm-build-ocaml >= 1.6

%package devel
Summary: Development files for programs which will use the BOS library
Group: Development/ML
Requires: %name = %EVR

%description
Bos provides support for basic and robust interaction with the operating system 
in OCaml. It has functions to access the process environment, parse command line
arguments, interact with the file system and run command line programs.

Bos works equally well on POSIX and Windows operating systems.

%description devel
This package includes development files necessary for developing 
programs which use %name

%prep
%setup

%build
ocaml pkg/pkg.ml build

%install
sed -i 's,%%%%VERSION_NUM%%%%,%version,g' pkg/META
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml
%ocaml_find_files

%files -f ocaml-files.runtime
%doc LICENSE.md CHANGES.md README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Nov 16 2023 Anton Farygin <rider@altlinux.ru> 0.2.1-alt2
- added support for bytecode-only version of the ocaml package

* Thu Nov 04 2021 Anton Farygin <rider@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 0.2.0-alt2
- rebuilt with ocaml-4.08

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 0.2.0-alt1
- first build for ALT

