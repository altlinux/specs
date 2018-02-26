Name: tbb
Version: 40_20120408
Release: alt1
Summary: Threading Building Blocks
License: GPL
Group: Development/Tools
Url: http://threadingbuildingblocks.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar.gz

Requires: lib%name = %version-%release

BuildPreReq: gcc-c++

%description
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

%package -n lib%name
Summary: Shared libraries of Threading Building Blocks
Group: Development/C++

%description -n lib%name
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains shared libraries of Threading Building Blocks.

%package headers
Summary: Headers for Threading Building Blocks
Group: Development/C++
BuildArch: noarch
Conflicts: lib%name-devel < %version-%release

%description headers
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains headers for Threading Building Blocks.

%package -n lib%name-devel
Summary: Development libraries of Threading Building Blocks
Group: Development/C++
Requires: lib%name = %version-%release
Requires: %name-headers = %version-%release
%ifarch x86_64
Provides: libtbb.so()(64bit)
Provides: libtbbmalloc.so()(64bit)
%else
Provides: libtbb.so
Provides: libtbbmalloc.so
%endif

%description -n lib%name-devel
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains development libraries for Threading Building
Blocks.

%package docs
Summary: Documentation for Threading Building Blocks
Group: Development/Documentation
BuildArch: noarch

%description docs
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains development documentation for Threading Building
Blocks.

%package examples
Summary: Examples for Threading Building Blocks
Group: Development/Documentation
Requires: lib%name = %version-%release

%description examples
Threading Building Blocks offers a rich and complete approach to
expressing parallelism in a C++ program. It is a library that helps you
leverage multi-core processors for performance and scalability without
having to be a threading expert.

This package contains examples for Threading Building Blocks.

%prep
%setup

%build
%make
%make_build rml

%install
install -d %buildroot%_libdir
install -m644 build/linux*release/*.so.* \
	%buildroot%_libdir
pushd %buildroot%_libdir
for i in *.so.*
do
	devlib=$(echo $i|sed 's|\.1||')
	devlib=$(echo $devlib|sed 's|\.2||')
	ln -s $i $devlib
done
popd
install -d %buildroot%_bindir
install -m755 build/linux*release/*.exe \
	%buildroot%_bindir
pushd %buildroot%_bindir
for i in $(ls *.exe|sed 's|\.exe||'); do
	mv $i.exe $i
done
popd

install -d %buildroot%_includedir
cp -fR include/%name %buildroot%_includedir/

install -d %buildroot%_libdir/%name
cp -fR examples %buildroot%_libdir/%name/

for i in $(find ./ -name '*.html'); do
	install -Dm644 $i %buildroot%_docdir/%name/$i
done

install -p -m644 CHANGES COPYING README %buildroot%_docdir/%name

%files
%_bindir/*

%files headers
%_includedir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so

%files docs
%_docdir/%name

%files examples
%_libdir/%name/

%changelog
* Mon May 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 40_20120408-alt1
- Version 40_20120408

* Wed Mar 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 40_297-alt1
- Version 40_297

* Sun Dec 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 40_233-alt1
- Version 40_233

* Sun May 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20110315-alt1
- Version 30_20110315
- Disabled debug packages (we have debuginfo packages now)

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt6
- Added -g into compiler flags

* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt5
- Rebuilt for debuginfo

* Wed Jan 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt4
- Added debug subpackages

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt3
- Fixed overlinking of libraries

* Wed Mar 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt2
- Disabled broken test

* Tue Mar 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 30_20100310-alt1
- Version 30_20100310 (ALT #23196)

* Fri Dec 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20.014-alt1
- Initial build for Sisyphus

