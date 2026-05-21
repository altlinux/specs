Name: rpm-macros-branding
Version: 1.0.28
Release: alt1
Summary: RPM helper macros to build branding packages
License: %gpl2plus
Group: Development/Other
Source0: branding.rpm.macros
BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

%description
%summary.

%build
cp %SOURCE0 branding.rpm.macros

VARIANTS="\
Platform6-server-light \
alt-desktop \
alt-education \
alt-platform-builder \
alt-server \
alt-server-v \
alt-sisyphus \
alt-spserver \
alt-spserver-se \
alt-spworkstation \
alt-spworkstation-se \
alt-spcontainer \
alt-starterkit \
alt-virtualization-pve \
alt-virtualization-one \
alt-workstation \
alt-tonk \
alt-mobile \
alt-mobile-sisyphus \
altlinux-backup-server \
altlinux-centaurus \
altlinux-desktop \
altlinux-gnome-desktop \
altlinux-kdesktop \
altlinux-lite \
altlinux-lxdesktop \
altlinux-office-desktop \
altlinux-office-server \
altlinux-p7 \
altlinux-school-server \
altlinux-sisyphus \
altlinux-spt \
altlinux-starterkit \
altlinux-tablet \
altlinux-workbench \
basealt-server \
basealt-starterkit \
basealt-workstation \
informika-schoolmaster \
ivk-chainmail \
lxde-desktop \
lxde-school-lite \
myoffice-plus \
school-junior \
school-lite \
school-master \
school-server \
school-teacher \
school-terminal \
simply-linux \
sisyphus-server-light \
xalt-kworkstation \
etersoft-ximper \
uzguard-server \
uzguard-workstation \
alt-container \
asman \
asman-server \
qazos \
altemu \
zephyrus \
alt-atomic-onyx \
alt-atomic-core \
alt-orchestra \
iamos \
alt-atomic-kyanite \
maplekavach \
maplekavach-server \
rudraverse \
"
sed -e "s/@BRANDING_VARIANTS@/$VARIANTS/" -i branding.rpm.macros

%install
install -d -m 0755 %buildroot%_rpmmacrosdir
install -m 0644 branding.rpm.macros %buildroot%_rpmmacrosdir/branding

%files
%_rpmmacrosdir/*

%changelog
* Tue May 19 2026 Anton Midyukov <antohami@altlinux.org> 1.0.28-alt1
- Added alt-spserver-se, alt-spworkstation-se.

* Thu Apr 16 2026 Andrey Cherepanov <cas@altlinux.org> 1.0.27-alt1
- Added rudraverse.

* Mon Mar 02 2026 Andrey Cherepanov <cas@altlinux.org> 1.0.26-alt1
- Added maplekavach and maplekavach-server.

* Fri Jan 23 2026 Vladimir Romanov <rirusha@altlinux.org> 1.0.25-alt1
- Added alt-atomic-kyanite.

* Fri Dec 12 2025 Andrey Cherepanov <cas@altlinux.org> 1.0.24-alt1
- Added iamos

* Mon Oct 27 2025 Nadezhda Fedorova <fedor@altlinux.org> 1.0.23-alt1
- Added alt-orchestra

* Thu Sep 25 2025 Vladimir Vaskov <rirusha@altlinux.org> 1.0.22-alt1
- Added alt-atomic-core

* Tue Aug 19 2025 Vladimir Vaskov <rirusha@altlinux.org> 1.0.21-alt1
- Added alt-atomic-onyx

* Thu May 22 2025 Andrey Cherepanov <cas@altlinux.org> 1.0.20-alt1
- Added zephyrus

* Mon May 19 2025 Artyom Bystrov <arbars@altlinux.org> 1.0.19-alt1
- Added altemu

* Tue May 06 2025 Andrey Cherepanov <cas@altlinux.org> 1.0.18-alt1
- Added asman-server

* Wed Apr 09 2025 Andrey Cherepanov <cas@altlinux.org> 1.0.17-alt1
- Added qazos

* Sun Oct 13 2024 Alexey Shabalin <shaba@altlinux.org> 1.0.16-alt1
- Added alt-virtualization-pve and alt-virtualization-one

* Sat Sep 28 2024 Andrey Cherepanov <cas@altlinux.org> 1.0.15-alt1
- Added asman

* Tue Sep 17 2024 Anton Midyukov <antohami@altlinux.org> 1.0.14-alt1
- Added alt-container

* Tue Jun 18 2024 Anton Midyukov <antohami@altlinux.org> 1.0.13-alt1
- Added alt-spcontainer

* Thu Apr 11 2024 Anton Midyukov <antohami@altlinux.org> 1.0.12-alt1
- Added alt-mobile, alt-mobile-sisyphus

* Wed Mar 27 2024 Andrey Cherepanov <cas@altlinux.org> 1.0.11-alt1
- Added uzguard-server

* Sun Dec 24 2023 Andrey Cherepanov <cas@altlinux.org> 1.0.10-alt1
- Added uzguard-workstation

* Thu Nov 23 2023 Anton Midyukov <antohami@altlinux.org> 1.0.9-alt1
- Added alt-platform-builder

* Fri Jun 09 2023 Roman Alifanov <ximper@altlinux.org> 1.0.8-alt1
- NMU: Added etersoft-ximper (ALT bug 47384)

* Fri Jul 29 2022 Andrey Cherepanov <cas@altlinux.org> 1.0.7-alt1
- Added myoffice-plus.

* Wed Mar 10 2021 Anton Midyukov <antohami@altlinux.org> 1.0.6-alt1
- Added alt-sisyphus.

* Wed May 13 2020 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.0.5-alt1
- Added alt-spserver and alt-spworkstation

* Mon Dec 02 2019 Alexey Shabalin <shaba@altlinux.org> 1.0.4-alt1
- Added server-v.

* Tue Feb 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.3-alt1
- Add alt-tonk

* Wed Aug 31 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.2-alt1
- Added 10 more brandings.

* Tue Aug 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.1-alt1
- Added xalt-kworkstation.

* Tue Aug 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt1
- Initial build.
