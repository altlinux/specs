Name: ocaml-camomile
Version: 2.0.0
Release: alt1
Summary: Unicode library for OCaml
License: LGPLv2+
Group: Development/ML
Url: https://github.com/yoriyuki/Camomile
Source0: %name-%version.tar
BuildRequires: ocaml >= 4.08
BuildRequires: dune
BuildRequires: ocaml-stdlib-random-devel
BuildRequires: ocaml-dune-site-devel
BuildRequires: ocaml-camlp-streams-devel
Requires: %name-data = %EVR

%description
Camomile is a Unicode library for ocaml. Camomile provides Unicode
character type, UTF-8, UTF-16, UTF-32 strings, conversion to/from
about 200 encodings, collation and locale-sensitive case mappings, and
more.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%package data
Group: Development/ML
Requires: %name = %EVR
Summary: Data files for %name

%description data
The %name-data package contains data files for developing
applications that use %name.

%prep
%setup 

%build
# This avoids a stack overflow in the OCaml > 4.05 compiler on POWER only.
%ifarch ppc64le
ulimit -Hs 65536
ulimit -Ss 65536
%endif
%dune_build

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md CHANGES.md LICENSE.md

%files devel -f ocaml-files.devel

%files data
%_datadir/camomile/

%changelog
* Tue Nov 07 2023 Anton Farygin <rider@altlinux.ru> 2.0.0-alt1
- 2.0.0

* Wed Aug 14 2019 Anton Farygin <rider@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 1.0.1-alt1
- first build for ALT, based on spec from RH

