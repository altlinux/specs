Name: libsz2
Version: 2.1
Release: alt4
Summary: SZIP compression library for HDF5
License: Free for non-commercial using
Group: System/Libraries
Url: http://www.hdfgroup.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: ftp://ftp.hdfgroup.org/lib-external/szip/2.1/src/szip-2.1.tar.gz

%description
SZIP compression library for HDF5.

%package devel
Summary: Development library of SZIP
Group: Development/C
Requires: %name = %version-%release
Conflicts: libsz0-devel < 2.2p1_1.1-alt2
Obsoletes: libsz0-devel < 2.2p1_1.1-alt2

%description devel
Development library of SZIP.

%package devel-static
Summary: Static development library of SZIP
Group: Development/C
Requires: %name-devel = %version-%release
Conflicts: libsz0-devel-static < 2.2p1_1.1-alt2
Obsoletes: libsz0-devel-static < 2.2p1_1.1-alt2

%description devel-static
Static development library of SZIP.

%prep
%setup

%build
%add_optflags %optflags_shared
%autoreconf
export CPPFLAGS="%optflags"
%configure --enable-production
%make_build

%install
%makeinstall_std

%files
%doc COPYING HISTORY.txt README RELEASE.txt
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so

%files devel-static
%_libdir/*.a

%changelog
* Sun Mar 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt4
- Added -g into compiler flags

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt3
- Rebuilt for debuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt2
- Rebuilt for soname set-versions

* Wed Jun 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1
- Initial build for Sisyphus

