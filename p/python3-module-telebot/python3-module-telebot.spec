%define _unpackaged_files_terminate_build 1
%define modulename telebot
%define pypi_name pyTelegramBotAPI
%def_with check

Name: python3-module-%modulename
Version: 4.26.0
Release: alt1

Summary: Python Telegram bot api
License: GPL-2.0
Group: Development/Python3
Url: https://pypi.org/project/pyTelegramBotAPI
VCS: https://github.com/eternnoir/pyTelegramBotAPI
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(hatchling)
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(requests)
BuildRequires: python3(pytest)
%endif

Provides: python3-module-pytelegrambotapi = %version-%release
%py3_provides %pypi_name

%description
A simple, but extensible Python implementation for the Telegram Bot API.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%{pyproject_distinfo pytelegrambotapi}

%changelog
* Thu Jan 09 2025 Alexander Makeenkov <amakeenk@altlinux.org> 4.26.0-alt1
- Updated to version 4.26.0.

* Sun Dec 15 2024 Alexander Makeenkov <amakeenk@altlinux.org> 4.25.0-alt1
- Updated to version 4.25.0.
- Enabled check.

* Wed May 15 2024 Anastasia Osmolovskaya <lola@altlinux.org> 4.18.0-alt1
- Updated to version 4.18.0.

* Fri Apr 19 2024 Alexander Makeenkov <amakeenk@altlinux.org> 4.17.0-alt1
- Updated to version 4.17.0.

* Mon Jan 15 2024 Alexander Makeenkov <amakeenk@altlinux.org> 4.15.2-alt1
- Updated to version 4.15.2.

* Thu Dec 21 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.14.1-alt1
- Updated to version 4.14.1.

* Wed Sep 27 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.14.0-alt1
- Updated to version 4.14.0.
- Changed to build from upstream tag.

* Mon Aug 21 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.13.0-alt1
- Updated to version 4.13.0.

* Tue Jul 11 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.12.0-alt1
- Updated to version 4.12.0.

* Sun Apr 16 2023 Alexander Makeenkov <amakeenk@altlinux.org> 4.11.0-alt1
- Updated to version 4.11.0

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

