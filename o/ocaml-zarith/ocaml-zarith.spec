# on i586: ./usr/lib/ocaml/stublibs/dllzarith.so 
%set_verify_elf_method textrel=relaxed

%global pkgname zarith
%define ocamlsitelib %_libdir/ocaml
%define ocamlstublib %_libdir/ocaml/stublibs/

Name: ocaml-%pkgname
Version: 1.4.1
Release: alt2%ubt
Summary: OCaml interface to GMP
Group: Development/ML
# The license has a static linking exception
License: LGPLv2 with exceptions
Url: https://github.com/ocaml/Zarith
Source0: %name-%version.tar

BuildRequires: libgmp-devel
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
BuildRequires(pre): rpm-build-ubt

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
mkdir -p %buildroot%ocamlsitelib
make install INSTALLDIR=%buildroot%_libdir/ocaml

%files
%doc Changes
%ocamlsitelib/%pkgname
%exclude %ocamlsitelib/%pkgname/*.mli
%exclude %ocamlsitelib/%pkgname/*.h
%ocamlstublib/*.so
%ocamlstublib/*.so.owner

%files devel
%doc README html
%ocamlsitelib/%pkgname/*.mli
%ocamlsitelib/%pkgname/*.h

%changelog
* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 1.4.1-alt2%ubt
- rebuild with ocaml 4.04.1

* Tue Apr 11 2017 Anton Farygin <rider@altlinux.ru> 1.4.1-alt1%ubt
- fist build for ALT, based on RH spec
