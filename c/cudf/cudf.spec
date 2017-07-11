Summary: CUDF (Common Upgradeability Description Format) tools and libraries
Name: cudf
Version: 0.9
Release: alt2%ubt
# https://scm.gforge.inria.fr/anonscm/git/cudf/cudf.git
Source: %name-%version.tar
Url: http://www.mancoosi.org/cudf/
License: LGPL
Group: Development/ML
BuildRequires: ocaml ocaml-findlib ocaml-extlib-devel perl-podlators ocaml-ocamlbuild libncurses-devel glib2-devel ocaml-ounit
BuildRequires(pre):rpm-build-ubt

%description
CUDF (for Common Upgradeability Description Format) is a format for describing
upgrade scenarios in package-based Free and Open Source Software distribution.

libCUDF is a library to manipulate so called CUDF documents. A CUDF document
describe an upgrade problem, as faced by package managers in popular
package-based GNU/Linux distributions.

%package tools
Summary: CUDF (Common Upgradeability Description Format) command-line tools
Group: System/Configuration/Packaging

%description tools
CUDF (for Common Upgradeability Description Format) is a format for describing
upgrade scenarios in package-based Free and Open Source Software distribution.

libCUDF is a library to manipulate so called CUDF documents. A CUDF document
describe an upgrade problem, as faced by package managers in popular
package-based GNU/Linux distributions.

This package contains command line tools to manipulate CUDF and related
documents. In particular it contains cudf-check, which enables checking of
document properties such as installation consistency and matching of problems
with their solutions.

%package devel
Summary: CUDF (Common Upgradeability Description Format) C development stuff
Group: Development/ML

%description devel
CUDF (for Common Upgradeability Description Format) is a format for describing
upgrade scenarios in package-based Free and Open Source Software distribution.

libCUDF is a library to manipulate so called CUDF documents. A CUDF document
describe an upgrade problem, as faced by package managers in popular
package-based GNU/Linux distributions.

This package contains the development stuff needed to use libCUDF in your C
programs.

%package -n ocaml-%name-devel
Summary: CUDF (Common Upgradeability Description Format) OCaml development stuff
Group: Development/ML

%description -n ocaml-%name-devel
CUDF (for Common Upgradeability Description Format) is a format for describing
upgrade scenarios in package-based Free and Open Source Software distribution.

libCUDF is a library to manipulate so called CUDF documents. A CUDF document
describe an upgrade problem, as faced by package managers in popular
package-based GNU/Linux distributions.

This package contains the development stuff needed to use libCUDF in your OCaml
programs.

%prep
%setup

%build
make all c-lib
which /usr/bin/ocamlopt > /dev/null && make opt c-lib-opt

%install
make install				\
    DESTDIR="$RPM_BUILD_ROOT"		\
    LIBDIR="%_libdir"			\
    OCAMLLIBDIR="%_libdir/ocaml"

%check
make test

%files tools
%_bindir/cudf-check
%_bindir/cudf-parse-822

%files devel
%_includedir/cudf.h
%_libdir/*.a
%_libdir/pkgconfig/cudf.pc

%files -n ocaml-%name-devel
%_libdir/ocaml/cudf

%changelog
* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 0.9-alt2%ubt
- rebuild with ocaml 4.04.2

* Mon May 15 2017 Anton Farygin <rider@altlinux.ru> 0.9-alt1%ubt
- first build for ALT
