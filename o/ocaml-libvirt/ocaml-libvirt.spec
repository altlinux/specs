Name: ocaml-libvirt
Version: 0.6.1.4
Release: alt4%ubt
Summary: OCaml binding for libvirt
Group: System/Libraries

License: LGPLv2+
Url: http://libvirt.org/ocaml/
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: http://libvirt.org/sources/ocaml/%name-%version.tar

# Upstream patch to fix int types.
Patch1: 0001-Use-C99-standard-int64_t-instead-of-OCaml-defined-an.patch

# Upstream patch to add virDomainCreateXML binding.
Patch2: 0001-Add-a-binding-for-virDomainCreateXML.patch

# Upstream patches to fix error handling.
Patch3: 0001-Suppress-errors-to-stderr-and-use-thread-local-virEr.patch
Patch4: 0002-Don-t-bother-checking-return-from-virInitialize.patch

# Upstream patch to remove unused function.
Patch5: 0001-Remove-unused-not_supported-function.patch

BuildRequires: ocaml >= 3.10.0
BuildRequires: ocaml-ocamldoc
BuildRequires: ocaml-findlib
BuildRequires(pre): rpm-build-ubt

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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
* Tue Jul 11 2017 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt4%ubt
- rebuild with ocaml 4.04.2

* Wed May 03 2017 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt3%ubt
- rebuild with ocaml 4.04.1

* Wed Apr 19 2017 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt2%ubt
- rebuild with new rpm-build-ocaml
- moved outsite from site-lib dir

* Sun Apr 09 2017 Anton Farygin <rider@altlinux.ru> 0.6.1.4-alt2
- rebuild with ocaml-4.04

* Tue Nov 22 2016 Lenar Shakirov <snejok@altlinux.ru> 0.6.1.4-alt1
- Initial build for ALT (based on 0.6.1.4-13.fc26.src)

