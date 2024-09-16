%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name: ocaml-camlbz2
Version: 0.8.0
Release: alt1
Summary: OCaml bindings for the libbz2
License: LGPLv2 with OCaml-LGPL-linking-exception
Group: Development/ML
Url: https://gitlab.com/irill/camlbz2
VCS: https://gitlab.com/irill/camlbz2
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires(pre): rpm-build-ocaml >= 1.6
BuildRequires: ocaml
BuildRequires: dune
BuildRequires: bzlib-devel

%description
CamlBZ2 provides OCaml bindings for libbz2 (AKA bzip2), a popular
compression library which typically compresses better (i.e., smaller
resulting files) than gzip.

Using CamlBZ2 you can read and write compressed "files", where
files can be anything offering an in_channel/out_channel abstraction
(files, sockets, ...).

Also, with CamlBZ2 you can compress and decompress strings in memory
using the bzip2 compression algorithm.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: bzlib-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build -p bz2

%install
%dune_install

%files -f ocaml-files.runtime
%doc BUGS COPYING ChangeLog INSTALL LICENSE README ROADMAP
%_libdir/ocaml/stublibs/*.so*

%files devel -f ocaml-files.devel

%changelog
* Thu Sep 05 2024 Anton Farygin <rider@altlinux.ru> 0.8.0-alt1
- 0.7.0 -> 0.8.0

* Sat Nov 18 2023 Anton Farygin <rider@altlinux.ru> 0.7.0-alt3
- fixed build without ocamlopt

* Sat Sep 18 2021 Anton Farygin <rider@altlinux.ru> 0.7.0-alt2
- fixed build with emabled LTO

* Mon Mar 22 2021 Anton Farygin <rider@altlinux.org> 0.7.0-alt1
- 0.7.0

* Sat Mar 16 2019 Anton Farygin <rider@altlinux.ru> 0.6.0-alt1
- first build for ALT
- ported from String to Bytes to avoid problems with latest ocaml and safe-string defaults
