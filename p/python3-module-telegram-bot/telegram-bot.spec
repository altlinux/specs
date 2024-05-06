Name: python3-module-telegram-bot
Version: 21.0.1
Release: alt1

Summary: Python interface for the Telegram Bot API
License: LGPLv3
Group: Development/Python
Url: https://pypi.org/project/python-telegram-bot/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

BuildRequires: python3(pytest)
BuildRequires: python3(pytest-asyncio)
BuildRequires: python3(xdist)
BuildRequires: python3(flaky)

BuildRequires: python3(anyio)
BuildRequires: python3(cachetools)
BuildRequires: python3(h2)
BuildRequires: python3(httpx)
BuildRequires: python3(pytz)
BuildRequires: python3(socksio)
BuildRequires: python3(tornado)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# some tests are online
%pyproject_run_pytest -n auto --dist=loadgroup -m no_req ||:

%files
%python3_sitelibdir/telegram
%python3_sitelibdir/python_telegram_bot-%version.dist-info

%changelog
* Wed Mar 27 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.0.1-alt1
- 21.0.1 released

* Wed Mar 27 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 13.15-alt2
- keep vendored copy of urllib3 (closes: 49817)

* Wed Nov 08 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.15-alt1
- 13.15 released

* Mon Nov 07 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.14-alt1
- 13.14 released

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.1-alt1
- 13.1 released

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.1.0-alt1
- initial
