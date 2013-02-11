# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-macros-fedora-compat
BuildRequires: gcc-c++ unzip
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname flann
%define fedora 18
%if 0%{?rhel} < 6 && ! 0%{?fedora}
%{!?python_sitearch: %global python_sitearch %(/usr/bin/python26 -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
%endif

Name:           libflann
Version:        1.8.1
Release:        alt2_3
Summary:        Fast Library for Approximate Nearest Neighbors

Group:          Development/C
License:        BSD
URL:            http://www.cs.ubc.ca/~mariusm/index.php/FLANN/FLANN
Source0:        http://www.cs.ubc.ca/~mariusm/uploads/FLANN/%{oldname}-%{version}-src.zip

# Prevent the buildsysem from running setup.py, not submitted upstream
Patch0:         flann-1.6.11.fixpyflann.patch 
BuildRequires:  ctest cmake
BuildRequires:  zlib-devel

%if 0%{?fedora}
BuildRequires:  libhdf5-devel
BuildRequires:  libgtest-devel
%endif

%if 0%{?rhel} >= 6 || 0%{?fedora}
BuildRequires:  python-devel
%else
BuildRequires:  python26
BuildRequires:  python26-devel
%endif
Source44: import.info
Provides: flann = %{version}-%{release}


%description
FLANN is a library for performing fast approximate nearest neighbor searches 
in high dimensional spaces. It contains a collection of algorithms found 
to work best for nearest neighbor search and a system for automatically 
choosing the best algorithm and optimum parameters depending on the data sets.

%package devel
Summary: Development headers and libraries for flann
Group: Development/C
Requires: %{name} = %{version}-%{release}
Provides: flann-devel = %{version}-%{release}
# flann/flann_mpi.hpp requires boost/mpi.hpp, which is a convenience header
# inside of the boost-devel package

%description devel
Development headers and libraries for flann.

%package static
Summary: Static libraries for flann
Group: Development/C
Provides: flann-static = %{version}-%{release}

%description static
Static libraries for flann.

%package -n python-module-libflann
Summary: Python bindings for flann
Group: Development/Python
Requires: %{name} = %{version}-%{release}
Requires: python-module-numpy python-module-numpy-addons python-module-numpy-testing

%description -n python-module-libflann
Python bindings for flann

%prep
%setup -q -n %{oldname}-%{version}-src
%patch0 -p0 -b .fixpyflann

# Fix library install directory
sed -i 's/"lib"/"%{_lib}"/' cmake/flann_utils.cmake

%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{fedora_cmake} -DBUILD_MATLAB_BINDINGS=OFF  -DCMAKE_BUILD_TYPE=RelWithDebInfo -DBUILD_PYTHON_BINDINGS=ON ..
popd
make %{?_smp_mflags} -C %{_target_platform}


%install
make install DESTDIR=%{buildroot} -C %{_target_platform}
rm -rf %{buildroot}%{_datadir}/%{oldname}/python

# install the python bindings
cp %{_target_platform}/src/python/setup.py src/python
pushd src/python
%if 0%{?rhel} >= 6 || ! 0%{?rhel}
python setup.py install --prefix=/usr --root=%{buildroot} --install-lib=%{python_sitelibdir}
%else
python26 setup.py install --prefix=/usr --root=%{buildroot} --install-lib=%{python_sitelibdir}
%endif
popd
# get rid of duplicate shared libraries
rm -rf %{buildroot}%{python_sitelibdir}/pyflann/lib
# Remove example binaries
rm -rf %{buildroot}%{_bindir}*
# Remove installed documentation, we'll install it later with the doc macro
rm -rf %{buildroot}%{_datadir}/doc/flann

%files
%doc doc/manual.pdf
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/flann

%files static
%{_libdir}/*.a

%files -n python-module-libflann
%{python_sitelibdir}/pyflann
%{python_sitelibdir}/flann-%{version}*.egg-info

%changelog
* Mon Feb 11 2013 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt2_3
- update to new release by fcimport

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt2_1
- added flann provides

* Thu Dec 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1_1
- sisyphus release

