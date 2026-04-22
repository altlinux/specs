%define _unpackaged_files_terminate_build 1

Name: pyright
Version: 1.1.408
Release: alt1

Summary: Static type checker for Python
License: MIT
Group: Development/Other

URL: https://github.com/microsoft/pyright
VCS: https://github.com/microsoft/pyright

Source0: %name-%version.tar
Source1: %name-vendor-%version.tar

BuildArch: noarch

BuildRequires: npm
BuildRequires: node >= 8
BuildRequires: esbuild
BuildRequires: rpm-macros-nodejs


%description
Pyright is a static type checker for Python written in TypeScript.

%prep
%setup -q -a 1

%build
export ESBUILD_BINARY_PATH=%_bindir/esbuild
%ifnarch x86_64
# esbuild npm package is platform-sensitive in vendor setup on non-x86_64.
# Patch only build tree: drop optional JS transform rule that uses esbuild-loader.
sed -i '/loader:[[:space:]]*.\{0,1\}esbuild-loader.\{0,1\}/,/^[[:space:]]*},$/d' packages/pyright/webpack.config.js
%endif
npm run build:cli:dev
npm prune --omit=dev

%install

install -d %buildroot%nodejs_sitelib/pyright
install -d %buildroot%_bindir

install -m 0755 packages/pyright/index.js %buildroot%nodejs_sitelib/pyright/
install -m 0755 packages/pyright/langserver.index.js %buildroot%nodejs_sitelib/pyright/
cp -a packages/pyright/dist %buildroot%nodejs_sitelib/pyright/

ln -s ../lib/node_modules/pyright/index.js %buildroot%_bindir/pyright
ln -s ../lib/node_modules/pyright/langserver.index.js %buildroot%_bindir/pyright-langserver

%check
# Lightweight runtime checks for installed entrypoints.
node %buildroot%nodejs_sitelib/pyright/index.js --version
# Send a minimal LSP initialize request and verify server response.
set +e
printf 'Content-Length: 65\r\n\r\n{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"capabilities":{}}}' \
    | timeout 2s node %buildroot%nodejs_sitelib/pyright/langserver.index.js --stdio > langserver.log 2>&1
set -e
grep -E '"jsonrpc":"2.0".*"window/logMessage"' langserver.log > /dev/null

%files
%_bindir/pyright
%_bindir/pyright-langserver
%nodejs_sitelib/pyright

%changelog
* Tue Feb 20 2026 sen <sen@altlinux.org> 1.1.408-alt1
- Firts build for ALT.
