%define realname firefox

Summary: The Mozilla Firefox project is a redesign of Mozilla's browser
Name: %realname-unmet-holder
Version: 100.0
Release: alt1
Group: Networking/WWW
License: GPL-3.0
Provides: %realname = %version-%release
ExclusiveArch: ppc64le

%description
%summary

%package wayland
Summary: Firefox Wayland launcher.
Group: Networking/WWW
Provides: %realname = %version-%release

%description wayland
The firefox-wayland package contains launcher and desktop file
to run Firefox natively on Wayland.

%files

%files wayland

%changelog
* Wed May 04 2022 Alexey Gladkov <legion@altlinux.ru> 100.0-alt1
- New release (100.0).

* Sat Apr 16 2022 Alexey Gladkov <legion@altlinux.ru> 99.0.1-alt1
- New release (99.0.1).

* Thu Apr 07 2022 Alexey Gladkov <legion@altlinux.ru> 99.0-alt2
- Don't provide noarch packages.

* Wed Apr 06 2022 Alexey Gladkov <legion@altlinux.ru> 99.0-alt1
- New release (99.0).

* Tue Sep 08 2020 Alexey Gladkov <legion@altlinux.ru> 80.0.1-alt2
- New release (80.0.1).

* Sat Aug 29 2020 Alexey Gladkov <legion@altlinux.ru> 80.0-alt2
- New release (80.0).

* Mon Aug 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 79.0-alt3
- drop armh from build arches

* Thu Jul 30 2020 Alexey Gladkov <legion@altlinux.ru> 79.0-alt2
- New release (79.0).
