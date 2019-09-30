# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 1
%define libname libopenspecfun%{major}
%define develname libopenspecfun-devel


Summary:        Library providing a collection of special mathematical functions
Name:           openspecfun
Version:        0.5.3
Release:        alt1_3
License:        MIT and Public Domain
Group:          System/Libraries
Source0:        https://github.com/JuliaLang/openspecfun/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
URL:            https://github.com/JuliaLang/openspecfun
BuildRequires:  gcc-fortran
Source44: import.info

%description
Currently provides AMOS and Faddeeva. AMOS (from Netlib) is a
portable package for Bessel Functions of a Complex Argument and
Nonnegative Order; it contains subroutines for computing Bessel
functions and Airy functions. Faddeeva allows computing the
various error functions of arbitrary complex arguments (Faddeeva
function, error function, complementary error function, scaled
complementary error function, imaginary error function, and Dawson function);
given these, one can also easily compute Voigt functions, Fresnel integrals,
and similar related functions as well.

%package -n %{libname}
Summary:        Library providing a collection of special mathematical functions
Group:          System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
Currently provides AMOS and Faddeeva. AMOS (from Netlib) is a
portable package for Bessel Functions of a Complex Argument and
Nonnegative Order; it contains subroutines for computing Bessel
functions and Airy functions. Faddeeva allows computing the
various error functions of arbitrary complex arguments (Faddeeva
function, error function, complementary error function, scaled
complementary error function, imaginary error function, and Dawson function);
given these, one can also easily compute Voigt functions, Fresnel integrals,
and similar related functions as well.

%package -n %{develname}
Summary:    Library providing a collection of special mathematical functions
Group:      System/Libraries
Requires:   %{libname} = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}

%description -n %{develname}
Contains header files for developing applications that use the %{name}
library.

%prep
%setup -q %{name}-%{version}

%build
%make \
      FFLAGS="%{optflags}" \
      CFLAGS="%{optflags}" \
      USE_OPENLIBM=0 \
      includedir=%{_includedir}

%install
make install prefix=%{_prefix} \
             libdir=%{_libdir} \
             includedir=%{_includedir} \
             DESTDIR=%{buildroot}

rm %{buildroot}/%{_libdir}/libopenspecfun.a

%files -n %{libname}
%doc LICENSE.md README.md
%{_libdir}/libopenspecfun.so.%{major}*

%files -n %{develname}
%{_libdir}/libopenspecfun.so
%{_includedir}/Faddeeva.h


%changelog
* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 0.5.3-alt1_3
- new version

