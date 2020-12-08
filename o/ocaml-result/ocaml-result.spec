%set_verify_elf_method textrel=relaxed
%define module result
Name: ocaml-%module
Version: 1.5
Release: alt2
Summary: Compat result type

License: BSD
Url: https://github.com/janestreet/result/
Source0: %name-%version.tar
Group: Development/ML

BuildRequires: ocaml 
BuildRequires: dune

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
%dune_build -p %module

%install
%dune_install

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Thu Sep 10 2020 Anton Farygin <rider@altlinux.ru> 1.5-alt2
- fixed checksum providing in module (add -p (--release) option to dune)

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 1.5-alt1
- 1.5

* Tue Jul 30 2019 Anton Farygin <rider@altlinux.ru> 1.4-alt2
- rebuilt with ocaml-4.08

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 1.4-alt1
- 1.4

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.3-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.3-alt2
- rebuilt for ocaml 4.07

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- 1.3

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.2-alt1
- first build for ALT, based on RH spec

