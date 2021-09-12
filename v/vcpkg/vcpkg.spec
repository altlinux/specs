%define oname vcpkg-tool

Name: vcpkg
Version: 2021.09.10
Release: alt1

Summary: C++ Library Manager

License: MIT
Group: System/Configuration/Packaging
Url: https://github.com/microsoft/vcpkg-tool

%define repotag %(echo %version | sed -e 's|\\.|-|g')
# Source-url: https://github.com/microsoft/vcpkg-tool/archive/refs/tags/%repotag.tar.gz
Source: %name-%version.tar
Source1: %name.sh

BuildRequires: catch2-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
Vcpkg is a package manager for the different C and C++ libraries.

Vcpkg can collect usage data. The data collected by Microsoft is anonymous.

Fedora package has telemetry disabled by default. If you want enable
telemetry, you should remove the %_sysconfdir/profile.d/%name.sh file
or unset the VCPKG_DISABLE_METRICS environment variable.

%prep
%setup

# Fixing line endings...
sed -e "s,\r,," -i README.md

# Unbundling catch...
rm -rv include/catch2
ln -svf %_includedir/catch2/ include/

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTING:BOOL=OFF \
    -DVCPKG_DEVELOPMENT_WARNINGS:BOOL=OFF \
    -DVCPKG_WARNINGS_AS_ERRORS:BOOL=OFF \
    -DVCPKG_BUILD_TLS12_DOWNLOADER:BOOL=OFF \
    -DVCPKG_BUILD_FUZZING:BOOL=OFF \
    -DVCPKG_EMBED_GIT_SHA:BOOL=OFF \
    -DVCPKG_BUILD_BENCHMARKING:BOOL=OFF \
    -DVCPKG_ADD_SOURCELINK:BOOL=OFF
%cmake_build

%install
%cmake_install

# Installing environment options override...
install -D -m 0644 -p "%SOURCE1" "%buildroot%_sysconfdir/profile.d/%name.sh"

%files
%doc README.md
%doc LICENSE.txt NOTICE.txt
%_bindir/%name
%config(noreplace) %_sysconfdir/profile.d/%name.sh

%changelog
* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 2021.09.10-alt1
- new version 2021.09.10 (with rpmrb script)

* Sun Sep 12 2021 Vitaly Lipatov <lav@altlinux.ru> 2021.08.12-alt1
- initial build for ALT Sisyphus

* Tue Aug 17 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.08.12-1
- Updated to version 2021.08.12.

* Wed Aug 04 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.08.03-1
- Updated to version 2021.08.03.

* Sun Jul 25 2021 Vitaly Zaitsev <vitaly@easycoding.org> - 2021.07.21-1
- Initial SPEC release.
