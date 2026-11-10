Name:    mongo-express
Version: 1.0.2
Release: alt1

Summary: Web-based MongoDB admin interface, written with Node.js and Express
License: MIT
Group:   Databases
URL:     https://github.com/mongo-express/mongo-express
VCS:     https://github.com/mongo-express/mongo-express

Source0: %name-%version.tar
Source1: vendor.tar
Source3: %name.service
Source4: %name.conf
Source5: %name.sysusers

Patch0: ejson-shell-parser.patch
Patch1: mongodb-query-parser.patch
Patch2: renderjson.patch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires(pre): rpm-macros-systemd
BuildRequires: yarn
BuildRequires: node
BuildRequires: /proc

BuildArch: noarch

%add_findreq_skiplist %nodejs_sitelib/%name/node_modules/**/*
%add_findprov_skiplist %nodejs_sitelib/%name/node_modules/**/*

%description
Web-based MongoDB admin interface written with Node.js, Express and Bootstrap3.

%prep
%setup -a1
cp vendor/{package.json,yarn.lock,.yarnrc} .
rm -rf .yarn .yarnrc.yml

%patch0 -p1 -d vendor/ejson-shell-parser
%patch1 -p1 -d vendor/mongodb-query-parser
%patch2 -p1 -d vendor/renderjson

%build
export YARN_IGNORE_PATH=1
export YARN_CACHE_FOLDER="$PWD/.yarn-cache"

yarn install --offline --frozen-lockfile --ignore-scripts --non-interactive
yarn build
yarn install --offline --frozen-lockfile --ignore-scripts --non-interactive --production

%install
install -d %buildroot%nodejs_sitelib/%name
cp -a \
    app.js config.default.js package.json build-assets.json \
    build lib public node_modules \
    %buildroot%nodejs_sitelib/%name/

sed -i 's/^  "version": "1\.0\.0",$/  "version": "%version",/' \
    %buildroot%nodejs_sitelib/%name/package.json

install -d %buildroot%_bindir
cat > %buildroot%_bindir/%name <<'EOF'
#!/bin/sh
cd %nodejs_sitelib/%name || exit 1
export NODE_ENV=production
exec %_bindir/node app.js "$@"
EOF
chmod 0755 %buildroot%_bindir/%name

install -Dm0644 %SOURCE3 %buildroot%_unitdir/%name.service
install -Dm0640 %SOURCE4 \
    %buildroot%_sysconfdir/%name/%name.conf

install -Dm0644 %SOURCE5 %buildroot%_sysusersdir/%name.conf

ln -s %_sysconfdir/%name/%name.conf \
    %buildroot%nodejs_sitelib/%name/.env

rm %buildroot%nodejs_sitelib/%name/node_modules/.yarn-integrity
rm %buildroot%nodejs_sitelib/%name/node_modules/foreground-child/changelog.sh
rm -r %buildroot%nodejs_sitelib/%name/node_modules/performance-now/test

%pre
%sysusers_create_package %name %SOURCE5

%post
%_bindir/node --input-type=commonjs <<'EOF' || exit 1
const fs = require('node:fs');
const { randomBytes } = require('node:crypto');

const configPath = '%_sysconfdir/%name/%name.conf';
const original = fs.readFileSync(configPath, 'utf8');
let updated = original;

for (const key of [
  'ME_CONFIG_BASICAUTH_PASSWORD',
  'ME_CONFIG_SITE_COOKIESECRET',
  'ME_CONFIG_SITE_SESSIONSECRET',
]) {
  const pattern = new RegExp(`^${key}=[ \\t]*$`, 'm');
  updated = updated.replace(
    pattern,
    () => `${key}=${randomBytes(32).toString('hex')}`,
  );
}

if (updated !== original) {
  fs.writeFileSync(configPath, updated);
}
EOF

%post_service %name

%preun
%preun_service %name

%files
%doc LICENSE.md README.md HISTORY.md
%_bindir/%name
%nodejs_sitelib/%name
%_unitdir/%name.service
%_sysusersdir/%name.conf
%attr(0750,root,%name) %dir %_sysconfdir/%name
%attr(0640,root,%name) %config(noreplace) %_sysconfdir/%name/%name.conf

%changelog
* Thu Oct 29 2026 Evgeniy Serov <scala@altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus.
