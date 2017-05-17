Name: ocamldsort
Version: 0.16.0
Release: alt1%ubt
Summary: Makefile helper for OCaml
License: GPL
Group: Development/ML
Url: http://www.normalesup.org/~ara/informatique.html
# ftp://quatramaran.salle-s.org/pub/ara/ocamldsort
Source: %name-%version.tar

BuildRequires: ocaml >= 4.04, ocaml-camlp4-devel
BuildRequires(pre):rpm-build-ubt

%description

 The ocamldsort command scans a set of Objective Caml source files (.ml and
.mli files) and sort them according to their dependencies in order to link
their corresponding .cmo files.

%prep
%setup

%build
%configure
make
mv ocamldsort.opt ocamldsort

%install
%makeinstall BINDIR=%buildroot%_bindir MANDIR=%buildroot%_mandir

%files
%_bindir/*
%doc %_man1dir/*
%doc README

%changelog
* Wed May 17 2017 Anton Farygin <rider@altlinux.ru> 0.16.0-alt1%ubt
- new version

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.14.4-alt1.qa1
- NMU: rebuilt for debuginfo.

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

