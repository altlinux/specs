%define _unpackaged_files_terminate_build 1

Name: exodusii
Version: 6.09.0
Release: alt6.git20150119
Summary: A model developed to store and retrieve transient data for finite element analyses
License: BSD
Group: Sciences/Mathematics
Url: http://sourceforge.net/projects/exodusii/

ExclusiveArch: %ix86 x86_64

%define somver 0
%define sover %somver.%version

# git://exodusii.git.sourceforge.net/gitroot/exodusii/exodusii
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: gcc-c++ gcc-fortran
BuildRequires: doxygen graphviz
BuildRequires: cmake imake
BuildRequires: libnetcdf-devel netcdf-tools libhdf5-devel
BuildRequires: libcurl-devel

%description
EXODUS II is a model developed to store and retrieve transient data for
finite element analyses. It is used for preprocessing, postprocessing,
as well as code to code data transfer. ExodusII is based on netcdf.
Includes the nemesis parallel extension.

%package -n lib%name
Summary: Shared libraries of EXODUS II
Group: System/Libraries

%description -n lib%name
EXODUS II is a model developed to store and retrieve transient data for
finite element analyses. It is used for preprocessing, postprocessing,
as well as code to code data transfer. ExodusII is based on netcdf.
Includes the nemesis parallel extension.

This package contains shared libraries of EXODUS II.

%package -n lib%name-devel
Summary: Development files of EXODUS II
Group: Development/C++
Requires: lib%name = %EVR

%description -n lib%name-devel
EXODUS II is a model developed to store and retrieve transient data for
finite element analyses. It is used for preprocessing, postprocessing,
as well as code to code data transfer. ExodusII is based on netcdf.
Includes the nemesis parallel extension.

This package contains development files of EXODUS II.

%package -n lib%name-devel-doc
Summary: Documentation for EXODUS II
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
EXODUS II is a model developed to store and retrieve transient data for
finite element analyses. It is used for preprocessing, postprocessing,
as well as code to code data transfer. ExodusII is based on netcdf.
Includes the nemesis parallel extension.

This package contains development documentation for EXODUS II.

%package -n python3-module-exodus
Summary: Python binding for EXODUS II
Group: Development/Python3
Requires: lib%name = %EVR

%description -n python3-module-exodus
EXODUS II is a model developed to store and retrieve transient data for
finite element analyses. It is used for preprocessing, postprocessing,
as well as code to code data transfer. ExodusII is based on netcdf.
Includes the nemesis parallel extension.

This package contains python binding for EXODUS II.

%prep
%setup
%patch0 -p1

%build
pushd exodus
%cmake_insource \
	-DSOMVER:STRING="%somver" \
	-DSOVER:STRING="%sover" \
	-DNETCDF_SO_ROOT=%_libdir \
	-DPYTHON_INSTALL=%python3_sitelibdir \
	-DNETCDF_INCLUDE_DIR:STRING="%_includedir" \
	-DNETCDF_LIBRARY:STRING=-lnetcdf \
	-DHDF5_LIBRARY:STRING=-lhdf5 \
	-DHDF5HL_LIBRARY:STRING=-lhdf5_hl \
	-DBUILD_TESTING:BOOL=OFF \
	-DEXODUS_LIBRARY:STRING=-lexoIIv2c \
	-DBUILD_SHARED:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	%nil
%make_build VERBOSE=1
popd

pushd nemesis
%cmake_insource \
	-DSOMVER:STRING="%somver" \
	-DSOVER:STRING="%sover" \
	-DNETCDF_INCLUDE_DIR:STRING="%_includedir" \
	-DNETCDF_LIBRARY:STRING=-lnetcdf \
	-DHDF5_LIBRARY:STRING=-lhdf5 \
	-DHDF5HL_LIBRARY:STRING=-lhdf5_hl \
	-DBUILD_TESTING:BOOL=OFF \
	-DEXODUS_LIBRARY:STRING=-lexoIIv2c \
	-DBUILD_SHARED:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	%nil

%make_build VERBOSE=1
popd

pushd exodus
doxygen
popd

%install
pushd exodus
%makeinstall_std
popd
pushd nemesis
%makeinstall_std
popd

install -d %buildroot%_includedir/%name
mv %buildroot%_includedir/*.h %buildroot%_includedir/%name/

mv nemesis/README README.Nemesis

%files -n lib%name
%doc exodus/COPYRIGHT exodus/README README.Nemesis ChangeLog
%_libdir/*.so.%{somver}
%_libdir/*.so.%{sover}

%files -n lib%name-devel
%_libdir/*.so
%_includedir/*

%files -n lib%name-devel-doc
%doc exodus/html exodus/doc/*

%files -n python3-module-exodus
%python3_sitelibdir/*

%changelog
* Fri Apr 16 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 6.09.0-alt6.git20150119
- Updated build and runtime dependencies.

* Thu Feb 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 6.09.0-alt5
- Porting python binding on python3.

* Tue Feb 04 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 6.09.0-alt4.git20150119
- Fixed build.

* Tue Jul 02 2019 Igor Vlasenko <viy@altlinux.ru> 6.09.0-alt3.git20150119
- NMU: fixed LIB_SUFFIX= on non-x86_64

* Wed Oct 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 6.09.0-alt2.git20150119
- NMU: updated build dependencies.

* Mon Aug 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 6.09.0-alt1.git20150119.2
- Rebuilt with libnetcdf11.

* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.09.0-alt1.git20150119
- Version 6.09.0

* Wed Jul 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt7.git20140623
- New snapshot

* Thu May 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt7.git20140509
- New snapshot

* Tue Nov 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt7.git20130820
- New snapshot

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt7.git20120917
- New snapshot

* Sat Aug 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt7
- New snapshot

* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt6
- Rebuilt with OpenMPI 1.6

* Wed Dec 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt5
- Fixed RPATH

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt4
- Rebuilt with Boost 1.48.0

* Tue Nov 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.14.0-alt3
- Version 5.14.0

* Sun Nov 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10-alt3
- Moved headers into %_includedir/%name/

* Fri Sep 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10-alt2
- Added headers for nemesis

* Fri Sep 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.10-alt1
- Version 5.10

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.98-alt2
- Rebuilt with libnetcdf7

* Wed Apr 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.98-alt1
- Version 4.98

* Fri Feb 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.96-alt3
- Rebuilt for debuginfo

* Tue Oct 12 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.96-alt2
- Fixed overlinking of libraries

* Fri Sep 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.96-alt1
- Initial build for Sisyphus

