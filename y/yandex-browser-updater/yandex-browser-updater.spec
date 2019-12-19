Name: yandex-browser-updater
Version: 1.2
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
Requires: qmmp1

%description
%summary.

%prep
%setup

%install
%makeinstall_std

%files
%_sbindir/%name

%changelog
* Thu Dec 19 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.2-alt1
- Version updated to 1.2

* Sat Nov 23 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.1-alt1
- Use libffmpeg from qmmp1 for h.264 support

* Wed Nov 20 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.0-alt1
- Initial build for ALT
