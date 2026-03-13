Name: ncdu
Version: 2.9.2
Release: alt1

Summary: Text-based disk usage viewer

Group: File tools
License: MIT
Url: http://dev.yorhel.nl/ncdu/

Source: http://dev.yorhel.nl/download/%name-%version.tar

ExclusiveArch: %zig_arches

BuildRequires(pre): rpm-macros-zig
BuildRequires: zig libncursesw-devel libzstd-devel

# No build.zig.zon, disable system integration
%define _zig_system_integration %nil

%description
ncdu (NCurses Disk Usage) is a curses-based version of the well-known 'du',
and provides a fast way to see what directories are using your disk space.

%prep
%setup

%build
%zig_build

%install
%zig_install
install -Dpm644 ncdu.1 %buildroot%_man1dir/ncdu.1

%files
%doc LICENSES/MIT.txt ChangeLog
%_bindir/ncdu
%_man1dir/ncdu.1.*

%changelog
* Thu Mar 12 2026 Vitaly Lipatov <lav@altlinux.ru> 2.9.2-alt1
- new version 2.9.2
- switch to Zig build system (ncdu 2.x)

* Thu Jun 19 2025 Vitaly Lipatov <lav@altlinux.ru> 1.22-alt1
- new version 1.22 (with rpmrb script)

* Tue Dec 03 2024 Vitaly Lipatov <lav@altlinux.ru> 1.21-alt1
- new version 1.21 (with rpmrb script)

* Sun Oct 01 2023 Vitaly Lipatov <lav@altlinux.ru> 1.19-alt1
- new version 1.19 (with rpmrb script)

* Thu Apr 20 2023 Vitaly Lipatov <lav@altlinux.ru> 1.18.1-alt1
- new version 1.18.1 (with rpmrb script)

* Fri Dec 30 2022 Vitaly Lipatov <lav@altlinux.ru> 1.18-alt1
- new version 1.18 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 1.17-alt1
- new version 1.17 (with rpmrb script)

* Tue Jul 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.16-alt1
- new version 1.16 (with rpmrb script)

* Wed Jun 24 2020 Vitaly Lipatov <lav@altlinux.ru> 1.15.1-alt1
- new version 1.15.1 (with rpmrb script)

* Wed Jun 03 2020 Vitaly Lipatov <lav@altlinux.ru> 1.15-alt1
- new version 1.15 (with rpmrb script)

* Wed Feb 19 2020 Vitaly Lipatov <lav@altlinux.ru> 1.14.2-alt1
- new version 1.14.2 (with rpmrb script)

* Fri Aug 16 2019 Vitaly Lipatov <lav@altlinux.ru> 1.14.1-alt1
- new version 1.14.1 (with rpmrb script)

* Sat Feb 23 2019 Vitaly Lipatov <lav@altlinux.ru> 1.14-alt1
- new version 1.14 (with rpmrb script)

* Wed Jun 13 2018 Vitaly Lipatov <lav@altlinux.ru> 1.13-alt1
- new version 1.13 (with rpmrb script)

* Thu Jan 05 2017 Vitaly Lipatov <lav@altlinux.ru> 1.12-alt1
- new version 1.12 (with rpmrb script)

* Thu Jan 05 2017 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- new version 1.11 (with rpmrb script)

* Mon Feb 08 2016 Lenar Shakirov <snejok@altlinux.ru> 1.7-alt2
- man packaging fixed

* Mon Aug 01 2011 Mykola Grechukh <gns@altlinux.ru> 1.7-alt1
- update to new upstream version 1.7

* Fri Jun 11 2010 Mykola Grechukh <gns@altlinux.ru> 1.6-alt1
- first build for ALT Linux

* Sat Nov 28 2009 Richard Fearn <richardfearn@gmail.com> - 1.6-1
- update to new upstream version 1.6

* Sun Jul 26 2009 Richard Fearn <richardfearn@gmail.com> - 1.5-1
- update to new upstream version 1.5

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Oct 25 2008 Richard Fearn <richardfearn@gmail.com> - 1.4-1
- new upstream version

* Fri Apr 25 2008 Richard Fearn <richardfearn@gmail.com> - 1.3-2
- remove unnecessary Requires:
- use %%configure macro instead of ./configure
- don't need to mark man page as %%doc
- make package summary more descriptive

* Sat Mar  1 2008 Richard Fearn <richardfearn@gmail.com> - 1.3-1
- initial package for Fedora
