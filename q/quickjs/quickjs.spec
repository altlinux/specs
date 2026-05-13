Name: quickjs
Version: 2025.09.13.2
Release: alt1

Summary: small and embeddable Javascript engine
License: MIT
Group: Development/Tools

Url: https://bellard.org/quickjs/
# repacked https://bellard.org/quickjs/quickjs-2025-09-13-2.tar.xz
Source0: %name-%version.tar

%define common_description \
QuickJS is a small and embeddable Javascript engine.\
It supports the ES2020 specification including modules,\
asynchronous generators, proxies and BigInt.\
It optionally supports mathematical extensions such as \
big decimal floating point numbers (BigDecimal),\
big binary floating point numbers (BigFloat) and operator overloading.

%description
%common_description

%package devel
Summary: Header files for QuickJS
Group: Development/C
Requires: %name = %EVR

%description devel
%common_description

%package devel-static
Summary: Static libraries for QuickJS
Group: Development/C
Requires: %name = %EVR

%description devel-static
%common_description

%package examples
Summary: Examples for QuickJS
Group: Development/Tools
BuildArch: noarch
Requires: %name = %EVR

%description examples
%common_description

%package doc
Summary: Documentation for QuickJS
Group: Documentation
BuildArch: noarch

%description doc
%common_description

%prep
%setup
sed -i 's|lib/quickjs|%_lib/quickjs|' Makefile qjsc.c
sed -i 's|/usr/local|/usr|g' Makefile

%build
%make_build

%install
%makeinstall_std

%files
%doc LICENSE
%_bindir/*

%files devel
%_includedir/*

%files devel-static
%_libdir/%name

%files examples
%doc examples/*.c
%doc examples/*.js

%files doc
%doc doc/*

%changelog
* Wed May 13 2026 Nikolay Burykin <bne@altlinux.org> 2025.09.13.2-alt1
- 2025.09.13.2

* Wed Jul 01 2025 Nikolay Burykin <bne@altlinux.org> 2025.04.26-alt1
- Initial build for ALT
