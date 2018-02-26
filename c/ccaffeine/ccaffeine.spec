%define mpiimpl openmpi
%define mpidir %_libexecdir/%mpiimpl

%define _ver 0_8_8
%define somver 0
%define sover %somver.8.8
%define classic_ver 0.5.7
Name: ccaffeine
Version: %sover
Release: alt5.svn20100330
Summary: CCA framework compliant with the CCA specification
License: LGPL
Group: Sciences/Mathematics
Url: http://www.cca-forum.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

Requires: lib%name-devel = %version-%release
Requires: %name-common = %version-%release

BuildPreReq: doxygen gcc-c++ gcc-fortran libgraphviz-devel graphviz babel
BuildPreReq: cca-spec-classic cca-spec-babel cca-spec-neo libreadline-devel
BuildPreReq: tcl-devel libruby-devel ruby swig %mpiimpl-devel
BuildPreReq: libxml2-devel boost-devel libnumpy-devel
BuildPreReq: python-devel doc++ libcca-spec-babel-devel libbabel-devel

%description
The Common Component Architecture Framework compliant with the CCA
specification.

%package -n lib%name
Summary: Shared libraries of CCA Caffeine Framework
Group: System/Libraries

%description -n lib%name
The Common Component Architecture Framework compliant with the CCA
specification.

This package contains shared libraries of CCA Caffeine Framework.

%package -n lib%name-devel
Summary: Development files of CCA Caffeine Framework
Group: Development/Other
Requires: lib%name = %version-%release
Requires: %name-common = %version-%release

%description -n lib%name-devel
The Common Component Architecture Framework compliant with the CCA
specification.

This package contains development files of CCA Caffeine Framework.

%package -n lib%name-devel-static
Summary: Static libraries of CCA Caffeine Framework
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
The Common Component Architecture Framework compliant with the CCA
specification.

This package contains static libraries of CCA Caffeine Framework.

%package common
Summary: Architecture independent files of CCA Caffeine Framework
Group: Development/Other
BuildArch: noarch

%description common
The Common Component Architecture Framework compliant with the CCA
specification.

This package contains architecture independent files of CCA Caffeine Framework.

%package doc
Summary: Documentation for CCA Caffeine Framework
Group: Development/Documentation
BuildArch: noarch

%description doc
The Common Component Architecture Framework compliant with the CCA
specification.

This package contains development documentation for CCA Caffeine Framework.

%package examples
Summary: Demonstrating use of an installed CCA Caffeine Framework
Group: Development/Documentation
BuildArch: noarch

%description examples
The Common Component Architecture Framework compliant with the CCA
specification.

This package contains examples witch demonstrating use of an installed CCA
Caffeine Framework.

%package -n python-module-%name
Summary: Python module of CCA Caffeine Framework
Group: Development/Python
%setup_python_module %name

%description -n python-module-%name
The Common Component Architecture Framework compliant with the CCA
specification.

This package contains Python module of CCA Caffeine Framework.

%package -n python-module-%name-devel
Summary: Headers for Python module of CCA Caffeine Framework
Group: Development/Python
Requires: python-module-%name = %version-%release
Requires: lib%name-devel = %version-%release

%description -n python-module-%name-devel
The Common Component Architecture Framework compliant with the CCA
specification.

This package contains headers for Python module of CCA Caffeine Framework.

%package -n python-module-ccafe
Summary: CCAFE Python module
Group: Development/Python
%setup_python_module ccafe0
%setup_python_module ccafe3

%description -n python-module-ccafe
The Common Component Architecture Framework compliant with the CCA
specification.

This package contains CCAFE Python module.

%package -n python-module-ccafe-devel
Summary: Headers for CCAFE Python module
Group: Development/Python
Requires: python-module-ccafe = %version-%release
Requires: python-module-%name-devel = %version-%release
Requires: lib%name-devel = %version-%release

%description -n python-module-ccafe-devel
The Common Component Architecture Framework compliant with the CCA
specification.

This package contains headers for CCAFE Python module.


%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

%autoreconf
%configure \
	--enable-shared \
	--enable-threads \
	--enable-sockets \
	--enable-showlibtool \
	--enable-showcompile \
	--enable-shell \
	--with-bash=/bin/bash \
	--with-cca-babel \
	--with-cca-neo \
	--with-cca-classic=%prefix \
	--with-rpm-prefix=%prefix \
	--with-rpm-libdir=%_libdir \
	--with-rpm-pkgdatadir=%_datadir \
	--with-gmake=%_bindir/make \
	--with-tclsh=%_bindir/tclsh \
	--with-ruby=%_bindir/ruby \
	--with-swig=%_bindir/swig \
	--with-xml2-config=%_bindir/xml2-config \
	--with-xml2-includes=-I%_includedir/libxml2 \
	--with-xml2-libs='-lxml2' \
	--with-doxygen=%_bindir/doxygen \
	--with-dot=yes \
	--with-boost=%_includedir \
	--with-babel-libtool=%_bindir/babel-libtool \
	--without-babel-python \
	--with-mpi=%mpidir \
	--with-mpi-arch='LINUX' \
	--with-mpi-inc=-I%mpidir/include \
	--with-mpi-ldflags-dynamic="-Wl,-R%mpidir/lib" \
	--with-mpi-bin=%mpidir/bin \
%ifarch x86_64
	--enable-64bit \
%endif
	--with-tools=gnu

export SCAN_CCA_XML=/usr/bin/scanCCAxml.x
# parallel build is broken
%make MPIDIR=%mpidir INSTALL_ROOT=%buildroot%prefix

pushd cxx/doc
%make_build
popd

%install
source %mpidir/bin/mpivars.sh
export OMPI_LDFLAGS="-Wl,--as-needed,-R,%mpidir/lib -L%mpidir/lib"

for dir in cxx/obj/.libs cxx/drivers/.libs; do
	pushd  $dir
	for i in $(ls *.la); do
		cp -f $i ${i}i
	done
	popd
done
%makeinstall_std MPIDIR=%mpidir INSTALL_ROOT=%buildroot%prefix

install -d %buildroot%_docdir/%name/html/cxx
install -d %buildroot%_man3dir

pushd cxx/dox
install -m644 man/man3/* %buildroot%_man3dir
install -m644 html/* %buildroot%_docdir/%name/html/cxx
popd

cp -fR examples %buildroot%_docdir/%name/

rm -f %buildroot%_libdir/*.la %buildroot%_libdir/ccafe-%version/*.la

# generating shared libraries

pushd %buildroot%_libdir
function compl () {
	rm -f $1.so* $1_%_ver.so
	ar x ${1}_%_ver.a
	mpicxx -shared \
		-Wl,-soname,$1.so.%somver \
		-o $1.so.%sover *.o \
		-Wl,-R%mpidir/lib -L$PWD $2 \
		-lsidlx -lsidlstub_cxx \
		-lsidl \
		-lcca_0_8_6_b_1.4.0-cxx \
		-lParameter-0.1.0 \
		-lSimpleStamper-0.9.0 -lneocca-0.2.8 \
		-lxml2 -lreadline
	ln -s $1.so.%sover $1.so.%somver
	ln -s $1.so.%sover ${1}_%_ver.so
	ln -s $1.so.%somver $1.so
	rm *.o -f
}

for i in $(ls *%_ver.a|sed 's|_%_ver\.a||'); do
	compl $i
done
compl libMPIComponent "-lccaffeine -lccafeCore"
compl libccafeCore "-lccaffeine -lMPIComponent -lpthread"
compl libStringConsumerPort "-lccaffeine"
for i in ccaffeine ccafeDrivers ccafePreload
do
	compl lib$i "-lccafeCore -lMPIComponent -lpthread"
done

for i in GoComponent PortTranslatorStarter PrinterComponent SCPProxy \
	StarterComponent classicTimeStamper \
	BasicParameterPortTest ConnectionEventServiceTest GUIServiceTest \
	ParameterPortFactoryTest ServiceRegistryTest SimpleProxyTest \
	TestMPI classicBSTest classicGoTest
do
	if [ "$i" = "SimpleProxyTest" ]; then
		compl lib$i "-lStringConsumerPort -lccaffeine -lccafeCore"
	else
		compl lib$i "-lStringConsumerPort -lccaffeine -lccafeDrivers -lccafeCore"
	fi
done

popd

%files
%doc *.html *.txt Changelog.* README* TODO*
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_libdir/*.cca
%_libdir/*.scl
%_includedir/*
#exclude %_includedir/python%_python_version

%files -n lib%name-devel-static
%_libdir/*.a
%_libdir/ccafe-%version

%files common
%dir %_datadir/ccafe-%version
%_datadir/ccafe-%version/*
%exclude %_datadir/ccafe-%version/examples

%files doc
%_docdir/%name
%exclude %_docdir/%name/examples
%_man3dir/*

%files examples
%_docdir/%name/examples
%dir %_datadir/ccafe-%version
%_datadir/ccafe-%version/examples

#files -n python-module-%name
#python_sitelibdir/%name
#python_sitelibdir/llnl_babel_%{name}*.egg-info

#files -n python-module-%name-devel
#dir %_includedir/python%_python_version
#_includedir/python%_python_version/llnl_babel_ccaffeine

#files -n python-module-ccafe
#python_sitelibdir/ccafe*
#python_sitelibdir/llnl_babel_ccafe0_ccafe3*.egg-info

#files -n python-module-ccafe-devel
#dir %_includedir/python%_python_version
#_includedir/python%_python_version/llnl_babel_ccafe*

%changelog
* Mon May 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt5.svn20100330
- Fixed build

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt4.svn20100330
- Fixed RPATH

* Thu Nov 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt3.svn20100330
- Fixed build

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt2.svn20100330.4
- Rebuilt with Boost 1.46.1

* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt2.svn20100330.3
- Rebuilt for debuginfo

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt2.svn20100330.2
- Rebuilt for soname set-versions

* Wed Oct 13 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt2.svn20100330.1
- Fixed linking

* Wed Mar 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt2.svn20100330
- New snapshot
- Disabled python modules

* Sat Feb 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt2.svn20090721.2
- Rebuilt with reformed NumPy

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt2.svn20090721.1
- Rebuilt with python 2.6

* Thu Sep 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt2.svn20090721
- Enabled MPI
- Added shared libraries
- Rebuilt with doc++ and fixed babel

* Thu Jul 02 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.8-alt1.1
- Use ruby(fileutils) instead of obsolete ruby(ftools)

* Sun Apr 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.8-alt1
- Initial build for Sisyphus

