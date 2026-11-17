# Line tables keep useful backtraces without full dependency debug data.
%define rust_debug "line-tables-only"

Name: metric-server
Version: 0.1.10
Release: alt1

Summary: Sentry-compatible error tracking server

License: MIT
Group: System/Servers
Url: https://biosshot.github.io/metric/
Vcs: https://github.com/biosshot/metric
# Source-url: https://github.com/biosshot/metric/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml
Source3: %name.service
Source4: %name.sysusers.conf
Source5: %name.toml
Source6: README.ALT

# Native Rollup bindings are not available for ix86.
ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-rust rpm-macros-systemd
BuildRequires: rpm-build-rust /proc /usr/bin/cmake /usr/bin/perl
BuildRequires: npm rollup rollup-native esbuild

%description
Metric is a self-hosted Sentry-compatible error tracking and observability
server. It accepts events from Sentry SDKs, groups failures into issues and
provides a web interface for errors, logs, traces and releases.

A separately configured PostgreSQL or MongoDB server is required. The default
ALT configuration selects PostgreSQL on localhost. Local attachments are
stored in /var/lib/metric-server. See README.ALT for database provisioning,
secret generation and initial administrator setup.

%prep
%setup -a1
install -D -m 0644 %SOURCE2 .cargo/config.toml
# Use native bundlers built from source in ALT, not npm binary downloads.
rm -rf node_modules/rollup
ln -s /usr/lib/node_modules/rollup node_modules/rollup
ln -s ../node_modules web/node_modules
rm -f node_modules/esbuild/bin/esbuild
ln -s %_bindir/esbuild node_modules/esbuild/bin/esbuild

%build
export ESBUILD_BINARY_PATH="$PWD/node_modules/esbuild/bin/esbuild"
cd web
npm run build --offline
cd ..
%rust_build

%install
%rust_install
mkdir -p %buildroot%_datadir/%name/web
cp -a web/dist/. %buildroot%_datadir/%name/web/
install -D -m 0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -D -m 0644 %SOURCE4 %buildroot%_sysusersdir/%name.conf
install -D -m 0640 %SOURCE5 %buildroot%_sysconfdir/%name/metric.toml
install -D -m 0644 %SOURCE6 README.ALT
mkdir -p %buildroot%_localstatedir/%name

%check
%rust_test -p metric-domain --lib

%pre
%sysusers_create_package %name %SOURCE4

%post
%post_service %name

%preun
%preun_service %name

%files
%doc README.md LICENSE README.ALT
%_bindir/%name
%_datadir/%name/
%_unitdir/%name.service
%_sysusersdir/%name.conf
%dir %attr(0750,root,metric-server) %_sysconfdir/%name
%config(noreplace) %attr(0640,root,metric-server) %_sysconfdir/%name/metric.toml
%dir %attr(0750,metric-server,metric-server) %_localstatedir/%name

%changelog
* Tue Nov 17 2026 Vitaly Lipatov <lav@altlinux.ru> 0.1.10-alt1
- initial build for ALT Sisyphus
- exclude ix86: native Rollup bindings are unavailable

