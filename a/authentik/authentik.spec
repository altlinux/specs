%define _unpackaged_files_terminate_build 1
%define appdir %_datadir/%name

Name: authentik
Version: 2026.8.3
Release: alt1

Summary: Open source identity provider (SSO, OAuth2/OIDC, SAML, LDAP, RADIUS)

License: MIT and CC-BY-SA-4.0
Group: System/Servers
Url: https://goauthentik.io
Vcs: https://github.com/goauthentik/authentik

# Source-url: https://github.com/goauthentik/authentik/archive/refs/tags/version/%version.tar.gz
Source: %name-%version.tar
# Go modules, Rust crates and web UI node_modules (.gear/predownloaded-preinstall-hook)
Source1: %name-development-%version.tar
Source2: config.toml
Source3: authentik.sysusers.conf
Source4: authentik.tmpfiles.conf
Source5: authentik.config.yml
Source6: ak.sh
Source7: authentik-server.service
Source8: authentik-worker.service
Source9: authentik-outpost.env
Source10: authentik-outpost-proxy.service
Source11: authentik-outpost-ldap.service
Source12: authentik-outpost-radius.service
Source13: authentik-outpost-rac.service

# Django 6.1 in Sisyphus (upstream is on 5.2)
Patch1: authentik-2026.8.3-django6-unpin.patch
Patch2: authentik-2026.8.3-django6-email.patch
# authentik/enterprise/ is removed from the source (EE license)
Patch3: authentik-2026.8.3-no-enterprise.patch
Patch4: authentik-2026.8.3-python3.patch
Patch5: authentik-2026.8.3-no-fips.patch
Patch6: authentik-2026.8.3-web-node22.patch
Patch7: authentik-2026.8.3-rac-guacd.patch
Patch8: authentik-2026.8.3-no-rpath.patch

# the Rust server embeds Python (pyo3), 32-bit is not supported upstream
ExcludeArch: %ix86 armh

AutoProv: yes,nopython3
%add_python3_path %appdir
%add_python3_self_prov_path %buildroot%appdir
# authentik/enterprise is removed, its optional imports are guarded
%add_python3_req_skip authentik.enterprise.apps authentik.enterprise.license
# development commands (build_schema, build_source_docs) and tests/ (not packaged)
%add_python3_req_skip drf_jsonschema_serializer.convert pdoc pdoc.render

BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-rust
BuildRequires(pre): rpm-macros-systemd
BuildRequires: rpm-build-rust
BuildRequires: golang
BuildRequires: node
BuildRequires: esbuild
BuildRequires: python3-devel
BuildRequires: /proc

# the Rust server starts gunicorn by the command name
Requires: /usr/bin/gunicorn
# Django apps listed by name in INSTALLED_APPS/MIDDLEWARE only (autodeps can't see
# them); python3(pgactivity) is also provided by pg_activity (another module)
Requires: python3-module-django-prometheus
Requires: python3-module-django-pgactivity
# lifecycle/worker.py configures uvicorn with loop=uvloop and http=httptools
# (loaded by name)
Requires: python3-module-uvloop
Requires: python3-module-httptools
# xmlsec (SAML) dlopens its crypto backend, python3-module-xmlsec does not require it
Requires: libxmlsec1-openssl

%description
authentik is an open source identity provider: single sign-on with
OAuth2/OpenID Connect, SAML, LDAP and RADIUS, flows for enrollment,
recovery and multi-factor authentication (TOTP, WebAuthn, Duo, SMS),
federation with external sources (OAuth, SAML, LDAP, Kerberos, SCIM)
and an administration web interface.

This package contains the server (web interface and API) and the worker
(background tasks): authentik-server and authentik-worker services.
They need a PostgreSQL database, see README.ALT.

The authentik Enterprise Edition code (authentik/enterprise, under a
non-free license) is removed from the source; the FIPS crypto provider
is not built.

%package outpost-proxy
Summary: authentik proxy outpost
Group: System/Servers

%description outpost-proxy
authentik outpost for proxy providers: forward authentication for
nginx/Traefik/Caddy and reverse proxy with authentication in front of
applications. Runs as the authentik-outpost-proxy service, connects to
an authentik server (/etc/authentik/outpost-proxy.env).

%package outpost-ldap
Summary: authentik LDAP outpost
Group: System/Servers

%description outpost-ldap
authentik outpost for LDAP providers: an LDAP server (bind and search)
backed by authentik users and groups. Runs as the authentik-outpost-ldap
service, connects to an authentik server (/etc/authentik/outpost-ldap.env).

%package outpost-radius
Summary: authentik RADIUS outpost
Group: System/Servers

%description outpost-radius
authentik outpost for RADIUS providers: a RADIUS server authenticating
against authentik flows. Runs as the authentik-outpost-radius service,
connects to an authentik server (/etc/authentik/outpost-radius.env).

%package outpost-rac
Summary: authentik RAC (remote access) outpost
Group: System/Servers
# the outpost starts /usr/sbin/guacd itself, autodeps can't see it
Requires: guacd

%description outpost-rac
authentik outpost for RAC providers: remote desktop (RDP, VNC, SSH) in
the browser through guacd. Runs as the authentik-outpost-rac service,
connects to an authentik server (/etc/authentik/outpost-rac.env).

%prep
%setup -a1
%autopatch -p1
cat %SOURCE2 >> .cargo/config.toml
# the system toolchain is used
rm -v rust-toolchain.toml
# system esbuild instead of the prebuilt @esbuild/* binary
ln -sv %_bindir/esbuild web/esbuild
sed -i "s/\"0\.28\.1\"/\"$(rpm -q --qf '%%{VERSION}' esbuild)\"/g" web/node_modules/esbuild/lib/main.js
sed -i '1s|^#!/usr/bin/env python3\?$|#!%__python3|' manage.py lifecycle/*.py

%build
# web UI (web/dist), also embedded into the Rust server
export ESBUILD_BINARY_PATH=$PWD/web/esbuild
export NODE_ENV=production
cd web
node scripts/build-locales.mjs
node scripts/build-web.mjs
cd -

# Rust server (embeds Python) and the proxy outpost (without Python)
# RUSTFLAGS from the environment override build.rustflags of .cargo/config.toml
export RUSTFLAGS="--cfg tokio_unstable"
export CARGO_PROFILE_RELEASE_STRIP=none
export CARGO_PROFILE_RELEASE_DEBUG=true
%rust_build --package authentik --no-default-features --features core
cp -v target/release/authentik authentik-core
%rust_build --package authentik --no-default-features --features proxy
cp -v target/release/authentik authentik-proxy

# Go outposts
export GOFLAGS="-mod=vendor -buildmode=pie -trimpath"
for o in ldap radius rac ; do
	go build -ldflags "-compressdwarf=false" -o authentik-$o ./cmd/$o
done

%install
mkdir -p %buildroot%appdir/web
cp -a authentik lifecycle blueprints schemas locale manage.py %buildroot%appdir/
# workspace packages (ak-guardian, django-*-postgres)
cp -a packages/ak-guardian/guardian \
      packages/django-channels-postgres/django_channels_postgres \
      packages/django-dramatiq-postgres/django_dramatiq_postgres \
      packages/django-postgres-cache/django_postgres_cache \
      %buildroot%appdir/
cp -a web/dist web/authentik %buildroot%appdir/web/
# source maps are not needed
find %buildroot%appdir/web/dist -name '*.map' -delete
# tests (with their pytest, freezegun, k5test... imports) and the benchmark
# command using test helpers; management/commands/test_email.py is a command
find %buildroot%appdir -depth \( -type d -name tests -o -name tests.py \
	-o -name 'test_*.py' ! -path '*/management/commands/*' \) -exec rm -rv {} + | wc -l
rm -v %buildroot%appdir/authentik/flows/management/commands/benchmark.py
# the container entrypoint (needs /data, /certs; replaced by ak)
rm -v %buildroot%appdir/lifecycle/ak %buildroot%appdir/lifecycle/ak.py
rm -rv %buildroot%appdir/lifecycle/aws %buildroot%appdir/lifecycle/container

install -D -m 0755 authentik-core %buildroot%_libexecdir/%name/authentik
install -D -m 0755 %SOURCE6 %buildroot%_bindir/ak
install -D -m 0755 authentik-proxy %buildroot%_bindir/authentik-proxy
for o in ldap radius rac ; do
	install -D -m 0755 authentik-$o %buildroot%_bindir/authentik-$o
done

install -D -m 0644 %SOURCE3 %buildroot%_sysusersdir/%name.conf
install -D -m 0644 %SOURCE4 %buildroot%_tmpfilesdir/%name.conf
install -D -m 0640 %SOURCE5 %buildroot%_sysconfdir/%name/config.yml
mkdir -p %buildroot%_sysconfdir/%name/config.d
touch %buildroot%_sysconfdir/%name/secret_key
touch %buildroot%_sysconfdir/%name/postgresql_password
install -D -m 0644 %SOURCE7 %buildroot%_unitdir/authentik-server.service
install -D -m 0644 %SOURCE8 %buildroot%_unitdir/authentik-worker.service
for o in proxy ldap radius rac ; do
	install -D -m 0640 %SOURCE9 %buildroot%_sysconfdir/%name/outpost-$o.env
done
install -D -m 0644 %SOURCE10 %buildroot%_unitdir/authentik-outpost-proxy.service
install -D -m 0644 %SOURCE11 %buildroot%_unitdir/authentik-outpost-ldap.service
install -D -m 0644 %SOURCE12 %buildroot%_unitdir/authentik-outpost-radius.service
install -D -m 0644 %SOURCE13 %buildroot%_unitdir/authentik-outpost-rac.service
mkdir -p %buildroot%_sharedstatedir/%name/{data,certs,templates}

cat > README.ALT <<'EOF'
authentik in ALT
================

1. PostgreSQL (14 or newer), a role and a database for authentik:

   su - postgres -s /bin/sh -c "psql -c \"CREATE ROLE authentik LOGIN PASSWORD '$(cat /etc/authentik/postgresql_password)'\""
   su - postgres -s /bin/sh -c "createdb -O authentik authentik"

   The password is generated on the installation into
   /etc/authentik/postgresql_password, the connection settings are in
   /etc/authentik/config.yml (or /etc/authentik/config.d/*.yml,
   AUTHENTIK_* environment variables).

2. systemctl enable --now authentik-server authentik-worker
   The database migrations run on the start. The web interface listens
   on http://HOST:9000 and https://HOST:9443 (self-signed certificate).

   The worker listens on 127.0.0.1:9001 (health) and 127.0.0.1:9301
   (metrics), see authentik-worker.service.

3. Initial setup: https://HOST:9443/if/flow/initial-setup/
   (set the password of akadmin), or a recovery link:
   ak create_recovery_key 10 akadmin
   Environment variables for both services (AUTHENTIK_*, for example
   AUTHENTIK_BOOTSTRAP_PASSWORD and AUTHENTIK_BOOTSTRAP_EMAIL for akadmin
   on the first start) can be put into /etc/authentik/authentik.env.

The secret key is /etc/authentik/secret_key, data (uploaded files) are
in /var/lib/authentik/data, certificates for discovery in
/var/lib/authentik/certs, custom email templates in
/var/lib/authentik/templates.

Outposts (packages authentik-outpost-proxy, -ldap, -radius, -rac):
create the outpost in the admin interface (Applications > Outposts,
manual deployment), put the URL and the token into
/etc/authentik/outpost-NAME.env and start authentik-outpost-NAME.
The embedded proxy outpost of the server needs no package.

Not included: the Enterprise Edition (authentik/enterprise), FIPS mode,
GeoIP databases (put GeoLite2-City.mmdb and GeoLite2-ASN.mmdb into
/usr/share/GeoIP to enable them).
EOF

%check
# no PostgreSQL here: the binaries start and the Python part is importable
%buildroot%_libexecdir/%name/authentik --help
%buildroot%_bindir/authentik-proxy --help
for o in ldap radius rac ; do
	%buildroot%_bindir/authentik-$o --version
done
PYTHONPATH=%buildroot%appdir %__python3 -c 'import authentik, lifecycle'

%pre
%sysusers_create_package %name %SOURCE3

%post
for f in secret_key postgresql_password ; do
	if [ ! -s %_sysconfdir/%name/$f ] ; then
		(umask 027 ; head -c 45 /dev/urandom | base64 > %_sysconfdir/%name/$f)
		chgrp %name %_sysconfdir/%name/$f
	fi
done
%post_service authentik-server
%post_service authentik-worker

%preun
%preun_service authentik-server
%preun_service authentik-worker

%post outpost-proxy
%post_service authentik-outpost-proxy

%preun outpost-proxy
%preun_service authentik-outpost-proxy

%post outpost-ldap
%post_service authentik-outpost-ldap

%preun outpost-ldap
%preun_service authentik-outpost-ldap

%post outpost-radius
%post_service authentik-outpost-radius

%preun outpost-radius
%preun_service authentik-outpost-radius

%post outpost-rac
%post_service authentik-outpost-rac

%preun outpost-rac
%preun_service authentik-outpost-rac

%files
%doc README.md SECURITY.md README.ALT
%doc LICENSE
%_bindir/ak
%_libexecdir/%name/
%appdir/
%_unitdir/authentik-server.service
%_unitdir/authentik-worker.service
%_sysusersdir/%name.conf
%_tmpfilesdir/%name.conf
%dir %_sysconfdir/%name
%dir %_sysconfdir/%name/config.d
%config(noreplace) %attr(0640,root,%name) %_sysconfdir/%name/config.yml
%ghost %config(noreplace) %attr(0640,root,%name) %_sysconfdir/%name/secret_key
%ghost %config(noreplace) %attr(0640,root,%name) %_sysconfdir/%name/postgresql_password
%dir %attr(0750,%name,%name) %_sharedstatedir/%name
%dir %attr(0750,%name,%name) %_sharedstatedir/%name/data
%dir %attr(0750,%name,%name) %_sharedstatedir/%name/certs
%dir %attr(0750,%name,%name) %_sharedstatedir/%name/templates

%files outpost-proxy
%doc LICENSE
%_bindir/authentik-proxy
%_unitdir/authentik-outpost-proxy.service
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/outpost-proxy.env

%files outpost-ldap
%doc LICENSE
%_bindir/authentik-ldap
%_unitdir/authentik-outpost-ldap.service
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/outpost-ldap.env

%files outpost-radius
%doc LICENSE
%_bindir/authentik-radius
%_unitdir/authentik-outpost-radius.service
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/outpost-radius.env

%files outpost-rac
%doc LICENSE
%_bindir/authentik-rac
%_unitdir/authentik-outpost-rac.service
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,root) %_sysconfdir/%name/outpost-rac.env

%changelog
* Mon Oct 19 2026 Vitaly Lipatov <lav@altlinux.ru> 2026.8.3-alt1
- initial build for Sisyphus
