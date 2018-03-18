# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 6
%define liboldx liboldx%{major}
%define devoldx liboldx-devel

Name: liboldx
Summary:  The oldX Library
Version: 1.0.1
Release: alt1_15
Group: Development/C
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/liboldX-%{version}.tar.bz2
BuildRequires: libX11-devel >= 1.0.0
BuildRequires: xorg-proto-devel >= 1.0.0
BuildRequires: xorg-util-macros >= 1.0.1
Source44: import.info

%description
X.Org X11 liboldX runtime library.

#-----------------------------------------------------------

%package -n %{liboldx}
Summary:  The oldX Library
Group: Development/C
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{liboldx}
The oldX Library

%files -n %{liboldx}
%{_libdir}/liboldX.so.%{major}
%{_libdir}/liboldX.so.%{major}.0.0

#-----------------------------------------------------------

%package -n %{devoldx}
Summary: Development files for %{name}
Group: Development/C
Requires: %{liboldx} = %{version}-%{release}
Provides: liboldx-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Obsoletes: %{_lib}oldx6-devel < 1.0.1-11
Obsoletes: %{_lib}oldx6-static-devel < 1.0.1-11

%description -n %{devoldx}
Development files for %{name}.

%files -n %{devoldx}
%{_libdir}/liboldX.so
%{_libdir}/pkgconfig/oldx.pc
%{_includedir}/X11/X10.h

#-----------------------------------------------------------

%prep
%setup -q -n liboldX-%{version}

%build
%configure \
	--disable-static
%make

%install
%makeinstall_std

find %{buildroot} -name "*.la" -delete


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_15
- new version

