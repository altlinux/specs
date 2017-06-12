Name: libvariant
Version: 1.1.5
Release: alt1

Summary: C++11/C++14 Variant

Group: Development/C++
License: BSD

Url: https://github.com/mapbox/variant
Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/mapbox/variant/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: gcc-c++

%description
An header-only alternative to boost::variant for C++11 and C++14.

%package devel
Group: Development/Other
Summary: Development files for %name

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup

%build
# build test skipped

%install
mkdir -p %buildroot%_includedir/%name/
cp -a include/mapbox %buildroot%_includedir/%name/

%files devel
%dir %_includedir/%name/
%_includedir/%name/mapbox/

%changelog
* Mon Jun 12 2017 Vitaly Lipatov <lav@altlinux.ru> 1.1.5-alt1
- initial build for ALT Sisyphus
