# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-cmake rpm-macros-fedora-compat
# END SourceDeps(oneline)
Group: Development/C
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define autorelease 1

Name:       xcb-imdkit
Version:    1.0.4
Release:    alt1_1
Summary:    Input method development support for xcb
# source files in src/xlibi18n use the "old style" MIT license known as NTP.
License:    LGPLv2 and MIT
URL:        https://github.com/fcitx/xcb-imdkit
Source:     https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
Source1:    https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz.sig
Source2:    https://pgp.key-server.io/download/0x8E8B898CBF2412F9

BuildRequires:  gnupg2
BuildRequires:  ctest cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)
Source44: import.info

%description
xcb-imdkit is an implementation of xim protocol in xcb, 
comparing with the implementation of IMDkit with Xlib, 
and xim inside Xlib, it has less memory foot print, 
better performance, and safer on malformed client.

%package -n libxcb-imdkit1
Summary:        Shared library for the %name library
Group:          System/Libraries
Provides: xcb-imdkit1 = %{version}-%{release}

%description -n libxcb-imdkit1
xcb-imdkit is an implementation of xim protocol in xcb, 
comparing with the implementation of IMDkit with Xlib, 
and xim inside Xlib, it has less memory foot print, 
better performance, and safer on malformed client.

This package contains the shared library.

%package -n libxcb-imdkit-devel
Group: Development/C
Summary:        Development files for %{name}
Requires:       libxcb-imdkit1 = %EVR
Provides: %name-devel = %EVR
Provides: xcb-imdkit-devel = %{version}-%{release}

%description -n libxcb-imdkit-devel
Devel files for xcb-imdkit

%prep
%setup -q


%build
%{fedora_v2_cmake}
%fedora_v2_cmake_build

%install
%fedora_v2_cmake_install

%check
%fedora_v2_ctest

%files -n libxcb-imdkit1
%doc --no-dereference LICENSES/LGPL-2.1-only.txt
%doc README.md
%_libdir/libxcb-imdkit.so.1
%_libdir/libxcb-imdkit.so.1.*

%files -n libxcb-imdkit-devel
%{_includedir}/xcb-imdkit/
%{_libdir}/cmake/XCBImdkit/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/xcb-imdkit.pc

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1.0.4-alt1_1
- update to new release by fcimport

* Fri Sep 16 2022 Igor Vlasenko <viy@altlinux.org> 1.0.3-alt1_5
- new version

