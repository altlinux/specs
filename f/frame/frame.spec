# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/a2x /usr/bin/sudo gcc-c++ pkgconfig(inputproto) pkgconfig(x11) pkgconfig(xext)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# %%name is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name frame
%define		major		6
%define		libname		lib%{name}%{major}
%define		devname		lib%{name}-devel

Name:		frame
Version:	2.5.0
Release:	alt1_4
Summary:	Buildup and synchronization of simultaneous touches
Group:		Development/Other
License:	LGPLv3 and GPLv3
URL:		https://launchpad.net/frame
Source0:	https://launchpad.net/%{name}trunk/v%{version}/+download/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(evemu)
BuildRequires:	pkgconfig(mtdev)
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(xorg-server)

Requires:	evemu
Source44: import.info

%description
Frame handles the buildup and synchronization of a
set of simultaneous touches.

#------------------------------------------------------------------

%package -n	%{libname}
Summary:	Frame Library Package
Group:		System/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n	%{libname}
This package contains the library needed to run programs
dynamically linked with %{name}.

#------------------------------------------------------------------

%package -n	%{devname}
Summary:	Frame Development Package
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n	%{devname}
This package provides headers files for %{name} development.

#------------------------------------------------------------------
%prep
%setup -q

%build
autoreconf -vfi
%configure \
		--disable-static
%make

%install
%makeinstall_std

# we don't want these
find %{buildroot} -name '*.la' -delete

%files
%doc COPYING COPYING.GPL3
%{_bindir}/%{name}-test-x11

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}
%{_libdir}/lib%{name}.so.%{major}.*

%files -n %{devname}
%{_includedir}/oif/%{name}.h
%{_includedir}/oif/%{name}_backend.h
%{_includedir}/oif/%{name}_internal.h
%{_includedir}/oif/%{name}_x11.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}*.pc


%changelog
* Fri Apr 06 2018 Igor Vlasenko <viy@altlinux.ru> 2.5.0-alt1_4
- new version

