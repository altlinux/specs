# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major		7
%define libname		libwindowswm%{major}
%define develname	libwindowswm-devel

Name:		libwindowswm
Summary:	The WindowsWM Library
Version:	1.0.1
Release:	alt1_8
Group:		Development/C
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libWindowsWM-%{version}.tar.bz2
BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xext) >= 1.0.0
BuildRequires: xorg-proto-devel >= 1.0.0
BuildRequires: xorg-util-macros >= 1.0.1
Source44: import.info

%description
The WindowsWM Library

#-----------------------------------------------------------

%package -n %{libname}
Summary:  The WindowsWM Library
Group: Development/C
Provides: %{name} = %{version}

%description -n %{libname}
The WindowsWM Library

%files -n %{libname}
%{_libdir}/libWindowsWM.so.%{major}*

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: libwindowswm7-devel
Obsoletes: %{_lib}windowswm-static-devel < 1.0.1-8

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%{_libdir}/libWindowsWM.so
%{_libdir}/pkgconfig/windowswm.pc
%{_mandir}/man3/WindowsWM.3*

#-----------------------------------------------------------

%prep
%setup -q -n libWindowsWM-%{version}

%build
# fix build on aarch64
autoreconf -vfi

%configure --disable-static
%make_build

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete


%changelog
* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_8
- update by mgaimport

* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_7
- new version

