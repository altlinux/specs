# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(trapproto) pkgconfig(xextproto)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major		6
%define libname		libxtrap%{major}
%define develname	libxtrap-devel

Name:		libxtrap
Summary:	X Trap Library
Version:	1.0.1
Release:	alt1_7
Group:		Development/C
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXTrap-%{version}.tar.bz2

BuildRequires:	libX11-devel >= 1.0.0
BuildRequires:	libXext-devel >= 1.0.0
BuildRequires:	libXt-devel >= 1.0.0
BuildRequires:	xorg-proto-devel >= 1.0.0
BuildRequires:	xorg-util-macros >= 1.0.1
Source44: import.info

%description
X Trap Library.

#-----------------------------------------------------------

%package -n %{libname}
Summary:  X Trap Library
Group: Development/C
Provides: %{name} = %{version}

%description -n %{libname}
X Trap Library

%files -n %{libname}
%{_libdir}/libXTrap.so.%{major}*

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}xtrap-static-devel < 1.0.1-3

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%{_libdir}/libXTrap.so
%{_libdir}/pkgconfig/xtrap.pc

#-----------------------------------------------------------

%prep
%setup -q -n libXTrap-%{version}

%build
%configure	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} \
		--disable-static

%make

%install
%makeinstall_std

#we don't want these
find %{buildroot} -name "*.la" -delete


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_7
- new version

