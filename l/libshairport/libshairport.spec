# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major	1
%define libname	libshairport%{major}
%define devname	libshairport-devel

%define snap	20120111
%define rel	8

Summary:	Apple RAOP server library
Name:		libshairport
Version:	1.2.1
Release:	alt1_0.git%snap.%rel
License:	MIT
Group:		System/Libraries
URL:		https://github.com/amejia1/libshairport
# git archive --prefix libshairport-20120111/ master | xz > libshairport-20120111.tar.xz
Source:		%name-%snap.tar.xz
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(ao)
Source44: import.info

%description
This library emulates an AirPort Express for the purpose of streaming
music from iTunes and compatible iPods. It implements a server for the
Apple RAOP protocol.

ShairPort does not support AirPlay v2 (video and photo streaming).

%package -n %libname
Summary:	Shared library of libshairport
Group:		System/Libraries
Provides:	%name = %version-%release

%description -n %libname
libshairport is an Apple RAOP server library.

This package contains the library needed to run programs dynamically
linked with libshairport.

%package -n %devname
Summary:	Headers for libshairport development
Group:		Development/C
Requires:	%libname = %version
# we are not actually linking against it (just using the headers), so this
# doesn't get added automatically:
Provides:	shairport-devel = %version-%release

%description -n %devname
libshairport is an Apple RAOP server library.

This package contains the headers that are needed to compile
applications that use libshairport.

%prep
%setup -q -n %name-%snap

%build
autoreconf -fi
%configure --disable-static
%make

%install
%makeinstall_std

find %{buildroot} -name '*.la' | xargs rm

%files -n %libname
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %devname
%doc README
%{_libdir}/*.so
%dir %{_includedir}/shairport
%{_includedir}/shairport/*.h
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.2.1-alt1_0.git20120111.8
- new version

