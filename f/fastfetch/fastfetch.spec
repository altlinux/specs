Name: fastfetch
Version: 1.11.0
Release: alt1
Summary: Like neofetch, but much faster because written in c

License: MIT
Group: Monitoring
Url: https://github.com/LinusDierheimer/fastfetch
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %url/archive/%version/%name-%version.tar.gz

BuildRequires: cmake
BuildRequires: gcc ctest
BuildRequires: libpci-devel
BuildRequires: wayland-devel
BuildRequires: libxcb-devel
BuildRequires: libXrandr-devel
BuildRequires: libdconf-devel
BuildRequires: libdbus-devel
BuildRequires: libsqlite3-devel
BuildRequires: ImageMagick-devel
BuildRequires: zlib-devel
BuildRequires: libglvnd-devel
BuildRequires: libOSMesa-devel
BuildRequires: libxfconf-devel
BuildRequires: glib2-devel
BuildRequires: ocl-icd-devel
BuildRequires: rpm-devel
BuildRequires: libvulkan-devel

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
%summary

%prep
%setup

%build
%cmake -D BUILD_TESTS=ON
%cmake_build

%check
pushd %_cmake__builddir
ctest
popd

%install
%cmake_install

%files
%doc LICENSE
%doc README.md
%config(noreplace) %_sysconfdir/%name/
%_bindir/%name
%_bindir/flashfetch
%_datadir/%name/

%files bash-completion
%_datadir/bash-completion/completions/%name

%changelog
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
