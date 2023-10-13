Group: Emulators
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/col /usr/bin/groff /usr/bin/pkgconf bzlib-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 7

Name:           advancecomp
Version:        2.5
Release:        alt1_8
Summary:        Recompression utilities for .png, .mng, .zip and .gz files

# Source file headers all specify GPL-2.0-or-later (see source file headers),
# except:
#
#   The bundled and forked 7z (7-Zip code) in 7z/ is under the a.'LGPLa.' license.
#   Based on https://www.7-zip.org/license.txt, and the absence of any mention
#   of license changes in https://www.7-zip.org/history.txt, 7-Zip has always
#   been licensed under LGPL-2.1-or-later, specifically; we thus assume this is
#   the intended specific license for the contents of the 7z/ directory. None
#   of the sources that would be covered by the a.'unRAR license restrictiona.' or
#   the BSD-3-Clause license for LZFSE are present in this fork.
#
#   Certain build-system files, which do not contribute to the license of the
#   binary RPM, are under other permissible licenses.
#
# However, in version 1.17, the COPYING file was updated to GPLv3, with a
# changelog message (in HISTORY and elsewhere) of a.'Changes to GPL3.a.' We
# interpret this as an overall license of GPL-3.0-only.
License:        GPL-3.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://www.advancemame.it/
%global forgeurl https://github.com/amadvance/advancecomp
Source:         %{forgeurl}/archive/v%{version}/advancecomp-%{version}.tar.gz

BuildRequires(pre): rpm-macros-valgrind
BuildRequires:  autoconf
BuildRequires:  automake

BuildRequires:  gcc
BuildRequires:  gcc-c++
%ifarch %valgrind_arches
BuildRequires: /usr/bin/valgrind
%endif

BuildRequires:  dos2unix

# System library supported by upstream
BuildRequires:  zlib-devel

# Unbundled downstream
BuildRequires:  pkgconfig(libdeflate)
BuildRequires:  libzopfli-devel

# From 7z/README:
#
#   This directory contains some source files from the
#   7z archive utility. (www.7-zip.org)
#
#   All the files in this directory was originally released
#   with the LGPL license.
#
#   All the modifications made on the original files must
#   be considered Copyright (C) 2002 Andrea Mazzoleni and
#   released under the LGPL license.
#
# It is not clear which version was forked. Because 7-Zip does not provide a
# library, and because the implementation is modified, there is no possibility
# of unbundling. Note that this was forked from the original 7-Zip, not from
# p7zip.
Provides:      bundled(7zip)
Source44: import.info

%description
AdvanceCOMP contains recompression utilities for your .zip archives,
.png images, .mng video clips and .gz files.

The official site of AdvanceCOMP is:

  https://www.advancemame.it

This package contains:
  advzip - Recompression and test utility for zip files
  advpng - Recompression utility for png files
  advmng - Recompression utility for mng files
  advdef - Recompression utility for deflate streams in .png, .mng and .gz files


%prep
%setup -q


dos2unix -k doc/*.txt

# Patch out bundled libdeflate
rm -rvf libdeflate
sed -r -i '/libdeflate[\/_]/d' Makefile.am
# Fix up #include paths. The find-then-modify pattern keeps us from discarding
# mtimes on any sources that do not need modification.
find . -type f -exec gawk \
    '/^[[:blank:]]*#include.*libdeflate/ { print FILENAME; nextfile }' \
    '{}' '+' |
  xargs -r -t sed -r -i 's@^([[:blank:]]*#include.*)libdeflate/@\1@'

# Patch out bundled zopfli
rm -rvf zopfli
sed -r -i \
    -e '/zopfli[\/_]/d' \
    -e 's/((\(7z_SOURCES\)|WindowOut\.h).*)[[:blank:]]*\\/\1/' \
    Makefile.am
# Fix up #include paths. The find-then-modify pattern keeps us from discarding
# mtimes on any sources that do not need modification.
find . -type f -exec gawk \
    '/^[[:blank:]]*#include.*zopfli/ { print FILENAME; nextfile }' \
    '{}' '+' |
  xargs -r -t sed -r -i -e 's@^([[:blank:]]*#include.*)zopfli/@\1@'


%build
autoreconf --force --install --verbose

# Link against system libdeflate
export CFLAGS="$(pkgconf --cflags libdeflate) ${CFLAGS-}"
export CXXFLAGS="$(pkgconf --cflags libdeflate) ${CXXFLAGS-}"
#export LDFLAGS="$(pkgconf --libs libdeflate) ${LDFLAGS-}"
export LIBS="$(pkgconf --libs libdeflate) ${LIBS-}"

# Link against system zopfli
#export LDFLAGS="-lzopfli ${LDFLAGS-}"
export LIBS="-lzopfli ${LIBS-}"

%configure
%make_build


%install
%makeinstall_std


# We don’t run upstream tests (%%make_build check) because they are too
# brittle, expecting recompressed outputs to be identical. Across platforms,
# compilers, and unbundled library versions, this doesn’t hold up.


%files
%doc --no-dereference COPYING
%doc AUTHORS
%doc HISTORY
%doc README
%doc doc/advdef.txt
%doc doc/advmng.txt
%doc doc/advpng.txt
%doc doc/advzip.txt

%{_bindir}/advdef
%{_bindir}/advmng
%{_bindir}/advpng
%{_bindir}/advzip
%{_mandir}/man1/advdef.1*
%{_mandir}/man1/advmng.1*
%{_mandir}/man1/advpng.1*
%{_mandir}/man1/advzip.1*


%changelog
* Fri Oct 13 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 2.5-alt1_8
- spec: do not require wine (used only when cross-compiling with mingw on Linux)
- spec: require valrgind only on supported architectures

* Thu Oct 12 2023 Igor Vlasenko <viy@altlinux.org> 2.5-alt1_7
- update to new release by fcimport

* Sat Dec 26 2020 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_16
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_11
- update to new release by fcimport

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_10
- update to new release by fcimport

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_7
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_6
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 2.1-alt1_4
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_1
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_3
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_2
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1_1
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_5
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_2
- update to new release by fcimport

* Thu Apr 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1_1
- update to new release by fcimport

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1_1
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_19
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_18
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_17
- update to new release by fcimport

* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_16
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt2_14
- rebuild to get rid of #27020

* Sat Jan 21 2012 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_14
- update to new release by fcimport

* Thu Jul 07 2011 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_13
- initial release by fcimport

