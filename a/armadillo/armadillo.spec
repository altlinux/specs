Group: Sciences/Mathematics
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat rpm-macros-generic-compat
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
%define fedora 37
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           armadillo
Version:        10.8.2
Release:        alt1_3
Summary:        Fast C++ matrix library with syntax similar to MATLAB and Octave

License:        ASL 2.0
URL:            http://arma.sourceforge.net/
Source:         http://sourceforge.net/projects/arma/files/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  ctest cmake
BuildRequires:  libarpack-ng-devel
BuildRequires:  hdf5-tools libhdf5-devel
BuildRequires:  libsuperlu-devel

# flexiblas is only available on Fedora, for EPEL replace it by atlas, lapack and openblas
%if %{?fedora}
%global extra_options -DALLOW_FLEXIBLAS_LINUX=ON
BuildRequires:  libflexiblas-devel
%else
%undefine __cmake_in_source_build
%global extra_options %{nil}
BuildRequires:  atlas-devel
BuildRequires:  liblapack-devel
%{!?openblas_arches:%global openblas_arches x86_64 %{ix86} armv7hl %{power64} aarch64}
%ifarch %{openblas_arches}
BuildRequires:  libopenblas-devel
%endif
%endif
Source44: import.info

%description
Armadillo is a C++ linear algebra library (matrix maths)
aiming towards a good balance between speed and ease of use.
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.
Various matrix decompositions are provided through optional
integration with LAPACK and ATLAS libraries.
A delayed evaluation approach is employed (during compile time)
to combine several operations into one and reduce (or eliminate)
the need for temporaries. This is accomplished through recursive
templates and template meta-programming.
This library is useful if C++ has been decided as the language
of choice (due to speed and/or integration capabilities), rather
than another language like Matlab or Octave.

%package -n libarmadillo10
Summary:        Shared library for the %name library
Group:          System/Libraries

%description -n libarmadillo10
Armadillo is a C++ linear algebra library (matrix maths)
aiming towards a good balance between speed and ease of use.
Integer, floating point and complex numbers are supported,
as well as a subset of trigonometric and statistics functions.
Various matrix decompositions are provided through optional
integration with LAPACK and ATLAS libraries.
A delayed evaluation approach is employed (during compile time)
to combine several operations into one and reduce (or eliminate)
the need for temporaries. This is accomplished through recursive
templates and template meta-programming.
This library is useful if C++ has been decided as the language
of choice (due to speed and/or integration capabilities), rather
than another language like Matlab or Octave.

This package contains the shared library.


%package -n libarmadillo-devel
Group: Sciences/Mathematics
Summary:        Development headers and documentation for the Armadillo C++ library
Requires:       libarmadillo10 = %EVR
Requires:       hdf5-tools

%if %{?fedora}
%else
%ifarch %{openblas_arches}
%endif
%endif
Provides: %name-devel = %EVR


%description -n libarmadillo-devel
This package contains files necessary for development using the
Armadillo C++ library. It contains header files, example programs,
and user documentation (API reference guide).


%prep
%setup -q

sed -i 's/\r//' README.md
rm -rf examples/*win64*


%build
%{fedora_v2_cmake} %{extra_options}
%fedora_v2_cmake_build


%install
%fedora_v2_cmake_install


%check
%{fedora_v2_cmake} %{extra_options} -DBUILD_SMOKE_TEST=ON
make -C "%{_vpath_builddir}"
%fedora_v2_ctest


%files -n libarmadillo10
%doc --no-dereference LICENSE.txt NOTICE.txt
%_libdir/libarmadillo.so.10
%_libdir/libarmadillo.so.10.*

%files -n libarmadillo-devel
%{_libdir}/libarmadillo.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/armadillo
%{_includedir}/armadillo_bits/
%{_datadir}/Armadillo/
%doc README.md
%doc index.html
%doc docs.html
%doc examples
%doc armadillo_icon.png
%doc mex_interface
%doc armadillo_nicta_2010.pdf
%doc rcpp_armadillo_csda_2014.pdf
%doc armadillo_joss_2016.pdf
%doc armadillo_spcs_2017.pdf
%doc armadillo_lncs_2018.pdf
%doc armadillo_solver_2020.pdf


%changelog
* Sat Feb 25 2023 Igor Vlasenko <viy@altlinux.org> 10.8.2-alt1_3
- update to new release by fcimport

* Sat Feb 27 2021 Igor Vlasenko <viy@altlinux.org> 10.2.0-alt1_2
- update to new release by fcimport

* Tue Jan 26 2021 Igor Vlasenko <viy@altlinux.ru> 10.1.2-alt1_1
- new version

* Mon Nov 09 2020 Igor Vlasenko <viy@altlinux.ru> 9.900.3-alt2_2
- restored to Sisyphus

* Wed Nov 04 2020 Igor Vlasenko <viy@altlinux.ru> 9.900.3-alt1_2
- new version

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 9.900.1-alt1_1
- update to new release by fcimport

* Sat Jun 13 2020 Igor Vlasenko <viy@altlinux.ru> 9.880.1-alt1_1
- update to new release by fcimport

* Tue Apr 07 2020 Igor Vlasenko <viy@altlinux.ru> 9.860.1-alt1_1
- update to new release by fcimport

* Thu Feb 27 2020 Igor Vlasenko <viy@altlinux.ru> 9.850.1-alt1_1
- update to new release by fcimport

* Sat Sep 28 2019 Igor Vlasenko <viy@altlinux.ru> 9.600.6-alt1_1
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 9.600.4-alt1_2
- update to new release by fcimport

* Mon Jul 01 2019 Igor Vlasenko <viy@altlinux.ru> 9.500.2-alt1_1
- update to new release by fcimport

* Sun Jun 02 2019 Igor Vlasenko <viy@altlinux.ru> 9.400.4-alt1_1
- update to new release by fcimport

* Mon May 13 2019 Igor Vlasenko <viy@altlinux.ru> 9.400.3-alt1_1
- update to new release by fcimport

* Mon Apr 29 2019 Igor Vlasenko <viy@altlinux.ru> 9.400.2-alt1_1
- update to new release by fcimport

* Thu Apr 11 2019 Igor Vlasenko <viy@altlinux.ru> 9.300.2-alt1_1
- update to new release by fcimport

* Mon Mar 18 2019 Igor Vlasenko <viy@altlinux.ru> 9.200.8-alt1_1
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 9.200.7-alt1_2
- update to new release by fcimport

* Fri Jan 25 2019 Igor Vlasenko <viy@altlinux.ru> 9.200.6-alt1_1
- update to new release by fcimport

* Mon Dec 17 2018 Igor Vlasenko <viy@altlinux.ru> 9.200.4-alt1_1
- update to new release by fcimport

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 9.100.5-alt1_1
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 8.600.0-alt1_2
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 8.600.0-alt1_1
- update to new release by fcimport

* Sat May 26 2018 Igor Vlasenko <viy@altlinux.ru> 8.300.0-alt1_3.1
- new version

* Wed Apr 04 2018 Igor Vlasenko <viy@altlinux.ru> 8.300.0-alt1_2
- update to new release by fcimport

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 8.100.1-alt1_2
- new version

* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.695.0-alt1.svn20150320
- Version 4.695.0

* Thu Jun 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.349.0-alt2.svn20140624
- Rebuilt with libarpack-ng-devel instead of libarpack-devel

* Wed Jun 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.349.0-alt1.svn20140624
- Version 4.349.0

* Tue May 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.300.6-alt1.svn20140523
- Version 4.300.6

* Fri Nov 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.929.0-alt1.svn20131107
- Version 3.929.0

* Tue Jun 18 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.810.0-alt1.svn20130403
- Version 3.810.0

* Fri Feb 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1.svn20130201
- Version 3.6.2

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1.svn20120910
- Version 3.4.0

* Sat Aug 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt2.svn20111208
- Built with OpenBLAS instead of GotoBLAS2

* Tue Dec 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.2-alt1.svn20111208
- Version 2.4.2

* Wed Aug 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.svn20110804
- Version 2.3.0

* Mon May 09 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.0-alt1.svn20110504
- Version 1.2.0

* Wed Apr 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.90-alt1.svn20101014.4
- Built with GotoBLAS2 instead of ATLAS

* Thu Mar 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.90-alt1.svn20101014.3
- Rebuilt with Boost 1.46.1

* Thu Mar 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.90-alt1.svn20101014.2
- Rebuilt for debuginfo

* Tue Oct 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.90-alt1.svn20101014.1
- Rebuilt for soname set-versions

* Mon Oct 18 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.90-alt1.svn20101014
- Version 0.9.90

* Wed Jun 16 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1.svn20100611.1
- Added pkg-config file

* Fri Jun 11 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.10-alt1.svn20100611
- Version 0.9.10

* Sun May 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.6-alt1.svn20090409
- Initial build for Sisyphus

* Wed Apr 02 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Updated description

* Wed Mar 24 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Added explicit dependence on libstdc++-devel

* Wed Mar 17 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Simplified specification of directories
- Removed library packages specified by "Requires",
  as library dependencies are detected automatically

* Wed Mar 12 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Modified to generate separate devel package (subsumes previous doc package)
- Removed redundant packages specified by "BuildRequires"
- Added CMake installation prefixes to allow for x86_64

* Wed Feb  4 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Modified to generate separate doc package

* Thu Jan 28 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Added argument to cmake: -DCMAKE_INSTALL_PREFIX=/usr 

* Thu Jan 22 2009  Conrad Sanderson  <conradsand at ieee dot org>
- Initial spec file prepared

