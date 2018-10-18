%define module result
Name: ocaml-%module
Version: 1.3
Release: alt3
Summary: Compat result type

License: BSD
Url: https://github.com/janestreet/result/
Source0: %name-%version.tar
Group: Development/ML

BuildRequires: ocaml 
BuildRequires: ocaml-findlib jbuilder opam

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
jbuilder build

%install
mkdir -p %buildroot%_libdir/ocaml
jbuilder install --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

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
* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.3-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.3-alt2
- rebuilt for ocaml 4.07

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 1.3-alt1
- 1.3

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.2-alt1
- first build for ALT, based on RH spec

