%def_without sse2

Name: atlas
Version: 3.9.35
Release: alt1

Summary: Automatically Tuned Linear Algebra Software (the BLAS library)
License: BSD
Group: System/Libraries

URL: http://math-atlas.sourceforge.net
Source: %name-%version.tar
Patch: %name-3.7.11-alt6.qa1.patch

ExclusiveArch: %ix86 amd64 x86_64
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Automatically added by buildreq on Fri Dec 08 2006
BuildRequires: gcc-fortran libgomp-devel

%description
The ATLAS (Automatically Tuned Linear Algebra Software) project is an
ongoing research effort focusing on applying empirical techniques in
order to provide portable performance. At present, it provides C and
Fortran77 interfaces to a portably efficient BLAS implementation, as
well as a few routines from LAPACK.

%prep
%setup -q -n ATLAS
%patch -p1
ln -s atlas.mk Make.Linux_i586
ln -s atlas.mk Make.Linux_sse2
ln -s atlas.mk Make.Linux_amd64
chmod +x atlas-run.sh
ln -s ../atlas-run.sh CONFIG/ATLrun.Linux_i586
ln -s ../atlas-run.sh CONFIG/ATLrun.Linux_sse2
ln -s ../atlas-run.sh CONFIG/ATLrun.Linux_amd64

%build
%add_optflags -fPIC -falign-loops=4
%add_optflags -mfpmath=387
%define soffix .so.3
%ifarch x86_64
%define bits 64
%else
%define bits 32
%endif

confIt()
{
	../configure \
		-Si cputhrchk 0 \
		-Si omp 1 \
		-b %bits -D c\
		-DWALL -Fa alg '-g -Wa,--noexecstack -fPIC' \
		--cc=gcc \
		--cflags="%optflags" \
		--prefix=%buildroot%prefix \
		--incdir=%buildroot%_includedir \
		--libdir=%buildroot%_libdir \
		--shared
}

mkdir BUILD
pushd BUILD

confIt

%ifarch x86_64
sed -i 's#ARCH =.*#ARCH = HAMMER64SSE2#' Make.inc
sed -i 's#-DATL_SSE3##' Make.inc 
sed -i 's#-msse3#-msse2#' Make.inc 
%else
sed -i 's#ARCH =.*#ARCH = PPRO32#' Make.inc
sed -i 's#-DATL_SSE3 -DATL_SSE2 -DATL_SSE1##' Make.inc
sed -i 's#-mfpmath=sse -msse3#-mfpmath=387#' Make.inc
%endif

shared()
{
	lib=$1; shift
	${linker:-gcc} -shared -Wl,--whole-archive $lib.a -Wl,--no-whole-archive \
		-o $lib%soffix -Wl,-soname=$lib%soffix "$@" -lm -Wl,-z,defs
}
all_shared()
{
	cd $1
	linker=gcc shared libatlas
	linker=gcc shared libcblas ./libatlas%soffix
	mv libf77blas.a libblas.a
	linker=g77 shared libblas ./libatlas%soffix
	linker=g77 shared libf77refblas ./libatlas%soffix
	mv liblapack.a liblapack_atlas.a
	linker=g77 shared liblapack_atlas ./libatlas%soffix ./libblas%soffix ./libcblas%soffix
	cd -
}

%make build
all_shared lib

popd

%ifnarch x86_64
%if_with sse2
mkdir BUILD.SSE2
pushd BUILD.SSE2

confIt

sed -i 's#ARCH =.*#ARCH = P432SSE2#' Make.inc
sed -i 's#-DATL_SSE3##' Make.inc 
sed -i 's#-msse3#-msse2#' Make.inc 

%make_build build
pushd lib
linker=gcc shared libatlas
popd

popd
%endif
%endif

%install
pushd BUILD

mkdir -p %buildroot%_libdir %buildroot%_includedir/atlas
cp -p ../include/*.h %buildroot%_includedir/atlas/
ln -s atlas/cblas.h %buildroot%_includedir/cblas.h
ln -s atlas/clapack.h %buildroot%_includedir/clapack.h
cp -p lib/lib*%soffix %buildroot%_libdir/
cp -p lib/lib*.a %buildroot%_libdir/

ln -s libatlas%soffix %buildroot%_libdir/libatlas.so
ln -s libcblas%soffix %buildroot%_libdir/libcblas.so
ln -s libblas%soffix %buildroot%_libdir/libf77blas%soffix
ln -s libblas%soffix %buildroot%_libdir/libblas.so
ln -s libf77blas%soffix %buildroot%_libdir/libf77blas.so
ln -s libf77refblas%soffix %buildroot%_libdir/libf77refblas.so
ln -s liblapack_atlas%soffix %buildroot%_libdir/liblapack_atlas.so

mv %buildroot%_libdir/libatlas{,_}.a
echo 'GROUP(%_libdir/libatlas_.a -lm)' >%buildroot%_libdir/libatlas.a
mv %buildroot%_libdir/libcblas{,_}.a
echo 'GROUP(%_libdir/libcblas_.a %_libdir/libatlas.a)' >%buildroot%_libdir/libcblas.a
mv %buildroot%_libdir/libblas.a %buildroot%_libdir/libblas_.a
ln -s libblas_.a %buildroot%_libdir/libf77blas.a
echo 'GROUP(%_libdir/libblas_.a %_libdir/libatlas.a -lgfortran)' >%buildroot%_libdir/libblas.a
mv %buildroot%_libdir/liblapack_atlas{,_}.a
echo 'GROUP(%_libdir/liblapack_atlas_.a %_libdir/libcblas.a %_libdir/libblas.a)' >%buildroot%_libdir/liblapack_atlas.a

%define pkgdocdir %_docdir/atlas-3.9
mkdir -p %buildroot%pkgdocdir
cp -p bin/INSTALL_LOG/SUMMARY.LOG %buildroot%pkgdocdir/SUMMARY.LOG

popd

cp -p README.ALT %buildroot%pkgdocdir/
cp -p doc/AtlasCredits.txt doc/ChangeLog doc/LibReadme.txt %buildroot%pkgdocdir/
cp -p doc/atlas_{contrib,devel,over}.pdf doc/cblas.pdf %buildroot%pkgdocdir/
gzip -9nf %buildroot%pkgdocdir/*.pdf

%ifnarch x86_64
%if_with sse2
mkdir %buildroot%_libdir/sse2
cp -p BUILD.SSE2/lib/libatlas%soffix %buildroot%_libdir/sse2/
%endif
%endif

%package -n libatlas
Summary: Automatically Tuned Linear Algebra Software (the BLAS library)
Group: System/Libraries
Conflicts: liblapack < 1:3.0-alt3

%description -n libatlas
The ATLAS (Automatically Tuned Linear Algebra Software) project is an
ongoing research effort focusing on applying empirical techniques in
order to provide portable performance. At present, it provides C and
Fortran77 interfaces to a portably efficient BLAS implementation, as
well as a few routines from LAPACK.

%files -n libatlas
%_libdir/lib*%soffix
%ifarch %ix86
%if_with sse2
%dir %_libdir/sse2
%_libdir/sse2/libatlas%soffix
%endif
%endif
%dir %pkgdocdir
%pkgdocdir/README.ALT
%pkgdocdir/*.txt
%pkgdocdir/ChangeLog
%pkgdocdir/SUMMARY.LOG*

%package -n libatlas-devel
Summary: Automatically Tuned Linear Algebra Software (the BLAS library)
Group: Development/Other
Requires: libatlas = %version-%release

%description -n libatlas-devel
The ATLAS (Automatically Tuned Linear Algebra Software) project is an
ongoing research effort focusing on applying empirical techniques in
order to provide portable performance. At present, it provides C and
Fortran77 interfaces to a portably efficient BLAS implementation, as
well as a few routines from LAPACK.

%files -n libatlas-devel
%_libdir/*.so
%_includedir/cblas.h
%_includedir/clapack.h
%dir %_includedir/atlas
%_includedir/atlas/*.h

%package -n libatlas-devel-static
Summary: Automatically Tuned Linear Algebra Software (the BLAS library)
Group: Development/Other
Requires: libatlas-devel = %version-%release
Requires: libgfortran-devel-static

%description -n libatlas-devel-static
The ATLAS (Automatically Tuned Linear Algebra Software) project is an
ongoing research effort focusing on applying empirical techniques in
order to provide portable performance. At present, it provides C and
Fortran77 interfaces to a portably efficient BLAS implementation, as
well as a few routines from LAPACK.

%files -n libatlas-devel-static
%_libdir/lib*.a
%exclude %_libdir/libtstatlas.a

%package doc
Summary: Automatically Tuned Linear Algebra Software (the BLAS library)
Group: Development/Other
Conflicts: libatlas < %version, libatlas > %version
BuildArch: noarch

%description doc
The ATLAS (Automatically Tuned Linear Algebra Software) project is an
ongoing research effort focusing on applying empirical techniques in
order to provide portable performance. At present, it provides C and
Fortran77 interfaces to a portably efficient BLAS implementation, as
well as a few routines from LAPACK.

%files doc
%dir %pkgdocdir
%pkgdocdir/*.pdf.gz

%changelog
* Sun Apr 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.35-alt1
- Version 3.9.35

* Wed Feb 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.32-alt2
- Rebuilt for debuginfo

* Mon Dec 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.32-alt1
- Version 3.9.32

* Thu Dec 02 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.28-alt2
- Rebuilt with new glibc

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.28-alt1
- Version 3.9.28
- Disabled SSE2 support for i586

* Thu Oct 21 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.25-alt1
- Version 3.9.25 (ALT #24252)

* Wed Feb 03 2010 Repocop Q. A. Robot <repocop@altlinux.org> 3.7.11-alt6.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libatlas
  * postun_ldconfig for libatlas
  * postclean-05-filetriggers for spec file

* Tue Nov 04 2008 Alexey Tourbin <at@altlinux.ru> 3.7.11-alt6
- rebuilt with gcc-4.3
- made atlas-doc package noarch

* Mon Oct 29 2007 Alexey Tourbin <at@altlinux.ru> 3.7.11-alt5
- packaged static libraries (requested by Pavel A. Piminov);
  use e.g. "g77 -static test.f -lblas" for static linkage
- changed src.rpm packaging to keep separate upstream tarball

* Tue Jan 09 2007 Alexey Tourbin <at@altlinux.ru> 3.7.11-alt4
- backported bugfix for "complex C = A A' bug"
- backported fix for ilaenv.f which improves LAPACK performance

* Sun Dec 10 2006 Alexey Tourbin <at@altlinux.ru> 3.7.11-alt3
- compiled with -mfpmath=387 to fix LAPACK test suite on x86_64
- actually packaged README.ALT

* Fri Dec 08 2006 Alexey Tourbin <at@altlinux.ru> 3.7.11-alt2
- imported sources into git and built with gear
- removed PRM_OPT_FLAGS hack that broke SSE2
- enabled /usr/lib/sse2/libatlas.so.3 for i586
- libatlas.so.3, libblas.so.3: made some internal functions hidden
- packaged docs (atlas-doc package has postscript documentation)
- added README.ALT, which explains some performance issues

* Tue Jun 06 2006 Alexey Tourbin <at@altlinux.ru> 3.7.11-alt1
- initial revision, with debian fixes
- PII-optimized BLAS (for i586) yields three-fold improvement
  over plain fortran BLAS (matrix cross-product in R)
- SSE2-optimized /usr/lib/sse2/libatlas.so disabled by default
  because of segfaults (try to rebuild `--with sse2' and let me know)
- HAMMER64SSE2 for x86_64
