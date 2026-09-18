%define _unpackaged_files_terminate_build 1

Name: marp-cli
Version: 4.5.1
Release: alt1

Summary: Markdown presentation writer and converter
License: MIT
Group: Office
URL: https://marp.app
VCS: https://github.com/marp-team/marp-cli.git

Source0: %name-%version.tar
Source1: %name-%version-predownloaded.tar

ExclusiveArch: x86_64

BuildRequires: /proc
BuildRequires: node
BuildRequires: npm

Requires: node

# Vendored npm modules are private to Marp, not system Python/Node modules.
%add_findprov_skiplist %_datadir/marp-cli/node_modules/*
%add_findreq_skiplist %_datadir/marp-cli/node_modules/*

%description
Marp CLI converts Markdown slide decks into HTML, PDF, PowerPoint, and
images. It supports themes, live preview, and a local web server.

%prep
%setup -a1

mv node_modules_dev node_modules
mkdir -p production
mv node_modules_prod production/node_modules

%build
./node_modules/.bin/patch-package --error-on-fail
npm run build
npm run types

%install
mkdir -p %buildroot%_datadir/marp-cli/types %buildroot%_bindir
cp -a lib marp-cli.js package.json production/node_modules %buildroot%_datadir/marp-cli
cp -a types/src %buildroot%_datadir/marp-cli/types/

cat > %buildroot%_bindir/marp <<'EOF'
#!/bin/sh
exec /usr/bin/node /usr/share/marp-cli/marp-cli.js "$@"
EOF
chmod 755 %buildroot%_bindir/marp

%check
npm test -- --runInBand test/engine.ts test/engine/ test/theme.ts test/utils/stdin.ts

smoke_dir=$(mktemp -d)

pushd "$smoke_dir"
/usr/bin/node %buildroot%_datadir/marp-cli/marp-cli.js --version
cat > smoke.md <<'EOF'
---
marp: true
---
# ALT Linux smoke test
EOF
/usr/bin/node %buildroot%_datadir/marp-cli/marp-cli.js smoke.md -o smoke.html
grep -q '<svg' smoke.html
grep -q 'ALT Linux smoke test' smoke.html
popd

rm -rf "$smoke_dir"

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/marp
%_datadir/marp-cli

%changelog
* Thu Sep 17 2026 Grant Makyan <karonus@altlinux.org> 4.5.1-alt1
- Initial build for ALT.
