%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl
%define babelver 1.4.0

Name: cca-spec-neo
Version: 0.2.8
Release: alt10
Summary: Neoclassic binding of the CCA specification and design pattern
License: LGPL
Group: Sciences/Mathematics
Url: http://www.cca-forum.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.cca-forum.org/download/cca-tools/cca-tools-0.7.0/cca-spec-neo-0.2.8.tar.gz

Requires: babel lib%name-devel = %version-%release

BuildPreReq: %mpiimpl-devel libgraphviz-devel doxygen boost-devel tcl-devel
BuildPreReq: babel gcc-c++ libxml2-devel graphviz
BuildPreReq: python-devel

%description
Neoclassic binding of the CCA specification and design pattern.

%package -n lib%name
Summary: Shared libraries of NEO CCA Specification
Group: System/Libraries
Requires: libbabel = %babelver

%description -n lib%name
Neoclassic binding of the CCA specification and design pattern.

This package contains shared libraries of NEO CCA Specification.

%package -n lib%name-devel
Summary: Development files of NEO CCA Specification
Group: Development/Other
Requires: lib%name = %version-%release
Requires: libbabel-devel = %babelver
Requires: %name-common = %version-%release

%description -n lib%name-devel
Neoclassic binding of the CCA specification and design pattern.

This package contains development files of NEO CCA Specification.

%package -n lib%name-devel-static
Summary: Static libraries of NEO CCA Specification
Group: Development/Other
Requires: lib%name-devel = %version-%release
Requires: libbabel-devel-static = %babelver

%description -n lib%name-devel-static
Neoclassic binding of the CCA specification and design pattern.

This package contains static libraries of NEO CCA Specification.

%package common
Summary: Architecture independent files of NEO CCA Specification
Group: Development/Other
BuildArch: noarch

%description common
Neoclassic binding of the CCA specification and design pattern.

This package contains architecture independent files of NEO CCA Specification.

%package doc
Summary: Documentation for NEO CCA Specification
Group: Development/Documentation
BuildArch: noarch

%description doc
Neoclassic binding of the CCA specification and design pattern.

This package contains development documentation for NEO CCA Specification.

%prep
%setup

%install
export INSTALL_ROOT=%buildroot%prefix
source %mpidir/bin/mpivars.sh
export LIBS="-Wl,-R%mpidir/lib -L%mpidir/lib -lmpi"
%configure \
	--with-boost=%prefix \
	--with-babel-libtool=%_bindir/babel-libtool \
	--with-mpi=%_libexecdir/%mpiimpl \
	--with-mpi-cxx=%_libexecdir/%mpiimpl/bin/mpicxx \
	--with-mpi-inc=%_libexecdir/%mpiimpl/include \
	--with-cca-neo=%buildroot%prefix \
	--with-xml2-config=%_bindir/xml2-config \
	--with-dot=%_bindir \
	--enable-showcompile \
	--enable-showlibtool \
	--with-doxygen \
	--with-xml2-includes=-I%_includedir/libxml2 \
	--with-xml2-libs='-lxml2 ' \
	--with-mpi=%mpidir \
	--with-mpi-arch=LINUX \
	--prefix=%buildroot%prefix
%make
%make_install install

%ifarch x86_64
install -d %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

sed -i "s|%buildroot||g" \
	$(egrep -R "%buildroot" %buildroot| egrep -v 'Binary file.*matches' |\
		awk -F : '{print $1}')
rm -fR %buildroot%_docdir/%name-%version/c++/man \
	%buildroot%_docdir/eg-neo-0.9.0 %buildroot%_docdir/neotest-go-0.1.0 \
	%buildroot%_docdir/neotest-parameter-0.1.0
install doc/README.NEO %buildroot%_docdir/%name-%version

%files
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

#files -n lib%name-devel-static
#_libdir/*.a

%files common
%_datadir/*
%exclude %_docdir

%files doc
%_docdir/*

%changelog
* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt10
- Disabled devel-static package

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt9
- Rebuilt with Boost 1.46.1

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt8
- Rebuilt for debuginfo

* Sun Feb 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt7
- Fixed build

* Mon Oct 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt6
- Fixed overlinking of libraries

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt5
- Rebuilt with python 2.6

* Mon Sep 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt4
- Rebuilt with updated babel

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt3
- Fixed work with temp files
- Rebuilt with fixed babel-libtool

* Sun Apr 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.8-alt1
- Initial build for Sisyphus

