#TODO: examples packing

%define oname hdf5
%define sover 7
%define cpp_sover 7
%define f_sover 7
%define hl_sover 7
%define hdfdir %_libdir/%oname-seq
%define priority 30
Name: lib%oname-%sover-seq
Version: 1.8.8
Release: alt2

Summary: Hierarchical Data Format 5 library

Group: System/Libraries
License: Nearly BSD, but changed sources must be marked
Url: http://www.hdfgroup.org/HDF5/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: ftp://ftp.hdfgroup.org/HDF5/current/src/%oname-%version.tar.bz2

Conflicts: lib%oname-mpi < 1.8.3-alt5
Provides: lib%oname = %version-%release
Provides: lib%oname-%sover = %version-%release
Conflicts: lib%oname-%sover < %version-%release
Obsoletes: lib%oname-%sover < %version-%release
%ifarch x86_64
Provides: lib%oname.so.%sover()(64bit)
Provides: lib%{oname}_hl.so.%sover()(64bit)
%else
Provides: lib%oname.so.%sover
Provides: lib%{oname}_hl.so.%sover
%endif
Requires(post,preun): alternatives

# Automatically added by buildreq on Sat Sep 15 2007
BuildRequires: gcc-c++ libssl-devel zlib-devel gcc-fortran

%description
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

%package -n lib%oname-devel
Summary: HDF5 library development package
Group: Development/C
Requires(post,preun): alternatives
Requires: libgfortran-devel libstdc++-devel zlib-devel
Requires: lib%oname = %version-%release
Conflicts: lib%oname-mpi-devel < 1.8.3-alt5

%description -n lib%oname-devel
Header files for HDF5 library.

%package -n %oname-%sover-tools
Summary: HDF5 tools
Group: Development/Tools
Requires(post,preun): alternatives
Requires: lib%oname = %version-%release
Conflicts: %oname-mpi-tools < 1.8.3-alt5
Conflicts: lib%oname < %version-%release
Provides: %oname-tools = %version-%release

%description -n %oname-%sover-tools
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

This package contains tools for work with HDF5.

%prep
%setup -q -n %oname-%version

%build
sed -i -e 's/(SOVER)/%sover/' src/H5detect.c
%autoreconf
%add_optflags -fno-strict-aliasing
%configure \
	--bindir=%hdfdir/bin \
	--libdir=%hdfdir/lib \
	--includedir=%hdfdir/include \
	--enable-cxx \
	--enable-linux-lfs \
	--enable-shared \
	--enable-production \
	--with-pthread \
	--with-ssl \
	--with-zlib \
	--enable-fortran \
	FC=f95

subst "s|^LT=.*|LT=../libtool|g" c++/src/Makefile c++/test/Makefile
cp src/lib%oname.settings src/lib%oname-%sover.settings
%make_build

%install
export LD_LIBRARY_PATH="../src/.libs"
install -d %buildroot%hdfdir/include

%makeinstall_std

mv %buildroot%hdfdir/lib/lib%oname.settings \
	%buildroot%hdfdir/lib/lib%oname-%sover.settings

# alternatives

install -d %buildroot%_altdir
mkdir -p %buildroot%_libdir
pushd %buildroot%hdfdir/lib
for i in $(ls *.so.*) $(ls *.settings); do
	ln -s ../..%hdfdir/lib/$i %buildroot%_libdir/
	echo "%_libdir/$i %hdfdir/lib/$i %priority" >> \
		%buildroot%_altdir/%name.alternatives
done
for i in $(ls *.so); do
	echo "%_libdir/$i %hdfdir/lib/$i %priority" >> \
		%buildroot%_altdir/%name-devel.alternatives
done
popd
pushd %buildroot%hdfdir/bin
for i in $(ls); do
	echo "%_bindir/$i %hdfdir/bin/$i %priority" >> \
		%buildroot%_altdir/%oname-tools.alternatives
done
popd

install -d %buildroot%_pkgconfigdir
cat <<EOF >%buildroot%_pkgconfigdir/%oname-seq.pc
prefix=%prefix
exec_prefix=%prefix
libdir=%hdfdir/lib
includedir=%hdfdir/include

Name: %oname
Description: Hierarchical Data Format 5 library
Version: %version
Libs: -lhdf5hl_fortran -lhdf5_hl_cpp -lhdf5_hl -lhdf_fortran -lhdf_cpp -lhdf -lgfortran -lstdc++ -lz
Cflags: -I%hdfdir/include
EOF

echo "%_pkgconfigdir/%oname.pc %_pkgconfigdir/%oname-seq.pc %priority" >> \
	%buildroot%_altdir/%name-devel.alternatives

%files
%doc COPYING README.txt release_docs/{HISTORY*,RELEASE.txt}
%ghost %_libdir/lib*.so.*
%hdfdir/lib/*.so.*
# used to show configuration at runtime
%hdfdir/lib/libhdf5-%sover.settings
%_altdir/%name.alternatives

%files -n lib%oname-devel
%hdfdir/lib/lib*.so
%hdfdir/include/*
%_pkgconfigdir/*
%_altdir/%name-devel.alternatives

%files -n %oname-%sover-tools
%hdfdir/bin/*
%_altdir/%oname-tools.alternatives

%changelog
* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt2
- Set native directory as %_libdir/%oname-seq instead of
  %_libexecdir/%oname-seq

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt1
- Version 1.8.8

* Tue Sep 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.7-alt1
- Version 1.8.7

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.6-alt1
- Version 1.8.6
- Disabled static package

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5_patch1-alt2
- Rebuilt for debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5_patch1-alt1
- Version 1.8.5-patch1

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt6
- Fixed soname set-versions by ghost links (thnx ldv@)

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt5
- Rebuilt for soname set-versions

* Wed Jul 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt4
- Added pkgconfig file

* Thu Jun 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt3
- Created alternatives

* Thu Jun 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt2
- Added explicit conflict with parallel version of HDF5 tools

* Thu May 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt1
- Version 1.8.3
- Added static libraries
- Add fortran interface libraries
- Add zlib support

* Sun Dec 14 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.6-alt2
- fixed build with gcc4.3

* Sat Sep 15 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6.6-alt1
- initial build for ALT Linux Sisyphus

