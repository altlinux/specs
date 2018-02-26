%define oname ocamlbdb
Name: ocaml-bdb
Version: 4.3.21
Release: alt4
Summary: OCaml interface to Berkeley-DB
Packager: Boris Savelev <boris@altlinux.org>
Source: http://www.eecs.harvard.edu/~stein/%oname-%version.tar.gz
Url: http://www.eecs.harvard.edu/~stein/
License: GPL
Group: Development/Other

# Automatically added by buildreq on Sat Aug 23 2008
BuildRequires: libdb4-devel ocaml
Requires: %name-runtime = %version-%release
Obsoletes: %name-devel
Provides: %name-devel = %version-%release

%description
This package contains the development files needed to build applications
using %name-runtime.

%package runtime
Summary: OCaml interface to Berkeley-DB
Group: Development/Other

%description runtime
CamlGI is a library to enable you to write CGI and FastCGI in OCaml. It is
written 100%% in OCaml so should run on many platforms. The library supports
multiple simultaneous connections and request multiplexing while presenting an
easy to use interface.

%prep
%setup -n %oname-%version

%build
%__subst 's:BDB_DIR=/usr/local/BerkeleyDB.4.3/:BDB_DIR=%prefix:g' Makefile
%__subst 's:/usr/local/lib:%_libdir:g' Makefile
%__subst 's:-ldb-4.1:-ldb:g' Makefile
%make

%install
mkdir -p %buildroot%_libdir/ocaml/site-lib/bdb
install -m 644 bdb.cma bdb.cmi libcamlbdb.a %buildroot%_libdir/ocaml/site-lib/bdb/

%files runtime
%doc CREDITS README
%dir %_libdir/ocaml/site-lib/bdb
%_libdir/ocaml/site-lib/bdb/*.cmi

%files
%_libdir/ocaml/site-lib/bdb/*
%exclude %_libdir/ocaml/site-lib/bdb/*.cmi

%changelog
* Mon Dec 26 2011 Alexey Shabalin <shaba@altlinux.ru> 4.3.21-alt4
- rebuild with new ocaml

* Thu Nov 18 2010 Boris Savelev <boris@altlinux.org> 4.3.21-alt3
- rename packages (%name -> %name-runtime ; %name-devel -> %name)

* Tue Aug 26 2008 Boris Savelev <boris@altlinux.org> 4.3.21-alt2
- fix x86_64 build

* Sat Aug 23 2008 Boris Savelev <boris@altlinux.org> 4.3.21-alt1
- initial build for Sisyphus from Mandriva

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 4.3.21-4mdv2008.1
+ Revision: 178361
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.3.21-3mdv2008.0
+ Revision: 77595
- drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage

* Tue Feb 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.3.21-2mdv2007.0
+ Revision: 123144
- requires corresponding native devel package

* Mon Feb 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.3.21-1mdv2007.1
+ Revision: 122841
- fix build dependencies

* Mon Feb 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 4.3.21-1mdv2007.1
- first mdv release

