%define pkgname lambda-term
Name: ocaml-%pkgname
Version: 3.4.0
Release: alt1
Summary: Terminal manipulation library for OCaml

Group: Development/ML
License: MIT
Url: https://github.com/ocaml-community/lambda-term
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: dune ocaml-cppo ocaml-mew-devel ocaml-mew_vi-devel
BuildRequires: ocaml-lwt_log-devel ocaml-zed-devel >= 3.2.0
BuildRequires: ocaml-trie-devel ocaml-lwt-devel ocaml-logs-devel
BuildRequires: ocaml-camomile-devel
BuildRequires: libev-devel
BuildRequires: rpm-build-ocaml >= 1.4

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
%patch0 -p1

%build
%dune_build -p %pkgname

%install
%dune_install %pkgname

%files -f ocaml-files.runtime
%doc CHANGES.md README.md
%doc %_datadir/lambda-term-inputrc
%doc %_datadir/lambda-termrc
%_man1dir/lambda-term-actions.1.*
%_man5dir/lambda-term-inputrc.5.*
%_bindir/lambda-term-actions

%files devel -f ocaml-files.devel

%changelog
* Mon Apr 06 2026 Anton Farygin <rider@altlinux.org> 3.4.0-alt1
- 3.3.3 -> 3.4.0

* Sun Apr 05 2026 Anton Farygin <rider@altlinux.ru> 3.3.3-alt2
- fixed mouse motion event decoding in X11 normal encoding (mode 1002)

* Thu Jan 15 2026 Anton Farygin <rider@altlinux.org> 3.3.3-alt1
- 3.3.2 -> 3.3.3

* Mon Nov 13 2023 Anton Farygin <rider@altlinux.ru> 3.3.2-alt1
- 3.3.2

* Thu Nov 04 2021 Anton Farygin <rider@altlinux.ru> 3.1.0-alt2
- cleanup specfile

* Sat Jun 20 2020 Mikhail Gordeev <obirvalger@altlinux.org> 3.1.0-alt1
- Initial build for Sisyphus
