%define somver 0
%define sover %somver.0.0

Name: advio
Version: 1.2
Release: alt4
Summary: ADVENTURE common input/output library
License: MIT
Group: Development/Tools
Url: https://wci.llnl.gov/codes/visit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: https://wci.llnl.gov/codes/visit/3rd_party/AdvIO-1.2.tar.gz

BuildPreReq: gcc-c++ gtk+-devel python-devel libX11-devel
BuildPreReq: ORBit2-devel zlib-devel libncurses-devel

%description
ADVENTURE_IO is a common input/output library, which is used by
other modules of the ADVENTURE System.

%package -n lib%name
Summary: Shared libraries of ADVENTURE_IO
Group: System/Libraries

%description -n lib%name
ADVENTURE_IO is a common input/output library, which is used by
other modules of the ADVENTURE System.

This package contains shared libraries of ADVENTURE_IO.

%package -n lib%name-devel
Summary: Development files of ADVENTURE_IO
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
ADVENTURE_IO is a common input/output library, which is used by
other modules of the ADVENTURE System.

This package contains development files of ADVENTURE_IO.

%package -n lib%name-devel-doc
Summary: Documentation for ADVENTURE_IO
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
ADVENTURE_IO is a common input/output library, which is used by
other modules of the ADVENTURE System.

This package contains development documentation for ADVENTURE_IO.

%prep
%setup
rm -f aclocal.m4

%build
%autoreconf
INCS="-I$PWD/Base -I$PWD/FileIO -I%buildroot%_includedir"
%add_optflags $INCS %optflags_shared
%configure \
	--with-docdir=%_docdir \
	--with-pyinc=%_includedir/python%_python_version \
	--with-orbit=%prefix
sed -i '8,13d' advsys-config.h
%make_build

%make_build -C Base
%make_build -C FileIO
%make -C IDL
%make -C DocIO
%make_build -C Utils

%install
%makeinstall_std

mkdir -p %buildroot%_libdir/tmp
pushd %buildroot%_libdir/tmp
#for i in libAdvBase libAdvFileIO libAdvIDL libAdvDocIO
for i in libAdvBase libAdvFileIO libAdvDocIO
do
	if [ "$i" == "libAdvDocIO" ]; then
		ADDLIB="-lAdvBase -lAdvFileIO -lORBit-2"
	else
		ADDLIB=-lORBit-2
	fi
	ar x ../$i.a
	gcc -shared * -Wl,-soname,$i.so.%somver -o ../$i.so.%sover \
		-L$PWD/.. $ADDLIB
	ln -s $i.so.%sover ../$i.so.%somver
	ln -s $i.so.%somver ../$i.so
	rm -f *
done
popd
rmdir %buildroot%_libdir/tmp

# antirepocop
rm -fR %buildroot%_docdir/AdvIO %buildroot%_libdir/*.a

%files
%doc README copyright
%_bindir/*
%exclude %_bindir/advsys-config

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/advsys-config
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%doc doc/AdvDocument.pdf doc/manual.pdf

%changelog
* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt4
- Rebuilt for debuginfo

* Sun Nov 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3
- Rebuilt for soname set-versions
- Rebuilt with ORBit2

* Fri Oct 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt2
- Fixed underlinking of libraries

* Thu Sep 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1
- Initial build for Sisyphus

