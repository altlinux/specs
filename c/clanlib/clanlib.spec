# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/perl gcc-c++ imake libX11-devel libXt-devel libalsa-devel libogg-devel libpng-devel perl(English.pm) xorg-cf-files zlib-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define api       2.3
%define major     1
%define libname   libclanlib%{api}_%{major}
%define develname libclanlib%{api}-devel

Name:		clanlib
Summary:	The ClanLib Game SDK series 2.3
Version:	2.3.7
Release:	alt2_13
License:	BSD-like
Group:		System/Libraries
URL:		https://www.clanlib.org/
Source0:	https://www.clanlib.org/download/releases-2.0/ClanLib-%version.tgz
Patch0:		ClanLib-2.3.6-link.patch
Patch1:		ClanLib-2.3.4-gcc47.patch
# from fedora
Patch3:		ClanLib-2.3.4-non-x86.patch
Patch6:		ClanLib-2.3.7-ftbfs.patch
Patch7:		ClanLib-2.3.7-mga-mutex.patch

Patch13:         ClanLib-2.3.7-no-wm_type-in-fs.patch
Patch14:         ClanLib-2.3.7-no-ldflags-for-conftest.patch
Patch15:         ClanLib-2.3.7-gcc7.patch
# suse
Patch9:         ClanLib-2.3.6-fix-opengl.patch

BuildRequires:	pkgconfig(libmikmod)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	libfreeglut-devel libGL-devel libGLU-devel libGLES-devel
BuildRequires:	autoconf
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(bzip2)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(SDL_gfx)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:  pkgconfig(libpcre)
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
%patch6 -p1
%patch7 -p1

%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch9 -p1


%build
export CXXFLAGS="%{optflags} -fno-stack-protector"

%ifarch aarch64
export CXXFLAGS="$CXXFLAGS -mno-outline-atomics"
%endif

autoreconf -fi
%configure \
	--disable-static     \
	--enable-docs
%make_build

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete

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
* Thu Sep 14 2023 Igor Vlasenko <viy@altlinux.org> 2.3.7-alt2_13
- update by mgaimport

* Mon Jan 25 2021 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt2_11
- update by mgaimport

* Wed Oct 02 2019 Michael Shigorin <mike@altlinux.org> 2.3.7-alt2_7
- E2K: explicit -std=c++11
- enable parallel build

* Thu Feb 07 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt1_7
- fixed build

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 2.3.7-alt1_6
- new version

