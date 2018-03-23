# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name spglib
%define major		0
%define libname		libsymspg%{major}
%define develname	lib%{name}-devel

Name:		spglib
Version:	1.10.2
Release:	alt1_1
Summary:	C library for finding and handling crystal symmetries
License:	BSD
Group:		System/Libraries
Url:		https://atztogo.github.io/spglib/
Source:		https://github.com/atztogo/spglib/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
Source44: import.info

%description
C library for finding and handling crystal symmetries.

#----------------------------------------------------

%package -n	%{libname}
Summary:	C library for finding and handling crystal symmetries
Group:		System/Libraries

%description -n	%{libname}
C library for finding and handling crystal symmetries.
This package contains library files for %{name}.

#----------------------------------------------------

%package -n	%{develname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	libspg-devel = %{version}-%{release}

%description -n	%{develname}
The %{develname} package contains libraries and header files for
developing applications that use %{name}.

#----------------------------------------------------

%prep
%setup -q

%build
touch INSTALL NEWS README AUTHORS
autoreconf -vfi

%configure --disable-static

%make_build

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%{_libdir}/libsymspg.so.%{major}*

%files -n %{develname}
%doc ChangeLog README.md
%doc --no-dereference COPYING
%{_includedir}/%{name}/
%{_libdir}/libsymspg.so


%changelog
* Fri Mar 23 2018 Igor Vlasenko <viy@altlinux.ru> 1.10.2-alt1_1
- new version

