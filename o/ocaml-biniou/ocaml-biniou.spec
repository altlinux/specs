%set_verify_elf_method textrel=relaxed

Name: ocaml-biniou
Version: 1.2.1
Release: alt1
Summary: Safe and fast binary data format
Group: Development/ML
License: BSD
Url: http://mjambon.com/biniou.html
# https://github.com/mjambon/biniou
Source0:%name-%version.tar

BuildRequires: ocaml >= 4.08
BuildRequires: ocaml-easy-format-devel
BuildRequires: ocaml-ocamldoc
BuildRequires: dune opam

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
%build
make all

%install
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p %buildroot%_bindir
mkdir -p $OCAMLFIND_DESTDIR
opam-installer --prefix=%buildroot%prefix --libdir=%buildroot%_libdir/ocaml

# avoid potential future name conflict
mv %buildroot%_bindir/{,ocaml-}bdump

%files
%doc LICENSE
%_libdir/ocaml/biniou
%exclude %_libdir/ocaml/*/*.a
%exclude %_libdir/ocaml/*/*.cmxa
%exclude %_libdir/ocaml/*/*.cmx
%exclude %_libdir/ocaml/*/*.mli

%files devel
%doc LICENSE README.md CHANGES.md
%_bindir/ocaml-bdump
%_libdir/ocaml/*/*.a
%_libdir/ocaml/*/*.cmxa
%_libdir/ocaml/*/*.cmx
%_libdir/ocaml/*/*.mli

%changelog
* Mon Aug 05 2019 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt4
- NMU: remove rpm-build-ubt from BR:

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.2.0-alt3
- rebuilt for ocaml-4.07.1

* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 1.2.0-alt2
- rebuilt for ocaml-4.07

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- new version

* Thu Dec 21 2017 Anton Farygin <rider@altlinux.ru> 1.0.13-alt3
- rebuilt for ocaml 4.06

* Thu Jul 06 2017 Anton Farygin <rider@altlinux.ru> 1.0.13-alt2
- new version

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.0.9-alt2
- rebuild with ocaml 4.04.1

* Thu Apr 20 2017 Anton Farygin <rider@altlinux.ru> 1.0.9-alt1
- first build for ALT, based on RH spec
