# SPDX-License-Identifier: GPL-2.0-only
%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%define sover 0
%def_enable ocaml

Name: libnbd
Version: 1.19.11
Release: alt1
Summary: NBD client library in userspace
License: LGPL-2.1-or-later
Group: Networking/File transfer
Url: https://gitlab.com/nbdkit/libnbd

Source: %name-%version.tar
BuildRequires: bash-completion
BuildRequires: gcc-c++
BuildRequires: hardlink
BuildRequires: libfuse3-devel
BuildRequires: libgnutls-devel
BuildRequires: liburing-devel
BuildRequires: libxml2-devel
BuildRequires: perl-podlators
%if_enabled ocaml
BuildRequires(pre): rpm-build-ocaml
BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: ocaml-ocamldoc
%endif

%description
%summary.

%package -n %name%sover
Summary: %name system library
Group: System/Libraries

%description -n %name%sover
%summary.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name%sover = %EVR

%description devel
%summary.

%package -n ocaml-%name
Summary: OCaml language bindings for %name
Group: Development/Other
Provides: ocaml-nbd = %EVR
Requires: %name%sover = %EVR

%description -n ocaml-%name
This package contains OCaml language bindings for %name.

%package -n ocaml-%name-devel
Summary: OCaml language development package for %name
Group: Development/Other
Provides: ocaml-nbd-devel = %EVR
Requires: ocaml-%name = %EVR

%description -n ocaml-%name-devel
This package contains OCaml language development package for
%name. Install this if you want to compile OCaml software which
uses %name.

%prep
%setup

%build
%autoreconf
%configure \
    --disable-static \
    --disable-golang \
    %{subst_enable ocaml} \
    --disable-python \
    %nil
%make_build

%install
%makeinstall_std
hardlink -v %buildroot

# For python script we don't build (yet).
rm %buildroot%_datadir/bash-completion/completions/nbdsh

%check
%make_build check
# qemu-nbd tests require nbdsh built, nbdkit will cause cyclic
# dependence, so be careful.

%files
%_bindir/nbd*
%_man1dir/nbd*.1*
%_datadir/bash-completion/completions/*

%files -n %name%sover
%_libdir/libnbd.so.%sover
%_libdir/libnbd.so.%sover.*

%files devel
%_includedir/libnbd.h
%_libdir/libnbd.so
%_pkgconfigdir/libnbd.pc
%_man1dir/libnbd-*.1*
%_man3dir/*.3*
%exclude %_man3dir/libnbd-ocaml.3*
%exclude %_man3dir/NBD*

%if_enabled ocaml
%files -n ocaml-%name
%_libdir/ocaml/nbd
%exclude %_libdir/ocaml/nbd/*.a
%ifarch %ocaml_native_arch
%exclude %_libdir/ocaml/nbd/*.cmxa
%exclude %_libdir/ocaml/nbd/*.cmx
%endif
%exclude %_libdir/ocaml/nbd/*.mli
%_libdir/ocaml/stublibs/*.so
%_libdir/ocaml/stublibs/*.so.owner

%files -n ocaml-%name-devel
%doc ocaml/examples/*.ml
%_libdir/ocaml/nbd/*.a
%ifarch %ocaml_native_arch
%_libdir/ocaml/nbd/*.cmxa
%_libdir/ocaml/nbd/*.cmx
%endif
%_libdir/ocaml/nbd/*.mli
%_man3dir/libnbd-ocaml.3*
%_man3dir/NBD*
%endif

%changelog
* Fri May 03 2024 Vitaly Chikunov <vt@altlinux.org> 1.19.11-alt1
- Update to v1.19.11 (2024-03-25).

* Thu Mar 07 2024 Vitaly Chikunov <vt@altlinux.org> 1.19.8-alt1
- Update to v1.19.8 (2024-03-04).

* Sun Jan 21 2024 Vitaly Chikunov <vt@altlinux.org> 1.19.4-alt1
- Update to v1.19.4 (2024-01-16).

* Fri Jan 12 2024 Alexey Shabalin <shaba@altlinux.org> 1.19.3-alt2
- Build with ocaml support.

* Sun Dec 31 2023 Vitaly Chikunov <vt@altlinux.org> 1.19.3-alt1
- Update to v1.19.3 (2023-12-19).

* Thu Oct 26 2023 Vitaly Chikunov <vt@altlinux.org> 1.19.1-alt1
- Update to v1.19.1 (2023-10-23).

* Wed Sep 27 2023 Vitaly Chikunov <vt@altlinux.org> 1.18.0-alt1
- Update to v1.18.0 (2023-09-27). (Fixes: CVE-2023-5215).

* Sun Sep 10 2023 Vitaly Chikunov <vt@altlinux.org> 1.17.5-alt1
- Update to v1.17.5 (2023-09-08).

* Mon Aug 07 2023 Vitaly Chikunov <vt@altlinux.org> 1.17.3-alt1
- Update to v1.17.3 (2023-08-04).

* Sun Jul 23 2023 Vitaly Chikunov <vt@altlinux.org> 1.17.2-alt1
- First import v1.17.2 (2023-07-14).
