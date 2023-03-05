%define realname firefox

Summary: Empty firefox dependency holder on platforms that don't have one
Name: %realname-unmet-holder
Version: 110.0.1
Release: alt1
Group: Networking/WWW
License: GPL-3.0
Provides: %realname = %version-%release
ExclusiveArch: ppc64le

%description
Empty firefox dependency holder on platforms that don't have one. Most likely,
firefox addons have noarch architecture. To avoid unmets on architectures where
firefox does not exist, something must provide such a dependency.

%files

%changelog
* Fri Mar 03 2023 Alexey Gladkov <legion@altlinux.ru> 110.0.1-alt1
- New release (110.0.1).

* Tue Feb 07 2023 Alexey Gladkov <legion@altlinux.ru> 109.0.1-alt1
- New release (109.0.1).

* Wed Jan 18 2023 Alexey Gladkov <legion@altlinux.ru> 109.0-alt1
- New release (109.0).

* Mon Dec 19 2022 Alexey Gladkov <legion@altlinux.ru> 108.0.1-alt1
- New release (108.0.1).

* Wed Dec 14 2022 Alexey Gladkov <legion@altlinux.ru> 108.0-alt1
- New release (108.0).

* Sat Dec 10 2022 Alexey Gladkov <legion@altlinux.ru> 107.0.1-alt2
- New build.

* Fri Dec 02 2022 Alexey Gladkov <legion@altlinux.ru> 107.0.1-alt1
- New release (107.0.1).

* Wed Nov 16 2022 Alexey Gladkov <legion@altlinux.ru> 107.0-alt1
- New release (107.0).

* Sat Nov 05 2022 Alexey Gladkov <legion@altlinux.ru> 106.0.5-alt1
- New release (106.0.5).

* Fri Oct 28 2022 Alexey Gladkov <legion@altlinux.ru> 106.0.2-alt1
- New release (106.0.2).

* Fri Oct 21 2022 Alexey Gladkov <legion@altlinux.ru> 106.0.1-alt1
- New release (106.0.1).

* Tue Oct 18 2022 Alexey Gladkov <legion@altlinux.ru> 106.0-alt1
- New release (106.0).

* Sat Oct 08 2022 Alexey Gladkov <legion@altlinux.ru> 105.0.3-alt1
- New release (105.0.3).

* Thu Oct 06 2022 Alexey Gladkov <legion@altlinux.ru> 105.0.2-alt1
- New release (105.0.2).

* Fri Sep 23 2022 Alexey Gladkov <legion@altlinux.ru> 105.0.1-alt1
- New release (105.0.1).

* Wed Sep 21 2022 Alexey Gladkov <legion@altlinux.ru> 105.0-alt1
- New release (105.0).

* Thu Sep 08 2022 Alexey Gladkov <legion@altlinux.ru> 104.0.2-alt2
- New build.

* Wed Sep 07 2022 Alexey Gladkov <legion@altlinux.ru> 104.0.2-alt1
- New release (104.0.2).

* Wed Aug 31 2022 Alexey Gladkov <legion@altlinux.ru> 104.0.1-alt1
- New release (104.0.1).

* Wed Aug 17 2022 Alexey Gladkov <legion@altlinux.ru> 104.0-alt1
- New release (104.0).

* Tue Aug 02 2022 Alexey Gladkov <legion@altlinux.ru> 103.0.1-alt1
- New release (103.0.1).

* Wed Jul 27 2022 Alexey Gladkov <legion@altlinux.ru> 103.0-alt1
- New release (103.0).

* Wed Jun 29 2022 Alexey Gladkov <legion@altlinux.ru> 102.0-alt1
- New release (102.0).

* Fri Jun 10 2022 Alexey Gladkov <legion@altlinux.ru> 101.0.1-alt1
- New release (101.0.1).

* Thu Jun 02 2022 Alexey Gladkov <legion@altlinux.ru> 101.0-alt2
- New release.

* Thu Jun 02 2022 Alexey Gladkov <legion@altlinux.ru> 101.0-alt1
- New release (101.0).

* Sat May 21 2022 Alexey Gladkov <legion@altlinux.ru> 100.0.2-alt1
- New release (100.0.2).

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
