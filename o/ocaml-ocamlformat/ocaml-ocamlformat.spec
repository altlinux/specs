%define pkgname ocamlformat
Name: ocaml-%pkgname
Version: 0.26.2 
Release: alt1
Summary: Auto-formatter for OCaml code 
License: MIT
Group: Development/ML
Url: https://github.com/ocaml-ppx/ocamlformat
VCS: https://github.com/ocaml-ppx/ocamlformat
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune ocaml >= 5.2.0
BuildRequires: ocaml-base-devel
BuildRequires: ocaml-ppx_yojson_conv_lib-devel
BuildRequires: ocaml-dune-build-info-devel
BuildRequires: ocaml-fix-devel
BuildRequires: ocaml-fpath-devel
BuildRequires: ocaml-menhir
BuildRequires: ocaml-version-devel
BuildRequires: ocaml-ocp-indent-devel
BuildRequires: ocaml-stdio-devel
BuildRequires: ocaml-uuseg-devel
BuildRequires: ocaml-uutf-devel
BuildRequires: ocaml-csexp-devel
BuildRequires: ocaml-astring-devel
BuildRequires: ocaml-result-devel
BuildRequires: ocaml-camlp-streams-devel
BuildRequires: ocaml-odoc-devel
BuildRequires: ocaml-alcotest-devel


%description
ocamlformat is a code formatter for OCaml. It comes with opinionated default
settings but is also fully customizable to suit your coding style.

Profiles:    ocamlformat offers profiles we predefined formatting configurations
             Profiles include default, ocamlformat, janestreet.
Configurable:Users can change the formatting profile and configure every
             option in their .ocamlformat configuration file.
Format Comments: ocamlformat can format comments, docstrings, and even code
                 blocks in your comments.
RPC: ocamlformat provides an RPC server that can be used by other tools to
     easily format OCaml Code.

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

%build
%dune_build --release @install

%install
%dune_install

%check
%dune_check

%files -f ocaml-files.runtime
%_bindir/ocamlformat*
%_man1dir/ocamlformat*
%_datadir//emacs/site-lisp/*.el

%files devel -f ocaml-files.devel

%changelog
* Sat Sep 14 2024 Anton Farygin <rider@altlinux.ru> 0.26.2-alt1
- first build for ALT Linux
