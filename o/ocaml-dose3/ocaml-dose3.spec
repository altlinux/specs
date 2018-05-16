# Currently packaging a snapshot to build with newer ocaml.
%set_verify_elf_method textrel=relaxed

Name: ocaml-dose3
Version: 5.0.1
Release: alt1.5.2git09392e2%ubt
Summary: Framework for managing distribution packages and dependencies
Group: Development/ML

%global libname %(echo %name | sed -e 's/^ocaml-//')

# Linking exception, see included COPYING file.
License: LGPLv3+ with exceptions
Url: http://www.mancoosi.org/software/

Source0: %name-%version.tar

# One remaining safe-string fix.
Patch0: ocaml-dose3-safe-string.patch

BuildRequires(Pre): rpm-build-ubt

BuildRequires: ocaml
BuildRequires: ocaml-ocamlbuild
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-ocamlgraph-devel
BuildRequires: ocaml-findlib-devel
BuildRequires: ocaml-extlib-devel
BuildRequires: ocaml-expat-devel
BuildRequires: ocaml-re-devel
BuildRequires: ocaml-cudf-devel
BuildRequires: ocaml-cppo
BuildRequires: ocaml-zip-devel
BuildRequires: ocaml-ounit-devel

BuildRequires: rpm-devel
BuildRequires: zlib-devel

BuildRequires: perl

# Depend on pod2man, pod2html.
BuildRequires: /usr/bin/pod2man
BuildRequires: /usr/bin/pod2html

%description
Dose3 is a framework made of several OCaml libraries for managing
distribution packages and their dependencies.

Though not tied to any particular distribution, dose3 constitutes a pool of
libraries which enable analyzing packages coming from various distributions.

Besides basic functionalities for querying and setting package properties,
dose3 also implements algorithms for solving more complex problems
(monitoring package evolutions, correct and complete dependency resolution,
repository-wide uninstallability checks).

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

# Since these are applications, I think the correct name is "dose3-tools"
# and not "ocaml-dose3-tools", but I'm happy to change it if necessary.

%package -n dose3-tools
Summary: Tools suite from the dose3 framework
Group: Development/ML

%description -n dose3-tools
Dose3 is a framework made of several OCaml libraries for managing
distribution packages and their dependencies.

This package contains the tools shipped with the dose3 framework
for manipulating packages of various formats.

%prep
%setup

%build
%configure --with-zip --with-oUnit --with-rpm4 --with-xml
make
make man

%install
make install DESTDIR=%buildroot

# Install manpages.
mkdir -p %buildroot%_mandir/man1/
mkdir -p %buildroot%_mandir/man5/
mkdir -p %buildroot%_mandir/man8/
cp -a doc/manpages/*.8 %buildroot%_mandir/man8/
cp -a doc/manpages/*.5 %buildroot%_mandir/man5/
cp -a doc/manpages/*.1 %buildroot%_mandir/man1/

# Rewrite symlinks.
rm -f %buildroot%_bindir/rpmcheck
rm -f %buildroot%_bindir/debcheck
rm -f %buildroot%_bindir/eclipsecheck
ln -s %_bindir/distcheck %buildroot%_bindir/rpmcheck
ln -s %_bindir/distcheck %buildroot%_bindir/debcheck
ln -s %_bindir/distcheck %buildroot%_bindir/eclipsecheck

%files
%doc README.architecture COPYING
%_libdir/ocaml/%libname
%exclude %_libdir/ocaml/*/*.a
%exclude %_libdir/ocaml/*/*.cmxa
%exclude %_libdir/ocaml/*/*.cmi
%_libdir/ocaml/stublibs/*.so
%_libdir/ocaml/stublibs/*.so.owner

%files devel
%doc COPYING
%_libdir/ocaml/*/*.a
%_libdir/ocaml/*/*.cmxa
%_libdir/ocaml/*/*.cmi

%files -n dose3-tools
%doc COPYING
%doc doc/apt-cudf/
%_bindir/apt-cudf
%_bindir/ceve
%_bindir/challenged
%_bindir/deb-buildcheck
%_bindir/deb-coinstall
%_bindir/debcheck
%_bindir/eclipsecheck
%_bindir/distcheck
%_bindir/outdated
%_bindir/rpmcheck
%_mandir/man1/*.1*
%_mandir/man5/*.5*
%_mandir/man8/*.8*

%changelog
* Wed May 16 2018 Anton Farygin <rider@altlinux.ru> 5.0.1-alt1.5.2git09392e2%ubt
- cleanup  buildrequires

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 5.0.1-alt0.5.2git09392e2%ubt
- first build for ALT, based on RH spec

