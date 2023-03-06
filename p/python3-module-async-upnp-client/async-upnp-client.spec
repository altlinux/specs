Name: python3-module-async-upnp-client
Version: 0.33.1
Release: alt1

Summary: UPnP Client library for Python/asyncio
License: Apache-2.0
Group: Development/Python
Url: https://pypi.org/project/async-upnp-client/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc LICENSE.* README.*
%_bindir/upnp-client
%python3_sitelibdir/async_upnp_client
%python3_sitelibdir/async_upnp_client-%version.dist-info

%changelog
* Mon Mar 06 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.33.1-alt1
- 0.33.1 released

* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.33.0-alt1
- 0.33.0 released

* Mon Nov  7 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.32.2-alt1
- 0.32.2 released

* Fri Jul 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.31.2-alt1
- 0.31.2 released

* Mon May 23 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.30.1-alt1
- 0.30.1 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.29.0-alt1
- 0.29.0 released

* Tue Mar 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.23.5-alt1
- 0.23.5 released

* Wed Feb 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.23.4-alt1
- 0.23.4 released

* Tue Oct 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.8-alt1
- 0.22.8 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.22.5-alt1
- 0.22.5 released

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.19.1-alt1
- 0.19.1 released

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.18.0-alt1
- 0.18.0 released

* Thu Apr 08 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.16.0-alt1
- 0.16.0 released

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.15-alt1
- 0.14.15 released

* Tue Jan 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.14.12-alt1
- initial
