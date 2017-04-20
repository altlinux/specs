%set_verify_elf_method textrel=relaxed

Name: ocaml-biniou
Version: 1.0.9
Release: alt1%ubt
Summary: Safe and fast binary data format
Group: Development/ML
License: BSD
Url: http://mjambon.com/biniou.html
# https://github.com/mjambon/biniou
Source0:%name-%version.tar

BuildRequires: ocaml >= 4.04
BuildRequires: ocaml-findlib
BuildRequires: ocaml-easy-format-devel
BuildRequires: ocaml-ocamldoc
BuildRequires(pre): rpm-build-ubt

%description
Biniou (pronounced "be new") is a binary data format designed for
speed, safety, ease of use and backward compatibility as protocols
evolve. Biniou is vastly equivalent to JSON in terms of functionality
but allows implementations several times faster (4 times faster than
yojson), with 25-35%% space savings.

Biniou data can be decoded into human-readable form without knowledge
of type definitions except for field and variant names which are
represented by 31-bit hashes. A program named bdump is provided for
routine visualization of biniou data files.

%package devel
Summary: Development files for %name
Requires: %name%{?_isa} = %version-%release
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
sed -i.add-debuginfo \
    's/ocamlopt/ocamlopt -g/;s/ocamlc \(-[co]\)/ocamlc -g \1/' \
    Makefile

%build
make all
make opt
make META

%install
export PREFIX=%buildroot%prefix
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p %buildroot%_bindir
mkdir -p $OCAMLFIND_DESTDIR
make install 

# avoid potential future name conflict
mv %buildroot%_bindir/{,ocaml-}bdump

%files
%doc LICENSE
%_libdir/ocaml/biniou
%exclude %_libdir/ocaml/*/*.a
%exclude %_libdir/ocaml/*/*.cmxa
%exclude %_libdir/ocaml/*/*.cmx
%exclude %_libdir/ocaml/*/*.o
%exclude %_libdir/ocaml/*/*.mli

%files devel
%doc LICENSE README.md Changes
%_bindir/ocaml-bdump
%_libdir/ocaml/*/*.a
%_libdir/ocaml/*/*.cmxa
%_libdir/ocaml/*/*.cmx
%_libdir/ocaml/*/*.o
%_libdir/ocaml/*/*.mli

%changelog
* Thu Apr 20 2017 Anton Farygin <rider@altlinux.ru> 1.0.9-alt1%ubt
- first build for ALT, based on RH spec
