%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name: ocaml-camlidl
Version: 1.12
Release: alt2
Summary: Stub code generator and COM binding for Objective Caml
License: QPL-1.0 WITH OCaml-LGPL-linking-exception and LGPL-2.0-or-later WITH OCaml-LGPL-linking-exception
Group: Development/ML
Url: https://github.com/xavierleroy/camlidl
Source0: %name-%version.tar
# META file from Debian
Source1: META.camlidl.in

Patch2: fedora-camlidl-Allow-destdir-installs.patch
Patch3: fedora-camlidl-Pass-g-option-to-ocamlmklib.patch

BuildRequires(pre): rpm-build-ocaml >= 1.6

BuildRequires: ocaml
BuildRequires: ocaml-ocamldoc


%description
CamlIDL is a stub code generator and COM binding for Objective Caml.

CamlIDL comprises two parts:

* A stub code generator that generates the C stub code required for
  the Caml/C interface, based on an MIDL specification. (MIDL stands
  for Microsoft's Interface Description Language; it looks like C
  header files with some extra annotations, plus a notion of object
  interfaces that look like C++ classes without inheritance.)

* A (currently small) library of functions and tools to import COM
  components in Caml applications, and export Caml code as COM
  components.

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/ML

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch2 -p1
%patch3 -p1

sed -e 's|^OCAMLLIB=.*|OCAMLLIB=%{_libdir}/ocaml|' \
    -e 's|^BINDIR=.*|BINDIR=%{_bindir}|' \
    -e 's|^CFLAGS=.*|CFLAGS=%{optflags}|' \
%ifarch %ocaml_native_arch
    -e 's|^OCAMLC=.*|OCAMLC=ocamlc.opt -g -bin-annot|' \
    -e 's|^OCAMLOPT=.*|OCAMLOPT=ocamlopt.opt -g|' \
%else
    -e 's|^OCAMLC=.*|OCAMLC=ocamlc -g -bin-annot|' \
%endif
    < config/Makefile.unix \
    > config/Makefile

cp %SOURCE1 .

%build
make all

%install
mkdir -p %buildroot%_libdir/ocaml/caml
mkdir -p %buildroot%_libdir/ocaml/camlidl
mkdir -p %buildroot%_libdir/ocaml/stublibs
mkdir -p %buildroot%_bindir

sed 's/@VERSION@/%version/' < %SOURCE1 > %buildroot%_ocamldir/camlidl/META

%makeinstall_std
%__install -m644 lib/*.cm* %buildroot%_ocamldir/

%ocaml_find_files

%files -f ocaml-files.runtime
%doc LICENSE
%_libdir/ocaml/stublibs/dllcamlidl.so
%_bindir/camlidl

%files devel -f ocaml-files.devel
%doc LICENSE README Changes tests
%_libdir/ocaml/caml/*.h

%changelog
* Sat Nov 18 2023 Anton Farygin <rider@altlinux.ru> 1.12-alt2
- fixed build for bytecode ocaml

* Fri Nov 10 2023 Anton Farygin <rider@altlinux.ru> 1.12-alt1
- 1.12

* Mon Dec 14 2020 Anton Farygin <rider@altlinux.ru> 1.09-alt2
- enable relaxed mode for textrel check

* Mon Jun 15 2020 Anton Farygin <rider@altlinux.ru> 1.09-alt1
- 1.09

* Mon Jul 01 2019 Anton Farygin <rider@altlinux.ru> 1.07-alt1
- 1.07

* Mon Oct 29 2018 Anton Farygin <rider@altlinux.ru> 1.06-alt1
- 1.06

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 1.05-alt5
- rebuilt with ocaml-4.07.1

* Wed Sep 05 2018 Anton Farygin <rider@altlinux.ru> 1.05-alt4
- rebuilt with ocaml 4.07

* Sat May 19 2018 Anton Farygin <rider@altlinux.ru> 1.05-alt3
- rebuilt for ocaml 4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 1.05-alt2
- rebuild with ocaml 4.04.2

* Mon Feb 13 2017 Anton Farygin <rider@altlinux.ru> 1.05-alt1
- first build for ALT
