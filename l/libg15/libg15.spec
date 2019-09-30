# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 1
%define libname libg15_%{major}
%define libname_devel libg15-devel
%define libname_static_devel libg15-devel-static

Name:           libg15
Version:        1.2.7
Release:        alt1_11
Summary:        Library to control logitech G15 keyboards
License:        GPLv2+
Group:          System/Libraries
URL:            http://g15tools.sourceforge.net/
Source:         http://downloads.sourceforge.net/g15tools/libg15-%{version}.tar.bz2
BuildRequires:  pkgconfig(libusb)
Source44: import.info

%description
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%package -n %{libname}
Summary:        Controls the G15 keyboard and LCD
Group:          System/Libraries
Provides:       g15 = %{version}-%{release}

%description -n %{libname}
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%package -n %{libname_devel}
Summary:        Controls the G15 keyboard and LCD
Group:          Development/C
Provides:       g15-devel = %{version}-%{release}
Requires:       g15 = %{version}-%{release}

%description -n %{libname_devel}
Controls the G15 keyboard, providing applications access
to the keyboard's LCD display, and the additional keys available
on this keyboard.

%prep
%setup -q

%build
# fix build on aarch64
autoreconf -vfi

%configure --disable-static
%make_build

%install
%makeinstall_std

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_libdir}/libg15.so.%{major}
%{_libdir}/libg15.so.%{major}.*

%files -n %{libname_devel}
%{_includedir}/*
%{_libdir}/libg15.so


%changelog
* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.7-alt1_11
- new version

