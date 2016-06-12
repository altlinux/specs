# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# %%name or %%version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name flatzebra
%define version 0.1.6
%define major	2
%define libname lib%{name}%{major}
%define develname lib%{name}-devel

Name:		flatzebra
Version:	0.1.6
Release:	alt1_7
Summary:	A Generic Game Engine library for 2D double-buffering animation
Group:		System/Libraries
License:	GPLv2
URL:		http://sarrazip.com/dev/burgerspace.html
Source:		http://sarrazip.com/dev/%{name}-%{version}.tar.gz
BuildRequires:	libSDL-devel
BuildRequires:	libSDL_image-devel
BuildRequires:	libSDL_mixer-devel
BuildRequires: zlib-devel zlib-devel-static
Source44: import.info

%description
Generic Game Engine library suitable for BurgerSpace, Afternoon Stalker
and Cosmosmash.

%package -n %{libname}
Summary: Main library for %{name}
Group: System/Libraries


%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n %{develname}
Summary: Headers for developing programs that will use %{name}
Group: Development/C
Requires: %{libname} = %{version}
Provides: flatzebra-devel = %{version}-%{release}


%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
%configure
%make

%install

%makeinstall
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}/%{name}-%{version}

%files -n %{libname}
%doc AUTHORS COPYING README INSTALL NEWS
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%{_includedir}/%name-0.1
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc




%changelog
* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1_7
- converted for ALT Linux by srpmconvert tools

