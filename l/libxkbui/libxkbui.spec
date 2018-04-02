# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major		1
%define libname		libxkbui%{major}
%define develname	libxkbui-devel

Name:		libxkbui
Summary:	The xkbui Library
Version:	1.0.2
Release:	alt1_15
Group:		Development/C
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
BuildRequires:	libX11-devel >= 1.0.0
BuildRequires:	libxkbfile-devel >= 1.0.1
BuildRequires:	libXt-devel >= 1.0.0
BuildRequires:	xorg-util-macros >= 1.0.1
Source44: import.info

%description
The xkbui Library

#-----------------------------------------------------------

%package -n %{libname}
Summary:  The xkbui Library
Group: Development/C
Provides: %{name} = %{version}

%description -n %{libname}
The xkbui Library

%files -n %{libname}
%{_libdir}/libxkbui.so.%{major}
%{_libdir}/libxkbui.so.%{major}.*

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}xkbui-static-devel < 1.0.2-11

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%{_libdir}/libxkbui.so
%{_libdir}/pkgconfig/xkbui.pc
%{_includedir}/X11/extensions/XKBui.h

#-----------------------------------------------------------

%prep
%setup -q -n libxkbui-%{version}

%build
%configure \
	--disable-static
%make

%install
%makeinstall_std

find %{buildroot} -name "*.la" -delete


%changelog
* Mon Apr 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1_15
- new version

* Thu Apr 27 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.2-alt1
- 1.0.2

* Tue Mar 28 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt4
- CVS snapshot 2006-03-27

* Mon Jan 23 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt3
- added requires to %name-devel from buildrequires

* Fri Jan 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt2
- fixed requires for %name-devel

* Mon Dec 26 2005 Valery Inozemtsev <shrek@altlinux.ru> 1.0.1-alt1
- Xorg-7.0

* Sun Dec 04 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.2-alt1
- Xorg-7.0RC3

* Mon Nov 21 2005 Valery Inozemtsev <shrek@altlinux.ru> 0.99.1-alt0.1
- initial build

