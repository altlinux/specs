%define oname hdf5
%define sover 103
%define soverhl 100

Name: libhdf51.10
Version: 1.10.6
Release: alt4

Summary: Hierarchical Data Format 5 library
License: Nearly BSD, but changed sources must be marked
Group: System/Libraries

Url: http://www.hdfgroup.org/HDF5/
# https://github.com/HDFGroup/hdf5.git
Source: %name-%version.tar
Patch: libhdf5-alt-disable-rpath.patch

# Automatically added by buildreq on Sat Sep 15 2007
BuildRequires: gcc-c++ libssl-devel zlib-devel

%description
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

%package -n libhdf5-%sover
Summary: Hierarchical Data Format 5 library
Group: System/Libraries

%description -n libhdf5-%sover
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

%package -n libhdf5-hl-%soverhl
Summary: Hierarchical Data Format 5 library
Group: System/Libraries
Requires: libhdf5-%sover = %EVR

%description -n libhdf5-hl-%soverhl
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

%package -n lib%oname-devel
Summary: HDF5 library development package
Group: Development/C
Requires: libstdc++-devel zlib-devel
Requires: lib%oname-%sover = %EVR
Requires: lib%oname-hl-%soverhl = %EVR
Conflicts: lib%oname-mpi-devel < 1.8.3-alt5

%description -n lib%oname-devel
Header files for HDF5 library.

%package -n %oname-tools
Summary: HDF5 tools
Group: Development/Tools
Conflicts: %oname-mpi-tools < 1.8.3-alt5

%description -n %oname-tools
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

This package contains tools for work with HDF5.

%package -n %oname-examples
Summary: HDF5 examples
Group: Development/Documentation
BuildArch: noarch

%description -n %oname-examples
HDF5 is a completely new Hierarchical Data Format product consisting
of a data format specification and a supporting library
implementation. HDF5 is designed to address some of the limitations of
the older HDF product and to address current and anticipated
requirements of modern systems and applications.

This package contains examples for HDF5.

%prep
%setup
%patch -p1

%ifarch %e2k
# unsupported by lcc as of 1.21.21
sed -i	-e 's,-Wlogical-op,,' \
	-e 's,-Wvla,,' \
	-e 's,-Wsync-nand,,' \
	-e 's,-Wdouble-promotion,,' \
	-e 's,-Wnull-dereference,,' \
	-e 's,-Whsa,,' \
	-e 's,-Wnormalized,,' \
	-e 's,-Walloc-zero,,' \
	-e 's,-Walloca,,' \
	-e 's,-Wformat-overflow=2,,' \
	-e 's,-Wrestrict,,' \
	-e 's,-Wattribute-alias=2,,' \
	-e 's,-Wattribute-alias,,' \
	-e 's,-Wmissing-profile,,' \
	CMakeLists.txt config/gnu-flags \
	config/cmake/HDFCompilerFlags.cmake
%endif

%build
%autoreconf
%add_optflags -fno-strict-aliasing
# --with-default-api-version=v18 is needed for libnetcdf
%configure \
	--enable-hl \
	--enable-cxx \
	--enable-shared \
	--disable-static \
	--disable-sharedlib-rpath \
	--enable-build-mode=production \
	--with-pic \
	--with-pthread \
	--with-zlib \
	--with-szlib \
	--with-default-api-version=v18 \
	%nil

%make_build

%install
%makeinstall_std

install -d %buildroot%_pkgconfigdir
cat << EOF > %buildroot%_pkgconfigdir/%oname.pc
prefix=%prefix
exec_prefix=%prefix
libdir=%_libdir
includedir=%_includedir

Name: %oname
Description: Hierarchical Data Format 5 library
Version: %version
Libs: -lhdf5_hl_cpp -lhdf5_hl -lhdf5_cpp -lhdf5 -lstdc++ -lz
EOF

%files -n libhdf5-%sover
%doc COPYING COPYING_LBNL_HDF5
%doc README.txt release_docs/{HISTORY*,RELEASE.txt}
%_libdir/lib*.so.%{sover}
%_libdir/lib*.so.%{sover}.*

%files -n libhdf5-hl-%soverhl
%_libdir/lib*.so.%{soverhl}
%_libdir/lib*.so.%{soverhl}.*

%changelog
* Fri Mar 01 2024 Michael Shigorin <mike@altlinux.org> 1.10.6-alt4
- E2K: avoid more lcc-unsupported options

* Sat Feb 10 2024 Anton Farygin <rider@altlinux.ru> 1.10.6-alt3
- built as compat package without development files

* Sat May 15 2021 Michael Shigorin <mike@altlinux.org> 1.10.6-alt2
- E2K: avoid lcc-unsupported options

* Wed Apr 14 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10.6-alt1
- Updated to upstream version 1.10.6.
- Removed alternatives.
- Updated packaging scheme.

* Wed Oct 31 2018 Michael Shigorin <mike@altlinux.org> 1.8.13-alt1.qa4
- Replace e2k arch name with %%e2k macro (grenka@)

* Mon Oct 09 2017 Michael Shigorin <mike@altlinux.org> 1.8.13-alt1.qa3
- E2K: avoid lcc-unsupported options
- introduce fortran knob (on by default)

* Thu May 11 2017 Andrey Cherepanov <cas@altlinux.org> 1.8.13-alt1.qa2
- Fix library names in pkgconfig file

* Fri Apr 08 2016 Gleb F-Malinovskiy (qa) <qa_glebfm@altlinux.org> 1.8.13-alt1.qa1
- Rebuilt for gcc5 C++11 ABI.

* Wed Jun 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.13-alt1
- Version 1.8.13

* Thu Sep 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt2
- Added links to headers into %_includedir

* Wed Jun 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.11-alt1
- Version 1.8.11

* Tue Oct 02 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.9-alt2
- Rebuilt with gcc 4.7

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.9-alt1
- Version 1.8.9

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt2
- Set native directory as %_libdir/%oname-seq instead of
  %_libexecdir/%oname-seq

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.8-alt1
- Version 1.8.8

* Tue Sep 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.7-alt1
- Version 1.8.7

* Sat Mar 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.6-alt1
- Version 1.8.6
- Disabled static package

* Thu Feb 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5_patch1-alt2
- Rebuilt for debuginfo

* Tue Nov 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5_patch1-alt1
- Version 1.8.5-patch1

* Wed Oct 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt6
- Fixed soname set-versions by ghost links (thnx ldv@)

* Fri Oct 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt5
- Rebuilt for soname set-versions

* Wed Jul 15 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt4
- Added pkgconfig file

* Thu Jun 18 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt3
- Created alternatives

* Thu Jun 04 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt2
- Added explicit conflict with parallel version of HDF5 tools

* Thu May 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.3-alt1
- Version 1.8.3
- Added static libraries
- Add fortran interface libraries
- Add zlib support

* Sun Dec 14 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.6.6-alt2
- fixed build with gcc4.3

* Sat Sep 15 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6.6-alt1
- initial build for ALT Linux Sisyphus

