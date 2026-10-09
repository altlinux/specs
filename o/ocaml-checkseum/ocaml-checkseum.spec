%def_with check
Name: ocaml-checkseum
Version: 0.5.4
Release: alt1
Summary: Adler-32, CRC32 and CRC32-C implementation in C and OCaml
Group: Development/ML
License: MIT
Url: https://github.com/mirage/checkseum
VCS: https://github.com/mirage/checkseum
Source0: %name-%version.tar

BuildRequires: ocaml >= 4.07.0
BuildRequires: dune >= 2.6.0

BuildRequires: ocaml-dune-configurator-devel
BuildRequires: ocaml-optint-devel >= 0.3.0

%if_with check
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-alcotest-devel
BuildRequires: ocaml-bos-devel
BuildRequires: ocaml-astring-devel
BuildRequires: ocaml-fmt-devel
BuildRequires: ocaml-fpath-devel
BuildRequires: ocaml-rresult-devel
%endif

%description
Checkseum is a library to provide implementation of Adler-32, CRC32 and
CRC32-C in C and OCaml.

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
%dune_build -p checkseum

%install
%dune_install checkseum

%check
%dune_check -p checkseum

%files -f ocaml-files.runtime
%doc README.md

%files devel -f ocaml-files.devel

%changelog
* Tue Oct 06 2026 Anton Farygin <rider@altlinux.org> 0.5.4-alt1
- initial build for ALT Linux

