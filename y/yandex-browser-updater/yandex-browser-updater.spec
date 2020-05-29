Name: yandex-browser-updater
Version: 1.6
Release: alt1
Summary: Script for automation installing and updating yandex browser
License: MIT
Group: Other
Url: https://github.com/amakeenk/yandex-browser-updater
Source: %name-%version.tar
Packager: Alexander Makeenkov <amakeenk@altlinux.org>

BuildArch: noarch
Requires: python3-module-BeautifulSoup4
Requires: python3-module-tqdm

%description
%summary.

%prep
%setup

%install
%makeinstall_std

%files
%_sbindir/%name

%changelog
* Fri May 29 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.6-alt1
- Version updated to 1.6

* Sun Mar 08 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.5-alt1
- Version updated to 1.5

* Fri Feb 07 2020 Alexander Makeenkov <amakeenk@altlinux.org> 1.4-alt1
- Version updated to 1.4

* Sun Dec 29 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.3-alt1
- Remove default libffmpeg

* Thu Dec 19 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.2-alt1
- Version updated to 1.2

* Sat Nov 23 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.1-alt1
- Use libffmpeg from qmmp1 for h.264 support

* Wed Nov 20 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.0-alt1
- Initial build for ALT
