%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name: ocaml-mysql
Version: 1.2.4
Release: alt3

Summary: MySQL bindings for OCaml
License: LGPL-2.1-only
Group: Development/ML

URL: https://ygrek.org/p/ocaml-mysql/
VCS: https://github.com/ygrek/ocaml-mysql
Source: ocaml-mysql-%version.tar
Patch0: ocaml-mysql-1.2.2-alt-mysql8-transition.patch

BuildRequires: ocaml-findlib libMySQL-devel zlib-devel chrpath
BuildRequires(pre): rpm-build-ocaml >= 1.6.1

%package devel
Summary: MySQL bindings for OCaml
Group: Development/ML
Conflicts: %name < %EVR
Requires: %name = %EVR

%description
ocaml-mysql is a package for OCaml that provides access to MySQL
databases. It consists of low level functions implemented in C and
a module Mysql intended for application development.

%description devel
ocaml-mysql is a package for OCaml that provides access to MySQL
databases. It consists of low level functions implemented in C and
a module Mysql intended for application development.


%prep
%setup -q

%patch0 -p0

%build
%configure
make all
%ifarch %ocaml_native_arch
make opt
%endif

%install
export OCAMLFIND_LDCONF=ignore
export OCAMLFIND_DESTDIR=%buildroot%_ocamldir
mkdir -p $OCAMLFIND_DESTDIR
%makeinstall_std

#remove rpath
chrpath -d %buildroot%_ocamldir/mysql/dllmysql_stubs.so

# move runtime to stublibs
mkdir -p %buildroot%_ocamldir/stublibs
mv %buildroot%_ocamldir/mysql/dllmysql_stubs.so %buildroot%_ocamldir/stublibs

%ocaml_find_files

%files -f ocaml-files.runtime
%doc CHANGES README

%files devel -f ocaml-files.devel

%changelog
* Thu Nov 23 2023 Anton Farygin <rider@altlinux.ru> 1.2.4-alt3
- fix build with bytecode ocaml

* Fri Oct 01 2021 Egor Ignatov <egori@altlinux.org> 1.2.4-alt2
- fix build with lto

* Tue Feb 25 2020 Anton Farygin <rider@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Wed Jul 24 2019 Anton Farygin <rider@altlinux.ru> 1.2.2-alt5
- rebuilt with ocaml-4.08.0
- removed campl4 from build requires

* Thu Feb 07 2019 Nikolai Kostrigin <nickel@altlinux.org> 1.2.2-alt4
- fix FTBFS against libmysqlclient21

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.2.2-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.2.2-alt2
- rebuilt with ocaml 4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.2.1-alt3
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.2.1-alt2
- rebuild with ocaml 4.04.1

* Mon Apr 10 2017 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- new version from new upstream git
- build with ocaml-4.04

* Sun Apr 14 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.0.4-alt5.qa1
- NMU: rebuilt with libmysqlclient.so.18.

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

