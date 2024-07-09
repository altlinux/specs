# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name:     lxqt-admin
Version:  2.0.0
Release:  alt1

Summary:  LXQt system administration tool
License:  LGPL-2.1
Group:    Graphical desktop/Other
Url:      https://github.com/lxqt/lxqt-admin

Source:   %name-%version.tar
Patch:    0001-Add-russian-translation-of-polkit-messages.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: qt6-base-devel
BuildRequires: qt6-tools-devel
BuildRequires: lxqt2-build-tools
BuildRequires: liblxqt-devel
BuildRequires: kf6-kwindowsystem-devel
BuildRequires: libpolkitqt6-qt6-devel

%description
%summary.

%prep
%setup
%autopatch -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%_bindir/*
%_desktopdir/*
%_datadir/lxqt/translations/*
%_datadir/polkit-1/actions/*
%doc AUTHORS CHANGELOG *.md

%changelog
* Thu Jun 13 2024 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- New version 2.0.0.

* Sun Nov 05 2023 Anton Midyukov <antohami@altlinux.org> 1.4.0-alt1
- New version 1.4.0.

* Mon Aug 07 2023 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt3
- do not pack %%_datadir/polkit-1/actions/, pack only its contents

* Fri May 05 2023 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt2
- Add russian translation of polkit messages

* Sat Apr 15 2023 Anton Midyukov <antohami@altlinux.org> 1.3.0-alt1
- New version 1.3.0.

* Sat Nov 05 2022 Anton Midyukov <antohami@altlinux.org> 1.2.0-alt1
- new version 1.2.0

* Sun Apr 17 2022 Anton Midyukov <antohami@altlinux.org> 1.1.0-alt1
- new version 1.1.0

* Fri Nov 05 2021 Anton Midyukov <antohami@altlinux.org> 1.0.0-alt1
- new version 1.0.0

* Fri Apr 16 2021 Anton Midyukov <antohami@altlinux.org> 0.17.0-alt1
- new version 0.17.0

* Thu Nov 05 2020 Anton Midyukov <antohami@altlinux.org> 0.16.0-alt1
- new version 0.16.0

* Sat Apr 25 2020 Anton Midyukov <antohami@altlinux.org> 0.15.0-alt1
- new version 0.15.0

* Fri Mar 08 2019 Anton Midyukov <antohami@altlinux.org> 0.14.1-alt1
- new version 0.14.1

* Mon Jan 28 2019 Anton Midyukov <antohami@altlinux.org> 0.14.0-alt1
- Initial build for Sisyphus
