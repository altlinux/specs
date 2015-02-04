%def_with python3

Name: geos
Version: 3.5.0
Release: alt2.dev.git20150203

Summary: Geometry Engine - Open Source
Group: Sciences/Geosciences
License: LGPL
Url: http://geos.refractions.net/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/libgeos/libgeos.git
# branch: svn-trunk
Source: %name-%version.tar

# Automatically added by buildreq on Sun Nov 09 2008 (-bi)
BuildRequires: gcc-c++ python-devel swig

BuildPreReq: cmake doxygen graphviz
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

%description
GEOS (Geometry Engine - Open Source) is a C++ port of the Java
Topology Suite (JTS). As such, it aims to contain the complete
functionality of JTS in C++. This includes all the OpenGIS
"Simple Features for SQL" spatial predicate functions and
spatial operators, as well as specific JTS topology functions
such as IsValid().

%package doc
Summary: Documentation for GEOS
Group: Development/Documentation
BuildArch: noarch

%description doc
GEOS (Geometry Engine - Open Source) is a C++ port of the Java
Topology Suite (JTS). As such, it aims to contain the complete
functionality of JTS in C++. This includes all the OpenGIS
"Simple Features for SQL" spatial predicate functions and
spatial operators, as well as specific JTS topology functions
such as IsValid().

This package contains documentation for GEOS.

%package -n lib%name
Summary: Geometry Engine - Open Source
Group: Sciences/Geosciences

%description -n lib%name
GEOS (Geometry Engine - Open Source) is a C++ port of the Java
Topology Suite (JTS). As such, it aims to contain the complete
functionality of JTS in C++. This includes all the OpenGIS
"Simple Features for SQL" spatial predicate functions and
spatial operators, as well as specific JTS topology functions
such as IsValid().

%package -n lib%name-devel
Summary: Development files for the Geometry Engine - Open Source
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Development files for the Geometry Engine - Open Source

%package -n python-module-%name
Summary: Python bindings for the lib%name library
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%name
Python bindings for the lib%name library.

%package -n python3-module-%name
Summary: Python bindings for the lib%name library
Group: Development/Python3
Requires: lib%name = %version-%release

%description -n python3-module-%name
Python bindings for the lib%name library.

%package -n ruby-%name
Summary: Ruby bindings for the lib%name library
Group: Development/Ruby
Requires: lib%name = %version-%release

%description -n ruby-%name
Ruby bindings for the lib%name library.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
./autogen.sh
%configure \
	--disable-static \
	--enable-python \
	--disable-ruby

%if_with python3
pushd ../python3
sed -i 's|\(\-python\)|\1 -py3|' macros/ac_pkg_swig.m4
sed -i 's|python\${PYTHON_VERSION}|python\${PYTHON_VERSION}m|' \
	macros/ac_python_devel.m4
export PYTHON=python3
./autogen.sh
%configure \
	--disable-static \
	--enable-python \
	--disable-ruby
export PYTHON=
popd
%endif

%if %_lib == lib64
LIB_SUFFIX=64
%endif

mkdir BUILD
pushd BUILD
cmake \
	-DLIB_SUFFIX=$LIB_SUFFIX \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS:STRING="%optflags" \
	-DCMAKE_Fortran_FLAGS:STRING="%optflags" \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	..

%make_build VERBOSE=1
popd

%make -C swig/python LIB_SUFFIX=$LIB_SUFFIX \
	ENABLE_PYTHON=1 ENABLE_SWIG=1

%if_with python3
ln -s $PWD/BUILD ../python3/
%make -C ../python3/swig/python LIB_SUFFIX=$LIB_SUFFIX \
	ENABLE_PYTHON=1 ENABLE_SWIG=1
%endif

%make -C doc doxygen-html

%install
%makeinstall_std -C BUILD

%if %_lib == lib64
LIB_SUFFIX=64
%endif
%makeinstall_std -C swig/python LIB_SUFFIX=$LIB_SUFFIX \
	ENABLE_PYTHON=1 ENABLE_SWIG=1

rm -f %buildroot%python_sitelibdir/geos/*.la
rm -f %buildroot%ruby_sitearchdir/*.la

%if_with python3
%makeinstall_std -C ../python3/swig/python LIB_SUFFIX=$LIB_SUFFIX \
	ENABLE_PYTHON=1 ENABLE_SWIG=1
rm -f %buildroot%python3_sitelibdir/geos/*.la
%endif

bzip2 ChangeLog

%files -n lib%name
%doc AUTHORS ChangeLog* COPYING NEWS README TODO
%_libdir/lib*.so.*

%files -n lib%name-devel
%_bindir/%name-config
%_libdir/lib*.so
%_includedir/*

%files -n python-module-%name
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*
%endif

%if 0
%files -n ruby-%name
%ruby_sitearchdir/*
%endif

%files doc
%doc doc/doxygen_docs/html/*

%changelog
* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2.dev.git20150203
- New snapshot

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1.dev.svn20140925
- New snapshot
- Added module for Python 3

* Thu Jul 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1.dev.svn20140630
- New snapshot

* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1.dev.svn20140521
- New snapshot

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1.dev.svn20130913
- Version 3.5.0dev

* Fri Jun 21 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1.svn20130612
- New snapshot

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1.svn20130201
- New snapshot

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1.svn20120910
- New snapshot

* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1.svn20120116
- Version 3.4.0

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt2.svn20110511
- Rebuilt

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3.0-alt1.svn20110511.1
- Rebuild with Python-2.7

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.svn20110511
- New snapshot

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.svn20101015.1
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.svn20101015
- New snapshot

* Mon Jul 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.svn20100708
- New snapshot

* Tue Feb 09 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.svn20100206
- Version 3.3.0 (svn snapshot)

* Fri Feb 05 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.0-alt1
- Version 3.2.0

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt3
- Rebuilt with python 2.6

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 3.0.2-alt2.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libgeos
  * postun_ldconfig for libgeos
  * postclean-05-filetriggers for spec file

* Fri Jul 03 2009 Alexey I. Froloff <raorn@altlinux.org> 3.0.2-alt2
- Rebuilt without ruby (swing fails to create correct code for 1.9)

* Sat Nov 08 2008 Sir Raorn <raorn@altlinux.ru> 3.0.2-alt1
- [3.0.2]
- Built with python and ruby support
- Dropped XMLTester (closes: #11455)

* Sat Mar 24 2007 Sir Raorn <raorn@altlinux.ru> 2.2.3-alt1
- Built for Sisyphus

