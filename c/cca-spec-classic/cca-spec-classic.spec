%define _ver 0_5_7
Name: cca-spec-classic
Version: 0.5.7
Release: alt7
Summary: Classic Common Component Architecture Specification
License: LGPL
Group: Sciences/Mathematics
Url: http://www.cca-forum.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.cca-forum.org/download/cca-tools/cca-tools-0.7.0/cca-spec-classic-0.5.7.tar.gz

Requires: lib%name = %version-%release
Requires: lib%name-devel = %version-%release
Requires: %name-common = %version-%release
Requires: lib%name-j = %version-%release

BuildRequires(pre): rpm-build-java
BuildPreReq: java-devel-default /proc doxygen gcc-c++ graphviz
BuildPreReq: libgraphviz-devel babel tcl-devel

%description
The Classic Common Component Architecture Specification.

%package -n lib%name
Summary: Shared libraries of Classic CCA Specification
Group: System/Libraries

%description -n lib%name
The Classic Common Component Architecture Specification.

This package contains shared libraries of Classic CCA Specification.

%package -n lib%name-devel
Summary: Development files of Classic CCA Specification
Group: Development/Other
Requires: lib%name = %version-%release
Requires: %name-common = %version-%release
Requires: lib%name-j = %version-%release

%description -n lib%name-devel
The Classic Common Component Architecture Specification.

This package contains development files of Classic CCA Specification.

%package -n lib%name-devel-static
Summary: Static libraries of Classic CCA Specification
Group: Development/Other
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
The Classic Common Component Architecture Specification.

This package contains static libraries of Classic CCA Specification.

%package -n lib%name-j
Summary: Java library of Classic CCA Specification
Group: Development/Java
BuildArch: noarch
Requires: java
Requires: %name-common = %version-%release

%description -n lib%name-j
The Classic Common Component Architecture Specification.

This package contains java library of Classic CCA Specification.

%package common
Summary: Architecture independent files of Classic CCA Specification
Group: Development/Other
BuildArch: noarch

%description common
The Classic Common Component Architecture Specification.

This package contains architecture independent files of Classic CCA
Specification.

%package doc
Summary: Documentation for Classic CCA Specification
Group: Development/Documentation
BuildArch: noarch

%description doc
The Classic Common Component Architecture Specification.

This package contains development documentation for Classic CCA Specification.

%package javadoc
Summary: Javadoc for Classic CCA Specification
Group: Development/Documentation
BuildArch: noarch

%description javadoc
The Classic Common Component Architecture Specification.

This package contains javadoc for Classic CCA Specification.


%prep
%setup

%build
%autoreconf
%configure \
%ifarch x86_64
	--enable-64bit \
%endif
	--enable-showcompile \
	--enable-showlibtool \
	--enable-gcc \
	--enable-shared \
	--with-babel-libtool=%_bindir/babel-libtool \
	--with-jdk12=%_libexecdir/jvm/java \
	--with-gmake=%_bindir/make \
	--with-tclsh=%_bindir/tclsh \
	--with-doxygen=%_bindir/doxygen
%make_build

%install
%makeinstall_std

pushd %buildroot%_libdir/%name-%version
rm -f libclassic.so libclassic.a
ln -s %_libdir/libclassic_%_ver.so libclassic.so
ln -s %_libdir/libclassic_%_ver.a libclassic.a
popd

install -d %buildroot%_man3dir
install -d %buildroot%_javadir
install -d %buildroot%_javadocdir/%name-%version

install -m644 java/*.jar %buildroot%_javadir
rm -f java/doc/Makefile java/doc/README
rm -fR %buildroot%_docdir/%name-%version/java
cp -fR java/doc/* %buildroot%_javadocdir/%name-%version/
mv %buildroot%_docdir/%name-%version/c++/man/man3/* %buildroot%_man3dir/
rm -fR %buildroot%_docdir/%name-%version/c++/man

%files
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%dir %_libdir/%name-%version
%_libdir/%name-%version/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a
%_libdir/%name-%version/*.a

%files -n lib%name-j
%_javadir/*.jar

%files common
%_datadir/%name-%version

%files doc
%_docdir/%name-%version
%_man3dir/*

%files javadoc
%_javadocdir/%name-%version

%changelog
* Mon Feb 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.7-alt7
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.7-alt6
- Rebuilt for soname set-versions

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.7-alt5
- Rebuilt with python 2.6

* Mon Sep 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.7-alt4
- Rebuilt with updated babel

* Tue Sep 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.7-alt3
- Rebuilt with fixed babel-libtool
- Added requirement for %name on lib%name-devel

* Thu May 14 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.7-alt2
- Rebuild with babel for gcc 4.4

* Sun Apr 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.7-alt1
- Initial build for Sisyphus

