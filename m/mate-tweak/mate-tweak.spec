Name: mate-tweak
Version: 18.04.10
Release: alt2
Epoch:   1

Summary: Mate desktop configuration tool
License: GPLv2+
Group: Graphical desktop/MATE
Url: https://bitbucket.org/ubuntu-mate/mate-tweak

Packager: Anton Midyukov <antohami@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-build-gir
BuildPreReq: python3-module-setuptools python3-module-distutils-extra intltool

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
