%define major   3
%define sname   atg
%define libname lib%{sname}%{major}
%define devname lib%{sname}-devel

Name:           libatg
Version:        3.0.0
Release:        alt1_1
Summary:        A Tiny GUI toolkit for SDL
Group:          System/Libraries
License:        GPLv3+
URL:            https://github.com/ec429/libatg
Source0:        https://github.com/ec429/libatg/archive/lv%{version}.tar.gz
# https://github.com/ec429/libatg/pull/5
Patch0:         0001-Makefile-Support-DESTDIR-and-overriding-LIBDIR.patch
Patch1:         0002-Makefile-Enforce-CC-tag-for-libtool.patch
Patch2:         0003-Makefile-Do-not-run-ldconfig-libtool-does-it-already.patch

Patch33:	atg-3.0.0-alt-link.patch

BuildRequires:  fonts-ttf-liberation
BuildRequires:  libtool
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(SDL_ttf)
Source44: import.info

%description
A Tiny GUI (atg) is a small, simple GUI library/toolkit for SDL, providing
things like buttons and clickables to allow you to concentrate on your
program logic. atg is loosely based on Spiffy's GUI, though genericised.

#----------------------------------------------------------------------------

%package -n     %{libname}
Summary:        A Tiny GUI toolkit for SDL
Group:          System/Libraries
Requires:       fonts-ttf-liberation

%description -n %{libname}
A Tiny GUI (atg) is a small, simple GUI library/toolkit for SDL, providing
things like buttons and clickables to allow you to concentrate on your
program logic. atg is loosely based on Spiffy's GUI, though genericised.

This package contains the shared libraries.

%files -n       %{libname}
%{_libdir}/lib%{sname}.so.%{major}*

#----------------------------------------------------------------------------

%package -n     %{devname}
Summary:        Development headers for A Tiny GUI
Group:          Development/C
Provides:       %{sname}-devel = %{version}-%{release}
Requires:       %{libname} = %{version}

%description -n %{devname}
A Tiny GUI (atg) is a small, simple GUI library/toolkit for SDL, providing
things like buttons and clickables to allow you to concentrate on your
program logic. atg is loosely based on Spiffy's GUI, though genericised.

This package contains the development headers.

%files -n       %{devname}
%{_includedir}/%{sname}*.h
%{_libdir}/lib%{sname}.so

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-lv%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch33 -p1

# we do not have make 4 :(
sed -i -e 's,MONOFONTPATH !=,MONOFONTPATH ?=', Makefile

%build

%make_build \
    MONOFONTPATH=`find /usr/share/fonts -name LiberationMono-Regular.ttf -print -quit` \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir}

%install
%makeinstall_std \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir}

find %{buildroot} -name "*.la" -delete
find %{buildroot} -name "*.a" -delete


%changelog
* Tue Nov 01 2016 Igor Vlasenko <viy@altlinux.ru> 3.0.0-alt1_1
- update by mgaimport

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_3
- converted for ALT Linux by srpmconvert tools

