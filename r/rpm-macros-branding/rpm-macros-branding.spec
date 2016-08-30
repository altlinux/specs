Name: rpm-macros-branding
Version: 1.0.0
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
altlinux-backup-server \
altlinux-centaurus \
altlinux-desktop \
altlinux-gnome-desktop \
altlinux-kdesktop \
altlinux-lite \
altlinux-lxdesktop \
altlinux-office-desktop \
altlinux-office-server \
altlinux-school-server \
altlinux-sisyphus \
altlinux-spt \
altlinux-tablet \
altlinux-workbench \
informika-schoolmaster \
ivk-chainmail \
lxde-desktop \
lxde-school-lite \
school-junior \
school-lite \
school-master \
school-server \
school-teacher \
school-terminal \
simply-linux \
sisyphus-server-light \
"
sed -e "s/@BRANDING_VARIANTS@/$VARIANTS/" -i branding.rpm.macros

%install
install -d -m 0755 %buildroot%_rpmmacrosdir
install -m 0644 branding.rpm.macros %buildroot%_rpmmacrosdir/branding

%files
%_rpmmacrosdir/*

%changelog
* Tue Aug 30 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.0.0-alt1
- Initial build.
