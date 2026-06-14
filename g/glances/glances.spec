%define _unpackaged_files_terminate_build 1
%def_with check
%ifarch %e2k
# uvicorn unavailable on elbrus (due to greenlet)
%def_without webserver
%else
%def_with webserver
%endif

Name: glances
Version: 4.5.5
Release: alt1

Summary: CLI curses based monitoring tool
License: GPLv3
Group: Monitoring
Url: https://github.com/nicolargo/glances
BuildArch: noarch

Source: %name-%version.tar
Source1: .gear/glances-webserver.service
Source2: .gear/glances.env
Patch0: %name-%version-alt.patch

Requires: python3-module-%name = %EVR

#skip findreq for optional dependencies from exports
%add_findreq_skiplist %python3_sitelibdir/%name/exports/*.py

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-dateutil
BuildRequires: python3-module-ujson
BuildRequires: python3-module-psutil
BuildRequires: /proc

%if_with webserver
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-uvicorn
BuildRequires: python3-module-jinja2
%endif

%if_with check
BuildRequires: python3-module-selenium
BuildRequires: python3-module-pytest
%endif

%description
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the PsUtil library to get information from your system.

%package -n python3-module-%name
Summary: CLI curses based monitoring tool
Group: Development/Python3
Requires: python3(defusedxml.xmlrpc)

%description -n python3-module-%name
Glances is a CLI curses based monitoring tool for both GNU/Linux and BSD.

Glances uses the PsUtil library to get information from your system.

%package webserver
Summary: CLI curses based monitoring tool web server
Group: Monitoring
Requires: python3-module-fastapi
Requires: python3-module-uvicorn
Requires: python3-module-jinja2
Requires: %name = %EVR

%description webserver
%summary.

%prep
%setup
%patch0 -p1

%build
%pyproject_build

%install
%pyproject_install
install -D -p -m 644 conf/glances.conf %buildroot%_sysconfdir/%name/glances.conf
%if_with webserver
# Create and install empty password file so glances-webserver.service won't ask
# for CLI input when run with --password flag
touch glances.pwd
install -D -p -m 660 glances.pwd %buildroot%_sharedstatedir/%name/.config/glances/glances.pwd
install -D -p -m 644 %SOURCE1 %buildroot%_unitdir/glances-webserver.service
install -D -p -m 644 %SOURCE2 %buildroot%_sysconfdir/%name/glances.env
%endif

%check
# see .github/workflows/test.yml
%pyproject_run_pytest ./tests/test_core.py

%pre webserver
%_sbindir/groupadd -r -f %name 2>/dev/null ||:
%_sbindir/useradd -r -g %name -d %_sharedstatedir/%name \
  -s /dev/null %name >/dev/null 2>&1 ||:

%post webserver
%post_service glances-webserver

%preun webserver
%preun_service glances-webserver

%files
%doc AUTHORS COPYING README.rst NEWS.rst
%_bindir/glances
%_man1dir/glances.1*
%_docdir/glances/
%dir %_sysconfdir/glances
%config(noreplace) %_sysconfdir/glances/glances.conf

%files -n python3-module-%name
%python3_sitelibdir/glances
%python3_sitelibdir/%{pyproject_distinfo %name}/

%if_with webserver
%files webserver
%_unitdir/glances-webserver.service
%config(noreplace) %_sysconfdir/%name/glances.env
%dir %attr(770,root,%name) %_sharedstatedir/%name
%dir %attr(770,root,%name) %_sharedstatedir/%name/.config
%dir %attr(770,root,%name) %_sharedstatedir/%name/.config/glances
%config(noreplace) %attr(660,root,%name) %_sharedstatedir/%name/.config/glances/glances.pwd
%endif

%changelog
* Sun Jun 14 2026 Egor Ignatov <egori@altlinux.org> 4.5.5-alt1
- New version 4.5.5.

* Tue Apr 21 2026 Egor Ignatov <egori@altlinux.org> 4.5.4-alt1
- New version 4.5.4.

* Tue Mar 31 2026 Egor Ignatov <egori@altlinux.org> 4.5.3-alt1
- New version 4.5.3.
- Fixes:
  + CVE-2026-30928 Unauthenticated Configuration Secrets Exposure via /api/4/config
  + CVE-2026-30930 SQL Injection via Process Names in TimescaleDB Export
  + CVE-2026-32596 REST API Exposed Without Authentication by Default
  + CVE-2026-32608 Command Injection via Process Names in Action Command Templates
  + CVE-2026-32609 Incomplete Secrets Redaction on /api/v4/args Endpoint
  + CVE-2026-32610 Cross-Origin Credential Theft via Default CORS Configuration
  + CVE-2026-32611 SQL Injection in DuckDB Export via Unparameterized DDL Statements
  + CVE-2026-32632 DNS Rebinding via Missing Host Validation in REST/WebUI
  + CVE-2026-32633 Browser API Exposes Reusable Downstream Credentials via /api/4/serverslist
  + CVE-2026-32634 Autodiscovery Leaks Reusable Credentials to Zeroconf-Spoofed Servers
  + CVE-2026-33533 Cross-Origin System Information Disclosure via XML-RPC Server CORS Wildcard
  + CVE-2026-33641 Command Injection via Dynamic Configuration Values

* Fri Aug 15 2025 Michael Shigorin <mike@altlinux.org> 4.3.0.8-alt1.2
- NMU: disable webserver on e2k due to uvicorn being missing

* Wed Apr 02 2025 Stanislav Levin <slev@altlinux.org> 4.3.0.8-alt1.1
- NMU: fixed FTBFS (setuptools 75.8.1)

* Tue Jan 21 2025 Alexander Kuznetsov <kuznetsovam@altlinux.org> 4.3.0.8-alt1
- New version 4.3.0.8 (closes: #53271).
- Add subpackage with webserver requirements and systemd unit.
- Add patch to fix default config dir path.

* Tue Oct 08 2024 Stanislav Levin <slev@altlinux.org> 3.4.0.5-alt2
- Migrated from removed setuptools' test command.

* Sun Apr 07 2024 Egor Ignatov <egori@altlinux.org> 3.4.0.5-alt1
- new version 3.4.0.5

* Wed May 24 2023 Egor Ignatov <egori@altlinux.org> 3.4.0.3-alt1
- new version 3.4.0.3

* Fri Mar 03 2023 Egor Ignatov <egori@altlinux.org> 3.3.1.1-alt1
- new version 3.3.1.1

* Sun Nov 06 2022 Egor Ignatov <egori@altlinux.org> 3.3.0.4-alt1
- new version 3.3.0.4

* Sun Oct 30 2022 Egor Ignatov <egori@altlinux.org> 3.3.0.2-alt1
- new version 3.3.0.2

* Tue Oct 18 2022 Egor Ignatov <egori@altlinux.org> 3.3.0.1-alt1
- new version 3.3.0.1

* Fri Jul 29 2022 Egor Ignatov <egori@altlinux.org> 3.2.7-alt1
- new version 3.2.7

* Mon Jun 20 2022 Egor Ignatov <egori@altlinux.org> 3.2.6.4-alt2
- remove 'future' and 'packaging' dependencies (9b9a7862)
  + future is python2 only dependency
  + packaging is optional and used to check for updates

* Tue May 31 2022 Egor Ignatov <egori@altlinux.org> 3.2.6.4-alt1
- new version 3.2.6.4

* Wed May 25 2022 Egor Ignatov <egori@altlinux.org> 3.2.6.1-alt1
- new version 3.2.6.1

* Mon Apr 11 2022 Egor Ignatov <egori@altlinux.org> 3.2.5-alt1
- new version 3.2.5

* Wed Dec 01 2021 Egor Ignatov <egori@altlinux.org> 3.2.4.2-alt1
- new version

* Wed Aug 25 2021 Egor Ignatov <egori@altlinux.org> 3.2.3.1-alt1
- new version

* Tue Aug 17 2021 Egor Ignatov <egori@altlinux.org> 3.2.3-alt1
- new version

* Fri Jul 09 2021 Egor Ignatov <egori@altlinux.org> 3.2.0-alt1
- new version

* Fri May 14 2021 Egor Ignatov <egori@altlinux.org> 3.1.7-alt1
- new version

* Mon Apr 26 2021 Egor Ignatov <egori@altlinux.org> 3.1.6-alt1
- new version

* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.11.1-alt2
- build for python2 disabled

* Wed Oct 11 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 2.11.1-alt1
- Initial build.
