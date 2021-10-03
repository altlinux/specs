%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Name: ocaml-libvirt
Version: 0.6.1.5
Release: alt2
Summary: OCaml binding for libvirt
Group: System/Libraries

License: LGPLv2+
Url: http://libvirt.org/ocaml/

Source: http://libvirt.org/sources/ocaml/%name-%version.tar
Patch0: 0001-block_peek-memory_peek-Use-bytes-for-return-buffer.patch
Patch1: 0001-Make-const-the-return-value-of-caml_named_value.patch
Patch2: 0002-String_val-returns-const-char-in-OCaml-4.10.patch
Patch3: 0003-Don-t-try-to-memcpy-into-a-String_val.patch

BuildRequires: ocaml >= 3.10.0
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-findlib

BuildRequires: libvirt-devel >= 0.2.1
BuildRequires: perl-devel
BuildRequires: gawk

%description
OCaml binding for libvirt.

%package devel
Summary: Development files for %name
Group: System/Libraries
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and signature files for
developing applications that use %name.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%configure
make all doc
make opt

%install
# These rules work if the library uses 'ocamlfind install' to install itself.
export DESTDIR=%buildroot
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml
mkdir -p $OCAMLFIND_DESTDIR/stublibs
make install-opt

%files
%doc COPYING.LIB README ChangeLog
%_libdir/ocaml/libvirt
%exclude %_libdir/ocaml/libvirt/*.a
%exclude %_libdir/ocaml/libvirt/*.cmxa
%exclude %_libdir/ocaml/libvirt/*.cmx
%exclude %_libdir/ocaml/libvirt/*.mli
%_libdir/ocaml/stublibs/*.so
%_libdir/ocaml/stublibs/*.so.owner

%files devel
%doc COPYING.LIB README TODO.libvirt ChangeLog html/*
%_libdir/ocaml/libvirt/*.a
%_libdir/ocaml/libvirt/*.cmxa
%_libdir/ocaml/libvirt/*.cmx
%_libdir/ocaml/libvirt/*.mli

%changelog
* Sun Oct 03 2021 Anton Farygin <rider@altlinux.ru> 0.6.1.5-alt2
- fixed build with LTO

* Wed Feb 26 2020 Anton Farygin <rider@altlinux.ru> 0.6.1.5-alt1
- 0.6.1.5

* Thu Aug 01 2019 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt8
- rebuilt with ocaml-4.08

* Thu Oct 18 2018 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt7
- rebuilt with ocaml-4.07.1

* Thu Sep 06 2018 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt6
- rebuilt with ocaml 4.07

* Sun May 20 2018 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt5
- rebuilt for ocaml 4.06.1

* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt4
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt3
- rebuild with ocaml 4.04.1

* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt2
- rebuild with new rpm-build-ocaml
- moved outsite from site-lib dir

* Sun Apr 09 2017 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt2
- rebuild with ocaml-4.04

* Tue Nov 22 2016 Lenar Shakirov <snejok@altlinux.ru> 0.6.1.4-alt1
- Initial build for ALT (based on 0.6.1.4-13.fc26.src)

