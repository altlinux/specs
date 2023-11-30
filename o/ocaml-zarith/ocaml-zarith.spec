%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%global pkgname zarith
%define ocamlstublib %_ocamldir/stublibs/
Name: ocaml-%pkgname
Version: 1.13
Release: alt1
Summary: OCaml interface to GMP
Group: Development/ML
# The license has a static linking exception
License: LGPLv2 with OCaml-LGPL-linking-exception
Url: https://github.com/ocaml/Zarith
Source0: %name-%version.tar
BuildRequires: libgmp-devel
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires(pre): rpm-build-ocaml >= 1.6

%description
This library implements arithmetic and logical operations over
arbitrary-precision integers.

The module is simply named "Z".  Its interface is similar to that of the
Int32, Int64 and Nativeint modules from the OCaml standard library, with
some additional functions.  See the file z.mlip for documentation.

The implementation uses GMP (the GNU Multiple Precision arithmetic
library) to compute over big integers.  However, small integers are
represented as unboxed Caml integers, to save space and improve
performance.  Big integers are allocated in the Caml heap, bypassing
GMP's memory management and achieving better GC behavior than e.g. the
MLGMP library.  Computations on small integers use a special, faster
path (coded in assembly for some platforms and functions) eschewing
calls to GMP, while computations on large integers use the low-level
MPN functions from GMP.

Arbitrary-precision integers can be compared correctly using OCaml's
polymorphic comparison operators (=, <, >, etc.).

Additional features include:
- a module Q for rationals, built on top of Z (see q.mli)
- a compatibility layer Big_int_Z that implements the same API as Big_int,
  but uses Z internally

%package devel
Summary: Development files for %name
Requires: %name = %version-%release
Group: Development/ML
Requires: libgmp-devel

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup

# Fix compilation flags
sed -i "s|^asopt=''|asopt='%optflags'|" configure
sed -i "s|-ccopt|-g &|;s|-shared|-linkall -g &|" project.mak

%build
export CC="gcc -Wa,--noexecstack"
export CFLAGS="%optflags"
export OCAMLFLAGS="-g"
export OCAMLOPTFLAGS="-g"
# This is NOT an autoconf-generated configure script; %%configure doesn't work
./configure
make
make doc

%install
mkdir -p %buildroot%ocamlstublib
mkdir -p %buildroot%_ocamldir
make install INSTALLDIR=%buildroot%_libdir/ocaml
%ocaml_find_files

%files -f ocaml-files.runtime
%doc Changes
%ocamlstublib/*.so.owner

%files devel -f ocaml-files.devel
%doc README.md html
%_ocamldir/%pkgname/*.h

%changelog
* Wed Nov 08 2023 Anton Farygin <rider@altlinux.ru> 1.13-alt1
- 1.13

* Sat Sep 18 2021 Anton Farygin <rider@altlinux.ru> 1.12-alt2
- fixed build with enabled LTO

* Fri Mar 19 2021 Anton Farygin <rider@altlinux.org> 1.12-alt1
- 1.12

* Thu Dec 31 2020 Anton Farygin <rider@altlinux.ru> 1.11-alt1
- 1.11

* Tue Sep 29 2020 Anton Farygin <rider@altlinux.ru> 1.10-alt1
- 1.10

* Tue Sep 08 2020 Anton Farygin <rider@altlinux.ru> 1.9.1-alt2
- devel parts moved to the ocaml-zarith-devel package

* Tue Sep 03 2019 Anton Farygin <rider@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Sun Jun 09 2019 Anton Farygin <rider@altlinux.ru> 1.8-alt1
- 1.8

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.7-alt3
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.7-alt2
- rebuilt with ocaml 4.07

* Fri May 18 2018 Anton Farygin <rider@altlinux.ru> 1.7-alt1
- new version

* Mon Jul 10 2017 Anton Farygin <rider@altlinux.ru> 1.5-alt1
- new version

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.4.1-alt2
- rebuild with ocaml 4.04.1

* Tue Apr 11 2017 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1
- fist build for ALT, based on RH spec
