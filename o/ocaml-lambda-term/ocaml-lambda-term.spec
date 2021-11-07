Name: ocaml-lambda-term
Version: 3.1.0
Release: alt2
Summary: Terminal manipulation library for OCaml

Group: Development/ML
License: MIT
Url: https://github.com/ocaml-community/lambda-term
Source: %name-%version.tar

BuildRequires: dune ocaml-cppo ocaml-mew-devel ocaml-mew_vi-devel
BuildRequires: ocaml-lwt_log-devel ocaml-zed-devel 
BuildRequires: ocaml-trie-devel ocaml-lwt-devel ocaml-charInfo_width-devel
BuildRequires: ocaml-camomile-devel
BuildRequires: libev-devel
BuildRequires: rpm-build-ocaml >= 1.1

%description
Lambda-Term is a cross-platform library for manipulating the terminal. It
provides an abstraction for keys, mouse events, colors, as well as a set of
widgets to write curses-like applications.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build --release @install

%install
%dune_install

%files -f ocaml-files.runtime
%doc CHANGES.md README.md
%doc %_datadir/lambda-term-inputrc
%doc %_datadir/lambda-termrc
%_man1dir/lambda-term-actions.1.*
%_man5dir/lambda-term-inputrc.5.*
%_bindir/lambda-term-actions

%files devel -f ocaml-files.devel

%changelog
* Thu Nov 04 2021 Anton Farygin <rider@altlinux.ru> 3.1.0-alt2
- cleanup specfile

* Sat Jun 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus
