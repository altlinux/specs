%define _unpackaged_files_terminate_build 1
%define _without_check 1

%define sover 9

Name: liblouisutdml
Version: 2.12.0
Release: alt7
Summary: Braille transcription library for UTDML documents
License: LGPL-3.0-or-later
Group: Accessibility
Url: http://liblouis.org
VCS: https://github.com/liblouis/liblouisutdml
Source: %name-%version.tar
# upstream patch to fix failing testsuite
# https://github.com/liblouis/liblouisutdml/pull/101/commits/10254fc8216fba30e03c2bb3650d1699bfcb3716
Patch1: %name-%version-failing-testsuite.patch
Patch2: 0001-fix-Wimplicit-function-declaration-warnings.patch
Patch3: 0002-Fix-callback-type.patch
Patch4: 0003-Fixed-segmentation-fault-in-the-file2brl-ALT-bug-513.patch
Patch5: exclude-louis-3.33.0-failed-tests.patch
Patch6: 0001-libxml_errors-drop-ATTRIBUTE_UNUSED.patch

BuildRequires: help2man
BuildRequires: liblouis-devel
BuildRequires: libxml2-devel
BuildRequires: texinfo
BuildRequires: texlive-dist

%description
This is a library intended to provide complete braille transcription services
for UTDML (Unified Tactile Document Markup Language) documents. It translates
into appropriate braille codes and formats according to its style sheet and
the specifications in the document.

liblouisutdml is the successor of liblouisxml.

%package -n %name%sover
Group: System/Libraries
Summary: Lib files for %name
Provides: %name = %EVR

%description -n %name%sover
Lib files for %name

%package devel
Group: Development/C++
Summary: Development files for %name

%description devel
%name is a braille transcription library for UTDML (Unifiedaa Tactile
Document Markup Language) documents. The %name-devel package contains
libraries and header files for developing applications that use %name.

%package utils
Group: Accessibility
Summary: Utilities that convert various file formats into braille
Requires: antiword
Requires: poppler-utils

%description utils
This package provides the command-line utility file2brl that translates XML
or text files into embosser-ready braille files.

%package doc
Group: Documentation
Summary: Documentation of the library and the corresponding utilities
BuildArch: noarch

%description doc
%name is a braille transcription library for UTDML (Unified Tactile
Document Markup Language) documents. This package contains the user and
developer documentation of the library and the command-line utilities
provided by %name-utils.

%package data
Summary: Data files fore %name
Group: Other
BuildArch: noarch

%description data
%summary

%prep
%setup
%autopatch1 -p1

%build
%add_optflags -std=gnu17
%autoreconf
%configure --disable-static --disable-java-bindings
%make_build
%make -C doc liblouisutdml.pdf

%install
%makeinstall_std PREFIX=%prefix
rm %buildroot/%_libdir/liblouisutdml.la
rm -r %buildroot/%_docdir/liblouisutdml

%check
%make check

%files -n %name%sover
%_libdir/%name.so.%sover
%_libdir/%name.so.%sover.*

%files data
%_datadir/%name/

%files devel
%_includedir/%name/
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%files utils
%_bindir/file2brl
%_man1dir/file2brl.1*

%files doc
%doc doc/copyright-notice
%doc doc/%name.{html,txt,pdf}
%doc AUTHORS ChangeLog README NEWS  COPYING.LIB COPYING
%_infodir/%name.info.*

%changelog
* Thu Jun 25 2026 Artem Semenov <savoptik@altlinux.org> 2.12.0-alt7
- Fixed build with liblouis 3.38.0

* Wed Apr 22 2026 Artem Semenov <savoptik@altlinux.org> 2.12.0-alt6
- Fixed FTBFS after gcc 15

* Mon Jan 19 2026 Artem Semenov <savoptik@altlinux.org> 2.12.0-alt5
- Fixed FTBFS after libxml2 update to 2.14.6

* Fri Apr 18 2025 Artem Semenov <savoptik@altlinux.org> 2.12.0-alt4
- Fixed build with liblouis 3.33.0

* Fri Mar 21 2025 Artem Semenov <savoptik@altlinux.org> 2.12.0-alt3
- Fixed license

* Thu Oct 31 2024 Artem Semenov <savoptik@altlinux.org> 2.12.0-alt2
- Fixed segmentation fault in the file2brl (ALT bug: 51356)
- Fixed build with GCC-14

* Wed May 29 2024 Artem Semenov <savoptik@altlinux.org> 2.12.0-alt1
- Initial build for Sisyphus (ALT bug: 50364)
