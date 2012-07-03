%define sover 0

Name: bfl
Version: 0.8.0
Release: alt2
Summary: The Bayesian Filtering Library (BFL)

Group: Sciences/Mathematics
License: LGPL
Url: http://www.orocos.org/bfl
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: orocos-%name-%version.tar.bz2
Requires: lib%name = %version-%release

BuildPreReq: cmake gcc-c++ cppunit-devel boost-devel doxygen
BuildPreReq: /usr/bin/dvips libscythe-devel libginac-devel ctest

%description
The Bayesian Filtering Library (BFL) provides an application independent
framework for inference in Dynamic Bayesian Networks, i.e., recursive
information processing and estimation algorithms based on Bayes' rule, such as
(Extended) Kalman Filters, Particle Filters (or Sequential Monte Carlo
methods), etc. These algorithms can, for example, be run on top of the Realtime
Services, or be used for estimation in Kinematics & Dynamics applications.

%package -n lib%name
Summary: Shared library of The Bayesian Filtering Library (BFL)
Group: System/Libraries

%description -n lib%name
The Bayesian Filtering Library (BFL) provides an application independent
framework for inference in Dynamic Bayesian Networks, i.e., recursive
information processing and estimation algorithms based on Bayes' rule, such as
(Extended) Kalman Filters, Particle Filters (or Sequential Monte Carlo
methods), etc. These algorithms can, for example, be run on top of the Realtime
Services, or be used for estimation in Kinematics & Dynamics applications.

This package contains shared library of BFL.

%package -n lib%name-devel
Summary: Development files of The Bayesian Filtering Library (BFL)
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
The Bayesian Filtering Library (BFL) provides an application independent
framework for inference in Dynamic Bayesian Networks, i.e., recursive
information processing and estimation algorithms based on Bayes' rule, such as
(Extended) Kalman Filters, Particle Filters (or Sequential Monte Carlo
methods), etc. These algorithms can, for example, be run on top of the Realtime
Services, or be used for estimation in Kinematics & Dynamics applications.

This package contains development files of The Bayesian Filtering Library
(BFL).

%package -n lib%name-devel-doc
Summary: Documentation for The Bayesian Filtering Library (BFL)
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-doc
The Bayesian Filtering Library (BFL) provides an application independent
framework for inference in Dynamic Bayesian Networks, i.e., recursive
information processing and estimation algorithms based on Bayes' rule, such as
(Extended) Kalman Filters, Particle Filters (or Sequential Monte Carlo
methods), etc. These algorithms can, for example, be run on top of the Realtime
Services, or be used for estimation in Kinematics & Dynamics applications.

This package contains documentation for The Bayesian Filtering Library (BFL).

%prep
%setup -n bfl

sed -i 's|@SOVER@|%sover|' src/CMakeLists.txt

%build
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
	-DGINAC_SUPPORT:BOOL=ON \
	__MATRIXWRAPPER_BOOST__:BOOL=ON \
	__RNGWRAPPER_BOOST__:BOOL=ON \
	.
%make_build VERBOSE=1
%make_build docs

%install
%makeinstall_std

pushd %buildroot%_bindir/%name
for i in $(ls); do
	mv $i ../%{name}_$i
done
popd
rmdir %buildroot%_bindir/%name

%ifarch x86_64
mkdir -p %buildroot%_libdir
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

mkdir -p %buildroot%_defaultdocdir/lib%name-devel
mv doc/html %buildroot%_defaultdocdir/lib%name-devel/

%check
%make check

%files
%doc AUTHORS ChangeLog COPYING THANKS README
%_bindir/*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_pkgconfigdir/*
%_includedir/*

%files -n lib%name-devel-doc
%_defaultdocdir/lib%name-devel

%changelog
* Tue Aug 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2
- Rebuilt with libginac 1.6.1

* Mon Apr 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Version 0.8.0

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt4
- Rebuilt with Boost 1.46.1

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt3
- Rebuilt for debuginfo

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2
- Rebuilt for soname set-versions

* Tue Aug 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Version 0.7.0

* Sun Mar 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.svn20090324
- New trunk from upstream

* Tue Mar 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.20090227
- Initial build for Sisyphus
