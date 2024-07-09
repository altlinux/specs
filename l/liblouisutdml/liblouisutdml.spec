%define _unpackaged_files_terminate_build 1

%define sover 9

Name: liblouisutdml
Version: 2.12.0
Release: alt1
Summary: Braille transcription library for UTDML documents
License: LGPLv3+
Group: Accessibility
Url: http://liblouis.org
Source: %name-%version.tar
# upstream patch to fix failing testsuite
# https://github.com/liblouis/liblouisutdml/pull/101/commits/10254fc8216fba30e03c2bb3650d1699bfcb3716
Patch1: %name-%version-failing-testsuite.patch

BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: help2man
BuildRequires: liblouis-devel  
BuildRequires: libxml2-devel
BuildRequires: texinfo
BuildRequires: texlive 
BuildRequires: texlive-collection-basic
BuildRequires: texlive-dist
BuildRequires: make

%description
This is a library intended to provide complete braille transcription services
for UTDML (Unified Tactile Document Markup Language) documents. It translates
into appropriate braille codes and formats according to its style sheet and
the specifications in the document.

liblouisutdml is the successor of liblouisxml.

%package -n %name%sover
Group: Accessibility
Summary: Lib files for %name
Provides: %name = %EVR

%description -n %name%sover
Lib files for %name

%package devel
Group: Development/C++
Summary: Development files for %name
Requires: %name = %EVR

%description devel
%name is a braille transcription library for UTDML (Unifiedaa Tactile
Document Markup Language) documents. The %name-devel package contains
libraries and header files for developing applications that use %name.

%package utils
Group: Accessibility
Summary: Utilities that convert various file formats into braille
License: GPLv3+
Requires: antiword
Requires: poppler-utils
Requires: %name = %EVR

%description utils
This package provides the command-line utility file2brl that translates XML
or text files into embosser-ready braille files.

%package doc
Group: Accessibility
Summary: Documentation of the library and the corresponding utilities
BuildArch: noarch
Requires: %name = %EVR

%description doc
%name is a braille transcription library for UTDML (Unified Tactile
Document Markup Language) documents. This package contains the user and
developer documentation of the library and the command-line utilities
provided by %name-utils.

%prep
%setup

%patch1 -p1

%build
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
%doc AUTHORS ChangeLog README NEWS
%doc COPYING.LIB
%_libdir/%name.so.%sover
%_libdir/%name.so.%sover.*
%_datadir/%name/

%files devel
%_includedir/%name/
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%files utils
%doc COPYING
%_bindir/file2brl
%_man1dir/file2brl.1*

%files doc
%doc doc/copyright-notice
%doc doc/%name.{html,txt,pdf}
%_infodir/%name.info.*

%changelog
* Wed May 29 2024 Artem Semenov <savoptik@altlinux.org> 2.12.0-alt1
- Initial build for Sisyphus (ALT bug: 50364)
