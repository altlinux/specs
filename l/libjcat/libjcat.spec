%define soname 1
Summary: Library for reading Jcat files
Name: libjcat
Version: 0.2.2
Release: alt1
License: LGPLv2+
Url: https://github.com/hughsie/libjcat
Source0: %name-%version.tar
Patch0: %name-%version-%release.patch
Group: System/Libraries
BuildRequires: gtk-doc
BuildRequires: meson
BuildRequires: gobject-introspection-devel
BuildRequires: glib2-devel
BuildRequires: libjson-glib-devel
BuildRequires: libjson-glib-gir-devel
BuildRequires: libgnutls-devel
BuildRequires: gnutls-utils
BuildRequires: libnettle-devel
BuildRequires: libgpgme-devel
BuildRequires: vala vala-tools
BuildRequires: /proc

%description
This library allows reading and writing gzip-compressed JSON catalog files,
which can be used to store GPG, PKCS-7 and SHA-256 checksums for each file.

This provides equivalent functionality to the catalog files supported in
Microsoft Windows.

%package devel
Group: Development/C
Summary: Development package for %name
Requires: %name%{?_isa} = %version-%release

%description devel
Files for development with %name.

%package tests
Group: Development/C
Summary: Files for installed tests

%description tests
Executable and data files for installed tests.

%prep
%setup
%patch0 -p1

%build
%meson \
    -Dgtkdoc=true \
    -Dman=true \
    -Dtests=true

%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md
%_bindir/jcat-tool
%_datadir/man/man1/*.1*
%dir %_libdir/girepository-1.0
%_libdir/girepository-1.0/*.typelib
%_libdir/libjcat.so.%{soname}
%_libdir/libjcat.so.%{soname}.*

%files devel
%dir %_datadir/gir-1.0
%_datadir/gir-1.0/*.gir
%dir %_datadir/gtk-doc
%dir %_datadir/gtk-doc/html
%_datadir/gtk-doc/html/libjcat
%_includedir/libjcat-1
%_libdir/libjcat.so
%_libdir/pkgconfig/jcat.pc
%_datadir/vala/vapi/jcat.deps
%_datadir/vala/vapi/jcat.vapi

%files tests
%doc README.md
%_libexecdir/installed-tests/libjcat/*
%_datadir/installed-tests/libjcat/*
%dir %_datadir/installed-tests/libjcat

%changelog
* Tue Oct 15 2024 Anton Farygin <rider@altlinux.ru> 0.2.2-alt1
- 0.2.1 -> 0.2.2

* Tue Apr 09 2024 Anton Farygin <rider@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Sun Jun 25 2023 Anton Farygin <rider@altlinux.ru> 0.1.14-alt1
- 0.1.14

* Thu Mar 30 2023 Anton Farygin <rider@altlinux.ru> 0.1.13-alt1
- 0.1.13

* Mon Oct 03 2022 Anton Farygin <rider@altlinux.ru> 0.1.12-alt1
- 0.1.12

* Mon Apr 11 2022 Anton Farygin <rider@altlinux.ru> 0.1.11-alt2
- libjcat-tests: add  data for ed25519

* Mon Mar 28 2022 Anton Farygin <rider@altlinux.ru> 0.1.11-alt1
- 0.1.11

* Sat Feb 19 2022 Anton Farygin <rider@altlinux.ru> 0.1.10-alt1
- 0.1.10

* Mon Nov 29 2021 Anton Farygin <rider@altlinux.ru> 0.1.9-alt1
- 0.1.9

* Thu May 27 2021 Anton Farygin <rider@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Wed May 12 2021 Anton Farygin <rider@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Thu Feb 25 2021 Anton Farygin <rider@altlinux.org> 0.1.6-alt1
- 0.1.6

* Mon Jan 11 2021 Anton Farygin <rider@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Thu Nov 05 2020 Anton Farygin <rider@altlinux.ru> 0.1.4-alt1
- 0.1.4

* Mon Jul 06 2020 Anton Farygin <rider@altlinux.ru> 0.1.3-alt2
- added patch from upstream to solve problem with lfvs signature,
  upstream issue #2223 (closes: 38672)

* Fri Jun 26 2020 Anton Farygin <rider@altlinux.ru> 0.1.3-alt1
- 0.1.3

* Fri May 08 2020 Ivan Razzhivin <underwit@altlinux.org> 0.1.2-alt2
- fix build man pages

* Wed May 06 2020 Anton Farygin <rider@altlinux.ru> 0.1.2-alt1
- 0.1.2

* Thu Apr 16 2020 Anton Farygin <rider@altlinux.ru> 0.1.1-alt1
- first build for ALT, based on specfile from RH

