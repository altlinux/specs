Name: ocaml-libvirt
Version: 0.6.1.4
Release: alt1
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
BuildRequires: ocamldoc
BuildRequires: findlib

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
export OCAMLFIND_DESTDIR=%buildroot%_libdir/ocaml/site-lib
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install-opt

%files
%doc COPYING.LIB README ChangeLog
%_libdir/ocaml/site-lib/libvirt
%exclude %_libdir/ocaml/site-lib/libvirt/*.a
%exclude %_libdir/ocaml/site-lib/libvirt/*.cmxa
%exclude %_libdir/ocaml/site-lib/libvirt/*.cmx
%exclude %_libdir/ocaml/site-lib/libvirt/*.mli
%_libdir/ocaml/site-lib/stublibs/*.so
%_libdir/ocaml/site-lib/stublibs/*.so.owner

%files devel
%doc COPYING.LIB README TODO.libvirt ChangeLog html/*
%_libdir/ocaml/site-lib/libvirt/*.a
%_libdir/ocaml/site-lib/libvirt/*.cmxa
%_libdir/ocaml/site-lib/libvirt/*.cmx
%_libdir/ocaml/site-lib/libvirt/*.mli

%changelog
* Tue Nov 22 2016 Lenar Shakirov <snejok@altlinux.ru> 0.6.1.4-alt1
- Initial build for ALT (based on 0.6.1.4-13.fc26.src)

