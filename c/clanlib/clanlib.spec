# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl gcc-c++ imake libX11-devel libXt-devel libalsa-devel libogg-devel libpng-devel perl(English.pm) xorg-cf-files zlib-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define api 2.3
%define major 1
%define libname libclanlib%{api}%{major}
%define develname libclanlib%{api}-devel

Name:		clanlib
Summary:	The ClanLib Game SDK series 2.3
Version:	2.3.7
Release:	alt1_6
License:	BSD-like
Group:		System/Libraries
Source0:	http://www.clanlib.org/download/releases-2.0/ClanLib-%version.tgz
Patch0:		ClanLib-2.3.6-link.patch
Patch1:		ClanLib-2.3.4-gcc47.patch
# from fedora
Patch3:		ClanLib-2.3.4-non-x86.patch
URL:		http://www.clanlib.org/
BuildRequires:	pkgconfig(libmikmod)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	libfreeglut-devel libGL-devel libGLU-devel libGLES-devel
BuildRequires:	autoconf-common autoconf_2.60
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	bzip2-devel
BuildRequires:	libvorbis-devel
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(SDL_gfx)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	xsltproc
BuildRequires:	libfreetype-devel
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libpcre)
BuildRequires:	doxygen
Source44: import.info

%description
The ClanLib Game SDK is a crossplatform game library designed to ease the work
for game developers. The goal is to provide a common interface to classical
game problems (loading graphics eg.), so games can share as much code as
possible. Ideally anyone with small resources should be able to write
commercial quality games.

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	ClanLib-devel = %{version}-%{release}
Provides:	clanlib-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package	docs
Summary:	ClanLib documentation
Group:		Documentation
BuildArch:	noarch

%description	docs
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package contains the documentation.

%prep
%setup -q -n ClanLib-%{version}
%patch0 -p0 -b .link
%patch1 -p1 -b .gcc
%patch3 -p1 -b .non-x86

%build
export CXXFLAGS="%{optflags} -fno-stack-protector"
autoreconf -fi
%configure \
	--disable-static \
	--enable-docs
%make

%install
%makeinstall_std
rm -rf %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc README COPYING CREDITS
%{_libdir}/libclan*-%{api}.so.%{major}
%{_libdir}/libclan*-%{api}.so.%{major}.*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%files docs
%{_docdir}/clanlib-%{api}


%changelog
* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt1_6
- new version

