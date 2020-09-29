%set_verify_elf_method textrel=relaxed
%define libname graphics
Name: ocaml-%libname
Version: 5.1.0
Release: alt2
Summary: The OCaml graphics library
License: LGPLv2.1 with exceptions
Group: Development/ML
Url: https://github.com/ocaml/graphics
Source0: %name-%version.tar
BuildRequires: ocaml ocaml-dune-devel libX11-devel

%description
The graphics library provides a set of portable drawing primitives. Drawing
takes place in a separate window that is created when Graphics.open_graph is
called.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build --release @install

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%doc README.md LICENSE CHANGES.md

%files devel -f ocaml-files.devel

%changelog
* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 5.1.0-alt2
- migrated to rpm-build-ocaml 1.4

* Fri Feb 28 2020 Anton Farygin <rider@altlinux.ru> 5.1.0-alt1
- first build for ALT

