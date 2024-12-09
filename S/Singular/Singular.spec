%global singulardir %_libdir/Singular
%global upstreamver	4-4-0
%global py3_slim_version %(rpm --eval %_python3_version | tr -d .)
%global patchver p6

%def_with python
%def_with emacs

%if_with python
# Singular installs python files into nonstandard places
%global _python_bytecompile_extra 0
%endif

Name: Singular
Version: 4.4.0.7
Release: alt1

Summary: Computer Algebra System for polynomial computations
# License analysis:
# - The project as a whole is GPL-2.0-only OR GPL-3.0-only
# - GPL-2.0-or-later:
#   - factory/cfNTLzzpEXGCD.{cc,h}
# - GPL-3.0-or-later WITH Bison-exception-2.2:
#   - Singular/grammar.{cc,h}
# - BSD-3-Clause:
#   - Singular/links/ndbm.{cc,h}
#   - Singular/svd
# - Not sure, but similar to HPND and NTP (TODO: check with Legal):
#   - omalloc/omReturn.h
License: GPL-2.0 or GPL-3.0
Group: Sciences/Mathematics

Url: https://www.singular.uni-kl.de/
Vcs: git://github.com/Singular/Singular.git
# Java sources omitted from the source tarball.  To recreate this:
# - git clone https://github.com/Singular/Singular.git
# - cd Sources
# - git checkout spielwiese
# - git reset --hard 0dabbb616c7d95f0c9e81e9f51b857e3a0bb9e7c
# - tar cJf surfex.tar.xz Singular/LIB/surfex
#Source1: surfex.tar.xz
# Source-url: https://github.com/Singular/Singular/archive/Release-%{upstreamver}%{?patchver}.tar.gz
Source: singular-%version.tar.gz

# fedora patches
# Support S390(x) architectures
Patch0: %name-arches.patch
# Fix overlinking
Patch1:	 %name-link.patch
# Fix the desktop files
Patch2: %name-desktop.patch
# Adapt to new template code in NTL 8
Patch3:	 %name-ntl8.patch
# Fix code that can overflow a character buffer with sprintf
Patch4: %name-format.patch
# Add missing parentheses that can change code meaning in a macro
Patch5: %name-parens.patch
# Unbundle gfanlib
Patch6:	 %name-gfanlib.patch
# Let ESingular read a compressed singular.info file
Patch7: %name-emacs.patch
# Fix several "use after free" scenarios due to temporary objects
Patch8:	 %name-use-after-free.patch
# Change little-endian-specific code to endian-agnostic code
Patch9: %name-endian.patch
# Disable examples that use the network to avoid hangs on the koji builders
Patch10: %name-doc-hang.patch
# Fix an off-by-one error in polymake.lib that leads to failed examples
# https://github.com/Singular/Singular/issues/1210
Patch11: %name-polymake-lib.patch

BuildRequires: 4ti2
BuildRequires: bison
BuildRequires: boost-program_options-devel
%if_with python
BuildRequires: boost-python3-devel
%endif
BuildRequires: desktop-file-utils
BuildRequires: doxygen
%if_with emacs
BuildRequires: emacs
%endif
BuildRequires: environment-modules
BuildRequires: flex
BuildRequires: libflint2-devel
BuildRequires: gcc-c++
BuildRequires: libgmp-devel
BuildRequires: graphviz
BuildRequires: java-devel
BuildRequires: javapackages-tools
BuildRequires: libxml2-devel
BuildRequires: libncurses-devel
BuildRequires: libreadline-devel
BuildRequires: tbb-devel
BuildRequires: zlib-devel
BuildRequires: libmemtailor-devel
%if_with python
BuildRequires: python3-devel
%endif
# Need uudecode for documentation images in tarball
BuildRequires: sharutils
BuildRequires: surf-geometry
BuildRequires: lrcalc
BuildRequires: texlive-dist
BuildRequires: texlive-collection-basic
# BuildRequires: TOPCOM
Requires: %name-libs = %version-%release
Requires: environment-modules
Requires: less
# Requires: surf-geometry

%description
Singular is a computer algebra system for polynomial computations, with
special emphasis on commutative and non-commutative algebra, algebraic
geometry, and singularity theory.

%package libs
Summary: Singular library
Group: System/Libraries

%description libs
This package contains the main Singular library.

%package devel
Summary: Singular development files
Group: Development/Other
Requires: %name-libs = %version-%release
Requires: libpolys-devel = %version-%release

%description devel
This package contains the Singular development files.

%package doc
Summary: Singular documentation files
Group: Documentation
BuildArch: noarch

%description doc
This package contains the Singular documentation files.

%package emacs
Summary: Emacs interface to Singular
Group: Editors
Requires: emacs-common

%description emacs
Emacs interface to Singular.

%package -n libfactory4
Summary: C++ class library for multivariate polynomial data
Group: System/Libraries
Requires: libfactory-gftables = %version-%release

%description -n libfactory4
Factory is a C++ class library that implements a recursive
representation of multivariate polynomial data.  It handles sparse
multivariate polynomials over different coefficient domains, such as Z,
Q and GF(q), as well as algebraic extensions over Q and GF(q) in an
efficient way.  Factory includes algorithms for computing univariate and
multivariate gcds, resultants, chinese remainders, and algorithms to
factorize multivariate polynomials and to compute the absolute
factorization of multivariate polynomials with integer coefficients.

%package -n libfactory-devel
Summary: Development files for the Singular factory
Group: Development/Other
Requires: libfactory4 = %version-%release
Requires: libgmp-devel

%description -n libfactory-devel
Development files for the Singular factory.

%package -n libfactory-gftables
Summary: Singular factory addition tables
Group: Development/Other
BuildArch: noarch

%description -n libfactory-gftables
Factory uses addition tables to calculate in GF(p^n) in an efficient way.

%package -n libpolys4
Summary: C++ class library for polynomials in Singular
Group: System/Libraries
Requires: libfactory4 = %version-%release

%description -n libpolys4
Libpolys contains the data structures and basic algorithms for
polynomials in Singular.

%package -n libpolys-devel
Summary: Development files for libpolys
Group: Development/Other
Requires: %name-libs = %version-%release
Requires: libfactory-devel = %version-%release
Requires: libflint2-devel

%description -n libpolys-devel
Development files for libpolys.

%package surfex
Summary: Singular java interface
Group: Development/Java
Requires: %_bindir/java
Requires: %name = %version-%release

%description surfex
This package contains the Singular java interface.

%prep
%setup -n singular-%version
%autopatch -p1

%if_with python
# Fix the name of the boost_python library
sed -ri 's/(lboost_python)-\$\{PYTHON_VERSION\}/\1%py3_slim_version/' \
    Singular/dyn_modules/python/Makefile.am
%endif

# Do not force the use of c++11, since the polymake code requires c++14
sed -i 's/-std=c++11//' m4/ntl-check.m4

# Do not add an rpath for ccluster
sed -i 's@ -Wl,-rpath,\${CCLUSTER_HOME}/lib@@' m4/ccluster-check.m4

# Make sure we do not use the bundled gfanlib
rm -fr gfanlib

# Regenerate configure due to patches
./autogen.sh

# The file countedref.cc needs to be built without strict aliasing
sed -i '/countedref\.cc/s/\$(CXXFLAGS)/& -fno-strict-aliasing/g' Singular/Makefile.in

sed -i -e '1 s/^/#!\/usr\/bin\/python3\n\n/;' \
    Singular/dyn_modules/machinelearning/ml_python/common/constants.py

%build
export CPPFLAGS="-I%_includedir/flint -I%_includedir/gfanlib"
%if_with python
pyincdir=$(python3 -Esc "import sysconfig; print(sysconfig.get_paths()['include'])")
CPPFLAGS="$CPPFLAGS -I$pyincdir"
%endif
export CFLAGS="%optflags -fPIC -fno-delete-null-pointer-checks"
export CXXFLAGS="$CFLAGS"
# Cannot use RPM_LD_FLAGS, as -Wl,-z,now breaks lazy module loading
export LDFLAGS="-Wl,-z,lazy"
# module load 4ti2-%%_arch
# module load lrcalc-%%_arch
%configure \
	--bindir=%singulardir \
	--infodir=%_datadir/info \
	--disable-silent-rules \
	--disable-optimizationflags \
	--disable-static \
	--enable-p-procs-dynamic \
	--enable-bigintm-module \
	--enable-gfanlib-module \
	--enable-Order-module \
%if_with polymake
	--enable-polymake-module \
%else
	--disable-polymake-module \
%endif
%if_with python
	--enable-python-module \
%else
	--disable-python-module \
%endif
	--enable-streamio \
	--with-gmp \
	--without-ntl \
	--with-flint \
	--without-mathicgb \
%if_with python
	--with-python=python3 \
%else
	--without-python \
%endif
	--with-readline \
	--disable-doc \
	--with-malloc=system \
#

%make_build
%make_build -C dox html

%install
%makeinstall_std

%ifnarch i586 armh
# Upstream forgot to move some modules from libexecdir
mv %buildroot%_libexecdir/singular/MOD/* %buildroot%_libdir/singular/MOD
rm -fr %buildroot%_libexecdir
%endif

# Validate the desktop files
desktop-file-validate %buildroot%_datadir/applications/Singular.desktop
desktop-file-validate \
  %buildroot%_datadir/applications/Singular-manual.desktop

# Remove unnecessary dependencies from the pkgconfig files
sed -i 's/ -lflint.*//;s/Libs\.private.*/& -lflint -lmpfr -lntl -lgmp/' \
  %buildroot%_libdir/pkgconfig/factory.pc

sed -i 's/ -lflint.*//;s/Libs\.private.*/& -lflint -lmpfr -lgmp/' \
  %buildroot%_libdir/pkgconfig/libpolys.pc

# We don't want the libtool files
rm -f %buildroot%_libdir/*.la
rm -f %buildroot%_libdir/singular/MOD/*.la

# Remove files we don't want in the installed tree
rm -f %buildroot%_datadir/singular/emacs/{ChangeLog,COPYING,NEWS}
rm -fr %buildroot%_docdir/singular

# Move the config scripts
mkdir -p %buildroot%_bindir
mv %buildroot%singulardir/*-config %buildroot%_bindir

# Install documentation files
mkdir -p %buildroot%_mandir/man1
for cmd in ESingular Singular TSingular; do
  cp -p Singular/$cmd.man %buildroot%_mandir/man1/$cmd.1
done
cp -a dox/html %buildroot%_datadir/singular

# remove script that calls surf; we don't ship it
rm -f %buildroot%singulardir/singularsurf

# create a script also setting SINGULARPATH
cat > %buildroot%_bindir/Singular << EOF
#!/bin/sh

# . /etc/profile.d/modules.sh
# module load surf-geometry-%%_arch
export SINGULAR_DATA_DIR=%_datadir
exec %singulardir/Singular "\$@"
EOF

chmod 0755 %buildroot%_bindir/Singular

# TSingular
cat > %buildroot%_bindir/TSingular << EOF
#!/bin/sh

# . /etc/profile.d/modules.sh
# module load surf-geometry-%%_arch
exec %singulardir/TSingular --singular %_bindir/Singular "\$@"
EOF

chmod 0755 %buildroot%_bindir/TSingular

# ESingular
cat > %buildroot%_bindir/ESingular << EOF
#!/bin/sh

# . /etc/profile.d/modules.sh
# module load surf-geometry-%%_arch
export ESINGULAR_EMACS_DIR=%_datadir/singular/emacs
exec %singulardir/ESingular --singular %_bindir/Singular "\$@"
EOF

chmod 0755 %buildroot%_bindir/ESingular

chmod +x %buildroot%_datadir/ml_python/common/keyword_vector.py
chmod +x %buildroot%_datadir/ml_python/common/constants.py

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
make check

%files
%doc README.md
%_bindir/Singular
%_bindir/TSingular
%_man1dir/Singular.1*
%_man1dir/TSingular.1*
%_desktopdir/Singular.desktop
%_iconsdir/Singular.png
%_datadir/ml_python/
%_datadir/ml_singular/
%_datadir/singular/html/
%singulardir/Singular
%singulardir/TSingular

%files libs
%doc libpolys/README
%doc COPYING
%doc GPL2
%doc GPL3
%_libdir/libSingular-4.4.0.so
%_libdir/singular/
%dir %_datadir/singular/
%_datadir/singular/LIB/
%exclude %_datadir/singular/LIB/surfex.lib
#%%exclude %%_datadir/singular/LIB/surfex

%files devel
%_bindir/libsingular-config
%_includedir/singular/kernel/
%_includedir/singular/Singular/
%_includedir/singular/singularconfig.h
%_libdir/libSingular.so
%_pkgconfigdir/Singular.pc

%files doc
%doc dox/*.html
%doc dox/*.png
%doc dox/*.css
%_desktopdir/Singular-manual.desktop

%if_with emacs
%files emacs
%doc emacs/COPYING
%doc emacs/BUGS
%_bindir/ESingular
%_man1dir/ESingular.1*
%_datadir/singular/emacs/
%singulardir/ESingular
%endif

%files surfex
#%%_bindir/surfex
%_datadir/singular/LIB/surfex.lib
#%%_datadir/singular/LIB/surfex/

%files -n libfactory4
%doc factory/COPYING
%doc factory/README
%_libdir/libfactory-4.4.0.so
%_libdir/libomalloc-0.9.6.so
%_libdir/libsingular_resources-4.4.0.so

%files -n libfactory-devel
%doc factory/examples
%_includedir/factory/
%_includedir/omalloc/
%_includedir/resources/
%_libdir/libfactory.so
%_libdir/libomalloc.so
%_libdir/libsingular_resources.so
%_pkgconfigdir/factory.pc
%_pkgconfigdir/omalloc.pc
%_pkgconfigdir/singular_resources.pc

%files -n libfactory-gftables
%_datadir/factory/

%files -n libpolys4
%doc libpolys/COPYING
%doc libpolys/README
%_libdir/libpolys-4.4.0.so

%files -n libpolys-devel
%_bindir/libpolys-config
%dir %_includedir/singular/
%_includedir/singular/coeffs/
%_includedir/singular/libpolysconfig.h
%_includedir/singular/misc/
%_includedir/singular/polys/
%_includedir/singular/reporter/
%_libdir/libpolys.so
%_pkgconfigdir/libpolys.pc

%changelog
* Mon Dec 09 2024 Leontiy Volodin <lvol@altlinux.org> 4.4.0.7-alt1
- New version Release-4-4-0p7.

* Mon Dec 02 2024 Leontiy Volodin <lvol@altlinux.org> 4.4.0.6-alt1
- New version Release-4-4-0p6.
- Added vcs tag.

* Sat Jan 15 2022 Michael Shigorin <mike@altlinux.org> 4.2.1-alt2
- Introduced emacs knob (on by default)
- Minor spec cleanup

* Thu Oct 14 2021 Leontiy Volodin <lvol@altlinux.org> 4.2.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for the spec).
- Build as require for libpynac and sagemath.
