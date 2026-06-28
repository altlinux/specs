%define _unpackaged_files_terminate_build 1

Name: fastfetch
Version: 2.65.2
Release: alt1

Summary: Like neofetch, but much faster because written in c
License: MIT
Group: Monitoring

Url: https://github.com/LinusDierheimer/fastfetch
Vcs: https://github.com/LinusDierheimer/fastfetch

Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++ ctest
BuildRequires: libpci-devel
BuildRequires: wayland-devel
BuildRequires: libwayland-client-devel
BuildRequires: libxcb-devel
BuildRequires: libXrandr-devel
BuildRequires: libdconf-devel
BuildRequires: libdbus-devel
BuildRequires: libsqlite3-devel
BuildRequires: ImageMagick-devel
BuildRequires: zlib-devel
BuildRequires: libglvnd-devel
BuildRequires: libGL-devel
BuildRequires: libxfconf-devel
BuildRequires: glib2-devel
BuildRequires: ocl-icd-devel
BuildRequires: rpm-devel
BuildRequires: libvulkan-devel
BuildRequires: libXau-devel
BuildRequires: libpcre2-devel
BuildRequires: libzstd-devel
BuildRequires: libffi-devel
BuildRequires: libdrm-devel
BuildRequires: librpm-devel
BuildRequires: libelf-devel
BuildRequires: chafa-devel

%description
fastfetch is a neofetch-like tool for fetching system information and
displaying them in a pretty way. It is written in c to achieve much better
performance, in return only Linux and Android are supported. It also uses
mechanisms like multithreading and caching to finish as fast as possible.

%package bash-completion
Group: Monitoring
Summary: Bash completion files for %name
Requires: bash-completion
Requires: %name = %version-%release
BuildArch: noarch
%description bash-completion
%summary.

%prep
%setup

%build
%cmake -D \
    BUILD_TESTS=ON \
    ENABLE_WAYLAND=ON \
    ENABLE_DRM=ON \
    ENABLE_DRM_AMDGPU=ON \
    ENABLE_RPM=ON
%cmake_build

%check
%ctest

%install
%cmake_install

%files
%doc LICENSE *.md
%_bindir/*
%_datadir/%name
%_datadir/licenses/%name/LICENSE
%_man1dir/%name.1.*

%files bash-completion
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_fastfetch

%changelog
* Mon Jun 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.65.2-alt1
- 2.65.1 -> 2.65.2

* Wed Jun 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.65.1-alt1
- 2.64.2 -> 2.65.1

* Sat Jun 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.64.2-alt1
- updated from 2.64.1 to 2.64.2

* Fri Jun 05 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.64.1-alt1
- 2.64.0 -> 2.64.1

* Thu Jun 04 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.64.0-alt1
- 2.63.1 -> 2.64.0

* Thu May 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.63.1-alt1
- 2.62.1 -> 2.63.1

* Fri Apr 24 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.62.1-alt1
- 2.62.0 -> 2.62.1

* Thu Apr 23 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.62.0-alt1
- 2.61.0 -> 2.62.0

* Sun Mar 29 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.61.0-alt1
- 2.60.0 -> 2.61.0

* Sat Mar 07 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.60.0-alt1
- 2.59.0 -> 2.60.0

* Sat Feb 14 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.59.0-alt1
- 2.58.0 -> 2.59.0

* Fri Jan 30 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.58.0-alt1
- 2.57.1 -> 2.58.0

* Thu Jan 15 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.57.1-alt1
- 2.57.0 -> 2.57.1

* Tue Jan 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 2.57.0-alt1
- 2.56.1 -> 2.57.0

* Fri Dec 19 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.56.1-alt1
- 2.56.0 -> 2.56.1

* Sat Dec 06 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.56.0-alt1
- 2.55.1 -> 2.56.0

* Sun Nov 16 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.55.1-alt1
- 2.55.0 -> 2.55.1

* Wed Nov 12 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.55.0-alt1
- 2.54.0 -> 2.55.0

* Sat Oct 18 2025 Aleksandr Shamaraev <shad@altlinux.org> 2.54.0-alt1
- NMU: 2.43.0 -> 2.54.0 (ALT #56347)

* Mon Jun 23 2025 Artyom Bystrov <arbars@altlinux.org> 2.43.0-alt1.2
- Fix build

* Fri May 30 2025 Artyom Bystrov <arbars@altlinux.org> 2.43.0-alt1.1
- Fix build

* Fri May 16 2025 Artyom Bystrov <arbars@altlinux.org> 2.43.0-alt1
- Update to new version

* Wed Mar 19 2025 Artyom Bystrov <arbars@altlinux.org> 2.39.0-alt1
- Fix version of package
- Add some modules

* Wed Mar 19 2025 Artyom Bystrov <arbars@altlinux.org> 2.38.0-alt1
- Update to new version

* Mon Jan 13 2025 Artyom Bystrov <arbars@altlinux.org> 2.34.0-alt2
- Fix source updating

* Mon Jan 13 2025 Artyom Bystrov <arbars@altlinux.org> 2.34.0-alt1
- Update to new version

* Mon Aug 26 2024 Artyom Bystrov <arbars@altlinux.org> 2.22.0-alt1
- Update to new version

* Thu Feb 15 2024 Artyom Bystrov <arbars@altlinux.org> 2.8.3-alt1
- Update to new version

* Tue Aug 22 2023 Artyom Bystrov <arbars@altlinux.org> 2.0.2-alt1
- Update to new version

* Thu Mar 30 2023 Artyom Bystrov <arbars@altlinux.org> 1.11.0-alt1
- initial build for ALT Sisyphus

* Sat Mar 25 2023 Jonathan Wright <jonathan@almalinux.org> - 1.11.0-1
- Update to 1.11.0 rhbz#2181737

* Thu Mar 02 2023 Jonathan Wright <jonathan@almalinux.org> - 1.10.3-1
- Update to 1.10.3 rhbz#2173294

* Wed Feb 22 2023 Jonathan Wright <jonathan@almalinux.org> - 1.10.2-1
- Update to 1.10.2 rhbz#2172629

* Wed Jan 25 2023 Jonathan Wright <jonathan@almalinux.org> - 1.9.1-1
- Update to 1.9.1 rhbz#2163335

* Mon Jan 23 2023 Jonathan Wright <jonathan@almalinux.org> - 1.9.0-1
- Update to 1.9.0 rhbz#2163335

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Jonathan Wright <jonathan@almalinux.org> - 1.8.2-1
- Update to 1.8.2 rhbz#2156978

* Tue Oct 11 2022 Jonathan Wright <jonathan@almalinux.org> - 1.7.5-1
- Update to 1.7.5 rhbz#2133467

* Fri Sep 16 2022 Jonathan Wright <jonathan@almalinux.org> - 1.7.2-1
- Update to 1.7.2 rhbz#2127329

* Wed Sep 07 2022 Jonathan Wright <jonathan@almalinux.org> - 1.7.0-1
- Update to 1.7.0
- rhbz#2124866

* Tue Aug 23 2022 Jonathan Wright <jonathan@almalinux.org> - 1.6.5-1
- Update to 1.6.5
- rhbz#2120472
- Fix typo in first changelog citing "khbz" instead of "rhbz"

* Mon Aug 22 2022 Jonathan Wright <jonathan@almalinux.org> - 1.6.4-3
- Compile with rpm support for listing package counts

* Mon Aug 22 2022 Jonathan Wright <jonathan@almalinux.org> - 1.6.4-2
- Fix spec for EPEL8 builds

* Tue Aug 16 2022 Jonathan Wright <jonathan@almalinux.org> - 1.6.4-1
- Initial package build
- rhbz#2118887
