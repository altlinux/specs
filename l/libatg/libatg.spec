BuildRequires:  gcc-c++ gcc-fortran
%define major   1
%define sname   atg
%define libname lib%{sname}%{major}
%define devname lib%{sname}-devel

Name:           libatg
Version:        2.1.1
Release:        alt1_3
Summary:        A Tiny GUI toolkit for SDL
Group:          System/Libraries
License:        GPLv3+
URL:            https://github.com/ec429/libatg
Source0:        https://github.com/ec429/libatg/archive/lv%{version}.tar.gz
Patch0:         atg-2.0.1-mga-fix-paths.patch
Patch1:         atg-2.0.1-mga-liberation-font-path.patch
Patch2: 	Makefile.alt.patch

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
#sed -i -e 's,libtool,libtool --tag=CC,' Makefile
%patch2 -p0

%build
%make PREFIX=%{_prefix} \
      LIBDIR=%{_libdir} \
      OPTFLAGS="%{optflags} -Wno-error=format-security"

%install
%makeinstall_std PREFIX=%{_prefix} \
                 LIBDIR=%{_libdir}

find %{buildroot} -name "*.la" -delete
find %{buildroot} -name "*.a" -delete


%changelog
* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 2.1.1-alt1_3
- converted for ALT Linux by srpmconvert tools

