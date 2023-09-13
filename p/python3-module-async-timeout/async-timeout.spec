Name: python3-module-async-timeout
Version: 4.0.3
Release: alt1

Summary: Timeout context manager for asyncio programs
License: Apache-2.0
Group: Development/Python3
Url: https://github.com/aio-libs/async_timeout/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
Timeout context manager for asyncio programs.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc *.rst LICENSE
%python3_sitelibdir/*

%changelog
* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.3-alt1
- 4.0.3

* Tue Feb 08 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.2-alt1
- 4.0.2

* Mon Aug 02 2021 Grigory Ustinov <grenka@altlinux.org> 3.0.1-alt2
- Rename package, spec cleanup.

* Sun Apr 07 2019 Anton Midyukov <antohami@altlinux.org> 3.0.1-alt1
- New version 3.0.1
- switch to git
- cleanup spec

* Sun Nov 19 2017 Anton Midyukov <antohami@altlinux.org> 1.4-alt1
- New version 1.4

* Sat Jan 21 2017 Anton Midyukov <antohami@altlinux.org> 1.1-alt1
- Initial build for ALT Linux Sisyphus.
