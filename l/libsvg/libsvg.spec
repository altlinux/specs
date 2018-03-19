# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major   1
%define libname libsvg%{major}
%define develname libsvg-devel

Summary:	A generic SVG library
Name:		libsvg
Version:	0.1.4
Release:	alt2_20
License:	LGPL
Group:		System/Libraries
URL:		http://cairographics.org/snapshots/
Source:		http://cairographics.org/snapshots/%{name}-%{version}.tar.bz2
Patch0:		libsvg-0.1.4-link.patch
Patch1:		libsvg-0.1.4-libpng14.patch
BuildRequires:	libxml2-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel libturbojpeg-devel
Source44: import.info

%description
A generic SVG library.

%package -n	%{libname}
Summary:	A generic SVG library
Group:		System/Libraries

%description -n	%{libname}
A generic SVG library.

%package -n	%{develname}
Summary:	Libraries and include files for developing with libsvg
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}

%description -n	%{develname}
This package provides the necessary development libraries and include
files to allow you to develop with libsvg.

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure --disable-static
%make

%install
%makeinstall_std

# remove .la file
rm -f %{buildroot}%{_libdir}/libsvg.la

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/libsvg.pc


%changelog
* Mon Mar 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.4-alt2_20
- new version

