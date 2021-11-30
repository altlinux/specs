Name: gap
Version: 4.11.1
Release: alt2
Summary: System for Computational Discrete Algebra
License: Zlib and LGPL-3.0+ and GPL-2.0+ and GPL-3.0+
Group: Sciences/Mathematics
Url: http://gap-system.org/

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

%define lname libgap0
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

%package -n %lname
Summary: Kernel for the GAP computation algebra system
Group: System/Libraries

%description -n %lname
This package contains the GAP kernel in a C library that can be
linked to.

%package devel
Summary: Development environment for GAP
Group: Development/Tools
Requires: %lname = %version

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
# C extensions suffer from broken gac
# [https://github.com/gap-system/gap/issues/3001] and mediocre header files
# [https://github.com/gap-system/gap/issues/3003]
#Requires: gap >= %%version
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
%patch2 -p0
#%%patch3 -p0
%patch4 -p0

subst 's/\#$(INSTALL) gac/$(INSTALL) gac/' Makefile.rules
# Fixed version
subst 's|4.11.0|4.11.1|; s|29-Feb|Feb|; s|2020|2021|' configure.ac

%build
#%%autoreconf
%configure
%make_build V=1

%install
b="%buildroot"
%make_install DESTDIR=%buildroot install-bin install-gaproot install-headers install-libgap

rm -fv %buildroot%_libdir/*.la

# Fixup incomplete installation
mkdir -p "$b/%_datadir/gap"
cp -a grp lib "$b/%_datadir/gap/"

mkdir -p "$b/%_libexecdir/%name" \
 "$b/%gap_sitearch" "$b/%gap_sitelib"
mv "$b/%_bindir/gap" "$b/%_libexecdir/%name/gap.bin"
cat >>"$b/%_bindir/gap" <<-EOF
	#!/bin/sh
	exec %_libexecdir/%name/gap.bin -l "%gap_sitearch/.." -l "%gap_sitelib/.." "\$@"
EOF
chmod a+x "$b/%_bindir/gap"

# Fixup gap.bin syntax
rm -f "$b/%_libexecdir/%name/gap.bin"
cat >>"$b/%_libexecdir/%name/gap.bin" <<-EOF
#!/bin/sh
exec "%_bindir/gap.real" -l "%_datadir/gap" "\$@"
EOF
chmod +x "$b/%_libexecdir/%name/gap.bin"

namei sysinfo.gap
. ./sysinfo.gap
cat >"$b/%_libdir/gap/sysinfo.gap" <<-EOF
	GAParch=$GAParch
	GAP_ABI=$GAP_ABI
	GAP_BIN_DIR="%_bindir"
	GAP_LIB_DIR="%_libdir/gap"
	GAP_CC="$GAP_CC"
	GAP_CFLAGS="%optflags"
	GAP_CPPFLAGS="-I%_includedir/gap"
	GAP_LIBS="-lgap"
	GAP_OBJS=""
EOF
ln -s . "$b/%_includedir/gap/src"
ln -s sysinfo.gap "$b/%_libdir/gap/sysinfo.gap-default$GAP_ABI"
mkdir -pv "$b/%gap_sitearch/../bin/$GAParch"
ln -s "%_bindir/gac" "$b/%gap_sitearch/../bin/$GAParch/"

# ALT-specific extras for RPMs
mkdir -p "$b/%_libexecdir/rpm/macros.d"
cp %SOURCE2 "$b/%_libexecdir/rpm/macros.d/gap"
cat >>"$b/%_libexecdir/rpm/macros.d/gap" <<-EOF
	# Directory for modules extending the core
	%%gap_sitelib %gap_sitelib
	%%gap_sitearch %gap_sitearch
	%%gap_sitelib_anchor %_datadir
	%%gap_sitearch_anchor %_libdir
	%%gapdir %_libdir/gap
EOF

install -p -m 0644 gen/config.h %buildroot%_includedir/gap

%files
%doc CITATION CONTRIBUTING.md COPYRIGHT INSTALL.md LICENSE README*
%_bindir/gap*
%dir %_libexecdir/%name/
%_libexecdir/%name/gap.bin
%dir %_libdir/gap/
%_datadir/gap/

%files -n %lname
%_libdir/libgap.so.0*

%files devel
%_bindir/gac*
%_includedir/gap/
%_libdir/libgap.so
%dir %_libdir/gap
%_libdir/gap/bin/
%_libdir/gap/sysinfo.gap*

%files -n rpm-macros-%name
%_libexecdir/rpm/macros.d/gap

%files full
%changelog
* Tue Nov 30 2021 Leontiy Volodin <lvol@altlinux.org> 4.11.1-alt2
- Packed config.h for sagemath.
- Added buildrequires.

* Sun Jun 20 2021 Leontiy Volodin <lvol@altlinux.org> 4.11.1-alt1
- New version (4.11.1).

* Fri Jun 18 2021 Leontiy Volodin <lvol@altlinux.org> 4.11.0-alt2
- Added gap-full package.

* Thu Jun 10 2021 Leontiy Volodin <lvol@altlinux.org> 4.11.0-alt1
- Initial build for ALT Sisyphus (thanks opensuse for the spec).
