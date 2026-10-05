%def_with check

%define mod_name etebase_server

Name: etebase-server
Version: 0.14.2
Release: alt1

Summary: Etebase (EteSync 2.0) server

License: AGPL-3.0-only
Group: System/Servers
Url: https://github.com/etesync/server

# Source-url: https://github.com/etesync/server/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: etebase-server.service
Source2: etebase-server.sh
Source3: etebase-server-check.py
Source4: etebase-server.sysusers.conf

# upstream master commit cc54a136f14dd434667776e30ee308ef7b65f6f9
Patch1: 0001-Fix-server-error-when-passing-null-collection-types.patch
# FastAPI 0.141 compatibility, the same change is in upstream PR #205
Patch2: 0002-Declare-collection_uid-as-a-path-parameter-explicitl.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-systemd
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-django
BuildRequires: python3-module-django-dbbackend-sqlite3
BuildRequires: python3-module-fastapi
BuildRequires: python3-module-pydantic
BuildRequires: python3-module-msgpack
BuildRequires: python3-module-pynacl
BuildRequires: python3-module-redis-py
BuildRequires: python3-module-aiofiles
BuildRequires: python3-module-httpx
%endif

# the default database engine is set by name in settings.py and in the config,
# not imported, so autodeps can't see it
Requires: python3-module-django-dbbackend-sqlite3

# optional LDAP authentication backend, enabled in the [ldap] config section
%add_python3_req_skip ldap

%description
An Etebase (EteSync 2.0) server so you can run your own.

Etebase is an end-to-end encrypted backend for contacts, calendars,
tasks and notes used by the EteSync clients.

The server runs as the etebase-server service (uvicorn on 127.0.0.1:3735)
with the configuration in /etc/etebase-server/etebase-server.ini and the data
(SQLite database, user media, secret key) in /var/lib/etebase-server.
Use 'etebase-server createsuperuser' to create an admin user.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

install -D -m 0755 %SOURCE2 %buildroot%_bindir/etebase-server
install -D -m 0644 %SOURCE1 %buildroot%_unitdir/etebase-server.service
install -D -m 0644 %SOURCE4 %buildroot%_sysusersdir/%name.conf

install -D -m 0640 etebase-server.ini.example %buildroot%_sysconfdir/%name/etebase-server.ini
sed -i \
    -e 's|^secret_file = .*|secret_file = %_localstatedir/%name/secret.txt|' \
    -e 's|^static_root = .*|static_root = %_localstatedir/%name/static|' \
    -e 's|^media_root = .*|media_root = %_localstatedir/%name/media|' \
    -e 's|^allowed_host1 = .*|allowed_host1 = localhost|' \
    -e 's|^name = db.sqlite3|name = %_localstatedir/%name/db.sqlite3|' \
    %buildroot%_sysconfdir/%name/etebase-server.ini
# fail if the upstream example changed and an active setting was not replaced
if grep -E '^[^;].*(/path/to|example\.com|= (secret\.txt|db\.sqlite3)$)' %buildroot%_sysconfdir/%name/etebase-server.ini; then
    exit 1
fi

mkdir -p %buildroot%_localstatedir/%name

%check
PYTHONPATH=%buildroot%python3_sitelibdir %__python3 %SOURCE3

%pre
%sysusers_create_package %name %SOURCE4

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md ChangeLog.md
%_bindir/etebase-server
%_unitdir/etebase-server.service
%_sysusersdir/%name.conf
%dir %attr(0750,root,etebase) %_sysconfdir/%name
%config(noreplace) %attr(0640,root,etebase) %_sysconfdir/%name/etebase-server.ini
%dir %attr(0750,etebase,etebase) %_localstatedir/%name
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %mod_name}/

%changelog
* Mon Oct 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.14.2-alt1
- initial build for Sisyphus
