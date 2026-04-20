Name: python3-module-async-upnp-client
Version: 0.47.0
Release: alt1

Summary: UPnP Client library for Python/asyncio
License: Apache-2.0
Group: Development/Python
URL: https://pypi.org/project/async-upnp-client
VCS: https://github.com/StevenLooman/async_upnp_client

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
%pyproject_deps_resync_check_tox tox.ini testenv

%build
%pyproject_build

%install
%pyproject_install

%check
# online tests filtered out
%pyproject_run_pytest tests -k 'not _get_local_ip'

%files
%doc LICENSE.* README.*
%_bindir/upnp-client
%python3_sitelibdir/async_upnp_client
%python3_sitelibdir/async_upnp_client-%version.dist-info

%changelog
* Mon Apr 20 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.47.0-alt1
- 0.47.0 released

* Mon Mar 30 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.46.2-alt2
- revert unsolicited packaging changes

* Wed Mar 25 2026 Grigory Ustinov <grenka@altlinux.org> 0.46.2-alt1.1
- Demodernized packaging.

* Tue Feb 03 2026 Sergey Bolshakov <sbolshakov@altlinux.org> 0.46.2-alt1
- 0.46.2 released

* Mon Dec 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.46.1-alt1
- 0.46.1 released

* Mon Nov 17 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.46.0-alt1
- 0.46.0 released

* Wed Oct 15 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.45.0-alt1
- 0.45.0 released

* Wed Jul 16 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.44.0-alt2
- fixed tests for aiohttp>=3.12.14

* Wed Jul 02 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.44.0-alt1
- 0.44.0 released

* Tue Jan 14 2025 Sergey Bolshakov <sbolshakov@altlinux.org> 0.42.0-alt1
- 0.42.0 released

* Fri Nov 08 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.41.0-alt1
- 0.41.0 released

* Thu Sep 05 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.40.0-alt1
- 0.40.0 released

* Thu Jul 04 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.39.0-alt1
- 0.39.0 released

* Thu May 02 2024 Sergey Bolshakov <sbolshakov@altlinux.org> 0.38.3-alt1
- 0.38.3 released

* Wed Mar 13 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.38.2-alt1
- 0.38.2 released

* Fri Jan 19 2024 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.38.0-alt1
- 0.38.0 released

* Fri Nov 03 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.36.2-alt1
- 0.36.2 released

* Wed Sep 13 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.35.1-alt1
- 0.35.1 released

* Fri Jul 07 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.33.2-alt1
- 0.33.2 released

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
