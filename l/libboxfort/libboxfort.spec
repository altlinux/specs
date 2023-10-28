%define optflags_lto %nil

%define oname boxfort
Name: libboxfort
Version: 0.1.4.0.4.c91d718
Release: alt1

Summary: Convenient & cross-platform sandboxing C library

License: MIT
Group: System/Libraries
Url: https://github.com/Snaipe/BoxFort

# Source-url: https://github.com/Snaipe/BoxFort/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Patch3500: 0001-Support-LoongArch-architecture-lp64-ABIs.patch

ExcludeArch: armh ppc64le

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson

%description
Convenient & cross-platform sandboxing C library

%package devel
Summary: Header files for %name library
Group: Development/C
#Requires: %name = %EVR

%description devel
Header files for %name library.


%prep
%setup
%patch3500 -p1

%build
%meson
%meson_build

%install
%meson_install

%files devel
%_libdir/%name.a
%_pkgconfigdir/*
%_includedir/*.h

%changelog
* Sat Oct 28 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.1.4.0.4.c91d718-alt1
- Support LoongArch and riscv64 architectures

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 0.1.4-alt1
- initial build for ALT Sisyphus
