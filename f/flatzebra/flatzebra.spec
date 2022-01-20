# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name flatzebra
%define major	2
%define libname lib%{name}%{major}
%define develname lib%{name}-devel

Name:		flatzebra
Version:	0.1.7
Release:	alt1_1
Summary:	A Generic Game Engine library for 2D double-buffering animation
Group:		System/Libraries
License:	GPLv2
URL:		http://perso.b2b2c.ca/~sarrazip/dev/burgerspace.html
Source:		http://perso.b2b2c.ca/~sarrazip/dev/burgerspace.html/dev/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	pkgconfig(zlib)
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
Requires: %{libname} = %{version}-%{release}
Provides: flatzebra-devel = %{version}-%{release}


%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%prep
%setup -q

%build
# fix build on aarch64
autoreconf -vfi

%configure
%make_build

%install

%makeinstall_std
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
* Thu Jan 20 2022 Igor Vlasenko <viy@altlinux.org> 0.1.7-alt1_1
- update by mgaimport

* Fri Oct 01 2021 Igor Vlasenko <viy@altlinux.org> 0.1.6-alt1_10
- fixed build with gcc11

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1_8
- update by mgaimport

* Sun Jun 12 2016 Igor Vlasenko <viy@altlinux.ru> 0.1.6-alt1_7
- converted for ALT Linux by srpmconvert tools

