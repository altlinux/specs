Name: ocaml-ctypes
Version: 0.20.0
Release: alt1
Summary: Combinators for binding to C libraries without writing any C

Group: Development/ML
License: MIT
Url: https://github.com/ocamllabs/ocaml-ctypes
Source: %name-%version.tar

Patch1: make-ocamlfind-ldconf.patch
Patch2: make-install-mls.patch

BuildRequires: ocaml-findlib ocaml-integers-devel ocaml-bigarray-compat-devel
BuildRequires: libffi-devel
Requires: rpm-build-ocaml >= 1.1
BuildPreReq: rpm-build-ocaml >= 1.1

%description
ctypes is a library for binding to C libraries using pure OCaml. The primary
aim is to make writing C extensions as straightforward as possible.

%package devel
Summary: Development files for %name
Group: Development/ML
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
%make

%install
mkdir -p %buildroot/%_libdir/ocaml
cp %_libdir/ocaml/ld.conf ld.conf
chmod +x ld.conf
%makeinstall_std OCAMLFIND_LDCONF=ld.conf OCAMLFIND_DESTDIR=%buildroot/%_libdir/ocaml
mkdir -p %buildroot/%_libdir/ocaml/stublibs
mv %buildroot/%_libdir/ocaml/ctypes/dll*.so %buildroot/%_libdir/ocaml/stublibs

%files
%doc README.md
%dir %_libdir/ocaml/ctypes
%_libdir/ocaml/ctypes*/META
%_libdir/ocaml/ctypes*/*.cma
%_libdir/ocaml/ctypes*/*.cmi
%_libdir/ocaml/ctypes*/*.cmxs
%_libdir/ocaml/stublibs/*.so

%files devel
%_libdir/ocaml/ctypes*/*.a
%_libdir/ocaml/ctypes*/*.cmt*
%_libdir/ocaml/ctypes*/*.cmxa
%_libdir/ocaml/ctypes*/*.cmx
%_libdir/ocaml/ctypes*/*.mli
%_libdir/ocaml/ctypes*/*.ml
%_libdir/ocaml/ctypes*/*.h

%changelog
* Mon Jan 03 2022 Anton Farygin <rider@altlinux.ru> 0.20.0-alt1
- 0.20.0

* Sat Oct 16 2021 Anton Farygin <rider@altlinux.ru> 0.19.1-alt1
- 0.19.1

* Sun Mar 28 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.18.0-alt1
- new version 0.18.0

* Wed Jul 08 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.17.1-alt1
- Initial build for Sisyphus
