%def_enable snapshot

%def_disable logging
%def_disable examples
%def_enable check

Name: libpisp
Version: 1.2.0
Release: alt1

Summary: A helper library to generate run-time configuration for the Raspberry Pi ISP (PiSP) 
Group: System/Libraries
License: BSD-2-Clause
Url: https://github.com/raspberrypi/libpisp

Vcs: https://github.com/raspberrypi/libpisp.git

%if_disabled snapshot
Source: https://github.com/raspberrypi/libpisp/archive/v%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif

#ExclusiveArch: aarch64

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson gcc-c++
BuildRequires: pkgconfig(nlohmann_json)
%{?_enable_logging:BuildRequires: boost-log-devel)}
%{?_enable_examples:BuildRequires: pkgconfig(cxxopts)}

%description
A helper library to generate run-time configuration for the Raspberry Pi
ISP (PiSP), consisting of the Frontend and Backend hardware components.

%package devel
Summary: libpisp development package
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%prep
%setup

%build
%meson \
    %{subst_enable_meson_feature logging logging} \
    %{subst_enable_meson_bool examples examples}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%name.so.*
%dir %_datadir/%name
%_datadir/%name/backend_default_config.json
%doc README*

%files devel
%_includedir/%name/
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Fri Apr 11 2025 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- first build for Sisyphus (v1.2.0-1-g3db57db)


