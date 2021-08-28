# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3 rpm-macros-cmake rpm-macros-fedora-compat
BuildRequires: /usr/bin/dpkg /usr/bin/mkoctfile boost-devel boost-mpi-devel openmpi-devel
# END SourceDeps(oneline)
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Group: Development/C
%add_optflags %optflags_shared
%define oldname flann
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%undefine __cmake_in_source_build
%global srcname flann
%global soversion 1.9

Name:           libflann
Version:        1.9.1
Release:        alt1_5
Summary:        Fast Library for Approximate Nearest Neighbors

License:        BSD
URL:            http://www.cs.ubc.ca/research/flann
Source0:        https://www.github.com/mariusmuja/%{oldname}/archive/%{version}/%{oldname}-%{version}.tar.gz

# Prevent the buildsysem from running setup.py, and use system-installed libflann.so
# Not submitted upstream
Patch0:         flann-1.9.1-fixpyflann.patch
# Add a file to shared library targets
Patch2:         flann-1.8.4-srcfile.patch
BuildRequires:  gcc-c++
BuildRequires:  ctest cmake
BuildRequires:  zlib-devel

BuildRequires:  hdf5-tools libhdf5-devel
BuildRequires:  libgtest-devel

BuildRequires:  latex2html
BuildRequires:  texlive texlive-collection-basic texlive-dist
BuildRequires:  texlive texlive-collection-basic
BuildRequires:  texlive-dist

BuildRequires:  python3-devel
Source44: import.info
Provides: flann = %{version}-%{release}

%description
FLANN is a library for performing fast approximate nearest neighbor searches
in high dimensional spaces. It contains a collection of algorithms found
to work best for nearest neighbor search and a system for automatically
choosing the best algorithm and optimum parameters depending on the data sets.

%package devel
Group: Development/Other
Summary: Development headers and libraries for flann
Requires: %{name} = %{version}-%{release}
# flann/flann_mpi.hpp requires boost/mpi.hpp, which is a convenience header
# inside of the boost-devel package
Requires: boost-complete
Provides: flann-devel = %{version}-%{release}

%description devel
Development headers and libraries for flann.

%package static
Group: Development/Other
Summary: Static libraries for flann
Provides: flann-static = %{version}-%{release}

%description static
Static libraries for flann.

%package -n python3-module-flann
Group: Development/Other
Summary: Python bindings for flann
Requires: %{name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-module-flann
Python 3 bindings for flann

%prep
%setup -n %{oldname}-%{version} 
%patch0 -p0 -b .fixpyflann
%patch2 -p0 -b .srcfile

# Fix library install directory
sed -i 's/"lib"/"%{_lib}"/' cmake/flann_utils.cmake

%build
%{fedora_v2_cmake} -DBUILD_MATLAB_BINDINGS=OFF -DCMAKE_BUILD_TYPE=Release -DBUILD_PYTHON_BINDINGS=ON 
%fedora_v2_cmake_build
%fedora_v2_cmake_build %{!?rhel:--target} doc

%install
%fedora_v2_cmake_install
rm -rf %{buildroot}%{_datadir}/%{oldname}/python

# install the python bindings
cp -r src/python src/python3

cp %{_vpath_builddir}/src/python/setup.py src/python3

pushd src/python3
%{__python3} setup.py install --prefix=/usr --root=%{buildroot} --install-lib=%{python3_sitelibdir}
popd

# get rid of duplicate shared libraries
rm -rf %{buildroot}%{python3_sitelibdir}/pyflann/lib
# Remove example binaries
rm -rf %{buildroot}%{_bindir}*
# Remove installed documentation, we'll install it later with the doc macro
rm -rf %{buildroot}%{_datadir}/doc/flann

%files
%doc doc/manual.pdf
%{_libdir}/*.so.%{version}
%{_libdir}/*.so.%{soversion}

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/flann

%files static
%{_libdir}/*.a

%files -n python3-module-flann
%{python3_sitelibdir}/pyflann
%{python3_sitelibdir}/flann-%{version}*.egg-info

%changelog
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

