%define _unpackaged_files_terminate_build 1

Name:     vokoscreenNG
Version:  4.3.0
Release:  alt1

Summary:  VokscreenNG is a user friendly Open Source screencaster for Linux and Windows
License:  GPL-2.0
Group:    Other
Url:      https://github.com/vkohaupt/vokoscreenNG

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: intltool
BuildRequires: qt6-base-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-tools-devel
BuildRequires: libgstreamermm1.0-devel
BuildRequires: libpulseaudio-devel

%description
%summary

%prep
%setup

%build
cd src
%qmake_qt6 CONFIG+=silent
%make_build

%install
%makeinstall_std -C src
install -Dpm0755 src/%name %buildroot%_bindir/%name
install -Dpm0644 src/applications/%name.desktop %buildroot%_desktopdir/%name.desktop
install -Dpm0644 src/applications/%name.png %buildroot%_pixmapsdir/%name.png

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png

%changelog
* Mon Sep 30 2024 Andrey Cherepanov <cas@altlinux.org> 4.3.0-alt1
- New version.

* Mon Jul 01 2024 Andrey Cherepanov <cas@altlinux.org> 4.2.0-alt1
- New version.

* Wed Mar 27 2024 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- New version.

* Wed Jan 03 2024 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version.

* Thu Oct 05 2023 Andrey Cherepanov <cas@altlinux.org> 3.8.0-alt1
- New version.

* Sat Jul 01 2023 Andrey Cherepanov <cas@altlinux.org> 3.7.0-alt1
- New version.

* Sat Apr 01 2023 Andrey Cherepanov <cas@altlinux.org> 3.6.0-alt1
- new version 3.6.0

* Sat Dec 31 2022 Andrey Cherepanov <cas@altlinux.org> 3.5.0-alt1
- New version.

* Mon Sep 26 2022 Andrey Cherepanov <cas@altlinux.org> 3.4.0-alt1
- New version.

* Fri Jun 24 2022 Andrey Cherepanov <cas@altlinux.org> 3.3.0-alt1
- New version.

* Thu Mar 31 2022 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version.

* Sat Jan 01 2022 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Thu May 27 2021 Andrey Cherepanov <cas@altlinux.org> 3.0.9-alt1
- New version.

* Mon Feb 01 2021 Andrey Cherepanov <cas@altlinux.org> 3.0.8-alt1
- New version.

* Thu Oct 01 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.7-alt1
- New version.

* Thu Sep 03 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.6-alt1
- New version.

* Mon Aug 24 2020 Andrey Cherepanov <cas@altlinux.org> 3.0.5-alt1
- Initial build for Sisyphus.
