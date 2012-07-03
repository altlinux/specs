Name: findlib
Version: 1.2.7
Release: alt1
Packager: Alex V. Myltsev <avm@altlinux.ru>

Summary: A module packaging tool for OCaml
License: Distributable
Group: Development/ML
Url: http://www.ocaml-programming.de/packages/documentation/findlib/

Source: http://www.ocaml-programming.de/packages/%name-%version.tar.gz
Patch1: findlib-1.1.2pl1-alt-native.patch
Patch2: findlib-1.1.2pl1-alt-wizard.patch

# Automatically added by buildreq on Tue Apr 08 2008 (-bi)
BuildRequires: camlp4 labltk libtinfo-devel ocamldoc
BuildRequires: ocamlbuild libX11-devel tcl-devel tk-devel

%package -n ocamlfind-mini
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

%description -n ocamlfind-mini
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
%setup -q
%patch1 -p2
%patch2 -p2

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

%files -n ocamlfind-mini
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
%_man5dir/*.5*
%doc doc/* LICENSE

%changelog
* Tue Dec 20 2011 Alexey Shabalin <shaba@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Tue Apr 08 2008 Alexey Tourbin <at@altlinux.ru> 1.2.1-alt4
- rebuild

* Thu Apr 03 2008 Alexey Tourbin <at@altlinux.ru> 1.2.1-alt3
- rebuilt for new dependencies
- fixed unpackaged %_bindir/findlib-make-wizard
- removed %_bindir/safe_camlp4 (not needed but yields extra deps)

* Mon Jan 07 2008 Alex V. Myltsev <avm@altlinux.ru> 1.2.1-alt2
- Move make-wizard to a separate package (findlib-toolbox).

* Fri Nov 30 2007 Alex V. Myltsev <avm@altlinux.ru> 1.2.1-alt1
- New version: bug fixes, support CamlP4 on OCaml 3.10.

* Sat Dec 23 2006 Grigory Batalov <bga@altlinux.ru> 1.1.2pl1-alt3
- Moving on to get_SVR.
- Docs updated.
- Compression enabled.
- BuildRequires updated.
- Ocamlfind-mini doesn't depend on findlib.
- Make optimized wizard binary.
- Use systemwide make_wizard.pattern if no custom.
- New packager.

* Tue Mar 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.1.2pl1-alt2
- moving on to get_dep.

* Wed Mar 01 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.1.2pl1-alt1
- New version.
- Adopted package.

* Thu Dec 22 2005 Pavlov Konstantin <thresh@altlinux.ru> 1.0.4-alt1.1
- NMU.
- rebuild with new ocaml.
- changed usr/lib to usr/%_lib.

* Tue Oct 26 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.0.4-alt1
- rebuild

* Sat Jul 17 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.0.4-alt0.2
- rebuild

* Wed Jul 07 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.0.4-alt0.1
- rebuild

* Fri May  7 2004 Alexander V. Nikolaev <avn@altlinux.org> 0.9-alt2.1
- Non-maintainer upload
- Add "packager" to spec
- Rebuild with glibc 2.3.x and ocaml 3.07-alt6.1

* Tue Jan 27 2004 Vitaly Lugovsky <vsl@altlinux.ru> 0.9-alt2
threads library issue fixed

* Tue Dec 16 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.9-alt1.1
rebuild


* Wed Oct 08 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.9-alt1
- A new version

* Wed Aug 27 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.8-alt3s
- rebuild

* Thu Mar 06 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.8-alt2s
- added static libraries METAs

* Fri Jan 31 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.8-alt1s
- rebuild with ocaml-3.06 [Shared]

* Sun Oct 27 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.8-alt1
- new version

* Sun Aug 18 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.2-alt1
- new release

*Tue Jul 30 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7.1-alt1
- new release

*Mon Jun 24 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.7-alt1
- new version released

*Tue Apr 16 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.6.2-alt6
- Rebuild with 3.04+9

*Sat Mar  2 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.6.2-alt4
- Rebuild with ocaml-3.04+7-alt1

*Sun Feb 17 2002 Vitaly Lugovsky <vsl@altlinux.ru>
- Rebuild with ocaml-3.04-alt4 (shared patch disabled)

*Mon Jan 14 2002 Vitaly Lugovsky <warlock@skeptik.net>
- First RPM release.
