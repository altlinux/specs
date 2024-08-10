# Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

Name: gns3-gui
Version: 2.2.49
Release: alt1

Summary: GNS3 Graphical User Interface
License: GPL-3.0-or-later
Group: Emulators
Url: https://github.com/GNS3/gns3-gui

Buildarch: noarch

Source: %name-%version.tar
Source1: gns3-16x16.png
Source2: gns3-32x32.png
Source3: gns3-48x48.png
#Source4: gns3.xml
Source5: gns3.desktop

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3 rpm-build-gir
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

Requires: telnet
Requires: socat

%description
GNS3 is a excellent complementary tool to real labs for administrators
of Cisco networks or people wanting to pass their CCNA, CCNP, CCIP or CCIE
certifications.

It can also be used to experiment features of Cisco IOS or to check
configurations that need to be deployed later on real routers.

Important notice: users must provide their own Cisco IOS to use GNS3.

%package -n gns3
Summary: GNS3 virtual package
Group: Games/Strategy
BuildArch: noarch
Requires: gns3-server = %version
Requires: gns3-net-converter >= 1.3.0
Requires: gns3-gui = %EVR

%description -n gns3
Full installation gns3-server, gns3-gui and optional Requires.

%prep
%setup
echo '' > requirements.txt

%build
%pyproject_build

%install
%pyproject_install
install -Dp -m0644 %SOURCE1 %buildroot%_miconsdir/gns3.png
install -Dp -m0644 %SOURCE1 %buildroot%_iconsdir/hicolor/48x48/mimetypes/application-x-gns3.png
install -Dp -m0644 %SOURCE2 %buildroot%_niconsdir/gns3.png
install -Dp -m0644 %SOURCE3 %buildroot%_liconsdir/gns3.png
#install -Dp -m0644 %SOURCE4 %buildroot%_datadir/mime/packages/gns3.xml
install -Dp -m0644 %SOURCE5 %buildroot%_desktopdir/gns3.desktop

	
# Remove shebang
for lib in `find %buildroot/%python3_sitelibdir/ -name '*.py'`; do
 echo $lib
 sed -i '1{\@^#!/usr/bin/env python@d}' $lib
done
 
# Remove empty files
find %buildroot/%python3_sitelibdir/ -name '.keep' -type f -delete
 
# Remove exec perm
find %buildroot/%python3_sitelibdir/ -type f -exec chmod -x {} \;

%files
%doc AUTHORS LICENSE README.md
%_bindir/*
%python3_sitelibdir/gns3
%python3_sitelibdir/gns3_gui-%version.dist-info/
%_desktopdir/gns3*.desktop
%_iconsdir/hicolor/*/apps/gns3.*
%_iconsdir/hicolor/*/mimetypes/application-x-gns3*.*
%_datadir/mime/packages/gns3-gui.xml

%files -n gns3

%changelog
* Sat Aug 10 2024 Anton Midyukov <antohami@altlinux.org> 2.2.49-alt1
- New version 2.2.49.

* Thu Feb 29 2024 Anton Midyukov <antohami@altlinux.org> 2.2.46-alt1
- New version 2.2.46.

* Mon Jan 29 2024 Anton Midyukov <antohami@altlinux.org> 2.2.45-alt1
- New version 2.2.45.

* Sat Nov 18 2023 Anton Midyukov <antohami@altlinux.org> 2.2.44.1-alt1
- New version 2.2.44.1
- fix License
- change Group: Emulators
- migration to PEP517

* Tue Jan 03 2023 Anton Midyukov <antohami@altlinux.org> 2.2.35.1-alt1
- new version 2.2.35.1

* Thu Jun 23 2022 Anton Midyukov <antohami@altlinux.org> 2.2.33.1-alt1
- new version 2.2.33.1
- cleanup spec

* Thu Mar 03 2022 Anton Midyukov <antohami@altlinux.org> 2.2.31-alt1
- new version 2.2.31

* Thu Jan 13 2022 Anton Midyukov <antohami@altlinux.org> 2.2.29-alt1
- new version 2.2.29

* Fri Jan 07 2022 Anton Midyukov <antohami@altlinux.org> 2.2.28-alt1
- new version 2.2.28

* Tue Nov 09 2021 Anton Midyukov <antohami@altlinux.org> 2.2.26-alt1
- new version 2.2.26

* Tue Jul 06 2021 Anton Midyukov <antohami@altlinux.org> 2.2.21-alt1
- new version 2.2.21

* Fri Jul 10 2020 Anton Midyukov <antohami@altlinux.org> 2.2.11-alt1
- new version 2.2.11

* Thu Jun 04 2020 Anton Midyukov <antohami@altlinux.org> 2.2.9-alt1
- new version 2.2.9

* Sun May 10 2020 Anton Midyukov <antohami@altlinux.org> 2.2.8-alt1
- new version 2.2.8

* Sun Apr 12 2020 Anton Midyukov <antohami@altlinux.org> 2.2.7-alt1
- new version 2.2.7

* Tue Jan 14 2020 Anton Midyukov <antohami@altlinux.org> 2.2.5-alt1
- new version 2.2.5

* Fri Nov 08 2019 Anton Midyukov <antohami@altlinux.org> 2.2.2-alt1
- new version 2.2.2

* Thu Oct 03 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt5
- New release 2.2.0

* Tue Sep 03 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt4.rc4
- New release candidate 2.2.0rc4

* Wed Jul 31 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt4.b4
- New beta release 2.2.0b4

* Sun Jun 09 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt3.b2
- New beta release 2.2.0b2

* Sun Apr 21 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt2.a4
- Add requires python3-module-service_identity

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 2.2.0-alt1.a4
- New alpha release 2.2.0a4

* Mon Feb 25 2019 Anton Midyukov <antohami@altlinux.org> 2.1.12-alt1
- new version 2.1.12

* Tue Oct 16 2018 Anton Midyukov <antohami@altlinux.org> 2.1.11-alt1
- new version 2.1.11

* Sun May 13 2018 Anton Midyukov <antohami@altlinux.org> 2.1.5-alt1
- new version 2.1.5

* Mon Mar 26 2018 Anton Midyukov <antohami@altlinux.org> 2.1.4-alt1
- new version 2.1.4

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 24 2018 Anton Midyukov <antohami@altlinux.org> 2.1.3-alt1
- new version 2.1.3

* Sat Nov 18 2017 Anton Midyukov <antohami@altlinux.org> 2.1.0-alt1
- new version 2.1.0

* Tue May 23 2017 Anton Midyukov <antohami@altlinux.org> 2.0.1-alt1
- new version 2.0.1

* Mon May 08 2017 Anton Midyukov <antohami@altlinux.org> 2.0.0-alt1
- New version 2.0.0

* Tue Aug 30 2016 Anton Midyukov <antohami@altlinux.org> 1.5.2-alt1
- New version 1.5.2
- added conflict with gns3

* Thu Aug 04 2016 Anton Midyukov <antohami@altlinux.org> 1.5.1-alt1
- Initial build for ALT Linux Sisyphus.
