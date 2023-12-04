Name: rpm-macros-branding
Version: 1.0.9
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
alt-spworkstation \
alt-starterkit \
alt-workstation \
alt-tonk \
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
"
sed -e "s/@BRANDING_VARIANTS@/$VARIANTS/" -i branding.rpm.macros

%install
install -d -m 0755 %buildroot%_rpmmacrosdir
install -m 0644 branding.rpm.macros %buildroot%_rpmmacrosdir/branding

%files
%_rpmmacrosdir/*

%changelog
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
