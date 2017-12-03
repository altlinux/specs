# Set Git revision of library...
%global commit0 0b0dd886bd05d389649a043bb1d0bcd27c2bf25d
%global shortcommit0 %(c=%commit0; echo ${c:0:7})
%global date 20171112

Name: range-v3

Summary: Experimental range library for C++11/14/17
Version: 0.3.0
Release: alt1.%{date}git%{shortcommit0}

License: Boost
Group: Development/C++
Url: https://github.com/ericniebler/%name

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: %url/archive/%commit0.tar.gz#/%name-%shortcommit0.tar.gz
Source: %name-%version.tar
BuildArch: noarch

%description
Header-only %summary.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/C++
Provides: %name-static = %version-%release

%description -n lib%name-devel
Experimental range library for C++11/14/17.

%prep
%setup

%build
# Nothing to build. Header-only library.

%install
# Installing headers...
mkdir -p "%buildroot%_includedir/%name"
cp -a include/* "%buildroot%_includedir/%name"

%files -n lib%name-devel
%doc README.md CREDITS.md TODO.md
%doc LICENSE.txt
%_includedir/%name

%changelog
* Sun Dec 03 2017 Vitaly Lipatov <lav@altlinux.ru> 0.3.0-alt1.20171112git0b0dd88
- initial build for ALT Sisyphus

* Fri Dec 01 2017 Vitaly Zaitsev <vitaly@easycoding.org> - 0.3.0-1.20171112git0b0dd88
- Initial SPEC release.
