%define libname fpath
Name:           ocaml-%libname
Version:        0.7.3
Release:        alt3
Summary:        File system paths for OCaml
License:        ISC
Group:          Development/ML
Url:            https://erratique.ch/software/fpath
VCS:		https://github.com/dbuenzli/fpath
Source: %name-%version.tar

BuildRequires: ocaml-findlib ocaml-ocamlbuild ocaml-topkg-devel ocaml >= 4.07.1 opam
BuildRequires: ocaml-result ocaml-astring-devel
BuildRequires: rpm-build-ocaml >= 1.6

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

%ocaml_find_files

%files -f ocaml-files.runtime
%doc LICENSE.md CHANGES.md README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Nov 16 2023 Anton Farygin <rider@altlinux.ru> 0.7.3-alt3
- added support for bytecode-only version of the ocaml package

* Mon Nov 06 2023 Anton Farygin <rider@altlinux.ru> 0.7.3-alt2
- fixed URL and VCS tags

* Mon Sep 21 2020 Anton Farygin <rider@altlinux.ru> 0.7.3-alt1
- 0.7.3

* Thu Jan 30 2020 Anton Farygin <rider@altlinux.ru> 0.7.2-alt3
- added ocaml-result BR

* Fri Aug 02 2019 Anton Farygin <rider@altlinux.ru> 0.7.2-alt2
- rebuilt with ocaml-4.08

* Tue Oct 23 2018 Anton Farygin <rider@altlinux.ru> 0.7.2-alt1
- first build for ALT

