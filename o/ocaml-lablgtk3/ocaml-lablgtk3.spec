%define libname lablgtk3
Name: ocaml-%libname
Version: 3.1.5
Release: alt1

Summary: Objective Caml interface to gtk+

License: LGPLv2.1 with OCaml-LGPL-linking-exception
Group: Development/ML
Url: https://github.com/garrigue/lablgtk
VCS: https://github.com/garrigue/lablgtk
Source: %name-%version.tar
BuildRequires:  ocaml dune
BuildRequires:  ocaml-dune-configurator-devel
BuildRequires:  ocaml-cairo2-devel >= 0.6
BuildRequires:  ocaml-camlp-streams-devel >= 5.0
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-odoc
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0)

%description
LablGTK is is an Objective Caml interface to gtk+.

It uses the rich type system of Objective Caml 3 to provide a strongly
typed, yet very comfortable, object-oriented interface to gtk+. This
is not that easy if you know the dynamic typing approach taken by
gtk+.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR
Requires: pkgconfig(gtk+-3.0)

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

%build
%dune_build -p %libname

%install
%dune_install -p %libname

%check
%dune_check -p %libname

%files -f ocaml-files.runtime
%doc LICENSE

%files devel -f ocaml-files.devel
%_bindir/*
%_libdir/ocaml/%libname/*.h
%doc README.md CHANGES.md

%changelog
* Sat Sep 21 2024 Anton Farygin <rider@altlinux.ru> 3.1.5-alt1
- 2.18.11 -> 3.1.5

* Fri Jul 03 2020 Anton Farygin <rider@altlinux.ru> 2.18.11-alt1
- 2.18.11

* Fri Jan 24 2020 Anton Farygin <rider@altlinux.ru> 2.18.10-alt1
- 2.18.10

* Tue Jul 30 2019 Anton Farygin <rider@altlinux.ru> 2.18.8-alt1
- 2.18.8
- switch to camlp5 preprocessor

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 2.18.6-alt3
- rebuilt with ocaml-4.07.1

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 2.18.6-alt2.qa1
- NMU: applied repocop patch

* Tue Sep 04 2018 Anton Farygin <rider@altlinux.ru> 2.18.6-alt2
- rebuilt with ocaml-4.07

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 2.18.6-alt1
- 2.18.6
- rebuilt for ocaml 4.06.1

* Mon Jul 10 2017 Anton Farygin <rider@altlinux.ru> 2.18.5-alt4
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 2.18.5-alt3
- rebuild with ocaml 4.04.1

* Fri Apr 21 2017 Anton Farygin <rider@altlinux.ru> 2.18.5-alt2
- rebuilt in new environment

* Sun Apr 16 2017 Anton Farygin <rider@altlinux.ru> 2.18.5-alt1
- first build for ALT, based on RH spec
