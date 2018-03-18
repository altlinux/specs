# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ pkgconfig(fontcacheproto) pkgconfig(xextproto)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 1
%define libxfontcache libxfontcache%{major}
%define develname libxfontcache-devel

Name: libxfontcache
Summary:  The Xfontcache Library
Version: 1.0.5
Release: alt1_10
Group: Development/C
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXfontcache-%{version}.tar.bz2
BuildRequires: libX11-devel >= 1.0.0
BuildRequires: libXext-devel >= 1.0.0
BuildRequires: xorg-proto-devel >= 1.0.0
BuildRequires: xorg-util-macros >= 1.0.1
Source44: import.info

%description
The Xfontcache Library

#-----------------------------------------------------------

%package -n %{libxfontcache}
Summary:  The Xfontcache Library
Group: Development/C
Provides: %{name} = %{version}

%description -n %{libxfontcache}
The Xfontcache Library

%files -n %{libxfontcache}
%{_libdir}/libXfontcache.so.%{major}
%{_libdir}/libXfontcache.so.%{major}.*

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libxfontcache} = %{version}-%{release}
Provides: libxfontcache-devel = %{version}-%{release}
Obsoletes: %{_lib}xfontcache1-devel < 1.0.5-3
Obsoletes: %{_lib}xfontcache-static-devel < 1.0.5-6

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%{_libdir}/libXfontcache.so
%{_libdir}/pkgconfig/xfontcache.pc
%{_mandir}/man3/FontCache*
%{_mandir}/man3/Xfontcache*

#-----------------------------------------------------------

%prep
%setup -q -n libXfontcache-%{version}

%build
%configure	--disable-static
%make

%install
%makeinstall_std

find %{buildroot} -name "*.la" -delete


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.5-alt1_10
- new version

