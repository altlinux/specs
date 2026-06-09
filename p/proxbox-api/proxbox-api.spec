%define mod_name proxbox_api

%def_with check

Name:    proxbox-api
Version: 0.0.17.post1
Release: alt1

Summary: Backend of NetBox Proxbox Plugin using FastAPI
License: Apache-2.0
Group:   Development/Python3
URL:     https://github.com/emersonfelipesp/proxbox-api

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-systemd
BuildRequires(pre): rpm-macros-apache2
BuildRequires(pre): rpm-build-webserver-common
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pytest-xdist
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-httpx
BuildRequires: python3-module-sqlalchemy
BuildRequires: python3-module-sqlmodel
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-jinja2
BuildRequires: python3-module-bcrypt
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-aiosqlite
BuildRequires: python3-module-greenlet
BuildRequires: python3-module-netbox-sdk
BuildRequires: python3-module-proxmox-sdk
BuildRequires: python3-module-yaml
%endif

Requires: python3-module-aiosqlite
Requires: python3-module-jinja2

BuildArch: noarch

Source:  %name-%version.tar
Source1: README
Source2: nginx.conf
Source3: httpd2.conf
Source4: httpd2-ssl.conf
Source5: proxbox-api.service
Source6: proxbox-api-tmpfile.conf
Source7: proxbox-api.logrotate

%description
%summary.

%package apache2
Group: Networking/WWW
BuildArch: noarch
Summary: apache2 support for %name
Requires: %name = %version-%release
Requires: apache2-httpd-prefork-like
Requires: apache2-base
Requires: apache2-mod_ssl
Requires: python3-module-uvicorn
Requires: cert-sh-functions

%description apache2
%summary.

%package nginx
Group: Networking/WWW
BuildArch: noarch
Summary: nginx support for %name
Requires: %name = %version-%release
Requires: nginx
Requires: python3-module-uvicorn
Requires: cert-sh-functions

%description nginx
%summary.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot{%_datadir,%_sharedstatedir}/proxbox-api
mkdir -p %buildroot%_logdir
touch %buildroot%_logdir/proxbox.log
install -p -D -m 644 %SOURCE7 %buildroot%_logrotatedir/proxbox-api
# httpd2
mkdir -p %buildroot%apache2_sites_available
install -p -D -m 644 %SOURCE3 %buildroot%apache2_sites_available/proxbox-api.conf
install -p -D -m 644 %SOURCE4 %buildroot%apache2_sites_available/proxbox-api-ssl.conf
mkdir -p %buildroot%apache2_sites_enabled
touch %buildroot%apache2_sites_enabled/proxbox-api.conf
touch %buildroot%apache2_sites_enabled/proxbox-api-ssl.conf
# nginx
mkdir -p %buildroot%_sysconfdir/nginx/sites-available.d
install -p -D -m 644 %SOURCE2 %buildroot%_sysconfdir/nginx/sites-available.d/proxbox-api.conf
mkdir -p %buildroot%_sysconfdir/nginx/sites-enabled.d
touch %buildroot%_sysconfdir/nginx/sites-enabled.d/proxbox-api.conf
# Units files
mkdir -p %buildroot%_unitdir
install -p -D -m 644 %SOURCE5 %buildroot%_unitdir/proxbox-api.service
# Tmp file
install -p -D -m 644 %SOURCE6 %buildroot%_tmpfilesdir/proxbox-api.conf
# Documentation
install -p -D -m 644 %SOURCE1 %buildroot%_defaultdocdir/proxbox-api/README

%check
%pyproject_run_pytest -k "not (test_generate_bundle_persists_artifacts or test_proxmox_mock_package_is_importable or test_codegen_source_url_accepts_default_proxmox_viewer)"

%pre
groupadd -r -f proxbox-api >/dev/null 2>&1 ||:
groupadd -r -f _webserver >/dev/null 2>&1 ||:
useradd -M -r -g proxbox-api -G _webserver -c 'Proxbox API Daemon' \
        -s /bin/false -d %_sharedstatedir/proxbox-api proxbox-api >/dev/null 2>&1 ||:

%post
%post_systemd_postponed proxbox-api.service

%preun
%preun_systemd proxbox-api.service

%post nginx
# Create SSL certificate for HTTPS server
cert-sh generate nginx-proxbox-api ||:

%post apache2
cert-sh generate apache2-proxbox-api ||:

%files
%doc *.md
%_bindir/proxbox-proxmox-codegen
%_bindir/proxbox-schema
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %name}
%_datadir/proxbox-api
%_defaultdocdir/proxbox-api/README
%config(noreplace) %_logrotatedir/proxbox-api
%attr(0644, proxbox-api, proxbox-api) %_logdir/proxbox.log
%dir %attr(0770, root, proxbox-api) %_sharedstatedir/proxbox-api
%_unitdir/proxbox-api.service
%_tmpfilesdir/proxbox-api.conf

%files apache2
%config(noreplace) %apache2_sites_available/*.conf
%ghost %apache2_sites_enabled/*.conf

%files nginx
%config(noreplace) %_sysconfdir/nginx/sites-available.d/proxbox-api.conf
%ghost %_sysconfdir/nginx/sites-enabled.d/proxbox-api.conf

%changelog
* Mon Jun 08 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.17.post1-alt1
- New 0.0.17.post1 version.

* Thu May 28 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.15-alt1
- New 0.0.15 version.

* Fri May 08 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.10.post3-alt1
- New 0.0.10.post3 version.

* Fri Apr 17 2026 Alexander Burmatov <thatman@altlinux.org> 0.0.8-alt1
- Initial build for Sisyphus.
