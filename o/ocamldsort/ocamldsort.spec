Name: ocamldsort
Version: 0.14.4
Release: alt1
Packager: Grigory Batalov <bga@altlinux.ru>

Summary: Makefile helper for OCaml
License: GPL
Group: Development/ML
Url: http://dimitri.mutu.net/ocaml.html

Source: ftp://quatramaran.ens.fr/pub/ara/ocamldsort/%name-%version.tar.gz
Patch: ocamldsort-0.14.3-alt-sed.patch

BuildRequires: ocaml >= 3.07, camlp4

%description

 The ocamldsort command scans a set of Objective Caml source files (.ml and
.mli files) and sort them according to their dependencies in order to link
their corresponding .cmo files.

%prep
%setup -q
%patch0 -p0

%build
%configure
%make_build opt
mv ocamldsort.opt ocamldsort

%install
%makeinstall BINDIR=%buildroot%_bindir MANDIR=%buildroot%_mandir

%files
%_bindir/*
%doc %_man1dir/*
%doc README

%changelog
* Thu Oct 04 2007 Grigory Batalov <bga@altlinux.ru> 0.14.4-alt1
- New upstream release.

* Sat Dec 23 2006 Grigory Batalov <bga@altlinux.ru> 0.14.3-alt1
- New upstream release.
- New group, url, packager.
- Old patches are obsolete.
- Patch configure with correct sed pattern.
- Install section updated: distribute native binary.
- Specfile cleanup.

* Fri May  7 2004 Alexander V. Nikolaev <avn@altlinux.org> 0.12-alt3.1
- Non-maintainer upload
- Add "packager" to spec
- Rebuild with glibc 2.3.x and ocaml 3.07-alt6.1

* Thu Dec 25 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.12-alt3
rebuild


* Fri Jan 31 2003 Vitaly Lugovsky <vsl@altlinux.ru> 0.12-alt2
- Requirements removed

* Sat Sep 28 2002 Vitaly Lugovsky <vsl@altlinux.ru> 0.12-alt1
- initial release

