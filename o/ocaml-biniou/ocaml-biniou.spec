%define ocamlmod biniou
Name: ocaml-%ocamlmod
Version: 1.2.2
Release: alt1
Summary: Safe and fast binary data format
Group: Development/ML
License: BSD-3-Clause
Url:https://github.com/mjambon/biniou
Source0:%name-%version.tar

BuildRequires: ocaml >= 4.14
BuildRequires: ocaml-easy-format-devel
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-camlp-streams-devel
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
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %ocamlmod


%install
%dune_install

%check
%dune_check

# avoid potential future name conflict
mv %buildroot%_bindir/{,ocaml-}bdump

%files -f ocaml-files.runtime
%doc LICENSE

%files devel -f ocaml-files.devel
%doc README.md CHANGES.md
%_bindir/ocaml-bdump

%changelog
* Wed Nov 08 2023 Anton Farygin <rider@altlinux.ru> 1.2.2-alt1
- 1.2.2
- fixed License and Url tags

* Fri Sep 18 2020 Anton Farygin <rider@altlinux.ru> 1.2.1-alt3
- migrated to rpm-build-ocaml 1.4

* Thu Jan 30 2020 Anton Farygin <rider@altlinux.ru> 1.2.1-alt2
- built with dune-2.x

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
