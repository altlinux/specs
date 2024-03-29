Name: btop
Version: 1.2.13
Release: alt3

Summary: Resource monitor that shows usage and stats for processor, memory, disks, network and processes.
License: Apache-2.0
Group: Monitoring

Url: https://github.com/aristocratos/btop
Source: %name-%version.tar.gz
Packager: Alexei Mezin <alexvm@altlinux.org>

Summary(ru_RU.UTF8): Монитор ресурсов, показывающий загрузку процессора, памяти, дисков, сети и список процессов.

BuildRequires(pre): gcc-c++


%description
Colorful resource monitor that shows usage and stats for processor, memory, disks, network and processes. It supports visual themes.

%description -l ru_RU.UTF8
Красочный монитор ресурсов, показывающий загрузку процессора, памяти, дисков, сети и список процессов. Поддерживает визуальные темы оформления.

%prep
%setup

%build
%make_build

%install
PREFIX=%buildroot/%_prefix make install

%files
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%_bindir/*
%_datadir/%name/themes/*
%_desktopdir/%name.desktop
%_iconsdir/hicolor/scalable/apps/%name.*
%_iconsdir/hicolor/48x48/apps/%name.*


%changelog
* Sun Oct 22 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.2.13-alt3
- NMU: build with default GCC. Fixes FTBFS on LoongArch.

* Sat Oct 21 2023 Alexei Mezin <alexvm@altlinux.org> 1.2.13-alt2
- Fix typo in package description.

* Sat Jan 14 2023 Alexei Mezin <alexvm@altlinux.org> 1.2.13-alt1
- New version

* Sun Oct 23 2022 Alexei Mezin <alexvm@altlinux.org> 1.2.12-alt1
- New version

* Sat Sep 24 2022 Alexei Mezin <alexvm@altlinux.org> 1.2.9-alt1
- New version

* Wed Jul 27 2022 Alexei Mezin <alexvm@altlinux.org> 1.2.8-alt1
- New version

* Sat Feb 26 2022 Alexei Mezin <alexvm@altlinux.org> 1.2.3-alt1
- New version

* Sat Jan 15 2022 Alexei Mezin <alexvm@altlinux.org> 1.1.4-alt1
- New version

* Wed Dec 15 2021 Alexei Mezin <alexvm@altlinux.org> 1.1.3-alt1
- New version

* Sat Dec 11 2021 Alexei Mezin <alexvm@altlinux.org> 1.1.2-alt1
- New version

* Fri Nov 19 2021 Alexei Mezin <alexvm@altlinux.org> 1.1.1-alt1
- Initial build


