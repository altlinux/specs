# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major	2
%define libname libpcd%{major}
%define devname libpcd-devel

Summary:	Library for decoding PhotoCD images
Name:		libpcd
Version:	1.0.1
Release:	alt1_14
License:	GPLv2
Group:		System/Libraries
URL:		http://linux.bytesex.org/fbida/libpcd.html
Source:		http://dl.bytesex.org/releases/%{name}/%{name}_%{version}.tar.bz2
Source44: import.info

%description
%{name} is a tiny library for decoding PhotoCD images. It used to come
bundled with xpcd, but software maintainer decided to release the library
separately after declaring xpcd obsolete.

%package	-n %{libname}
Summary:	Library for decoding PhotoCD images
Group:		System/Libraries

%description	-n %{libname}
%{name} is a tiny library for decoding PhotoCD images. It used to come
bundled with xpcd, but software maintainer decided to release the library
separately after declaring xpcd obsolete.

%package	-n %{devname}
Summary:	Development related files of %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}pcd2-devel < 1.0.1-10

%description	-n %{devname}
%{name} is a tiny library for decoding PhotoCD images. It used to come
bundled with xpcd, but software maintainer decided to release the library
separately after declaring xpcd obsolete.

This package contains all files you need to compile applications/libraries
that has Photo CD image support.

%prep
%setup -q

%build
export CFLAGS="%optflags"
%make

%install
# don't use makeinstall_std
%makeinstall

find %{buildroot} -name "*.a" -delete

%files -n %{libname}
%doc README
%{_libdir}/%{name}.so.%{major}
%{_libdir}/%{name}.so.%{major}.*

%files -n %{devname}
%doc pcd.css pcd.html
%{_includedir}/pcd.h
%{_libdir}/%{name}.so


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_14
- new version

