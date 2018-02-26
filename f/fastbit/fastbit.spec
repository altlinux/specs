Name: fastbit
Version: ibis1.3.0.3
Release: alt1.svn20120601
Summary: An Efficient Compressed Bitmap Index Technology
License: LGPL v2.1 or later
Group: Development/Databases
Url: https://sdm.lbl.gov/fastbit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://codeforge.lbl.gov/anonscm/fastbit/trunk
Source: %name-%version.tar.gz

BuildPreReq: java-devel-default flex gcc-c++ doxygen graphviz
BuildPreReq: sharutils ant /proc

%description
FastBit is an open-source data processing library following the spirit
of NoSQL movement. It offers a set of searching functions supported by
compressed bitmap indexes. It treats user data in the column-oriented
fashion similar to well-known database management systems such as Sybase
IQ, MonetDB, and Vertica. It is designed to accelerate user's data
selection tasks without imposing undue requirements. In particular, the
user data is NOT required to be under the control of FastBit software.

%package -n lib%name
Summary: Shared libraries of FastBit
Group: System/Libraries

%description -n lib%name
FastBit is an open-source data processing library following the spirit
of NoSQL movement. It offers a set of searching functions supported by
compressed bitmap indexes. It treats user data in the column-oriented
fashion similar to well-known database management systems such as Sybase
IQ, MonetDB, and Vertica. It is designed to accelerate user's data
selection tasks without imposing undue requirements. In particular, the
user data is NOT required to be under the control of FastBit software.

This package contains shared libraries of FastBit.

%package -n lib%name-devel
Summary: Development files of FastBit
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
FastBit is an open-source data processing library following the spirit
of NoSQL movement. It offers a set of searching functions supported by
compressed bitmap indexes. It treats user data in the column-oriented
fashion similar to well-known database management systems such as Sybase
IQ, MonetDB, and Vertica. It is designed to accelerate user's data
selection tasks without imposing undue requirements. In particular, the
user data is NOT required to be under the control of FastBit software.

This package contains development files of FastBit.

%package -n lib%name-devel-doc
Summary: Documentation for FastBit
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
FastBit is an open-source data processing library following the spirit
of NoSQL movement. It offers a set of searching functions supported by
compressed bitmap indexes. It treats user data in the column-oriented
fashion similar to well-known database management systems such as Sybase
IQ, MonetDB, and Vertica. It is designed to accelerate user's data
selection tasks without imposing undue requirements. In particular, the
user data is NOT required to be under the control of FastBit software.

This package contains development documentation for FastBit.

%package examples
Summary: Examples for FastBit
Group: Development/Databases
Requires: lib%name = %version-%release
Conflicts: ibutils

%description examples
FastBit is an open-source data processing library following the spirit
of NoSQL movement. It offers a set of searching functions supported by
compressed bitmap indexes. It treats user data in the column-oriented
fashion similar to well-known database management systems such as Sybase
IQ, MonetDB, and Vertica. It is designed to accelerate user's data
selection tasks without imposing undue requirements. In particular, the
user data is NOT required to be under the control of FastBit software.

This package contains examples for FastBit.

%package j
Summary: FastBit Java interface
Group: Development/Databases
BuildArch: noarch
Requires: lib%name = %version-%release
Requires: jakarta-commons-logging junit log4j

%description j
FastBit is an open-source data processing library following the spirit
of NoSQL movement. It offers a set of searching functions supported by
compressed bitmap indexes. It treats user data in the column-oriented
fashion similar to well-known database management systems such as Sybase
IQ, MonetDB, and Vertica. It is designed to accelerate user's data
selection tasks without imposing undue requirements. In particular, the
user data is NOT required to be under the control of FastBit software.

This package contains FastBit Java interface.

%package j-javadoc
Summary: Javadoc for FastBit Java interface
Group: Development/Databases
BuildArch: noarch

%description j-javadoc
FastBit is an open-source data processing library following the spirit
of NoSQL movement. It offers a set of searching functions supported by
compressed bitmap indexes. It treats user data in the column-oriented
fashion similar to well-known database management systems such as Sybase
IQ, MonetDB, and Vertica. It is designed to accelerate user's data
selection tasks without imposing undue requirements. In particular, the
user data is NOT required to be under the control of FastBit software.

This package contains Javadoc for FastBit Java interface.

%prep
%setup

%build
%autoreconf
%add_optflags -fno-strict-aliasing
%configure \
	--enable-static=no \
	--disable-debug \
	--with-java=%_libexecdir/jvm/java
%make_build

pushd java
ant build
ant buildJar

mkdir tmp
cp -fR gov tmp/
pushd tmp
javadoc javadoc gov.lbl.fastbit
rm -f gov/lbl/fastbit/*.java
popd
popd

pushd src
doxygen
popd

%install
%makeinstall_std

install -d %buildroot%_includedir/%name
mv %buildroot%_includedir/*.h* %buildroot%_includedir/%name/

install -d %buildroot%_javadir
install -m644 java/distr/* %buildroot%_javadir

install -d %buildroot%_javadocdir/%name
cp -fR java/tmp/* %buildroot%_javadocdir/%name/

gzip ChangeLog

%files examples
%doc examples/*.c* examples/Makefile examples/README
%_bindir/*

%files -n lib%name
%doc AUTHORS COPYING ChangeLog* NEWS README
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%doc doc/*

%files j
%_javadir/*

%files j-javadoc
%_javadocdir/%name

%changelog
* Sun Jun 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> ibis1.3.0.3-alt1.svn20120601
- Version ibis1.3.0.3

* Fri Dec 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> ibis1.2.6.1-alt1.svn20111215
- Version ibis1.2.6.1

* Sat Sep 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> ibis1.2.4.10-alt1.svn20110829
- Version ibis1.2.4.10

* Thu May 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> ibis1.2.3.2-alt1.svn20110508
- Version ibis1.2.3.2

* Wed Mar 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> ibis1.2.0.2-alt1.svn20100924.5
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> ibis1.2.0.2-alt1.svn20100924.4
- Rebuilt for debuginfo

* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> ibis1.2.0.2-alt1.svn20100924.3
- Rebuilt for soname set-versions

* Mon Oct 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> ibis1.2.0.2-alt1.svn20100924.2
- Fixed underlinking of libraries

* Thu Sep 30 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> ibis1.2.0.2-alt1.svn20100924.1
- Added explicit conflict between %name-examples and ibutils
- Avoid conflicts with libCoinCsdp-devel and libprimme-devel

* Wed Sep 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> ibis1.2.0.2-alt1.svn20100924
- Initial build for Sisyphus

