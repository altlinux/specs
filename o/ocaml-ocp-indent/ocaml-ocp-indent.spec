%define libname ocp-indent
Name: ocaml-%libname
Version: 1.8.2
Release: alt3
Summary: A simple tool to indent OCaml programs
License: LGPLv2.1 with OCaml-LGPL-linking-exception
Group: Development/ML
Url: https://www.typerex.org/ocp-indent.html
VCS: https://github.com/OCamlPro/ocp-indent
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
BuildRequires: dune
BuildRequires: ocaml ocaml-cmdliner-devel ocaml-findlib-devel
%description
Ocp-indent is based on an approximate, tolerant OCaml parser and a simple stack
machine ; this is much faster and more reliable than using regexps. Presets and
configuration options available, with the possibility to set them project-wide.
Supports most common syntax extensions, and extensible for others.


%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1

%build
%dune_build -p %libname

%install
%dune_install

%files -f ocaml-files.runtime
%doc README.md LICENSE CHANGELOG
%_bindir/ocp-indent
%_man1dir/ocp-indent.1.*
%_datadir/ocp-indent
%_datadir/emacs

%files devel -f ocaml-files.devel

%changelog
* Thu Jan 23 2025 Anton Farygin <rider@altlinux.ru> 1.8.2-alt3
- applied PR 236 from upstream git to remove unnecessary 'bytes' dependency

* Sat Sep 14 2024 Anton Farygin <rider@altlinux.ru> 1.8.2-alt2
- returned to Sisyphus

* Sat Sep 14 2024 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- first build for ALT
