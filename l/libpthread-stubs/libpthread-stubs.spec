# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# This package only contains arch specific .pc file
%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Name: libpthread-stubs
Summary: PThread Stubs for XCB
Version: 0.4
Release: alt1_1
Group: System/X11
License: MIT
URL: http://xcb.freedesktop.org
Source0: http://xcb.freedesktop.org/dist/libpthread-stubs-%{version}.tar.bz2
BuildRequires: xorg-proto-devel >= 1.2.0
BuildRequires: xorg-util-macros >= 1.0.1
BuildRequires: xsltproc
Source44: import.info

%description
PThread Stubs for XCB

%prep
%setup -q -n libpthread-stubs-%{version}

%build
%configure
%make

%install
%makeinstall_std

%files 
%{_libdir}/pkgconfig/pthread-stubs.pc


%changelog
* Sun Mar 18 2018 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_1
- new version

