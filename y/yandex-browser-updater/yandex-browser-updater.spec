Name: yandex-browser-updater
Version: 1.0
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
* Wed Nov 20 2019 Alexander Makeenkov <amakeenk@altlinux.org> 1.0-alt1
- Initial build for ALT
