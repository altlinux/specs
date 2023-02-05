%define _unpackaged_files_terminate_build 1
%define modulename telebot
%define pypi_name pyTelegramBotAPI

Name: python3-module-%modulename
Version: 4.10.0
Release: alt1

Summary: Python Telegram bot api
License: GPL2
Group: Development/Python3
Url: https://github.com/eternnoir/pyTelegramBotAPI
BuildArch: noarch

# Source-url: https://github.com/eternnoir/pyTelegramBotAPI/archive/%version.tar.gz
Source: %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

Provides: python3-module-pytelegrambotapi = %version-%release
%py3_provides %pypi_name

%description
A simple, but extensible Python implementation for the Telegram Bot API.

%prep
%setup -n %modulename-%version

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%pypi_name-%version.dist-info


%changelog
* Sun Feb 05 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.10.0-alt1
- Updated to version 4.10.0

* Mon Jan 23 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.9.0-alt1
- Updated to version 4.9.0

* Sat Dec 17 2022 Alexander Makeenkov <amakeenk@altlinux.org> 4.8.0-alt1
- Updated to version 4.8.0
- Use pyproject macroses for build
- Added py3_provides

* Fri Aug 05 2022 Alexander Makeenkov <amakeenk@altlinux.org> 4.6.1-alt1
- NMU: updated to version 4.6.1

* Thu Jan 14 2021 Grigory Ustinov <grenka@altlinux.org> 3.7.5-alt1
- Build new version (Closes: #39533).

* Mon Nov 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.6.6-alt2
- python2 disabled

* Sat Apr 27 2019 Vitaly Lipatov <lav@altlinux.ru> 3.6.6-alt1
- NMU: new version 3.6.6 (with rpmrb script)

* Wed Nov 08 2017 Konstantin Artyushkin <akv@altlinux.org> 3.2.0-alt1
- new version

* Thu May 25 2017 Konstantin Artyushkin <akv@altlinux.org> 3.0.0-alt1
- initial build

