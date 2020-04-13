Name: gtk-theme-qogir
Version: 20200226
Release: alt2
Summary: Qogir GTK theme

Group: Graphical desktop/GNOME
License: GPL-3.0-only
Url: https://github.com/vinceliuice/Qogir-theme

Source: %name-%version.tar.gz

Patch: gtk-theme-qogir-20200226-alt-fix_build_with_new_sassc.patch

BuildArch: noarch
Packager: Leontiy Volodin <lvol@altlinux.org>
BuildRequires: libgtk+3-devel libgtk+2-devel sassc
#Requires: libgtk-engine-murrine

%description
A flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell.
Based on Arc gtk theme

%prep
%setup
%patch -p2

%build

%install
mkdir -p %buildroot%_datadir/themes/Qogir
./install.sh -d %buildroot%_datadir/themes

%files
%doc AUTHORS COPYING HACKING README.md
%dir %_datadir/themes
%_datadir/themes/Qogir*

%changelog
* Mon Apr 13 2020 Leontiy Volodin <lvol@altlinux.org> 20200226-alt2
- Fixed build with new sassc.
- Disabled background image for nautilus.

* Thu Mar 12 2020 Leontiy Volodin <lvol@altlinux.org> 20200226-alt1
- New version.

* Tue Nov 05 2019 Leontiy Volodin <lvol@altlinux.org> 20191025-alt1
- New version.

* Tue Sep 03 2019 Leontiy Volodin <lvol@altlinux.org> 20190831-alt1
- New version.
- Added sassc in BR for generate css styles.

* Mon May 06 2019 Leontiy Volodin <lvol@altlinux.org> 20190503-alt1
- New version

* Thu Apr 11 2019 Leontiy Volodin <lvol@altlinux.org> 20190407-alt1
- Initial build for ALT Sysiphus

