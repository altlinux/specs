Name: mate-tweak
Version: 22.10.0
Release: alt2
Epoch:   1

Summary: Mate desktop configuration tool
License: GPL-2.0
Group: Graphical desktop/MATE
URL: https://bitbucket.org/ubuntu-mate/mate-tweak

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildRequires: python3-module-setuptools python3-module-distutils-extra intltool

%filter_from_requires /nvidia-settings/d

%description
Configures some aspects of the MATE desktop not exposed via the
MATE Control Center applets.

Settings that can be handled via MATE Tweak:
 * Show/hide standard desktop icons.
 * Panel fine-tuning (icon visibility, in menus and on buttons,
   icon size, button labelling, contex menus, etc.).
 * Window manager fine-tuning.

%prep
%setup

%build
%python3_build

%install
%python3_install

%find_lang %name

%files -f %name.lang
%doc README.md
%_bindir/*
%_libexecdir/%name
%python3_sitelibdir/*egg-info
%_desktopdir/*
%_man1dir/*.1.*
%_datadir/polkit-1/actions/*

%changelog
* Fri Nov 18 2022 Andrey Cherepanov <cas@altlinux.org> 1:22.10.0-alt2
- Do not require nvidia-settings (ALT #44356).

* Fri Sep 23 2022 Andrey Cherepanov <cas@altlinux.org> 1:22.10.0-alt1
- New version.

* Thu Mar 31 2022 Andrey Cherepanov <cas@altlinux.org> 1:22.04.8-alt1
- New version.

* Fri Mar 25 2022 Andrey Cherepanov <cas@altlinux.org> 1:22.04.7-alt1
- New version.

* Wed Mar 23 2022 Andrey Cherepanov <cas@altlinux.org> 1:22.04.5-alt1
- New version.

* Thu Mar 03 2022 Andrey Cherepanov <cas@altlinux.org> 1:22.04.4-alt1
- New version.

* Fri Feb 25 2022 Andrey Cherepanov <cas@altlinux.org> 1:22.04.2-alt1
- New version.

* Thu Jan 27 2022 Andrey Cherepanov <cas@altlinux.org> 1:22.04.1-alt1
- New version.

* Thu Jan 27 2022 Andrey Cherepanov <cas@altlinux.org> 1:22.04.0-alt1
- New version.

* Wed Sep 01 2021 Andrey Cherepanov <cas@altlinux.org> 1:21.10.0-alt1
- New version.

* Wed Aug 11 2021 Andrey Cherepanov <cas@altlinux.org> 1:21.04.3-alt1
- New version.

* Mon Mar 26 2018 Anton Midyukov <antohami@altlinux.org> 1:18.04.14-alt1
- new version 18.04.14

* Mon Feb 26 2018 Anton Midyukov <antohami@altlinux.org> 1:18.04.10-alt2
- Added missing polkit action

* Sun Feb 25 2018 Anton Midyukov <antohami@altlinux.org> 1:18.04.10-alt1
- new version 18.04.10

* Wed Jun 14 2017 Andrey Cherepanov <cas@altlinux.org> 1:17.10.6-alt1
- New version

* Tue Jun 13 2017 Andrey Cherepanov <cas@altlinux.org> 1:17.10.5-alt1
- New version

* Sun Jun 11 2017 Andrey Cherepanov <cas@altlinux.org> 1:17.10.4-alt1
- New version

* Fri May 19 2017 Andrey Cherepanov <cas@altlinux.org> 1:17.10.2-alt1
- New version
- New Epoch to downgrade version in p8

* Wed Mar 15 2017 Anton Midyukov <antohami@altlinux.org> 16.10.5-alt3
- Added buildrequires rpm-build-gir.

* Sun Mar 12 2017 Anton Midyukov <antohami@altlinux.org> 16.10.5-alt2
- Added missing requires libnotify-gir.

* Sat Oct 15 2016 Anton Midyukov <antohami@altlinux.org> 16.10.5-alt1
- new version 16.10.5

* Sat Jun 04 2016 Anton Midyukov <antohami@altlinux.org> 3.5.10-alt1
- Initial build for ALT Linux Sisyphus.
