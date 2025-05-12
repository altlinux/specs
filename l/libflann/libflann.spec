%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    devel
%def_enable    python3
%def_disable   matlab
%def_disable   doc
%global        srcname flann
%global        soversion 1.9

Name:          libflann
Version:       1.9.2
Release:       alt3
Summary:       Fast Library for Approximate Nearest Neighbors
Group:         Development/C
License:       BSD
URL:           http://www.cs.ubc.ca/research/flann
Vcs:           https://github.com/flann-lib/flann.git
Source:        %{name}-%{version}.tar

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-cmake
BuildRequires: /proc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: zlib-devel
BuildRequires: liblz4-devel
BuildRequires: libgomp-devel
BuildRequires: hdf5-tools
BuildRequires: libhdf5-devel
BuildRequires: boost-devel
BuildRequires: boost-mpi-devel
BuildRequires: openmpi-devel
%{?_enable_matlab:BuildRequires: getfemxx}
%if_enabled    check
BuildRequires: ctest
BuildRequires: libgtest-devel
%endif
%if_enabled    doc
BuildRequires: latex2html
BuildRequires: texlive
BuildRequires: texlive-collection-basic
BuildRequires: texlive-dist
%endif
%if_enabled    python3
BuildRequires: python3-devel
BuildRequires: python3-module-distutils-extra
%endif

Provides:      flann = %EVR

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%add_optflags %optflags_shared

%description
FLANN is a library for performing fast approximate nearest neighbor searches
in high dimensional spaces. It contains a collection of algorithms found
to work best for nearest neighbor search and a system for automatically
choosing the best algorithm and optimum parameters depending on the data sets.

%package       -n %srcname
Group:         Development/C
Summary:       Example binaries for flann

%description   -n %srcname
Example binaries for flann.


%if_enabled    devel
%package       devel
Group:         Development/Other
Summary:       Development headers and libraries for flann
#Requires:      %{name} = %{version}-%{release}
Provides:      flann-devel = %EVR
Requires:      gcc-c++
Requires:      cmake
Requires:      zlib-devel
Requires:      liblz4-devel
Requires:      libgomp-devel
Requires:      hdf5-tools
Requires:      libhdf5-devel
Requires:      boost-devel-headers
Requires:      boost-mpi-devel
Requires:      openmpi-devel
Requires:      ctest
Requires:      libgtest-devel
Requires:      latex2html
Requires:      texlive
Requires:      texlive-collection-basic
Requires:      texlive-dist
Requires:      python3-devel
Requires:      python3-module-distutils-extra


%description   devel
Development headers and libraries for flann.


%package       devel-static
Group:         Development/Other
Summary:       Static libraries for flann
Provides:      flann-static = %EVR

%description   devel-static
Static libraries for flann.
%endif


%if_enabled    python3
%package       -n python3-module-flann
Group:         Development/Other
Summary:       Python bindings for flann
Requires:      %{name} = %EVR
%{?python_provide:%python_provide python3-%{srcname}}

%description   -n python3-module-flann
Python 3 bindings for flann
%endif


%prep
%setup
#%ifarch %e2k
#sed -i "/num_threads(params\.cores)/{s/params\.cores/nthreads/;s/^/int nthreads=params.cores;\n/}" \
#	src/cpp/flann/algorithms/{nn,lsh}_index.h
#%endif

%build
%cmake \
   -DCMAKE_BUILD_TYPE=RelWithDebInfo \
   -DBUILDROOT=%buildroot \
   %{!?_enable_doc:-DBUILD_DOC=OFF} \
   %{!?_enable_matlab:-DBUILD_MATLAB_BINDINGS=OFF}

%cmake_build

%install
%cmake_install

%check
%ctest

%files
%{?_enable_doc:%doc doc/manual.pdf}
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}

%files         -n %srcname
%_bindir/%{srcname}*

%if_enabled    devel
%files         devel
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/pkgconfig/*
%{_includedir}/%{srcname}

%files         devel-static
%{_libdir}/*.a
%endif

%if_enabled    python3
%files -n python3-module-flann
%{python3_sitelibdir}/pyflann
%{python3_sitelibdir}/flann-%{version}*.egg-info
%endif


%changelog
* Thu May 08 2025 Pavel Skrylev <majioa@altlinux.org> 1.9.2-alt3
- * quite rewrite spec
- * rebased to upstream with .gear
- ! fixed FTBFS with doc disabling

* Wed Jan 24 2024 Pavel Skrylev <majioa@altlinux.org> 1.9.2-alt2.1
- ! fixed python3 deps

* Wed Jun 28 2023 Michael Shigorin <mike@altlinux.org> 1.9.2-alt2
- E2K: lcc 1.26 ftbfs workaround (ilyakurdyukov@)

* Tue Jun 27 2023 Andrey Cherepanov <cas@altlinux.org> 1.9.2-alt1
- NMU: new version

* Sat Aug 28 2021 Igor Vlasenko <viy@altlinux.org> 1.9.1-alt1_5
- fixed build with LTO

* Tue Jul 06 2021 Igor Vlasenko <viy@altlinux.org> 1.9.1-alt1_4
- new version (closes: #40407)

* Thu Oct 17 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt2_24
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt2_21
- update to new release by fcimport

* Tue Feb 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt2_20
- update to new release by fcimport

* Mon Dec 10 2018 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt2_18
- update to new release by fcimport

* Wed Sep 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.8.4-alt2_15
- NMU: fixed build with new cmake.

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt1_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt1_6
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt1_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt1_2
- update to new release by fcimport

* Tue Apr 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.8.4-alt1_1
- update to new release by fcimport

* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt2_3
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt2_1
- added flann provides

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_1
- sisyphus release

