%define somver 1
%define sover %somver.1.12
Name: sowing
Version: 1.1.16
Release: alt4
Summary: The program development and maintenance environment
License: Free
Group: Development/Tools
Url: http://ftp.mcs.anl.gov/pub/sowing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://ftp.mcs.anl.gov/pub/sowing/sowing.tar.gz

Requires: %name-common = %version-%release

BuildPreReq: ghostscript-utils gcc-c++

%description
The tools that are part of the program development and maintenance environment.
They are really a collection of mostly simple tools that help leverage many of
the excellent Unix tools for programmers.

%package common
Summary: Architecture independend files of Sowing
Group: Development/Tools
BuildArch: noarch

%description common
The tools that are part of the program development and maintenance environment.
They are really a collection of mostly simple tools that help leverage many of
the excellent Unix tools for programmers.

This package contains architecture independend files of Sowing.

%package -n lib%name
Summary: Shared libraries of Sowing
Group: System/Libraries

%description -n lib%name
The tools that are part of the program development and maintenance environment.
They are really a collection of mostly simple tools that help leverage many of
the excellent Unix tools for programmers.

This package contains shared libraries of Sowing.

%package -n lib%name-devel
Summary: Development files of Sowing
Group: Development/C++
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release
Obsoletes: lib%name-devel < %version-%release

%description -n lib%name-devel
The tools that are part of the program development and maintenance environment.
They are really a collection of mostly simple tools that help leverage many of
the excellent Unix tools for programmers.

This package contains development files of Sowing.

%package -n lib%name-devel-static
Summary: Static libraries of Sowing
Group: Development/C++
Requires: lib%name-devel = %version-%release
Conflicts: lib%name-devel < %version-%release

%description -n lib%name-devel-static
The tools that are part of the program development and maintenance environment.
They are really a collection of mostly simple tools that help leverage many of
the excellent Unix tools for programmers.

This package contains static libraries of Sowing.

%prep
%setup

%build
%add_optflags %optflags_shared
%autoreconf
%configure \
	--enable-strict \
	--enable-memorycheck \
	--with-wwwdir=$PWD/www/www1
%make_build

%install
%makeinstall \
	man1dir=%buildroot%_man1dir \
	datadir=%buildroot%_datadir/%name

install -d %buildroot%_libdir
install -d %buildroot%_includedir
install -m644 lib/*.a %buildroot%_libdir
cp -fR include/* %buildroot%_includedir/

# shared libraries

pushd %buildroot%_libdir
mkdir tmp
pushd tmp
for i in sowing tfilter; do
	ar x ../lib$i.a
	g++ -shared * \
		-Wl,-soname,lib$i.so.%somver -o ../lib$i.so.%sover
	ln -s lib$i.so.%sover ../lib$i.so.%somver
	ln -s lib$i.so.%somver ../lib$i.so
	rm -f *
done
popd
rmdir tmp
popd

sed -i '1s|/sh|/bash|' %buildroot%_bindir/pstoxbm

%files
%_bindir/*

%files common
%_man1dir/*
%_datadir/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Fri Feb 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.16-alt4
- Rebuilt for debuginfo

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.16-alt3
- Rebuilt for soname set-versions

* Tue Aug 31 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.16-alt2
- Fixed for checkbashisms

* Mon Jul 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.16-alt1
- Version 1.1.16

* Sat Aug 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.12-alt4
- Added shared libraries

* Fri Jun 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.12-alt3
- Rebuild with PIC

* Tue May 26 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.12-alt2
- Add static libraries and headers

* Sat Apr 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.12-alt1
- Initial build for Sisyphus
