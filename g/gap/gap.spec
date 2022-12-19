Name: gap
Version: 4.12.2
Release: alt1
Summary: System for Computational Discrete Algebra
License: Zlib and LGPL-3.0+ and GPL-2.0+ and GPL-3.0+
Group: Sciences/Mathematics
Url: https://gap-system.org/

Source: https://www.gap-system.org/pub/gap/gap4core/gap-%version-core.zip
Source2: macros.gap
Source3: %name-rpmlintrc

# Patch applied in bootstrap mode to break circular dependencies.
Patch: %name-bootstrap.patch
# This patch applies a change from Debian to allow help files to be in gzip
# compressed DVI files, and also adds support for viewing with xdg-open.
Patch1: %name-help.patch
# Fix broken references in the reference manual's lab file
Patch2: %name-ref.patch
# Fix paths in gac
Patch3: %name-gac.patch
# On i386 only, and with recent versions of gcc only, various parts of the
# compiled code disagree about the size of a BagHeader.  Some parts think it
# is 12 bytes, and some parts think it is 16 bytes.  This leads to pointers
# pointing 4 bytes off from the actual first byte of a BagHeader, leading to
# weird failure modes.  This does not affect 32-bit ARM, so it is not purely
# a 32-bit issue.  I do not yet know if this behavior is due to a GCC bug, or
# if the GAP code is in fact wrong, but this patch works around the issue.
Patch4: %name-bagheader.patch

BuildRequires: gcc-c++
BuildRequires: libgmp-devel
BuildRequires: libtool
BuildRequires: libreadline-devel
BuildRequires: unzip
BuildRequires: zlib-devel
BuildRequires: libatomic_ops-devel libgc-devel
Obsoletes: gap-core < %version
Provides: gap-core = %version
Obsoletes: gap-data < %version
Provides: gap-data = %version
#Requires: gap-gapdoc >= 1.5.1

%define soname 8
%global gap_sitearch %_libdir/gap/pkg
%global gap_sitelib  %_datadir/gap/pkg

%description
GAP is a system for computational discrete algebra, with particular
emphasis on Computational Group Theory. GAP provides a programming
language, a library of thousands of functions implementing algebraic
algorithms written in the GAP language as well as large data
libraries of algebraic objects. GAP is used in research and teaching
for studying groups and their representations, rings, vector spaces,
algebras, combinatorial structures, and more.

%package -n lib%name%soname
Summary: Kernel for the GAP computation algebra system
Group: System/Libraries

%description -n lib%name%soname
This package contains the GAP kernel in a C library that can be
linked to.

%package devel
Summary: Development environment for GAP
Group: Development/Tools
Requires: lib%name%soname = %version

%description devel
GAP is a system for computational discrete algebra, with particular
emphasis on Computational Group Theory.

This package will pull in the current version of the GAP compiler and
utilities required to build GAP packages that need compilation.

%package -n rpm-macros-%name
Summary: RPM macros for building GAP packages
# Not noarch: contains arch-specific paths in RPM macros
Group: Development/Tools

%description -n rpm-macros-%name
GAP is a system for computational discrete algebra, with particular
emphasis on Computational Group Theory.

This subpackage provides RPM macros for use with packaging trivial
GAP modules that itself do not require the presence of GAP.

%package full
Summary: Metapackage to cause installation of the GAP Distribution
Group: Sciences/Mathematics
BuildArch: noarch
Requires: gap-4ti2interface
Requires: gap-autpgrp
Requires: gap-polycyclic
Requires: gap-alnuth
Requires: gap-aclib
Requires: gap-gapdoc
Requires: gap-atlasrep
Requires: gap-cohomolo
Requires: gap-quagroup
Requires: gap-sla
Requires: gap-corelg
Requires: gap-utils
Requires: gap-toric
Requires: gap-tomlib
Requires: gap-gbnp
Requires: gap-qpa
Requires: gap-mapclass
Requires: gap-grape
Requires: gap-design
Requires: gap-primgrp
Requires: gap-smallgrp
Requires: gap-transgrp
Requires: gap-crisp
Requires: gap-ctbllib
Requires: gap-factint
Requires: gap-fga
Requires: gap-irredsol
Requires: gap-laguna
Requires: gap-polenta
Requires: gap-radiroot
Requires: gap-resclasses
Requires: gap-sophus

%description full
GAP is a system for computational discrete algebra, with particular
emphasis on Computational Group Theory.

This subpackage will pull in all optional packages of the GAP distribution.

%prep
%setup
#%%patch -p0
%patch1 -p0
#%%patch2 -p0
#%%patch3 -p0
%patch4 -p0
sed -i 's|2.4.6|%{get_version libtool_2.4}|' \
  cnf/ltmain.sh \
  cnf/m4/ltversion.m4 \
  extern/gmp/aclocal.m4 \
  extern/gmp/configure \
  extern/gmp/ltmain.sh \
  hpcgap/extern/gc/configure \
  hpcgap/extern/gc/ltmain.sh \
  hpcgap/extern/gc/m4/ltversion.m4 \
  hpcgap/extern/libatomic_ops/configure \
  hpcgap/extern/libatomic_ops/ltmain.sh \
  hpcgap/extern/libatomic_ops/m4/ltversion.m4
# Don't exist in doc/.
sed -i 's|ext in css html js txt pdf six lab|xml|' \
  Makefile.rules

%build
%autoreconf
%configure

# Get rid of undesirable hardcoded rpaths.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -i libtool

%make_build V=1

%install
%makeinstall_std

# Fixup incomplete installation
sed -i 's|GAP_LIBS=""|GAP_LIBS="-lgap"|' \
  %buildroot%_libdir/gap/sysinfo.gap

# ALT-specific extras for RPMs
mkdir -p "%buildroot%_libexecdir/rpm/macros.d"
cp %SOURCE2 "%buildroot%_libexecdir/rpm/macros.d/gap"
cat >>"%buildroot%_libexecdir/rpm/macros.d/gap" <<-EOF
	# Directory for modules extending the core
	%%gap_sitelib %gap_sitelib
	%%gap_sitearch %gap_sitearch
	%%gap_sitelib_anchor %_datadir
	%%gap_sitearch_anchor %_libdir
	%%gapdir %_libdir/gap
EOF

rm -rf %buildroot%_libdir/libgap.la

# config.h is needed for sagemath.
# install -p -m 0644 build/config.h %%buildroot%%_includedir/gap/

# Already packed in %%doc.
rm -rf %buildroot%_datadir/gap/{CITATION,CONTRIBUTING.md,COPYRIGHT,INSTALL.md,LICENSE,README.md}

%files
%doc CITATION CONTRIBUTING.md COPYRIGHT INSTALL.md LICENSE README.md
%_bindir/gap
%dir %_libdir/gap/
%_libdir/gap/gap
%_datadir/gap/

%files -n lib%name%soname
%_libdir/libgap.so.%{soname}*

%files devel
%_bindir/gac
%_includedir/gap/
%_libdir/libgap.so
%dir %_libdir/gap/
%_libdir/gap/sysinfo.gap

%files -n rpm-macros-%name
%_libexecdir/rpm/macros.d/gap

%files full

%changelog
* Mon Dec 19 2022 Leontiy Volodin <lvol@altlinux.org> 4.12.2-alt1
- New version (4.12.2).

* Fri Oct 21 2022 Leontiy Volodin <lvol@altlinux.org> 4.12.1-alt1
- New version (4.12.1).

* Fri Oct 14 2022 Leontiy Volodin <lvol@altlinux.org> 4.12.0-alt2
- Applied some suggestions for improvements by upstream.

* Fri Oct 07 2022 Leontiy Volodin <lvol@altlinux.org> 4.12.0-alt1.1
- Fixed url tag.

* Tue Oct 04 2022 Leontiy Volodin <lvol@altlinux.org> 4.12.0-alt1
- New version (4.12.0).

* Tue Nov 30 2021 Leontiy Volodin <lvol@altlinux.org> 4.11.1-alt2
- Packed config.h for sagemath.
- Added buildrequires.

* Sun Jun 20 2021 Leontiy Volodin <lvol@altlinux.org> 4.11.1-alt1
- New version (4.11.1).

* Fri Jun 18 2021 Leontiy Volodin <lvol@altlinux.org> 4.11.0-alt2
- Added gap-full package.

* Thu Jun 10 2021 Leontiy Volodin <lvol@altlinux.org> 4.11.0-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
