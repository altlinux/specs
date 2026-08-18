%def_with check
Name: ocaml-fuse3
Version: 3.10.0
Release: alt1
Summary: OCaml bindings for FUSE 3
Group: Development/ML
License: LGPL-2.1-only
Url: https://github.com/libfuse/libfuse
VCS: https://github.com/astrada/ocamlfuse
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.08.0
BuildRequires: dune >= 3.7
BuildRequires: ocaml-camlidl-devel
BuildRequires: ocaml-camlidl
BuildRequires: opam
BuildRequires: ocaml-findlib
BuildRequires: pkgconfig
BuildRequires: ocaml-dune-configurator-devel
BuildRequires: ocaml-odoc-devel
BuildRequires: pkgconfig(fuse3)

%if_with check
BuildRequires: ocaml-ounit-devel
%endif

%description
This is a binding to FUSE 3 for the OCaml programming language, enabling
users to implement high-level FUSE filesystems in OCaml. It has been designed
with simplicity as a goal, as you can see by looking at example/fusexmp.ml.
The Bigarray library is used for read and write buffers, allowing the library
to do zero-copy in OCaml land.

%package devel
Summary: Development files for ocaml-fuse3
Requires: %name = %EVR
Requires: pkgconfig(fuse3)
Group: Development/ML

%description devel
Development files for ocaml-fuse3.

%prep
%setup

%build
%dune_build -p fuse3

%install
%dune_install_multi fuse3

%check
%dune_check -p fuse3

%files -f ocaml-files.runtime.fuse3

%files devel -f ocaml-files.devel.fuse3

%changelog
* Tue Aug 18 2026 Anton Farygin <rider@altlinux.org> 3.10.0-alt1
- Initial build for ALT Linux.

