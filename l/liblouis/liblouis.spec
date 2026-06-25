%define _unpackaged_files_terminate_build 1

%define sover 20

Name: liblouis
Version: 3.38.0
Release: alt1
Summary: Braille translation and back-translation library

# LGPL-2.1-or-later: the project as a whole
# LGPL-2.0-or-later: parts of gnulib
# - gnulib/_Noreturn.h
# - gnulib/arg-nonnull.h
# - gnulib/c++defs.h
# - gnulib/warn-on-use.h
License: LGPL-2.1-or-later AND LGPL-2.0-or-later
Group: Accessibility
Url: http://liblouis.org
VCS: https://github.com/liblouis/liblouis

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: hardlink
BuildRequires: help2man
BuildRequires: libyaml-devel
BuildRequires: texinfo
BuildRequires: texlive
BuildRequires: texlive-collection-basic
BuildRequires: texlive-dist
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(pytest)

%description
Liblouis is an open-source braille translator and back-translator named in
honor of Louis Braille. It features support for computer and literary braille,
supports contracted and uncontracted translation for many languages and has
support for hyphenation. New languages can easily be added through tables that
support a rule- or dictionary based approach. Liblouis also supports math
braille (Nemeth and Marburg).

Liblouis has features to support screen-reading programs. This has led to its
use in two open-source screen readers, NVDA and Orca. It is also used in some
commercial assistive technology applications for example by ViewPlus.

Liblouis is based on the translation routines in the BRLTTY screen reader for
Linux. It has, however, gone far beyond these routines.

%package -n %name%sover
Group: Accessibility
License: LGPL-2.1-or-later AND LGPL-2.0-or-later
Summary: Lib files for %name
Provides: %name = %EVR

%description -n %name%sover
Lib files for %name

%package devel
Summary: Development files for %name
Group: Development/C++
License: LGPL-2.1-or-later

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package devel-doc
Summary: Development files for %name
Group: Documentation
License: LGPL-2.1-or-later
BuildArch: noarch

%description devel-doc
%summary

%package data
Summary: Data tables
Group: Accessibility
# LGPL-2.1-or-later: most of the tables
# LGPL-3.0-or-later:
# - tables/Es-Es-G0.utb
# - tables/et-g0.utb
# - tables/is-chardefs6.cti
# - tables/is-chardefs8.cti
# - tables/pt-pt-g2.ctb
# - tables/sr-chardefs.cti
# - tables/sr-g1.ctb
License: LGPL-2.1-or-later AND LGPL-3.0-or-later
BuildArch: noarch
Provides: %name-tables = %EVR
Obsoletes: %name-tables < %EVR

%description data
Data tables for liblouis, containing attributes and dot patterns.

%package utils
Summary: Command-line utilities to test %name
Group: Accessibility
# GPL-3.0-or-later: the source code in tools
# LGPL-2.0-or-later AND LGPL-2.1-or-later: tools/gnulib
# LGPL-3.0-or-later: tools/gnulib/version-etc.{c,h}
# LGPL-3.0-or-later OR GPL-2.0-or-later:
# - tools/gnulib/unistr/u16-mbtoucr.c
# - tools/gnulib/unistr/u16-to-u8.c
License: GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later AND (LGPL-3.0-or-later OR GPL-2.0-or-later)

%description utils
Six test programs are provided as part of the liblouis package. They
are intended for testing liblouis and for debugging tables. None of
them is suitable for braille transcription.

%package utils-doc
Summary: Doc fore command-line utilities to test %name
Group: Documentation
# GPL-3.0-or-later: the source code in tools
# LGPL-2.0-or-later AND LGPL-2.1-or-later: tools/gnulib
# LGPL-3.0-or-later: tools/gnulib/version-etc.{c,h}
# LGPL-3.0-or-later OR GPL-2.0-or-later:
# - tools/gnulib/unistr/u16-mbtoucr.c
# - tools/gnulib/unistr/u16-to-u8.c
License: GPL-3.0-or-later AND LGPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-2.0-or-later AND (LGPL-3.0-or-later OR GPL-2.0-or-later)
BuildArch: noarch

%description utils-doc
%summary

%package -n python3-module-louis
Summary: Python 3 language bindings for %name
Group: Development/Python
BuildArch: noarch
License: LGPL-2.1-or-later

%description -n python3-module-louis
This package provides Python 3 language bindings for %name.

%package doc
Summary: Documentation for %name
Group: Documentation
BuildArch: noarch
# See doc/liblouis.texi
License: LGPL-3.0-or-later

%description doc
This package provides the documentation for liblouis.

%prep
%setup
chmod 664 tables/*

%build
%autoreconf
%configure --disable-static --enable-ucs4

%make_build -j1
pushd doc; xetex %name.texi; popd
pushd python
%pyproject_build

%install
%makeinstall_std PREFIX=%prefix
rm %buildroot%_libdir/%name.la
rm -r %buildroot%_bindir/lou_maketable*

# Install internal.h for MuseScore
install -pm 0644 liblouis/internal.h %buildroot%_includedir/%name

# Hardlink table files with identical content
hardlink -t %buildroot/%_datadir/%name/tables/

pushd python
%pyproject_install
popd

mv %buildroot%python3_sitelibdir_noarch/louis %buildroot%python3_sitelibdir_noarch/%name
mv %buildroot%python3_sitelibdir_noarch/louis-%version.dist-info %buildroot%python3_sitelibdir_noarch/%name-%version.dist-info

%check
LD_LIBRARY_PATH=%buildroot/%_libdir %make check

%files -n %name%sover
%_libdir/%name.so.%sover
%_libdir/%name.so.%sover.*

%files devel
%_includedir/%name/
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%files devel-doc
%doc HACKING
%_infodir/%name.info*

%files data
%_datadir/%name/

%files utils
%_bindir/lou_*

%files utils-doc
%doc COPYING
%_man1dir/lou_*.1*

%files -n python3-module-louis
%python3_sitelibdir_noarch/%name
  %python3_sitelibdir_noarch/%name-%version.dist-info

%files doc
%doc doc/%name.pdf README AUTHORS NEWS ChangeLog TODO COPYING.LESSER

%changelog
* Thu Jun 25 2026 Artem Semenov <savoptik@altlinux.org> 3.38.0-alt1
- Updated to new version 3.38.0

* Tue Mar 10 2026 Artem Semenov <savoptik@altlinux.org> 3.37.0-alt1
- Updated to new version 3.37.0

* Thu Dec 04 2025 Artem Semenov <savoptik@altlinux.org> 3.36.0-alt1
- Updated to new version 3.36.0

* Thu Sep 04 2025 Artem Semenov <savoptik@altlinux.org> 3.35.0-alt1
- Updated to new version 3.35.0

* Tue Jun 17 2025 Artem Semenov <savoptik@altlinux.org> 3.34.0-alt1
- Updated to new version 3.34.0

* Wed Apr 16 2025 Artem Semenov <savoptik@altlinux.org> 3.33.0-alt1
- Build new version 3.33.0

* Wed Jul 17 2024 Artem Semenov <savoptik@altlinux.org> 3.28.0-alt2
- Renamed to data for the tables package

* Thu May 16 2024 Artem Semenov <savoptik@altlinux.org> 3.28.0-alt1
- Initial build for Sisyphus (ALT bug: 50363)
