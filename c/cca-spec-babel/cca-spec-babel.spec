%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl
%define babelver 1.4.0

Name: cca-spec-babel
Version: 0.8.6
Release: alt4.svn20090721.1
Summary: The Common Component Architecture Specification for Babel
License: LGPL
Group: Sciences/Mathematics
Url: http://www.cca-forum.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

Requires: lib%name = %version-%release
Requires: lib%name-devel = %version-%release
Requires: lib%name-j = %version-%release
Requires: python-module-%name = %version-%release
Requires: babel >= %babelver
%add_python_req_skip Index Symbol boccalib

BuildRequires(pre): rpm-build-python rpm-build-java /proc
BuildPreReq: %mpiimpl-devel libgraphviz-devel doxygen boost-devel
BuildPreReq: gcc-fortran gcc-c++ libbabel-devel libxml2-devel tcl-devel babel
BuildPreReq: python-devel libgfortran-devel chrpath
BuildPreReq: java-devel-default libnumpy-devel graphviz

%description
The Common Component Architecture Specification for Babel.

%package -n lib%name
Summary: Shared libraries of CCA Specification for Babel
Group: System/Libraries
Requires: libbabel >= %babelver

%description -n lib%name
The Common Component Architecture Specification for Babel.

This package contains shared libraries of CCA Specification for Babel.

%package -n lib%name-devel
Summary: Development files of CCA Specification for Babel
Group: Development/Other
Requires: libbabel-devel >= %babelver
Requires: lib%name = %version-%release
Requires: %name = %version-%release
Requires: lib%name-j = %version-%release
Requires: python-module-%name = %version-%release

%description -n lib%name-devel
The Common Component Architecture Specification for Babel.

This package contains development files of CCA Specification for Babel.

%package -n lib%name-devel-static
Summary: Static libraries of CCA Specification for Babel
Group: Development/Other
Requires: libbabel-devel-static >= %babelver
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
The Common Component Architecture Specification for Babel.

This package contains static libraries of CCA Specification for Babel.

%package -n lib%name-j
Summary: Java library of CCA Specification for Babel
Group: Development/Java
#BuildArch: noarch
Requires: java babel-j >= %babelver

%description -n lib%name-j
The Common Component Architecture Specification for Babel.

This package contains java library of CCA Specification for Babel.

%package -n python-module-%name
Summary: Python modules of CCA Specification for Babel
Group: Development/Python
Requires: python-module-sidl >= %babelver
Requires: python-module-sidlx >= %babelver
Requires: lib%name = %version-%release
Requires: %name = %version-%release
%py_provides CCAXMLQuery

%description -n python-module-%name
The Common Component Architecture Specification for Babel.

This package contains python modules of CCA Specification for Babel.

%package doc
Summary: Documentation for CCA Specification for Babel
Group: Development/Documentation
BuildArch: noarch

%description doc
The Common Component Architecture Specification for Babel.

This package contains development documentation for CCA Specification for Babel.


%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export MPI=%mpidir

%add_optflags -fno-strict-aliasing
%autoreconf
%configure \
	--enable-showcompile \
	--enable-showlibtool \
	--enable-mpi=yes \
	--with-boost=yes \
	--with-tclsh=%_bindir/tclsh \
	--with-babel-config=%_bindir/babel-config \
	--with-babel=%prefix \
	--with-libxml2=%prefix \
	--with-util-python=%_bindir/python \
	--with-babel-python
%make_build

pushd doc
%make_build
popd

%install
install -d %buildroot%_libexecdir
%makeinstall_std
install -d %buildroot%_libdir
install -d %buildroot%_javadir
install -d %buildroot%_docdir/%name/html
TOPDIR=$PWD

pushd %buildroot%_libexecdir/
if [ -s cca-spec.jar ]; then
	rm -f cca-spec.jar
fi
%ifarch x86_64
install -d %buildroot%python_sitelibdir
install -d %buildroot%_javadir
mv *.so* *.a %buildroot%_libdir/
mv python%_python_version/site-packages/* \
	%buildroot%python_sitelibdir/
mv $(find $TOPDIR -name '*.jar') \
	%buildroot%_javadir/
%else
mv $(find ./ -name '*.jar') \
	%buildroot%_javadir/
%endif
popd
pushd %buildroot%_javadir
if [ ! -f cca-spec.jar ]; then
	ln -s $(ls *.jar) cca-spec.jar
fi
popd

install -m644 doc/html/* %buildroot%_docdir/%name/html

for i in %buildroot%_libdir/*.so
do
	chrpath -d $i
done
%ifnarch x86_64
for i in %buildroot%_libdir/%name-*/*.so
do
	chrpath -d $i
done
%endif

%files
%doc CHANGELOG TODO
%_bindir/*
%_datadir/cca
%_datadir/%name-*-babel-%babelver

%files -n lib%name
%_libdir/*.so.*
%dir %_libdir/%name-*
%ifnarch x86_64
%_libdir/%name-*/*.so.*
%endif

%files -n lib%name-devel
%_libdir/*.so
%ifnarch x86_64
%_libdir/%name-*/*.so
%endif
%_includedir/*

#files -n lib%name-devel-static
#_libdir/*.a
#ifnarch x86_64
#_libdir/%name-*/*.a
#endif

%files -n python-module-%name
%python_sitelibdir/*
#_libdir/%name-*/python%_python_version

%files -n lib%name-j
%_javadir/*.jar

%files doc
%_docdir/%name

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.6-alt4.svn20090721.1
- Rebuild to remove redundant libpython2.7 dependency

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt4.svn20090721
- Fixed RPATH

* Tue Dec 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt3.svn20090721
- Disabled devel-static package

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.6-alt2.svn20090721.9.1
- Rebuild with Python-2.7

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt2.svn20090721.9
- Rebuilt with Boost 1.46.1

* Thu Mar 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt2.svn20090721.8
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt2.svn20090721.7
- Rebuilt for soname set-versions

* Thu Mar 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt2.svn20090721.6
- Fixed build on x86_64

* Thu Dec 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt2.svn20090721.5
- Enabled requirement on bocca

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt2.svn20090721.4
- Rebuilt with python 2.6 (bootstrap)

* Mon Sep 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt2.svn20090721.3
- Rebuilt with updatet babel

* Fri Sep 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt2.svn20090721.2
- Set doc and java packages as noarch

* Thu Sep 10 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt2.svn20090721.1
- Disabled strict-aliasing rules

* Thu Jul 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt2.svn20090721
- Snapshot 20090721
- Resolved conflict with babel
- Enabled x86_64 arch

* Sat Jun 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.6-alt1
- Initial build for Sisyphus

