%define _name labltk

Name: ocaml4-%_name
Version: 8.06.0
Release: alt1

Summary: Tcl/Tk interface for OCaml
Group: Development/ML

License: LGPLv2+ with exceptions

Url: https://forge.ocamlcore.org/projects/labltk/
Source: %_name-%version.tar

Requires: ocaml4
Requires: %name-runtime = %version-%release
BuildRequires: ocaml4
BuildRequires: tcl-devel, tk-devel

%description
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

LablTk gives OCaml program access to Tcl/Tk GUI widgets. This package
contains files needed to develop OCaml programs using LablTk.

%package runtime
Summary: Tk toolkit bindings for OCaml
Group: Development/ML
Requires: ocaml4-runtime

%description runtime
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

LablTk gives OCaml program access to Tcl/Tk GUI widgets. This package
contains files needed to run bytecode OCaml programs using LablTk.

%package -n ocaml4-ocamlbrowser
Summary: OCaml interface browser
Group: Development/ML
Requires: %name-runtime

%description -n ocaml4-ocamlbrowser
Objective Caml is a high-level, strongly-typed, functional and
object-oriented programming language from the ML family of languages.

This package provides OCamlBrowser, a source and compiled interface
browser, written using LablTk.

%prep
%setup -q -n %_name-%version

%build
./configure
make all
make opt

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libdir/ocaml/labltk
mkdir -p %buildroot%_libdir/ocaml/stublibs

make install \
    BINDIR=%buildroot%_bindir \
    INSTALLDIR=%buildroot%_libdir/ocaml/labltk \
    STUBLIBDIR=%buildroot%_libdir/ocaml/stublibs

%files
%doc Changes README.mlTk
%_bindir/labltk
%_libdir/ocaml/labltk

%files runtime
%_libdir/ocaml/stublibs/dlllabltk.so

%files -n ocaml4-ocamlbrowser
%_bindir/ocamlbrowser

%changelog
* Tue Oct 28 2014 Alexey Shabalin <shaba@altlinux.ru> 8.06.0-alt1
- initial build for ocaml4
