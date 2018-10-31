Name: ocamlmod
Version: 0.0.9
Release: alt1
Summary: Generate OCaml modules from source files
License: LGPL-2.1 with OCaml linking exception
Group: Development/ML
Url: http://forge.ocamlcore.org/projects/ocamlmod/
# https://github.com/gildor478/ocamlmod
Source0: %name-%version.tar
Patch0: ocamlmod-setupml.patch
Patch1: ocamlmod-native.patch
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-ocamlbuild

%description
Generate OCaml modules from source files.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
ocaml setup.ml -configure \
    --prefix %prefix \
    --libdir %_libdir \
    --libexecdir %_libexecdir \
    --exec-prefix %_exec_prefix \
    --bindir %_bindir \
    --sbindir %_sbindir \
    --mandir %_mandir \
    --datadir %_datadir \
    --localstatedir %_localstatedir \
    --sharedstatedir %_sharedstatedir \
    --destdir %buildroot

make

%install
make install

%files
%doc README.txt AUTHORS.txt INSTALL.txt
%_bindir/ocamlmod

%changelog
* Wed Oct 31 2018 Anton Farygin <rider@altlinux.ru> 0.0.9-alt1
- first build for ALT with patches from Mageia

