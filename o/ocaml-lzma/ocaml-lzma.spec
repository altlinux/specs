ExcludeArch: %ix86
Name: ocaml-lzma
Version: 1.0.0
Release: alt1
Summary: OCaml bindings to liblzma for multithreaded XZ compression and decompression
Group: Development/ML
License: LGPL-2.1-or-later
Url: https://altlinux.space/rider/ocaml-lzma2
VCS: https://altlinux.space/rider/ocaml-lzma2
Source0: %name-%version.tar

BuildRequires: ocaml >= 5.0.0
BuildRequires: dune >= 3.0
BuildRequires: liblzma-devel
BuildRequires: ocaml-odoc-devel

%description
OCaml bindings to liblzma (xz-utils) for XZ/LZMA2 compression and
decompression. Multithreaded compression via lzma_stream_encoder_mt,
parallel decompression of concatenated streams via OCaml 5 Domains.
Domain-safe. Includes oxz CLI tool.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Requires: liblzma-devel
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p lzma

%install
%dune_install lzma

%files -f ocaml-files.runtime
%doc README.md README.ru.md
%_bindir/oxz

%files devel -f ocaml-files.devel

%changelog
* Thu Apr 02 2026 Anton Farygin <rider@altlinux.org> 1.0.0-alt1
- First stable release.
- Multithreaded compression via lzma_stream_encoder_mt.
- Decompression with concatenated stream support.
- oxz CLI tool.

* Thu Apr 02 2026 Anton Farygin <rider@altlinux.org> 0.1.0-alt1
- Initial build for ALT Linux.
