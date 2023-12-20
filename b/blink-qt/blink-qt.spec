Name:    blink-qt
Version: 5.6.0
Release: alt4

Summary: Blink SIP Client
License: GPL-3.0+
Group:   Other
URL:     http://icanblink.com/

Packager: Andrey Cherepanov <cas@altlinux.org>

# python3-module-sipsimple adapted only for these architectures
ExclusiveArch: x86_64 aarch64 loongarch64 %e2k

BuildRequires(pre): rpm-build-python3
BuildRequires: libvncserver-devel
BuildRequires: python3-dev
BuildRequires: python3-module-distribute
BuildRequires: python3-module-Cython
BuildRequires: python3-module-PyQt5 >= 5.0

%py3_requires service_identity twisted.names
%filter_from_provides /^python3(blink.*/d
%filter_from_requires /^python3(blink.*/d

Conflicts: python3-module-blink

Source: %name-%version.tar
Patch1: alt-desktop-l10n.patch
Patch2: blink-qt-disable-__main__-import.patch
Patch3: blink-qt-fix-build-with-cython3.patch

%description
Fully featured, easy to use SIP client with a Qt based UI Blink is a
fully featured SIP client written in Python and built on top of SIP
SIMPLE client SDK with a Qt based user interface. Blink provides real
time applications based on SIP and related protocols for Audio, Video,
Instant Messaging, File Transfers, Desktop Sharing and Presence.

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
%patch3 -p1
# Set correct python3 executable in shebang
grep -Rl '#!.*python2$' * | xargs -n1 -i{} subst 's|#!.*python2$|#!%__python3|' "{}"

%build
%python3_build

%install
%python3_install
install -Dm 0644 debian/blink.desktop %buildroot%_desktopdir/blink.desktop
install -Dm 0644 debian/blink.xpm %buildroot%_pixmapsdir/blink.xpm
install -Dm 0644 debian/blink.1 %buildroot%_man1dir/blink.1

%files
%doc README LICENSE TODO
%_bindir/blink
%_datadir/blink
%_desktopdir/blink.desktop
%_pixmapsdir/blink.xpm
%python3_sitelibdir/blink/
%python3_sitelibdir/*.egg-info
%_man1dir/blink.1*

%changelog
* Wed Dec 20 2023 Grigory Ustinov <grenka@altlinux.org> 5.6.0-alt4
- NMU: fix building with Cython>3.

* Sat Nov 04 2023 Michael Shigorin <mike@altlinux.org> 5.6.0-alt3
- NMU: build for %%e2k too

* Thu Nov 02 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 5.6.0-alt2
- NMU: build for more architectures (aarch64, LoongArch).

* Fri Jul 21 2023 Andrey Cherepanov <cas@altlinux.org> 5.6.0-alt1
- New version.

* Tue May 02 2023 Andrey Cherepanov <cas@altlinux.org> 5.5.1-alt1
- New version.

* Sun Dec 11 2022 Andrey Cherepanov <cas@altlinux.org> 5.5.0-alt1
- New version.

* Tue Sep 13 2022 Andrey Cherepanov <cas@altlinux.org> 5.3.0-alt1
- New version.

* Mon Jun 13 2022 Andrey Cherepanov <cas@altlinux.org> 5.2.0-alt1
- New version.

* Mon Jun 28 2021 Andrey Cherepanov <cas@altlinux.org> 5.1.1-alt1
- New version.
- Build only for x86_64.

* Tue Jun 15 2021 Andrey Cherepanov <cas@altlinux.org> 5.0.0-alt1
- New version.

* Fri May 21 2021 Andrey Cherepanov <cas@altlinux.org> 4.1.0-alt1
- New version.

* Fri Mar 12 2021 Andrey Cherepanov <cas@altlinux.org> 4.0.0-alt1
- New version.
- Build with Python3.

* Thu Mar 05 2020 Andrey Cherepanov <cas@altlinux.org> 3.2.1-alt1
- New version.
- Fix license tag according to SPDX.

* Wed Feb 27 2019 Andrey Cherepanov <cas@altlinux.org> 3.2.0-alt1
- New version.

* Mon Oct 08 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.0-alt1
- New version.

* Wed Mar 07 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt2
- Add desktop file, pixmap and man page

* Thu Mar 01 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.3-alt1
- Initial build in Sisyphus
