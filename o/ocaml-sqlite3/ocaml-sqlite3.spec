Name: ocaml-sqlite3
Version: 1.6.1
Release: alt1

Summary: OCaml library for accessing SQLite3 databases
License: GPL
Group: Development/ML
Url: http://www.ocaml.info/home/ocaml_sources.html

Packager: Veaceslav Grecea <slavutich@altlinux.org>
Source: http://www.ocaml.info/ocaml_sources/%name-release-%version.tar.bz2
Patch0: ocaml-sqlite-debian-install-no-mktop.patch

# Automatically added by buildreq on Mon Sep 08 2008
BuildRequires: camlp4 findlib libsqlite3-devel ocamldoc

Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

%description
SQLite 3 database library wrapper for OCaml.

%package runtime
Summary: OCaml library for accessing SQLite3 databases
Group: Development/ML

%description runtime
Runtime part of OCaml library for accessing SQLite3 databases

%prep
%setup -q -n %name-release-%version
%patch0 -p1

./configure --libdir=%_libdir

%build
make all

%check
pushd test
for f in test_db test_exec test_stmt test_fun; do
  ocamlopt -I .. str.cmxa sqlite3.cmxa $f.ml -o $f
  ./$f
done
popd

%install
mkdir -p %buildroot%_libdir/ocaml/stublibs
mkdir -p %buildroot%_libdir/ocaml/site-lib/sqlite3

#%make_install install
cp *.{cma,cmxa,cmi,cmo,a} %buildroot%_libdir/ocaml/site-lib/sqlite3
cp META %buildroot%_libdir/ocaml/site-lib/sqlite3
cp *.so %buildroot%_libdir/ocaml/stublibs

%files
%doc COPYING Changelog doc README.txt TODO
%_libdir/ocaml/site-lib/sqlite3

%files runtime
%_libdir/ocaml/stublibs/*.so

%changelog
* Wed Jan 11 2012 Alexey Shabalin <shaba@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Sep 17 2008 Veaceslav Grecea <slavutich@altlinux.org> 1.2.0-alt1
- updated to new version

* Thu Mar 06 2008 Veaceslav Grecea <slavutich@altlinux.org> 0.23.0-alt1
- Adapted for ALTLinux

* Fri Feb 29 2008 Richard W.M. Jones <rjones@redhat.com> - 0.23.0-2
- Added BR ocaml-camlp4-devel.

* Sun Feb 24 2008 Richard W.M. Jones <rjones@redhat.com> - 0.23.0-1
- Initial RPM release.
