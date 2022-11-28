%def_with check

%define soname 29
Summary: Command-line tools and library for transforming PDF files
Name: qpdf
Version: 11.2.0
Release: alt1
License: Apache-2.0
Group: System/Base
Url: http://qpdf.sourceforge.net/
Source0: http://downloads.sourceforge.net/sourceforge/qpdf/qpdf-%version.tar
Source1: %name.watch
Patch0: %name-%version-%release.patch

BuildRequires: zlib-devel xml-utils xsltproc docbook-style-xsl
BuildRequires: python3-module-sphinx-sphinx-build-symlink python3(sphinx_rtd_theme)
BuildRequires: pcre-devel
BuildRequires: libjpeg-devel
BuildRequires: perl-base
BuildRequires: libgnutls-devel
BuildRequires: gcc-c++
BuildRequires: cmake ctest

%if_with check
# for testing
BuildRequires: perl(Digest/SHA.pm)
BuildRequires: /usr/bin/gs
BuildRequires: /usr/bin/tiffcmp
%endif

Requires: lib%name%soname = %EVR

%package -n lib%name%soname
Summary: QPDF library for transforming PDF files
Group: System/Libraries

%package -n lib%name-devel
Summary: Development files for QPDF library
Group: Development/C
Requires: lib%name%soname = %EVR

%description
QPDF is a command-line program that does structural, content-preserving
transformations on PDF files. It could have been called something
like pdf-to-pdf. It includes support for merging and splitting PDFs
and to manipulate the list of pages in a PDF file. It is not a PDF viewer
or a program capable of converting PDF into other formats.

%description -n lib%name%soname
QPDF is a C++ library that inspect and manipulate the structure of PDF files.
It can encrypt and linearize files, expose the internals of a PDF file,
and do many other operations useful to PDF developers.

%description -n lib%name-devel
Header files and libraries necessary
for developing programs using the QPDF library.

%prep
%setup
%patch0 -p1

%build
%cmake -DBUILD_STATIC_LIBS=0 \
       -DREQUIRE_CRYPTO_GNUTLS=1 \
       -DUSE_IMPLICIT_CRYPTO=0 \
       -DSHOW_FAILED_TEST_OUTPUT=1 \
       -DINSTALL_EXAMPLES=0 \
       -DINSTALL_CMAKE_PACKAGE=0
%cmake_build

%install
%cmake_install
rm -rf %buildroot%_docdir/qpdf

%check
make test -C %_target_platform


%files
%_bindir/fix-qdf
%_bindir/qpdf
%_bindir/zlib-flate
%_mandir/man1/*

%files -n lib%name%soname
%doc README.md TODO ChangeLog LICENSE.txt
%_libdir/libqpdf*.so.%{soname}*

%files -n lib%name-devel
%doc examples/*.cc examples/*.c
%_includedir/*
%_libdir/libqpdf*.so
%_libdir/pkgconfig/libqpdf.pc

%changelog
* Mon Nov 28 2022 Anton Farygin <rider@altlinux.ru> 11.2.0-alt1
- 11.2.0

* Thu Nov 03 2022 Anton Farygin <rider@altlinux.ru> 11.1.1-alt1
- 11.1.1

* Fri Oct 07 2022 Anton Farygin <rider@altlinux.ru> 11.1.0-alt1
- 11.1.0
- removed documentation package

* Mon Jun 20 2022 Anton Farygin <rider@altlinux.ru> 10.6.3-alt2
- FTBFS: replace egrep to grep -E

* Thu Mar 24 2022 Anton Farygin <rider@altlinux.ru> 10.6.3-alt1
- 10.6.3

* Sat Feb 19 2022 Anton Farygin <rider@altlinux.ru> 10.6.2-alt1
- 10.6.2

* Sat Feb 12 2022 Anton Farygin <rider@altlinux.ru> 10.6.1-alt1
- 10.6.1

* Fri Feb 11 2022 Anton Farygin <rider@altlinux.ru> 10.6.0-alt1
- 10.6.0

* Thu Dec 23 2021 Anton Farygin <rider@altlinux.ru> 10.5.0-alt1
- 10.5.0

* Sat Nov 20 2021 Anton Farygin <rider@altlinux.ru> 10.4.0-alt1
- 10.3.2 -> 10.4.0

* Tue May 11 2021 Anton Farygin <rider@altlinux.ru> 10.3.2-alt1
- 10.3.2

* Tue Mar 16 2021 Anton Farygin <rider@altlinux.org> 10.3.1-alt1
- 10.3.1

* Sun Mar 07 2021 Anton Farygin <rider@altlinux.org> 10.3.0-alt1
- 10.3.0

* Thu Feb 25 2021 Anton Farygin <rider@altlinux.org> 10.2.0-alt1
- 10.2.0

* Mon Jan 11 2021 Anton Farygin <rider@altlinux.ru> 10.1.0-alt1
- 10.1.0 (Fixes: CVE-2021-36978)

* Mon Nov 23 2020 Anton Farygin <rider@altlinux.ru> 10.0.4-alt1
- 10.0.4

* Thu Nov 05 2020 Anton Farygin <rider@altlinux.ru> 10.0.3-alt1
- 10.0.3

* Thu Oct 29 2020 Anton Farygin <rider@altlinux.ru> 10.0.2-alt1
- 10.0.2
- enabled tests

* Mon Apr 13 2020 Anton Farygin <rider@altlinux.ru> 10.0.1-alt1
- 10.0.1

* Tue Jan 28 2020 Anton Farygin <rider@altlinux.ru> 9.1.1-alt1
- 9.1.1

* Tue Nov 19 2019 Anton Farygin <rider@altlinux.ru> 9.1.0-alt1
- 9.1.0

* Tue Oct 15 2019 Anton Farygin <rider@altlinux.ru> 9.0.2-alt1
- 9.0.2

* Sun Sep 22 2019 Anton Farygin <rider@altlinux.ru> 9.0.1-alt1
- 9.0.1

* Tue Sep 03 2019 Anton Farygin <rider@altlinux.ru> 9.0.0-alt1
- 9.0.0

* Wed May 22 2019 Anton Farygin <rider@altlinux.ru> 8.4.2-alt1
- 8.4.2

* Mon May 06 2019 Anton Farygin <rider@altlinux.ru> 8.4.1-alt1
- 8.4.1

* Wed Feb 06 2019 Anton Farygin <rider@altlinux.ru> 8.4.0-alt1
- 8.4.0

* Sat Jan 19 2019 Anton Farygin <rider@altlinux.ru> 8.3.0-alt1
- 8.3.0

* Sun Sep 02 2018 Anton Farygin <rider@altlinux.ru> 8.2.1-alt1
- 8.2.1

* Tue Jun 26 2018 Anton Farygin <rider@altlinux.ru> 8.1.0-alt1
- 8.1.0

* Sat Mar 31 2018 Anton Farygin <rider@altlinux.ru> 8.0.2-alt1
- new version

* Fri Mar 02 2018 Anton Farygin <rider@altlinux.ru> 8.0.0-alt1
- new version
- library package renamed to match the shared libs policy

* Mon Feb 26 2018 Anton Farygin <rider@altlinux.ru> 7.1.1-alt1
- new version

* Mon Jan 29 2018 Anton Farygin <rider@altlinux.ru> 7.1.0-alt1
- new version

* Mon Sep 18 2017 Anton Farygin <rider@altlinux.ru> 7.0.0-alt1
- new version

* Tue May 10 2016 Anton Farygin <rider@altlinux.ru> 6.0.0-alt1
- new version

* Thu May 28 2015 Anton Farygin <rider@altlinux.ru> 5.1.3-alt1
- new version

* Mon Jun 16 2014 Anton Farygin <rider@altlinux.ru> 5.1.2-alt1
- new version

* Wed Feb 19 2014 Anton Farygin <rider@altlinux.ru> 5.1.1-alt1
- new version

* Fri Dec 27 2013 Anton Farygin <rider@altlinux.ru> 5.1.0-alt1
- new version

* Thu Oct 24 2013 Anton Farygin <rider@altlinux.ru> 5.0.1-alt1
- new version

* Fri Oct 11 2013 Anton Farygin <rider@altlinux.ru> 5.0.0-alt1
- new version

* Tue Sep 18 2012 Anton Farygin <rider@altlinux.ru> 3.0.2-alt1
- first build for Sisyphus
