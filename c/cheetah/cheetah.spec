%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

%define somver 0
%define sover %somver.1.1
Name: cheetah
Version: 1.1.4
Release: alt7
Summary: High performance messaging library
License: Free
Group: Networking/Other
Url: http://acts.nersc.gov/pete/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: gcc-c++ %mpiimpl-devel chrpath

%description
Cheetah is a high performance messaging library which provides get/put
and invoke (remote method invocation) semantics.

%package -n lib%name
Summary: Shared library of Cheetah
Group: System/Libraries

%description -n lib%name
Cheetah is a high performance messaging library which provides get/put
and invoke (remote method invocation) semantics.

This package contains shared library of Cheetah.

%package -n lib%name-devel
Summary: Development files of Cheetah
Group: Development/C++
Requires: %name = %version-%release
Requires: %mpiimpl-devel
Requires: lib%name = %version-%release

%description -n lib%name-devel
Cheetah is a high performance messaging library which provides get/put
and invoke (remote method invocation) semantics.

This package contains development files of Cheetah.

%package -n lib%name-devel-doc
Summary: Documentation and examples for Cheetah
Group: Development/Documentation
BuildArch: noarch
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-doc
Cheetah is a high performance messaging library which provides get/put
and invoke (remote method invocation) semantics.

This package contains development documentation and examples for Cheetah.

%prep
%setup
rm -fR $(find ./ -name CVS)

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed -Wl,-rpath,%mpidir/lib -L%mpidir/lib"

sed -i 's|@MPIDIR@|%mpidir|g' configure
sed -i 's|@SOMVER@|%somver|g' configure
sed -i 's|@SOVER@|%sover|g' configure
./configure \
	--shared \
	--prefix %prefix \
	--arch LINUXGCC \
	--opt \
	--ex \
	--mpi \
	--ulm
pushd lib/LINUXGCC
%make_build
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed -Wl,-rpath,%mpidir/lib -L%mpidir/lib"
TOPDIR=$PWD
pushd lib/LINUXGCC
%make_install CHEETAH_INSTALL_DIR=%buildroot%prefix install
popd

install -d %buildroot%_includedir/%name
if [ ! -d %buildroot%_libdir ]; then
	install -d %buildroot%_libdir
	mv %buildroot%_libexecdir/*.so.* %buildroot%_libdir/
fi
ln -s lib%name.so.%somver %buildroot%_libdir/lib%name.so
#chrpath -r %mpidir/lib %buildroot%_libdir/lib%name.so.*

mv %buildroot%_libexecdir/*.h %buildroot%_libexecdir/Makefile* \
	%buildroot%prefix/src/* \
	%buildroot%_includedir/%name

install -d %buildroot%_docdir/%name/html
install -p -m644 doc/* %buildroot%_docdir/%name
install -p -m644 html/* %buildroot%_docdir/%name/html

%files
%doc README

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/%name

%files -n lib%name-devel-doc
%_docdir/%name

%changelog
* Tue Jun 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt7
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt6
- Fixed RPATH

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt5
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt4
- Rebuilt for debuginfo

* Tue Oct 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt3
- Rebuilt for soname set-versions

* Tue Sep 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt2
- Built with shared library

* Sun May 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt1
- Initial build for Sisyphus
