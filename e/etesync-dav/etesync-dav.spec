%def_with check

%define pypi_name etesync-dav
%define mod_name etesync_dav

Name: etesync-dav
Version: 0.35.1
Release: alt2

Summary: CalDAV and CardDAV adapter for EteSync

License: GPL-3.0-only
Group: Networking/Other
Url: https://github.com/etesync/etesync-dav

# Source-url: https://github.com/etesync/etesync-dav/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: radicale38-check.py

# Radicale 3.5+ compatibility
# upstream master: https://github.com/etesync/etesync-dav/pull/357
Patch1: 0001-Fix-usage-with-radicale-3.5.1-357.patch
# upstream master: https://github.com/etesync/etesync-dav/pull/362
Patch2: 0002-fix-compatibility-with-radicale-3.5.9-362.patch
# upstream PR (open): https://github.com/etesync/etesync-dav/pull/365
Patch3: 0003-Fix-upload-return-type-for-Radicale-3.5.5.patch
Patch4: 0004-Fix-WSGIResponse-for-Radicale-3.5.10.patch
Patch5: 0005-Fix-method-signatures-for-Radicale-3.6.0.patch
# drop the Radicale < 3.3 pin (not yet proposed upstream)
Patch6: 0006-setup.py-allow-Radicale-3.3-and-newer.patch
# peewee 4.x removed SqliteExtDatabase (not yet proposed upstream)
Patch7: 0007-Use-peewee.SqliteDatabase-for-peewee-4-compatibility.patch
# https://bugzilla.altlinux.org/60849 (attachment 22355)
Patch8: 0007-Fix-Radicale-3.8-metadata-and-last-modified.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-systemd
BuildRequires: python3-module-setuptools python3-module-wheel

%if_with check
BuildRequires: python3-module-radicale >= 3.5.10
BuildRequires: python3-module-etebase
BuildRequires: python3-module-etesync
BuildRequires: python3-module-flask
BuildRequires: python3-module-flask-wtf
BuildRequires: python3-module-appdirs
BuildRequires: python3-module-msgpack
BuildRequires: python3-module-requests
BuildRequires: python3-module-packaging
BuildRequires: python3-module-cryptography
BuildRequires: python3-module-peewee
BuildRequires: python3-module-vobject
%endif

# macOS only
%add_python3_req_skip PyObjCTools

%description
EteSync DAV is a local CalDAV and CardDAV adapter for EteSync,
the end-to-end encrypted and journaled sync service for contacts,
calendars, tasks and notes.

It allows to use EteSync with any DAV client, for example
Thunderbird, Evolution, KAddressBook or GNOME Calendar: the adapter
runs locally and keeps all data encrypted on the server.

Run etesync-dav (or enable the etesync-dav systemd user service)
and open http://127.0.0.1:37358/ to add an account.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install
install -Dpm0644 examples/systemd-user/%name.service %buildroot%_userunitdir/%name.service

%check
export HOME=$(mktemp -d)
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 %SOURCE1
%buildroot%_bindir/etesync-dav --version
# start the server and check its web UI, as nixos tests do
# (localhost does not resolve in hasher, use the IP address;
# the web UI only trusts the Host matching the listen address)
ETESYNC_LISTEN_ADDRESS=127.0.0.1 %buildroot%_bindir/etesync-dav &
pid=$!
trap "kill $pid" EXIT
for i in $(seq 30); do
    %__python3 -c 'import urllib.request; urllib.request.urlopen("http://127.0.0.1:37358/.web/")' 2>/dev/null && break
    sleep 1
done
%__python3 -c 'import urllib.request; r = urllib.request.urlopen("http://127.0.0.1:37358/.web/add/").read().decode(); assert "Add User" in r, r'

%files
%doc README.md ChangeLog.md DESCRIPTION.rst LICENSE
%_bindir/etesync-dav
%_userunitdir/%name.service
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Wed Oct 07 2026 Vitaly Lipatov <lav@altlinux.ru> 0.35.1-alt2
- fix compatibility with peewee 4.x (SqliteExtDatabase was removed).
- Fix PROPFIND and GET with Radicale 3.8 (closes: #60849).

* Mon Oct 05 2026 Vitaly Lipatov <lav@altlinux.ru> 0.35.1-alt1
- initial build for Sisyphus
