%global glib2_version 2.58.1
%define soversion 2
Summary: Library for querying compressed XML metadata
Name: libxmlb
Version: 0.3.11
Release: alt1
License: LGPLv2+
Group: System/Libraries
Url: https://github.com/hughsie/libxmlb
Source0: %name-%version.tar
BuildRequires: glib2-devel >= %glib2_version
BuildRequires: gtk-doc
BuildRequires: libstemmer-devel
BuildRequires: meson
BuildRequires: liblzma-devel
BuildRequires: libzstd-devel
BuildRequires: gobject-introspection-devel

# needed for the self tests
BuildRequires: shared-mime-info

Requires: glib2 >= %glib2_version
Requires: shared-mime-info

%description
XML is slow to parse and strings inside the document cannot be memory mapped as
they do not have a trailing NUL char. The libxmlb library takes XML source, and
converts it to a structured binary representation with a deduplicated string
table -- where the strings have the NULs included.

This allows an application to mmap the binary XML file, do an XPath query and
return some strings without actually parsing the entire document. This is all
done using (almost) zero allocations and no actual copying of the binary data.

%package -n libxmlb%soversion
Summary: Library for querying compressed XML metadata
Group: System/Libraries
Requires: %name-common = %EVR
Obsoletes: libxmlb1 <= 0.1.15-alt1

%description -n libxmlb%soversion
XML is slow to parse and strings inside the document cannot be memory mapped as
they do not have a trailing NUL char. The libxmlb library takes XML source, and
converts it to a structured binary representation with a deduplicated string
table -- where the strings have the NULs included.

%package common
Summary: Common files for %name. 
Group: System/Libraries

%description common
Common files for %name.

%package -n libxmlb-devel
Summary: Development package for %name
Group: Development/C
Requires: %name%soversion = %EVR

%description -n libxmlb-devel
Files for development with %name.

%prep
%setup

%build
%meson \
    -Dgtkdoc=true \
    -Dtests=true

%meson_build

%check
%meson_test

%install
%meson_install

%files common
%doc README.md LICENSE
%_bindir/xb-tool
%_man1dir/*.1*
%dir %_libdir/girepository-1.0
%_libdir/girepository-1.0/*.typelib

%files -n libxmlb%soversion
%_libdir/libxmlb.so.%{soversion}*

%files devel
%dir %_datadir/gir-1.0
%_datadir/gir-1.0/*.gir
%dir %_datadir/gtk-doc
%dir %_datadir/gtk-doc/html
%_datadir/gtk-doc/html/libxmlb
%_includedir/libxmlb-2
%_libdir/libxmlb.so
%_libdir/pkgconfig/xmlb.pc

%changelog
* Mon Feb 27 2023 Anton Farygin <rider@altlinux.ru> 0.3.11-alt1
- 0.3.10 -> 0.3.11

* Wed Oct 05 2022 Anton Farygin <rider@altlinux.ru> 0.3.10-alt1
- 0.3.9 -> 0.3.10

* Sat Jun 04 2022 Anton Farygin <rider@altlinux.ru> 0.3.9-alt1
- 0.3.8 -> 0.3.9

* Thu Mar 24 2022 Anton Farygin <rider@altlinux.ru> 0.3.8-alt1
- 0.3.7 -> 0.3.8

* Sun Feb 20 2022 Anton Farygin <rider@altlinux.ru> 0.3.7-alt1
- 0.3.6 -> 0.3.7

* Tue Dec 07 2021 Anton Farygin <rider@altlinux.ru> 0.3.6-alt1
- 0.3.5 -> 0.3.6

* Sun Dec 05 2021 Anton Farygin <rider@altlinux.ru> 0.3.5-alt1
- 0.3.3 -> 0.3.5

* Mon Oct 25 2021 Anton Farygin <rider@altlinux.ru> 0.3.3-alt1
- 0.3.3

* Thu Jun 10 2021 Anton Farygin <rider@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Tue May 11 2021 Anton Farygin <rider@altlinux.ru> 0.3.1-alt1
- 0.3.1

* Thu Mar 18 2021 Anton Farygin <rider@altlinux.org> 0.3.0-alt1
- 0.3.0

* Mon Oct 12 2020 Anton Farygin <rider@altlinux.ru> 0.2.1-alt1
- 0.2.1

* Thu Sep 03 2020 Anton Farygin <rider@altlinux.ru> 0.2.0-alt2
- move common files to %name-common package (closes: #38873)
- rename source package to libxmlb

* Wed Sep 02 2020 Anton Farygin <rider@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Thu Mar 12 2020 Anton Farygin <rider@altlinux.ru> 0.1.15-alt1
- 0.1.15

* Tue Jan 14 2020 Anton Farygin <rider@altlinux.ru> 0.1.14-alt1
- 0.1.14

* Fri Oct 25 2019 Anton Farygin <rider@altlinux.ru> 0.1.13-alt1
- 0.1.13

* Thu Oct 03 2019 Anton Farygin <rider@altlinux.ru> 0.1.12-alt1
- 0.1.12

* Mon Jul 22 2019 Anton Farygin <rider@altlinux.ru> 0.1.11-alt1
- 0.1.11

* Tue Jun 04 2019 Anton Farygin <rider@altlinux.ru> 0.1.10-alt1
- 0.1.10

* Thu Apr 04 2019 Anton Farygin <rider@altlinux.ru> 0.1.8-alt1
- 0.1.8

* Thu Mar 14 2019 Anton Farygin <rider@altlinux.ru> 0.1.7-alt1
- 0.1.7

* Tue Jan 22 2019 Anton Farygin <rider@altlinux.ru> 0.1.6-alt1
- 0.1.6

* Mon Dec 03 2018 Anton Farygin <rider@altlinux.ru> 0.1.5-alt1
- 0.1.5

* Mon Nov 12 2018 Anton Farygin <rider@altlinux.ru> 0.1.4-alt1
- first build for ALT

