Name: python3-module-telegram-bot
Version: 22.5
Release: alt2

Summary: Python interface for the Telegram Bot API
License: LGPLv3
Group: Development/Python
URL: https://pypi.org/project/python-telegram-bot/
VCS: https://github.com/python-telegram-bot/python-telegram-bot

Source0: %name-%version.tar
Source1: pyproject_deps.json

Autoreq: yes, nopython3
%pyproject_runtimedeps_metadata

BuildArch: noarch
BuildRequires(pre): rpm-build-pyproject
%pyproject_builddeps_build
%pyproject_builddeps_metadata
%pyproject_builddeps_check

%description
%summary

%prep
%setup
%pyproject_deps_resync_build
%pyproject_deps_resync_metadata
%pyproject_deps_resync_check_depgroup tests

%build
%pyproject_build

%install
%pyproject_install

%check
# some tests are online and/or depend on optional packages
%pyproject_run_pytest -n auto --dist=loadgroup -m no_req ||:

%files
%python3_sitelibdir/telegram
%python3_sitelibdir/python_telegram_bot-%version.dist-info

%changelog
* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 22.5-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 22.5-alt1.1
- Demodernized packaging.

* Mon Oct 13 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 22.5-alt1
- 22.5 released

* Fri Jul 12 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 21.3-alt1
- 21.3 released

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
