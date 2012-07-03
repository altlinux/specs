%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define oname hdf5
%define sover 7
%define priority 40
Name: lib%{oname}-%sover-mpi
Version: 1.8.8
Release: alt3

Summary: Hierarchical Data Format 5 library, parallel version

Group: System/Libraries
License: Nearly BSD, but changed sources must be marked
Url: http://www.hdfgroup.org/HDF5/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: ftp://ftp.hdfgroup.org/HDF5/current/src/%oname-%version.tar.bz2

Provides: lib%oname-mpi = %version-%release
Conflicts: lib%oname < 1.8.3-alt3
Requires(post,preun): alternatives
%ifarch x86_64
Provides: lib%oname.so.%sover()(64bit)
Provides: lib%{oname}_hl.so.%sover()(64bit)
%else
Provides: lib%oname.so.%sover
Provides: lib%{oname}_hl.so.%sover
%endif

# Automatically added by buildreq on Sat Sep 15 2007
BuildRequires: gcc-c++ libssl-devel zlib-devel %mpiimpl-devel
BuildPreReq: libmpe2-devel libsz2-devel

%description
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

This version of library supports MPI.

%package -n lib%oname-mpi-devel
Summary: HDF5 library development package
Group: Development/C
Requires(post,preun): alternatives
Requires: %name = %version-%release
Conflicts: lib%oname-devel < 1.8.3-alt3

%description -n lib%oname-mpi-devel
Development files for HDF5 library.

%package -n %oname-%sover-mpi-tools
Summary: HDF5 tools
Group: Development/Tools
Requires(post,preun): alternatives
Requires: %name = %version-%release
Provides: %oname-mpi-tools = %version-%release
Conflicts: lib%oname-tools < 1.8.3-alt3
Conflicts: lib%oname-mpi < %version-%release
Obsoletes: lib%oname-mpi < %version-%release

%description -n %oname-%sover-mpi-tools
HDF5 tools.

%prep
%setup -n %oname-%version

%build
sed -i -e 's/(SOVER)/%sover/' src/H5detect.c
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"

%add_optflags -DH5_HAVE_MPE
%autoreconf
%configure \
	--bindir=%mpidir/bin \
	--libdir=%mpidir/lib \
	--includedir=%mpidir/include \
	--enable-linux-lfs \
	--enable-shared \
	--enable-production \
	--with-pthread \
	--with-ssl \
	--with-zlib=%prefix \
	--with-szlib=%prefix \
	--enable-fortran \
	--enable-parallel \
	--with-mpe=%prefix \
	MPIDIR=%mpidir

subst "s|^LT=.*|LT=../libtool|g" c++/src/Makefile c++/test/Makefile
cp src/lib%oname.settings src/lib%oname-%sover.settings
%make_build MPIDIR=%mpidir

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-rpath,%mpidir/lib -L%mpidir/lib"
export LD_LIBRARY_PATH="../src/.libs"

%make_install DESTDIR=%buildroot install

mv %buildroot%mpidir/lib/lib%oname.settings \
	%buildroot%mpidir/lib/lib%oname-%sover.settings

# alternatives

install -d %buildroot%_altdir
mkdir -p %buildroot%_libdir
pushd %buildroot%mpidir/lib
for i in $(ls *.so.*) $(ls *.settings); do
	ln -s ../..%mpidir/lib/$i %buildroot%_libdir/
	echo "%_libdir/$i %mpidir/lib/$i %priority" >> \
		%buildroot%_altdir/%name.alternatives
done
for i in $(ls *.so); do
	echo "%_libdir/$i %mpidir/lib/$i %priority" >> \
		%buildroot%_altdir/%name-devel.alternatives
done
popd
pushd %buildroot%mpidir/bin
for i in $(ls); do
	echo "%_bindir/$i %mpidir/bin/$i %priority" >> \
		%buildroot%_altdir/%oname-mpi-tools.alternatives
done
popd

install -d %buildroot%_pkgconfigdir
cat <<EOF >%buildroot%_pkgconfigdir/%oname-mpi.pc
prefix=%prefix
exec_prefix=%prefix
libdir=%mpidir/lib
includedir=%mpidir/include

Name: %oname
Description: Hierarchical Data Format 5 library
Version: %version
Libs: -L%mpidir/lib -lhdf5hl_fortran -lhdf5_hl -lhdf_fortran -lhdf -lgfortran -lz
Cflags: -I%mpidir/include
EOF

echo "%_pkgconfigdir/%oname.pc %_pkgconfigdir/%oname-mpi.pc %priority" >> \
	%buildroot%_altdir/%name-devel.alternatives

%files
%doc COPYING README.txt release_docs/{HISTORY*,RELEASE.txt}
%ghost %_libdir/lib*.so.*
%mpidir/lib/*.so.*
# used to show configuration at runtime
%mpidir/lib/lib%oname-%sover.settings
%_altdir/%name.alternatives

%files -n lib%oname-mpi-devel
%mpidir/lib/lib*.so
%mpidir/include/*
%_pkgconfigdir/*
%_altdir/%name-devel.alternatives

%files -n %oname-%sover-mpi-tools
%mpidir/bin/*
%_altdir/%oname-mpi-tools.alternatives

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt3
- Rebuilt with OpenMPI 1.6

* Wed Jun 06 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt2
- Fixed build

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt1
- Version 1.8.8

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.7-alt2
- Fixed RPATH

* Tue Sep 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.7-alt1
- Version 1.8.7

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.6-alt1
- Version 1.8.6

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5_patch1-alt2
- Rebuilt with debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5_patch1-alt1
- Version 1.8.5-patch1

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt9
- Fixed soname set-versions by ghost links (thnx ldv@)

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt8
- Fixed overlinking of libraries

* Wed Jul 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt7
- Added pkgconfig file

* Fri Jun 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt6
- Fixed wrong MPE check in configure script

* Thu Jun 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt5
- Enabled szlib compression
- Created alternatives

* Thu Jun 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt4
- Rebuild with MPE instrumentation
- Added explicit conflict with sequential version of HDF5 tools

* Tue Jun 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt3
- Enable zlib compression

* Sun May 31 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt2
- Add szlib support

* Fri May 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt1
- Version 1.8.3
- Rename settings file: libhdf5.settings -> libhdf5-6.settings
- Extract tools into separate package

* Thu May 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.2-alt1
- MPI version: initial build for sisyphus

* Sun Dec 14 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.6-alt2
- fixed build with gcc4.3

* Sat Sep 15 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6.6-alt1
- initial build for ALT Linux Sisyphus

