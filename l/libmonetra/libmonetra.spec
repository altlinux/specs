# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define	major 7
%define libname libmonetra%{major}
%define develname libmonetra-devel

Summary:	Library to allow credit card processing through MCVE
Name:		libmonetra
Version:	7.7.0
Release:	alt1_8
Group:		System/Libraries
License:	BSD
URL:		http://www.mainstreetsoftworks.com/
Source0:	ftp://ftp.mcve.com/pub/libmonetra/%{name}-%{version}.tar.gz
Patch0:		libmonetra-7.7.0-lib64.diff
Patch1:		libmonetra-7.7.0-openssl11.patch
BuildRequires:	pkgconfig(openssl)
Source44: import.info

%description
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

%package -n	%{libname}
Summary:	Library to allow credit card processing through MCVE
Group:          System/Libraries

%description -n	%{libname}
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

%package -n	%{develname}
Summary:	Static library and header files for the %{name} library
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
library for connecting to a MCVE Credit Card Processing Daemon via
SSL, TCP/IP, and drop-files.

This package contains the static %{name} library and its header
files.

%prep

%setup -q
%patch0 -p1
%patch1 -p1

%build
export WANT_AUTOCONF_2_5=1
rm -f configure
libtoolize --copy --force; aclocal; autoconf; automake --add-missing --copy

%configure

%make

%install
%makeinstall_std


%files -n %{libname}
%doc AUTHORS ChangeLog LICENSE README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%doc LICENSE
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a




%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 7.7.0-alt1_8
- new version

