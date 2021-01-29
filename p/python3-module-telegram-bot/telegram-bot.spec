Name: python3-module-telegram-bot
Version: 13.1
Release: alt1

Summary: Python interface for the Telegram Bot API
License: LGPLv3
Group: Development/Python
Url: https://pypi.org/project/python-telegram-bot/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
%summary

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/telegram
%python3_sitelibdir/python_telegram_bot-%version-*-info

%changelog
* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 13.1-alt1
- 13.1 released

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 11.1.0-alt1
- initial
