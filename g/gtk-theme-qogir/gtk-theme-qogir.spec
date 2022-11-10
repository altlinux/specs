Name: gtk-theme-qogir
Version: 2022.11.09
Release: alt1
Epoch: 1
Summary: Qogir GTK theme

Group: Graphical desktop/GNOME
License: GPL-3.0-only
Url: https://github.com/vinceliuice/Qogir-theme

Source: %name-%version.tar.gz

BuildArch: noarch
Packager: Leontiy Volodin <lvol@altlinux.org>
BuildRequires: sassc
#BuildRequires: libgtk+3-devel libgtk+2-devel
#Requires: libgtk-engine-murrine

%description
A flat theme with transparent elements for GTK 3, GTK 2 and Gnome-Shell.
Based on Arc gtk theme

%prep
%setup

%build

%install
mkdir -p %buildroot%_datadir/themes/Qogir
./install.sh -d %buildroot%_datadir/themes

%files
%doc AUTHORS COPYING HACKING README.md
%dir %_datadir/themes
%_datadir/themes/Qogir*

%changelog
* Thu Nov 10 2022 Leontiy Volodin <lvol@altlinux.org> 1:2022.11.09-alt1
- New version.
- Upstream:
  + Update login screen.
  + Add gnome screenshot ui support.
  + Use red color for close buttons.
  + Fix title in gnome software.
  + Fix popup menu selected colors.
  + Add rtl support for nautilus.

* Tue Oct 18 2022 Leontiy Volodin <lvol@altlinux.org> 1:2022.10.16-alt1
- New version.
- Upstream:
  + Fixed Gnome 40 and 42 issues.

* Mon Jul 18 2022 Leontiy Volodin <lvol@altlinux.org> 1:2022.07.17-alt1
- New version.
- Upstream:
  + Fixed Gnome 42 issues.

* Mon Jun 06 2022 Leontiy Volodin <lvol@altlinux.org> 1:2022.05.29-alt1
- New version.

* Fri May 13 2022 Leontiy Volodin <lvol@altlinux.org> 1:2022.04.29-alt1
- New version.
- Upstream:
  + Added HiDPI support for xfwm4 version.
  + Fixed Gnome 42 issues.

* Thu Mar 17 2022 Leontiy Volodin <lvol@altlinux.org> 1:2021.12.25-alt1
- New version.
- Upstream:
  + Fixed firefox, GDM, cinnamon, gnome-shell issues.
  + Add rounded window version.

* Fri Aug 20 2021 Leontiy Volodin <lvol@altlinux.org> 1:2021.08.02-alt1
- New version.
- Upstream:
  + Fixed gtk themes and gnome-shell issues.

* Fri Jul 02 2021 Leontiy Volodin <lvol@altlinux.org> 1:2021.06.25-alt1
- New version.
- Upstream:
  + Fixed firefox theme, nemo, gnome-shell, xfce and budgie issues.

* Wed Apr 21 2021 Leontiy Volodin <lvol@altlinux.org> 1:2021.04.20-alt1
- New version.
- Upstream:
  + Add gnome-shell 40.0 supported.
  + Add Gtk+ 4.0 supported.

* Wed Feb 10 2021 Leontiy Volodin <lvol@altlinux.org> 1:2021.02.09-alt1
- New version.
- Upstream:
  + Fixed gnome 3.38 issues.

* Tue Nov 17 2020 Leontiy Volodin <lvol@altlinux.org> 1:2020.11.16-alt1
- New version.
- Upstream:
  + Fixed gnome 3.38 issues.

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

