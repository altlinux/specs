Name: woof
Version: 10.4.0
Release: alt1
Summary: continuation of Lee Killough's Doom source port MBF targeted at modern systems
Group: Games/Arcade
License: GPLv2
Url: https://github.com/fabiangreffrath/woof

Source: %name-%version.tar

BuildRequires: gcc-c++ cmake rpm-macros-cmake
BuildRequires: libSDL2-devel libSDL2_mixer-devel libSDL2_net-devel
BuildRequires: make
BuildRequires: python3-module-cmake_build_extension

ExcludeArch: armh

%description
Woof! is a continuation of Lee Killough's Doom source port MBF targeted at modern systems.

%prep
%setup -n %name-%version

%build
%cmake
%cmake_build \


%install
mkdir -p %buildroot%_bindir/
mkdir -p %buildroot%_datadir/%name
install -m 0755 ./%_arch-alt-linux/src/woof %buildroot%_bindir/%name
install -m 0755 ./%_arch-alt-linux/src/woof-setup %buildroot%_bindir/%name
cp -r ./%_arch-alt-linux/src/autoload %buildroot%_datadir/%name

%find_lang %name

%files -f %name.lang
%doc CHANGELOG.md README.md COPYING docs/*
%_bindir/%name
%_datadir/%name/

%changelog

* Sun Nov 13 2022 Artyom Bystrov <arbars@altlinux.org> 10.4.0-alt1
- Update to new version

* Thu Sep 22 2022 Artyom Bystrov <arbars@altlinux.org> 10.2.0-alt2
- Fix URL of project

* Sun Sep 18 2022 Artyom Bystrov <arbars@altlinux.org> 10.2.0-alt1
- initial build for ALT Sisyphus
