# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname cminpack
Name:           libcminpack
Version:        1.3.0
Release:        alt1_2
Summary:        Solver for nonlinear equations and nonlinear least squares problems

Group:          Development/C
License:        BSD
URL:            http://devernay.free.fr/hacks/cminpack/cminpack.html
Source0:        http://devernay.free.fr/hacks/cminpack/%{oldname}-%{version}.tar.gz

BuildRequires:  ctest cmake
BuildRequires:  gcc-fortran
Source44: import.info
Provides: cminpack = %{version}-%{release}
Patch33: cminpack-1.3.0-alt-linkage.patch


%description
cminpack is an ISO C99 implementation of the FORTRAN Minpack solver package.
It is fully re-entrant and thread-safe.

%package devel
Summary: Header files and libraries for cminpack
Group: Development/C
Requires: %{name} = %{version}-%{release}
Provides: cminpack-devel = %{version}-%{release}

%description devel
Contains the development headers and libraries needed to build a program with
cminpack.

%prep
%setup -n %{oldname}-%{version} -q
%patch33 -p1

%build
mkdir build
pushd build
%{fedora_cmake} -DUSE_FPIC=ON -DSHARED_LIBS=ON -DBUILD_EXAMPLES=ON -DBUILD_EXAMPLES_FORTRAN=ON -DCMINPACK_LIB_INSTALL_DIR=%{_lib} ..
popd
make -C build  %{?_smp_mflags}


%install
make -C build install DESTDIR=%{buildroot}


%files
%doc CopyrightMINPACK.txt readme.txt readmeC.txt
%{_libdir}/libcminpack.so.*

%files devel
%doc doc/*.html doc/*.txt
%{_libdir}/pkgconfig/*
%{_libdir}/libcminpack.so
%{_includedir}/cminpack-1


%changelog
* Wed Dec 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.3.0-alt1_2
- initial fc import

