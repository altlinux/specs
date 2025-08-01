# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major                3
%define libname              libg15_%{major}
%define libname_devel        libg15-devel

Name:           libg15
Version:        3.0.7
Release:        alt1_2
Summary:        Library to control logitech G15 keyboards
License:        GPLv2+
Group:          System/Libraries
URL:            https://gitlab.com/menelkir/libg15
Source:         https://gitlab.com/menelkir/libg15/-/archive/%{version}/libg15-%{version}.tar.bz2
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
%configure --disable-static
%make_build

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%doc AUTHORS ChangeLog README
%doc --no-dereference COPYING
%{_libdir}/libg15.so.%{major}
%{_libdir}/libg15.so.%{major}.*

%files -n %{libname_devel}
%{_includedir}/*
%{_libdir}/libg15.so


%changelog
* Fri Aug 01 2025 Igor Vlasenko <viy@altlinux.org> 3.0.7-alt1_2
- update by mgaimport

* Mon Jan 30 2023 Andrey Cherepanov <cas@altlinux.org> 1.3.1-alt1
- New version.

* Sun Sep 29 2019 Igor Vlasenko <viy@altlinux.ru> 1.2.7-alt1_11
- new version

