Name: libslatec
Version: 4.1
Release: alt6
Summary: SLATEC Common Mathematical Library
License: GPL
Group: Sciences/Mathematics
Url: http://www.netlib.org/slatec/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://www.netlib.org/slatec/slatec_src.tar.gz
Source1: http://www.netlib.org/slatec/slatec4linux.tar.gz
Source2: http://www.netlib.org/slatec/guide
Source3: http://www.netlib.org/slatec/gams

BuildPreReq: gcc-fortran liblapack-goto-devel

%description
SLATEC Common Mathematical Library, Version 4.1, July 1993
a comprehensive software library containing over
1400 general purpose mathematical and statistical routines
written in Fortran 77.

In addition install a libslatec-devel-docs package for documentation.

%package devel
Summary: SLATEC Common Mathematical Library (static)
Group: Development/Other
Requires: %name = %version-%release

%description devel
SLATEC Common Mathematical Library, Version 4.1, July 1993
a comprehensive software library containing over
1400 general purpose mathematical and statistical routines
written in Fortran 77.

This package contains shared library of SLATEC and gams.

%package devel-static
Summary: SLATEC Common Mathematical Library (static)
Group: Development/Other
Requires: %name-devel = %version-%release

%description devel-static
SLATEC Common Mathematical Library, Version 4.1, July 1993
a comprehensive software library containing over
1400 general purpose mathematical and statistical routines
written in Fortran 77.

This package contains static library of SLATEC.

%package devel-docs
Summary: Documentation for ARPACK
Group: Development/Documentation
BuildArch: noarch

%description devel-docs
SLATEC Common Mathematical Library, Version 4.1, July 1993
a comprehensive software library containing over
1400 general purpose mathematical and statistical routines
written in Fortran 77.

This package contains guide and man pages for developers.

%prep
%setup
tar -xzf %SOURCE1
install %SOURCE2 .

%build
%make_build
mv dynamic/libslatec.so dynamic/libslatec.so.4.1.0
rm -f *.f
for i in $(ls *.1|sed -e 's/\(.*\)\.1/\1/'); do
	mv $i.1 $i.f
done
bzip2 *.f

%install
install -d %buildroot%_libdir
install -d %buildroot%_datadir/%name
install -d %buildroot%_mandir/manf
#install -m644 static/*.a %buildroot%_libdir
install -m644 dynamic/*.so* %buildroot%_libdir
install -m644 %SOURCE3 %buildroot%_datadir/%name
install -m644 *.bz2 %buildroot%_mandir/manf
pushd %buildroot%_libdir
ln -s libslatec.so.4.1.0 libslatec.so.4
ln -s libslatec.so.4 libslatec.so
popd

%files
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_datadir/%name

#files devel-static
#_libdir/*.a

%files devel-docs
%doc guide
%_mandir/manf/*

%changelog
* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt6
- Built with GotoBLAS2 instead of ATLAS
- Disabled devel-static package

* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt5
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt4
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt3
- Rebuilt for soname set-versions

* Wed Apr 22 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt2
- Move man files into %_mandir/manf for fix conflicts with another packages.
  For see man pages You need call `man -S f MANPAGE'

* Sun Apr 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1-alt1
- Initial build for Sisyphus

