Name: geos3
Version: 3.3.0
Release: alt1.svn20101015.2

Summary: Geometry Engine - Open Source
Group: Sciences/Geosciences
License: LGPL
Url: http://geos.refractions.net/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.osgeo.org/geos/trunk
Source: %name-%version.tar

# Automatically added by buildreq on Sun Nov 09 2008 (-bi)
BuildRequires: gcc-c++ python-devel swig

%description
GEOS (Geometry Engine - Open Source) is a C++ port of the Java
Topology Suite (JTS). As such, it aims to contain the complete
functionality of JTS in C++. This includes all the OpenGIS
"Simple Features for SQL" spatial predicate functions and
spatial operators, as well as specific JTS topology functions
such as IsValid().

%package -n lib%name
Summary: Geometry Engine - Open Source
Group: System/Legacy libraries

%description -n lib%name
GEOS (Geometry Engine - Open Source) is a C++ port of the Java
Topology Suite (JTS). As such, it aims to contain the complete
functionality of JTS in C++. This includes all the OpenGIS
"Simple Features for SQL" spatial predicate functions and
spatial operators, as well as specific JTS topology functions
such as IsValid().

%package -n lib%name-devel
Summary: Development headers for the Geometry Engine - Open Source
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Dedelopment headers for the Geometry Engine - Open Source

%package -n python-module-%name
Summary: Python bindings for the lib%name library
Group: Development/Python
Requires: lib%name = %version-%release

%description -n python-module-%name
Python bindings for the lib%name library.

%package -n ruby-%name
Summary: Ruby bindings for the lib%name library
Group: Development/Ruby
Requires: lib%name = %version-%release

%description -n ruby-%name
Ruby bindings for the lib%name library.

%prep
%setup

%build
ACLOCAL="aclocal -I macros" %autoreconf -I macros
%add_optflags -fno-strict-aliasing
%configure \
	--disable-static \
	--enable-python \
	--disable-ruby
%make_build

%install
%make_install DESTDIR=%buildroot install
rm -f %buildroot%python_sitelibdir/geos/*.la
rm -f %buildroot%ruby_sitearchdir/*.la
rm -fR %buildroot%_includedir

#bzip2 ChangeLog

%files -n lib%name
#doc AUTHORS ChangeLog* COPYING NEWS README TODO
%_libdir/lib*3.3.0.so

#files -n lib%name-devel
#_bindir/%name-config
#_libdir/lib*.so
#_includedir/*

#files -n python-module-%name
#python_sitelibdir/*

%if 0
%files -n ruby-%name
%ruby_sitearchdir/*
%endif

%changelog
* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.0-alt1.svn20101015.2
- Moved this version into System/Legacy libraries

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

