%define _unpackaged_files_terminate_build 1

Name:     vokoscreenNG
Version:  4.10.0
Release:  alt1

Summary:  VokscreenNG is a user friendly Open Source screencaster for Linux and Windows
License:  GPL-2.0
Group:    Other
Url:      https://github.com/vkohaupt/vokoscreenNG

Packager: Andrey Cherepanov <cas@altlinux.org>

Source:   %name-%version.tar
Patch0:   %name-alt-mkv-playback.patch

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
%patch0 -p1

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
* Sat Jun 27 2026 Andrey Cherepanov <cas@altlinux.org> 4.10.0-alt1
- New version.

* Mon Mar 30 2026 Andrey Cherepanov <cas@altlinux.org> 4.9.0-alt1
- New version.

* Fri Jan 09 2026 Andrey Cherepanov <cas@altlinux.org> 4.8.3-alt1
- New version.

* Wed Jan 07 2026 Andrey Cherepanov <cas@altlinux.org> 4.8.1-alt1
- New version.

* Thu Jan 01 2026 Andrey Cherepanov <cas@altlinux.org> 4.8.0-alt1
- New version.

* Mon Dec 08 2025 Andrey Cherepanov <cas@altlinux.org> 4.7.4-alt1
- New version.

* Fri Dec 05 2025 Andrey Cherepanov <cas@altlinux.org> 4.7.3-alt1
- New version.

* Thu Dec 04 2025 Andrey Cherepanov <cas@altlinux.org> 4.7.2-alt1
- New version.

* Wed Oct 29 2025 Andrey Cherepanov <cas@altlinux.org> 4.7.1-alt1
- New version.

* Mon Sep 29 2025 Andrey Cherepanov <cas@altlinux.org> 4.7.0-alt2
- Fixed crash on MKV playback (ALT #55913) (thanks @dan1257).

* Thu Sep 25 2025 Andrey Cherepanov <cas@altlinux.org> 4.7.0-alt1
- New version.

* Sat Sep 06 2025 Andrey Cherepanov <cas@altlinux.org> 4.6.2-alt1
- New version.

* Mon Jul 21 2025 Andrey Cherepanov <cas@altlinux.org> 4.6.1-alt1
- New version.

* Sun Jun 29 2025 Andrey Cherepanov <cas@altlinux.org> 4.6.0-alt1
- New version.

* Thu May 01 2025 Andrey Cherepanov <cas@altlinux.org> 4.5.2-alt1
- New version.

* Mon Apr 28 2025 Andrey Cherepanov <cas@altlinux.org> 4.5.1-alt1
- New version.

* Tue Mar 25 2025 Andrey Cherepanov <cas@altlinux.org> 4.5.0-alt1
- New version.

* Mon Mar 17 2025 Andrey Cherepanov <cas@altlinux.org> 4.4.7-alt1
- New version.

* Sun Mar 09 2025 Andrey Cherepanov <cas@altlinux.org> 4.4.6-alt1
- New version.

* Sun Feb 16 2025 Andrey Cherepanov <cas@altlinux.org> 4.4.5-alt1
- New version.

* Sun Feb 09 2025 Andrey Cherepanov <cas@altlinux.org> 4.4.4-alt1
- New version.

* Fri Feb 07 2025 Andrey Cherepanov <cas@altlinux.org> 4.4.3-alt1
- New version.

* Thu Jan 09 2025 Andrey Cherepanov <cas@altlinux.org> 4.4.2-alt1
- New version.

* Wed Jan 08 2025 Andrey Cherepanov <cas@altlinux.org> 4.4.1-alt1
- New version.

* Thu Jan 02 2025 Andrey Cherepanov <cas@altlinux.org> 4.4.0-alt1
- New version.

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
