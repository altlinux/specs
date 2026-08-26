%define _unpackaged_files_terminate_build 1

Name: pi
Epoch:1 
Version: 0.84.3
Release: alt2

Summary: Terminal AI coding agent with read, bash, edit and write tools
License: MIT
Group: Development/Tools
Url: https://pi.dev
Vcs: https://github.com/earendil-works/pi.git

Source0: %name-%version.tar
Source1: %name-%version-node_modules.tar
Source2: %name-%version-model-data.tar
Source3: copy-production-tree.mjs
Patch0: pi-0.84.3-alt-tsconfig-es2024.patch
# Vendored model data (Source2) is newer than the tag: cloudflare-ai-gateway
# lost its openai-completions models, drop the dead api registration.
Patch1: pi-0.84.3-alt-cloudflare-drop-openai-completions.patch
# pi is managed by RPM: no online version check, no self-update.
Patch2: pi-0.84.3-alt-disable-update-check.patch
# The esbuild bundle is only for npm distribution; we ship the unbundled
# dist + node_modules. Vendored esbuild is linux-x64 only and breaks the
# noarch rebuild on other arches.
Patch3: pi-0.84.3-alt-no-esbuild-bundle.patch

BuildArch: noarch

BuildRequires(pre): rpm-macros-nodejs
BuildRequires: rpm-build-nodejs
BuildRequires: node >= 22.19
BuildRequires: npm
BuildRequires: typescript-go
BuildRequires: /proc

Requires: node >= 22.19
Requires: ripgrep
Requires: fd

# Vendored node_modules: do not generate Requires on bundled modules.
# nodejs.req would emit npm(@types/node) from hoisted protobufjs.
# Image resize uses photon wasm and is optional.
AutoReq: yes,nonodejs,nonodejs_native,nomono,nolua,nopython,nopython3,noshebang
AutoProv: no

Provides: node-%name = %EVR
Obsoletes: pi-coding-agent

%description
pi.dev is a terminal-based AI coding agent built on the pi.dev unified LLM API.
It provides read, bash, edit and write tools, session management, an
interactive TUI and export-to-HTML.

This package builds the TypeScript monorepo offline from the upstream git
tag and ships the production JavaScript tree plus vendored npm dependencies.
It needs only a Node.js runtime at install time.

%prep
%setup -a1 -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export HUSKY=0
export npm_config_ignore_scripts=true
# npm puts node_modules/.bin first; the vendored tsgo is host-only native-preview.
ln -sfn /usr/bin/tsgo node_modules/.bin/tsgo
npm run build:offline

%install
install -d %buildroot%nodejs_sitelib/%name
node %SOURCE3 . %buildroot%nodejs_sitelib/%name
chmod 0755 %buildroot%nodejs_sitelib/%name/dist/cli.js

# Drop native addons so the noarch package does not ship arch-specific ELF.
# photon-node still works via photon_rs_bg.wasm; clipboard is optional.
find %buildroot%nodejs_sitelib/%name -type f -name '*.node' -delete
find %buildroot%nodejs_sitelib/%name -depth -type d \( \
	-name '*-darwin-*' -o -name '*-win32-*' -o -name '*-windows-*' \
	-o -name '*-freebsd-*' -o -name '*-android-*' \
	\) -exec rm -rf {} +

install -d %buildroot%_bindir
cat > %buildroot%_bindir/pi <<EOF
#!/bin/sh
exec /usr/bin/node %nodejs_sitelib/%name/dist/cli.js "\$@"
EOF
chmod 0755 %buildroot%_bindir/pi

%check
node packages/coding-agent/dist/cli.js --help >/dev/null

%files
%doc LICENSE README.md packages/coding-agent/CHANGELOG.md
%_bindir/pi
%nodejs_sitelib/%name/

%changelog
* Wed Aug 26 2026 Anton Farygin <rider@altlinux.org> 1:0.84.3-alt2
- Added Requires: fd to avoid runtime download from GitHub (closes: 60282).

* Tue Aug 25 2026 Anton Farygin <rider@altlinux.org> 1:0.84.3-alt1
- 0.84.2 -> 0.84.3
- Disabled online version check and self-update: pi is managed by RPM
  (override with PI_FORCE_VERSION_CHECK / PI_FORCE_SELF_UPDATE).

* Wed Aug 19 2026 Anton Farygin <rider@altlinux.org> 1:0.84.2-alt2
- Build with system typescript-go (tsgo 7.0.2) instead of vendored native-preview.
- Target ES2024 so tsgo 7.0.2 accepts /v regexes in packages/tui.

* Tue Aug 18 2026 Anton Farygin <rider@altlinux.org> 0.84.2-alt1
- Initial build for ALT Sisyphus.
