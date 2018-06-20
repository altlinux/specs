# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major		7
%define libname		libwindowswm%{major}
%define develname	libwindowswm-devel
%define staticname	libwindowswm-devel-static

Name:		libwindowswm
Summary:	The WindowsWM Library
Version:	1.0.1
Release:	alt1_7
Group:		Development/C
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libWindowsWM-%{version}.tar.bz2
BuildRequires: libX11-devel >= 1.0.0
BuildRequires: libXext-devel >= 1.0.0
BuildRequires: xorg-proto-devel >= 1.0.0
BuildRequires: xorg-util-macros >= 1.0.1
Source44: import.info

%description
The WindowsWM Library

#-----------------------------------------------------------

%package -n %{libname}
Summary:  The WindowsWM Library
Group: Development/C
Conflicts: libxorg-x11 < 7.0
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
Conflicts: libxorg-x11-devel < 7.0
Obsoletes: libwindowswm7-devel

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%{_libdir}/libWindowsWM.so
%{_libdir}/pkgconfig/windowswm.pc
%{_mandir}/man3/WindowsWM.3*


#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/C
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel-static < 7.0
Obsoletes: libwindowswm7-devel-static

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%{_libdir}/libWindowsWM.a

#-----------------------------------------------------------

%prep
%setup -q -n libWindowsWM-%{version}

%build
%configure
%make

%install
%makeinstall_std
rm -f %{buildroot}%{_libdir}/*.la


%changelog
* Thu Jun 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_7
- new version

