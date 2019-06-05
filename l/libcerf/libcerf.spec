# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-mageia-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
BuildRequires: /usr/bin/pod2man /usr/bin/pod2html
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major	1
%define libname	libcerf%{major}
%define devname	libcerf-devel

%global _cmake_skip_rpath %nil

Name:		libcerf
Summary:	Complex error functions, Dawson, Faddeeva, and Voigt function
Version:	1.13
Release:	alt1_3
Group:		System/Libraries
License:	MIT
Url:		http://apps.jcns.fz-juelich.de/libcerf
Source0:	http://apps.jcns.fz-juelich.de/src/libcerf/libcerf-%{version}.tgz
Patch1:		0001-Fix-64bit-library-location.patch
Patch2:		0001-Fix-64bit-pkgconfig-.pc-file-location.patch
BuildRequires:	ccmake cmake ctest
BuildRequires:	clang7.0 llvm7.0
Source44: import.info

%description
A self-contained C library providing complex error functions, based on
Faddeeva's plasma dispersion function w(z).

Also provides Dawson's integral and Voigt's convolution of a Gaussian
and a Lorentzian.

%package -n %{libname}
Summary:	Complex error functions, Dawson, Faddeeva, and Voigt function
Group:		System/Libraries

%description -n %{libname}
A self-contained C library providing complex error functions, based on
Faddeeva's plasma dispersion function w(z).

Also provides Dawson's integral and Voigt's convolution of a Gaussian
and a Lorentzian.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
%remove_optflags -frecord-gcc-switches
# for some reason %ix86 tests fails with gcc
export CC=clang
%{mageia_cmake}
%make_build V=1

%install
%makeinstall_std -C build

%check
%{mageia_ctest}

%files -n %{libname}
%doc CHANGELOG README
%doc --no-dereference COPYING
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{version}

%files -n %{devname}
%doc %{_docdir}/libcerf/
%{_includedir}/cerf.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*


%changelog
* Wed Jun 05 2019 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_3
- mga update

* Mon Mar 18 2019 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_2
- new version

* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1
- new version

