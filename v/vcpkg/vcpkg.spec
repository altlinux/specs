%define oname vcpkg-tool

Name: vcpkg
Version: 2026.09.26
Release: alt2

Summary: C++ Library Manager

License: MIT
Group: System/Configuration/Packaging
Url: https://github.com/microsoft/vcpkg-tool

%define repotag %(echo %version | sed -e 's|\\.|-|g')
# Source-url: https://github.com/microsoft/vcpkg-tool/archive/refs/tags/%repotag.tar.gz
Source: %name-%version.tar
Source1: %name.sh
Source2: %name-wrapper.sh
Source3: README.ALT

Requires: /usr/bin/git

BuildRequires(pre): rpm-macros-cmake
BuildRequires: catch2-devel
BuildRequires: libfmt-devel >= 9.1.0
BuildRequires: libcurl-devel
BuildRequires: rpm-build-cmake
BuildRequires: cmrc >= 2.0.1
BuildRequires: gcc-c++
BuildRequires: ninja-build

%description
Vcpkg is a package manager for the different C and C++ libraries.

Vcpkg can collect usage data. The data collected by Microsoft is anonymous.

Telemetry is disabled by default. If you want enable telemetry, you should
remove the %_sysconfdir/profile.d/%name.sh file or unset the
VCPKG_DISABLE_METRICS environment variable.

vcpkg needs a clone of the https://github.com/microsoft/vcpkg registry
(VCPKG_ROOT, $HOME/.local/share/vcpkg by default). The /usr/bin/vcpkg
wrapper clones it on the first use, see README.ALT.

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
    -DVCPKG_VERSION=%repotag \
    -DVCPKG_BASE_VERSION=%repotag \
    -DVCPKG_DEVELOPMENT_WARNINGS:BOOL=OFF \
    -DVCPKG_WARNINGS_AS_ERRORS:BOOL=OFF \
    -DVCPKG_BUILD_TLS12_DOWNLOADER:BOOL=OFF \
    -DVCPKG_BUILD_FUZZING:BOOL=OFF \
    -DVCPKG_EMBED_GIT_SHA:BOOL=OFF \
    -DVCPKG_BUILD_BENCHMARKING:BOOL=OFF \
    -DVCPKG_ADD_SOURCELINK:BOOL=OFF \
    -DVCPKG_LIBCURL_DLSYM:BOOL=OFF \
    -DVCPKG_DEPENDENCY_CMAKERC:BOOL=ON \
    -DVCPKG_DEPENDENCY_EXTERNAL_FMT:BOOL=ON
%cmake_build

%install
%cmake_install

# The wrapper takes care of VCPKG_ROOT
install -D -m 0755 -p %buildroot%_bindir/%name %buildroot%_libexecdir/%name/%name
install -m 0755 -p "%SOURCE2" %buildroot%_bindir/%name
install -m 0644 -p "%SOURCE3" README.ALT

# Installing environment options override...
install -D -m 0644 -p "%SOURCE1" "%buildroot%_sysconfdir/profile.d/%name.sh"

%files
%doc README.md README.ALT
%doc LICENSE.txt NOTICE.txt
%_bindir/%name
%dir %_libexecdir/%name
%_libexecdir/%name/%name
%config(noreplace) %_sysconfdir/profile.d/%name.sh

%changelog
* Tue Oct 13 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.09.26-alt2
- add vcpkg wrapper: default VCPKG_ROOT, clone the registry on first use (closes: #54865)
- add "vcpkg update-registry" command
- add README.ALT

* Tue Oct 06 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.09.26-alt1
- new version 2026.09.26
- drop fmt 12 workaround (fixed upstream)
- link system libcurl (upstream fetches curl headers at configure time), add libcurl-devel BR

* Wed Mar 11 2026 Vitaly Lipatov <lav@altlinux.ru> 2025.12.16-alt1
- new version 2025.12.16

* Thu Sep 25 2025 Nazarov Denis <nenderus@altlinux.org> 2025.05.19-alt1.1
- fix build with fmt 12

* Tue May 27 2025 Vitaly Lipatov <lav@altlinux.ru> 2025.05.19-alt1
- new version (2025.05.19) with rpmgs script (ALT bug 53482)

* Wed Mar 12 2025 Vitaly Lipatov <lav@altlinux.ru> 2025.02.11-alt1
- new version 2025.02.11 (with rpmrb script)

* Sun Jan 26 2025 Vitaly Lipatov <lav@altlinux.ru> 2025.01.11-alt1
- new version 2025.01.11 (with rpmrb script)

* Sun Oct 20 2024 Nazarov Denis <nenderus@altlinux.org> 2024.10.18-alt1
- new version 2024.10.18 (with rpmrb script)

* Thu Oct 12 2023 Nazarov Denis <nenderus@altlinux.org> 2023.09.15-alt1
- new version 2023.09.15 (with rpmrb script)

* Wed May 10 2023 Vitaly Lipatov <lav@altlinux.ru> 2023.04.07-alt1
- new version 2023.04.07 (with rpmrb script)
- add BR: cmrc

* Thu Oct 27 2022 Vitaly Lipatov <lav@altlinux.ru> 2022.10.17-alt1
- new version 2022.10.17 (with rpmrb script)

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 2022.07.14-alt1
- new version (2022.07.14) with rpmgs script

* Mon Jul 18 2022 Vitaly Lipatov <lav@altlinux.ru> 2022.06.15-alt1
- new version 2022.06.15 (with rpmrb script)

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
