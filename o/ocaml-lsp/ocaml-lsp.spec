%define pkgname lsp
Name: ocaml-%pkgname
Version: 1.19.0
Release: alt1
Summary: LSP Server for OCaml
License: MIT
Group: Development/ML
Url: https://github.com/ocaml/ocaml-lsp
VCS: https://github.com/ocaml/ocaml-lsp
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-yojson-devel
BuildRequires: ocaml-ppx_yojson_conv_lib-devel
BuildRequires: cinaps
BuildRequires: ocaml-uutf-devel
BuildRequires: ocaml-ppx_expect-devel
BuildRequires: ocaml-odoc-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-chrome-trace-devel
BuildRequires: ocaml-dyn-devel
BuildRequires: ocaml-stdune-devel
BuildRequires: ocaml-fiber-devel
BuildRequires: ocaml-xdg-devel
BuildRequires: ocaml-ordering-devel
BuildRequires: ocaml-dune-build-info-devel
BuildRequires: ocaml-dune-rpc-devel
BuildRequires: ocaml-spawn-devel
BuildRequires: ocaml-astring-devel
BuildRequires: ocaml-camlp-streams-devel
BuildRequires: ocaml-ocamlformat
BuildRequires: ocaml-ocamlc-loc-devel
BuildRequires: ocaml-pp-devel
BuildRequires: ocaml-odoc-devel
BuildRequires: ocaml-merlin-devel
BuildRequires: ocaml-ocamlformat-devel

%description
%summary


%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

find . -type f -name 'dune' -exec sed -si '/ppx_expect\.common/d' {} \;

%build
%dune_build --release @install

%install
%dune_install

%check
make test-ocaml

%files -f ocaml-files.runtime
%_bindir/ocamllsp

%files devel -f ocaml-files.devel

%changelog
* Sat Sep 14 2024 Anton Farygin <rider@altlinux.ru> 1.19.0-alt1
- first build for ALT Linux
