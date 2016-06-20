%define _name findlib
Name: ocaml4-%_name
Version: 1.6.2
Release: alt1

Summary: A module packaging tool for OCaml
License: Distributable
Group: Development/ML
Url: http://www.ocaml-programming.de/packages/documentation/findlib/

Source: %_name-%version.tar
Patch1: findlib-1.1.2pl1-alt-native.patch
Patch2: findlib-1.1.2pl1-alt-wizard.patch
Patch3: findlib-1.6.2-alt-install-doc.patch

# Automatically added by buildreq on Tue Apr 08 2008 (-bi)
BuildRequires: rpm-build-ocaml4 ocaml4-camlp4 ocaml4-labltk libtinfo-devel ocaml4-ocamldoc
BuildRequires: ocaml4-ocamlbuild libX11-devel tcl-devel tk-devel

%package -n ocaml4-ocamlfind-mini
Summary: Minimal findlib script to be distributed with user libraries
Group: Development/ML
BuildArch: noarch

%package toolbox
Summary: graphical wizard to create findlib-enabled Makefiles
Group: Development/ML

%description
The "findlib" library provides a scheme to manage reusable software
components (packages), and includes tools that support this
scheme. Packages are collections of OCaml modules for which
metainformation can be stored. The packages are kept in the filesystem
hierarchy, but with strict directory structure. The library contains
functions to look the directory up that stores a package, to query
metainformation about a package, and to retrieve dependency
information about multiple packages. There is also a tool that allows
the user to enter queries on the command-line. In order to simplify
compilation and linkage, there are new frontends of the various OCaml
compilers that can directly deal with packages.

%description -n ocaml4-ocamlfind-mini
ocamlfind-mini is an O'Caml script that implements a subset of the
full functionality of ocamlfind. It consists only of one file, so it
is easy to distribute it with any software.

The subset is normally sufficient to compile a library and to
install the library; but it is insufficient to link the library
into an executable.

%description toolbox
The graphical 'findlib-make-wizard' tool to aid in creating
findlib-enabled Makefiles.

%prep
%setup -q -n %_name-%version
%patch1 -p2
%patch2 -p2
%patch3 -p2

sed -i -e 's,@LIBDIR@,%_libdir,g' src/findlib-toolbox/make_wizard.ml

%build
./configure -mandir %_mandir -config %_libdir/ocaml/etc/findlib.conf -with-toolbox
make
make opt

%install
%make_install install prefix=%buildroot

install -pD -m755 mini/ocamlfind-mini %buildroot%_bindir/ocamlfind-mini

# remove default byte-coded wizard and install native one
rm -f %buildroot%_libdir/ocaml/site-lib/findlib/make_wizard
install -m755 src/findlib-toolbox/make_wizard.opt %buildroot%_bindir/findlib-make-wizard

# remove native dynlink plugin
rm -f %buildroot%_libdir/ocaml/site-lib/findlib/findlib.cmxs
rm -f %buildroot%_libdir/ocaml/site-lib/findlib/*.cmxs

%files -n ocaml4-ocamlfind-mini
%doc mini/README
%_bindir/ocamlfind-mini

%files toolbox
%_bindir/findlib-make-wizard

%files
%exclude %_bindir/ocamlfind-mini
%exclude %_bindir/findlib-make-wizard
%_bindir/ocamlfind
%exclude %_bindir/safe_camlp4
%_libdir/ocaml/etc/*
%_libdir/ocaml/topfind
%_libdir/ocaml/site-lib/*
%_man1dir/ocamlfind.1*
%_man5dir/*
%doc doc/* LICENSE

%changelog
* Sat Jun 18 2016 Andrey Bergman <vkni@altlinux.org> 1.6.2-alt1
- 1.6.2

* Wed Jul 01 2015 Andrey Bergman <vkni@altlinux.org> 1.5.5-alt2
- Rebuild with new rpm-build-ocaml4.

* Tue Oct 28 2014 Alexey Shabalin <shaba@altlinux.ru> 1.5.5-alt1
- 1.5.5
- initial build for ocaml4
