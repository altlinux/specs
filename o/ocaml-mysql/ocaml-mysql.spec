Name: ocaml-mysql
Version: 1.0.4
Release: alt5

Summary: MySQL bindings for OCaml
License: LGPL
Group: Development/ML

URL: http://raevnos.pennmush.org/code/ocaml-mysql/
Packager: Alexey Morsov <swi@altlinux.ru>

Source: ocaml-mysql-%version.tar.gz
Patch: ocaml-mysql-1.0.4-CVE-2009-2942-missing-escape.patch

Requires: %name-runtime = %version-%release

# Automatically added by buildreq on Tue Apr 08 2008
BuildRequires: camlp4 findlib libMySQL-devel zlib-devel

%package runtime
Summary: MySQL bindings for OCaml
Group: Development/ML
Conflicts: %name < %version-%release

%description
ocaml-mysql is a package for OCaml that provides access to MySQL
databases. It consists of low level functions implemented in C and
a module Mysql intended for application development.

%description runtime
ocaml-mysql is a package for OCaml that provides access to MySQL
databases. It consists of low level functions implemented in C and
a module Mysql intended for application development.

%prep
%setup -q
%patch -p1

%build
%configure
make all opt

%install
mkdir -p %buildroot%_libdir/ocaml/stublibs
install -p -m755 dll*.so %buildroot%_libdir/ocaml/stublibs/

mkdir -p %buildroot%_libdir/ocaml/site-lib/mysql
install -p -m644 *.{mli,cmi,cma,cmxa,a} META %buildroot%_libdir/ocaml/site-lib/mysql/

%files
%dir %_libdir/ocaml/site-lib/mysql
%_libdir/ocaml/site-lib/mysql/*
%doc CHANGES README doc/html

%files runtime
%_libdir/ocaml/stublibs/dll*.so

%changelog
* Wed Jan 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.0.4-alt5
- rebuilt for new ocaml
- patch for CVE 2009-2942 Missing escape function

* Mon Dec 06 2010 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt4.1
- rebuild with new libmysqlclient by request of libmysqlclient maintainer

* Wed Apr 09 2008 Alexey Tourbin <at@altlinux.ru> 1.0.4-alt4
- rebuilt for new ocaml dependencies
- split ocaml-mysql-runtime subpackage

* Thu Jan 11 2007 Alexey Morsov <swi@altlinux.ru> 1.0.4-alt3
- fix version condition for ocaml

* Mon Dec 18 2006 Alexey Morsov <swi@altlinux.ru> 1.0.4-alt2
- fix version conditions in spec

* Thu Dec 07 2006 Alexey Morsov <swi@altlinux.ru> 1.0.4-alt1
- new version
- change Packager

* Fri May  7 2004 Alexander V. Nikolaev <avn@altlinux.org> 1.0.2-alt4.1
- Non-maintainer upload
- Add "packager" to spec
- Rebuild with glibc 2.3.x and ocaml 3.07-alt6.1

* Wed Mar 17 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.0.2-alt4
- rebuild

* Wed Feb 18 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.0.2-alt3
- rebuild

* Tue Jan 27 2004 Vitaly Lugovsky <vsl@altlinux.ru> 1.0.2-alt2
rebuild

* Wed Nov 12 2003 Vitaly Lugovsky <vsl@altlinux.ru> 1.0.1-alt2
relaxed elf verifying

* Mon Oct 27 2003 Vitaly Lugovsky <vsl@altlinux.ru> 1.0.1-alt1
first release

