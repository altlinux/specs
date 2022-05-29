%define modulename vk_api

Name: python3-module-vk_api
Version: 11.9.8
Release: alt1

Summary: Module for writing scripts for vk.com (vkontakte)

License: Apache-2.0
Group: Development/Python3
Url: https://github.com/python273/vk_api

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_requires enum

%description
Module for writing scripts for vk.com (vkontakte).

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%doc README.md examples/
%python3_sitelibdir/*

%changelog
* Sun May 29 2022 Grigory Ustinov <grenka@altlinux.org> 11.9.8-alt1
- Automatically updated to 11.9.8.

* Tue Jul 13 2021 Grigory Ustinov <grenka@altlinux.org> 9.3.1-alt3
- Drop python2 support.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 9.3.1-alt2.qa1
- NMU: applied repocop patch

* Thu May 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 9.3.1-alt2
- Rebuilt to regenerate dependencies.

* Mon Mar 19 2018 Andrey Bychkov <mrdrew@altlinux.ru> 9.3.1-alt1
- Version 9.3.1

* Fri Jun 16 2017 Vitaly Lipatov <lav@altlinux.ru> 8.8-alt1
- initial build for ALT Sisyphus
