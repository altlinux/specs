# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/pod2man
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major	1
%define libname	libcerf%{major}
%define devname	libcerf-devel

Name:		libcerf
Summary:	Complex error functions, Dawson, Faddeeva, and Voigt function
Version:	1.5
Release:	alt1_1
Group:		System/Libraries
License:	MIT
Url:		http://apps.jcns.fz-juelich.de/libcerf
Source0:	http://apps.jcns.fz-juelich.de/src/libcerf/libcerf-%{version}.tgz
Patch0:		libcerf-1.5-fix-version.patch
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
%patch0 -p1

%build
autoreconf -vfi
%configure
%make_build

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete

%files -n %{libname}
%doc CHANGELOG README
%doc --no-dereference COPYING
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{devname}
%doc %{_docdir}/libcerf/
%{_includedir}/cerf.h
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1_1
- new version

