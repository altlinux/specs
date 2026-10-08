%def_with check

%define pypi_name radicale

Name: radicale
Version: 3.8.2
Release: alt1

Summary: CalDAV and CardDAV server

License: GPL-3.0-or-later
Group: Networking/Other
Url: https://radicale.org/

# Source-url: https://github.com/Kozea/Radicale/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name.sysusers.conf

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-waitress
BuildRequires: python3-module-bcrypt
BuildRequires: python3-module-argon2-cffi
BuildRequires: python3-module-PAM
BuildRequires: python3-module-ldap3
BuildRequires: python3-module-defusedxml
BuildRequires: python3-module-passlib
BuildRequires: python3-module-vobject
BuildRequires: python3-module-pika
BuildRequires: python3-module-requests
%endif

Requires: python3-module-%pypi_name = %EVR

%description
Radicale is a small but powerful CalDAV (calendars, to-do lists) and
CardDAV (contacts) server, that:
- shares calendars and contact lists through CalDAV, CardDAV and HTTP;
- supports events, todos, journal entries and business cards;
- works out-of-the-box, no complicated setup or configuration required;
- can limit access by authentication and can be extended with plugins.

This package contains the standalone server with its configuration
and systemd unit.

%package -n python3-module-%pypi_name
Summary: CalDAV and CardDAV server (Python module)
Group: Development/Python3

%description -n python3-module-%pypi_name
Radicale is a small but powerful CalDAV (calendars, to-do lists) and
CardDAV (contacts) server.

This package contains the Python module, which can also be used
as a library by other applications (for example, etesync-dav).

%prep
%setup
# upstream unit expects the binary in /usr/libexec/radicale
subst 's|^ExecStart=.*|ExecStart=%_bindir/radicale|' contrib/systemd/radicale.service

%build
%pyproject_build

%install
%pyproject_install
rm -rv %buildroot%python3_sitelibdir/%pypi_name/tests/
install -Dpm0640 config %buildroot%_sysconfdir/%name/config
install -Dpm0640 rights %buildroot%_sysconfdir/%name/rights
install -Dpm0644 contrib/systemd/radicale.service %buildroot%_unitdir/%name.service
install -Dpm0644 %SOURCE1 %buildroot%_sysusersdir/%name.conf
mkdir -p %buildroot%_localstatedir/%name/collections %buildroot%_cachedir/%name

%check
%pyproject_run_pytest -v radicale/tests

%pre
%sysusers_create_package %name %SOURCE1

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md CHANGELOG.md DOCUMENTATION.md
%_bindir/radicale
%dir %attr(0750,root,%name) %_sysconfdir/%name/
%config(noreplace) %attr(0640,root,%name) %_sysconfdir/%name/config
%config(noreplace) %attr(0640,root,%name) %_sysconfdir/%name/rights
%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %attr(0750,%name,%name) %_localstatedir/%name/
%dir %attr(0750,%name,%name) %_localstatedir/%name/collections/
%dir %attr(0750,%name,%name) %_cachedir/%name/

%files -n python3-module-%pypi_name
%doc COPYING.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Oct 08 2026 Vitaly Lipatov <lav@altlinux.ru> 3.8.2-alt1
- new version 3.8.2.

* Mon Oct 05 2026 Vitaly Lipatov <lav@altlinux.ru> 3.8.1-alt2
- create the radicale user and group via sysusers.d

* Mon Oct 05 2026 Vitaly Lipatov <lav@altlinux.ru> 3.8.1-alt1
- initial build for Sisyphus

